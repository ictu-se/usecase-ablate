# Deterministic random code snippets
### app/Api/V1/Controllers/Models/Attachment/StoreController.php
<?php

/*
 * StoreController.php
 * Copyright (c) 2021 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Controllers\Models\Attachment;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Api\V1\Middleware\ApiDemoUser;
use FireflyIII\Api\V1\Requests\Models\Attachment\StoreRequest;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Helpers\Attachments\AttachmentHelperInterface;
use FireflyIII\Models\Attachment;
use FireflyIII\Repositories\Attachment\AttachmentRepositoryInterface;
use FireflyIII\Transformers\AttachmentTransformer;
use FireflyIII\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use League\Fractal\Resource\Item;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

/**
 * Class StoreController
 */
final class StoreController extends Controller
{
    private AttachmentRepositoryInterface $repository;

    /**
     * StoreController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(ApiDemoUser::class)->except(['delete', 'download', 'show', 'index']);
        $this->middleware(function ($request, $next) {
            /** @var User $user */
            $user             = auth()->user();
            $this->repository = app(AttachmentRepositoryInterface::class);
            $this->repository->setUser($user);

            return $next($request);
        });
    }

    /**
     * This endpoint is documented at:
     * https://api-docs.firefly-iii.org/?urls.primaryName=2.0.0%20(v1)#/attachments/uploadAttachment
     *
     * Store a newly created resource in storage.
     *
     * @throws FireflyException
     */
    public function store(StoreRequest $request): JsonResponse
    {
        if (true === auth()->user()->hasRole('demo')) {
 
...[truncated]...

### app/Console/Commands/Correction/CorrectsTransferBudgets.php
<?php

/**
 * TransferBudgets.php
 * Copyright (c) 2020 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Console\Commands\Correction;

use FireflyIII\Console\Commands\ShowsFriendlyMessages;
use FireflyIII\Enums\TransactionTypeEnum;
use FireflyIII\Models\TransactionJournal;
use Illuminate\Console\Command;
use Illuminate\Support\Facades\Log;

class CorrectsTransferBudgets extends Command
{
    use ShowsFriendlyMessages;

    protected $description = 'Removes budgets from transfers.';
    protected $signature   = 'correction:transfer-budgets';

    /**
     * Execute the console command.
     */
    public function handle(): int
    {
        $set   = TransactionJournal::query()
            ->distinct()
            ->leftJoin('transaction_types', 'transaction_types.id', '=', 'transaction_journals.transaction_type_id')
            ->leftJoin('budget_transaction_journal', 'transaction_journals.id', '=', 'budget_transaction_journal.transaction_journal_id')
            ->whereNotIn('transaction_types.type', [TransactionTypeEnum::WITHDRAWAL->value])
            ->whereNotNull('budget_transaction_journal.budget_id')
            ->get(['transaction_journals.*'])
        ;
        $count = 0;

        /** @var TransactionJournal $entry */
        foreach ($set as $entry) {
            $message = sprintf('Transaction journal #%d is a %s, so has no longer a budget.', $entry->id, $entry->transactionType->type);
            $this->friendlyInfo($message);
            Log::debug($message);
            $entry->budgets()->sync([]);
            ++$count;
        }
        if (0 !== $count) {
            $message = sprintf('Corrected %d invalid budget/journal entries (entry).', $count);
            Log::debug($message);
            $this->friendlyInfo($message);
        }

        return 0;
    }
}

### tests/unit/Support/NavigationPreferredSqlFormatTest.php
<?php

/*
 * NavigationPreferredSqlFormatTest.php
 * Copyright (c) 2023 Antonio Spinelli <https://github.com/tonicospinelli>
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace Tests\unit\Support;

use Carbon\Carbon;
use FireflyIII\Support\Navigation;
use Override;
use PHPUnit\Framework\Attributes\DataProvider;
use Tests\integration\TestCase;

/**
 * @group unit-test
 * @group support
 * @group navigation
 *
 * @internal
 *
 * @coversNothing
 */
final class NavigationPreferredSqlFormatTest extends TestCase
{
    private Navigation $navigation;

    #[DataProvider('provideDates')]
    public function testGivenStartAndEndDatesWhenCallPreferredSqlFormatThenReturnsTheExpectedFormatSuccessful(
        Carbon $start,
        Carbon $end,
        string $expected
    ): void {
        $formatPeriod = $this->navigation->preferredSqlFormat($start, $end);
        $this->assertSame($expected, $formatPeriod);
    }

    public static function provideDates(): iterable
    {
        yield '1 week' => [Carbon::now(), Carbon::now()->addWeek(), '%Y-%m-%d'];

        yield '1 month' => [Carbon::now(), Carbon::now()->addMonth(), '%Y-%m-%d'];

        yield '2 months' => [Carbon::now(), Carbon::now()->addMonths(2), '%Y-%m'];

        yield '3 months' => [Carbon::now(), Carbon::now()->addMonths(3), '%Y-%m'];

        yield '6 months' => [Carbon::now(), Carbon::now()->addMonths(6), '%Y-%m'];

        yield '7 months' => [Carbon::now(), Carbon::now()->addMonths(7), '%Y-%m'];

        yield '11 months' => [Carbon::now(), Carbon::now()->addMonths(11), '%Y-%m'];

        yield '12 months' => [Carbon::now(), Carbon::now()->addMonths(12), '%Y-%m'];

        yield '13 months' => [Carbon::now(), Carbon::now()->addMonths(13), '%Y'];

        yield '16 months' => [Carbon::now(), Carbon::now()->addMonths(16), '%Y'];

        yield '1 year' => [Carbon::now(), Carbon::n
...[truncated]...

### app/Notifications/User/UserRegistration.php
<?php

/*
 * UserRegistration.php
 * Copyright (c) 2022 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Notifications\User;

use FireflyIII\User;
use Illuminate\Bus\Queueable;
use Illuminate\Notifications\Messages\MailMessage;
use Illuminate\Notifications\Notification;

/**
 * Class UserRegistration
 */
class UserRegistration extends Notification
{
    use Queueable;

    /**
     * @SuppressWarnings("PHPMD.UnusedFormalParameter")
     */
    public function toArray(User $notifiable): array
    {
        return [];
    }

    /**
     * @SuppressWarnings("PHPMD.UnusedFormalParameter")
     */
    public function toMail(User $notifiable): MailMessage
    {
        return new MailMessage()
            ->markdown('emails.registered', ['address' => route('index')])
            ->subject((string) trans('email.registered_subject'))
        ;
    }

    /**
     * @SuppressWarnings("PHPMD.UnusedFormalParameter")
     */
    public function via(User $notifiable): array
    {
        // other settings will not be available at this point anyway.
        return ['mail'];
    }
}

### app/Events/Model/Budget/UpdatedBudget.php
<?php

declare(strict_types=1);

/*
 * UpdatedBudget.php
 * Copyright (c) 2026 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

namespace FireflyIII\Events\Model\Budget;

use FireflyIII\Events\Event;
use FireflyIII\Models\Budget;
use Illuminate\Queue\SerializesModels;

class UpdatedBudget extends Event
{
    use SerializesModels;

    public function __construct(
        public Budget $budget,
        public bool $createWebhookMessages
    ) {}
}

### app/Transformers/UserTransformer.php
<?php

/**
 * UserTransformer.php
 * Copyright (c) 2019 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Transformers;

use FireflyIII\Repositories\User\UserRepositoryInterface;
use FireflyIII\User;

/**
 * Class UserTransformer
 */
class UserTransformer extends AbstractTransformer
{
    private UserRepositoryInterface $repository;

    /**
     * Transform user.
     */
    public function transform(User $user): array
    {
        $this->repository ??= app(UserRepositoryInterface::class);

        return [
            'id'           => (int) $user->id,
            'created_at'   => $user->created_at->toAtomString(),
            'updated_at'   => $user->updated_at->toAtomString(),
            'email'        => $user->email,
            'blocked'      => 1 === (int) $user->blocked,
            'blocked_code' => '' === $user->blocked_code ? null : $user->blocked_code,
            'role'         => $this->repository->getRoleByUser($user),
            'links'        => [['rel' => 'self', 'uri' => '/users/'.$user->id]],
        ];
    }
}

### app/Api/V1/Requests/Models/TransactionLink/StoreRequest.php
<?php

/**
 * TransactionLinkRequest.php
 * Copyright (c) 2019 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Requests\Models\TransactionLink;

use FireflyIII\Repositories\Journal\JournalRepositoryInterface;
use FireflyIII\Repositories\LinkType\LinkTypeRepositoryInterface;
use FireflyIII\Support\Request\ChecksLogin;
use FireflyIII\Support\Request\ConvertsDataTypes;
use FireflyIII\User;
use Illuminate\Contracts\Validation\Validator;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Support\Facades\Log;

/**
 * Class StoreRequest
 */
class StoreRequest extends FormRequest
{
    use ChecksLogin;
    use ConvertsDataTypes;

    protected array $acceptedRoles = [];

    /**
     * Get all data from the request.
     */
    public function getAll(): array
    {
        return [
            'link_type_id'   => $this->convertInteger('link_type_id'),
            'link_type_name' => $this->convertString('link_type_name'),
            'inward_id'      => $this->convertInteger('inward_id'),
            'outward_id'     => $this->convertInteger('outward_id'),
            'notes'          => $this->stringWithNewlines('notes'),
        ];
    }

    /**
     * The rules that the incoming request must be matched against.
     */
    public function rules(): array
    {
        return [
            'link_type_id'   => ['exists:link_types,id', 'required_without:link_type_name'],
            'link_type_name' => ['exists:link_types,name', 'required_without:link_type_id'],
            'inward_id'      => ['required', 'belongsToUser:transaction_journals,id', 'different:outward_id'],
            'outward_id'     => ['required', 'belongsToUser:transaction_journals,id', 'different:inward_id'],
            'notes'          => ['min:1', 'max:32768', 'nullable'],
        ];
    }

    /**
     * Configure the 
...[truncated]...

### resources/views/v2/partials/dashboard/category-chart.blade.php
<div class="row mb-2" x-data="categories" x-bind="eventListeners">
    <div class="col">
        <div class="card">
            <div class="card-header">
                <h3 class="card-title"><a href="{{ route('categories.index') }}"
                                          title="{{ __('firefly.go_to_categories') }}">{{ __('firefly.categories') }}</a>
                </h3>
            </div>
            <div class="card-body p-0" style="position: relative;height:350px;">
                <canvas id="category-chart"></canvas>
            </div>
        </div>
    </div>
</div>

### app/Console/Commands/Upgrade/UpgradesDatabase.php
<?php

/**
 * UpgradeDatabase.php
 * Copyright (c) 2020 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Console\Commands\Upgrade;

use FireflyIII\Console\Commands\ShowsFriendlyMessages;
use FireflyIII\Support\Facades\FireflyConfig;
use Illuminate\Console\Command;
use Illuminate\Support\Facades\Log;
use Safe\Exceptions\InfoException;

use function Safe\set_time_limit;

try {
    set_time_limit(0);
} catch (InfoException) {
    Log::warning('set_time_limit returned false. This could be an issue, unless you also run XDebug.');
}

class UpgradesDatabase extends Command
{
    use ShowsFriendlyMessages;

    protected $description = 'Upgrades the database to the latest version.';
    protected $signature   = 'firefly-iii:upgrade-database {--F|force : Force all upgrades.}';

    /**
     * Execute the console command.
     */
    public function handle(): int
    {
        $this->callInitialCommands();
        $commands = [
            'upgrade:480-transaction-identifiers',
            'upgrade:480-migrate-to-groups',
            'upgrade:480-account-currencies',
            'upgrade:480-transfer-currencies',
            'upgrade:480-currency-information',
            'upgrade:480-notes',
            'upgrade:480-attachments',
            'upgrade:480-bills-to-rules',
            'upgrade:480-budget-limit-currencies',
            'upgrade:480-cc-liabilities',
            'upgrade:480-journal-meta-data',
            'upgrade:480-account-meta',
            'upgrade:481-recurrence-meta',
            'upgrade:500-tag-locations',
            'upgrade:560-liabilities',
            'upgrade:600-liabilities',
            'upgrade:550-budget-limit-periods',
            'upgrade:600-rule-actions',
            'upgrade:610-account-balance',
            'upgrade:610-currency-preferences',
            'upgrade:610-curr
...[truncated]...

### app/Api/V1/Controllers/Insight/Income/TagController.php
<?php

/*
 * TagController.php
 * Copyright (c) 2021 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Controllers\Insight\Income;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Api\V1\Requests\Insight\GenericRequest;
use FireflyIII\Enums\TransactionTypeEnum;
use FireflyIII\Helpers\Collector\GroupCollectorInterface;
use FireflyIII\Repositories\Tag\TagRepositoryInterface;
use FireflyIII\Support\Facades\Amount;
use FireflyIII\Support\Facades\Steam;
use Illuminate\Http\JsonResponse;

/**
 * Class TagController
 */
final class TagController extends Controller
{
    private TagRepositoryInterface $repository;

    /**
     * TagController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            $user             = auth()->user();
            $this->repository = app(TagRepositoryInterface::class);
            $this->repository->setUser($user);

            return $next($request);
        });
    }

    /**
     * Expenses for no tag filtered by account.
     */
    public function noTag(GenericRequest $request): JsonResponse
    {
        $accounts         = $request->getAssetAccounts();
        $start            = $request->getStart();
        $end              = $request->getEnd();
        $response         = [];
        $convertToPrimary = Amount::convertToPrimary();
        $primary          = Amount::getPrimaryCurrency();

        // collect all expenses in this period (regardless of type) by the given bills and accounts.
        $collector        = app(GroupCollectorInterface::class);
        $collector->setTypes([TransactionTypeEnum::DEPOSIT->value])->setRange($start, $end)->setDestinationAccounts($accounts);
        $collector->withoutTags();

        $genericSet       = $colle
...[truncated]...

### app/Api/V1/Controllers/Models/AvailableBudget/ShowController.php
<?php

/*
 * ShowController.php
 * Copyright (c) 2021 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Controllers\Models\AvailableBudget;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Api\V1\Requests\Generic\PaginationDateRangeRequest;
use FireflyIII\Models\AvailableBudget;
use FireflyIII\Repositories\Budget\AvailableBudgetRepositoryInterface;
use FireflyIII\Support\JsonApi\Enrichments\AvailableBudgetEnrichment;
use FireflyIII\Transformers\AvailableBudgetTransformer;
use FireflyIII\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Pagination\LengthAwarePaginator;
use League\Fractal\Pagination\IlluminatePaginatorAdapter;
use League\Fractal\Resource\Collection as FractalCollection;
use League\Fractal\Resource\Item;

/**
 * Class ShowController
 */
final class ShowController extends Controller
{
    private AvailableBudgetRepositoryInterface $abRepository;

    /**
     * AvailableBudgetController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            /** @var User $user */
            $user               = auth()->user();
            $this->abRepository = app(AvailableBudgetRepositoryInterface::class);
            $this->abRepository->setUser($user);

            return $next($request);
        });
    }

    /**
     * This endpoint is documented at:
     * https://api-docs.firefly-iii.org/?urls.primaryName=2.0.0%20(v1)#/available_budgets/getAvailableBudget
     *
     * Display a listing of the resource.
     */
    public function index(PaginationDateRangeRequest $request): JsonResponse
    {
        $manager                                                                                    = $this->getManager();
        ['limit' => $limit, 'offset' => $offset, 'page' 
...[truncated]...

### app/Api/V1/Controllers/Models/TransactionCurrency/ShowController.php
<?php

/*
 * ShowController.php
 * Copyright (c) 2021 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Controllers\Models\TransactionCurrency;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Models\TransactionCurrency;
use FireflyIII\Repositories\Currency\CurrencyRepositoryInterface;
use FireflyIII\Support\Http\Api\AccountFilter;
use FireflyIII\Support\Http\Api\TransactionFilter;
use FireflyIII\Transformers\CurrencyTransformer;
use FireflyIII\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Pagination\LengthAwarePaginator;
use League\Fractal\Pagination\IlluminatePaginatorAdapter;
use League\Fractal\Resource\Collection as FractalCollection;
use League\Fractal\Resource\Item;

/**
 * Class ShowController
 */
final class ShowController extends Controller
{
    use AccountFilter;
    use TransactionFilter;

    private CurrencyRepositoryInterface $repository;

    /**
     * CurrencyRepository constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            $this->repository = app(CurrencyRepositoryInterface::class);
            $this->repository->setUser(auth()->user());

            return $next($request);
        });
    }

    /**
     * This endpoint is documented at:
     * https://api-docs.firefly-iii.org/?urls.primaryName=2.0.0%20(v1)#/currencies/listCurrency
     *
     * Display a listing of the resource.
     */
    public function index(): JsonResponse
    {
        $pageSize    = $this->parameters->get('limit');
        $collection  = $this->repository->getAll();
        $count       = $collection->count();

        // slice them:
        $currencies  = $collection->slice(($this->parameters->get('page') - 1) * $pageSize, $pageSize);
        $paginator   = new LengthAwarePag
...[truncated]...

### app/Events/Model/Webhook/WebhookMessagesRequestSending.php
<?php

declare(strict_types=1);

/*
 * WebhookMessagesRequestSending.php
 * Copyright (c) 2026 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

namespace FireflyIII\Events\Model\Webhook;

use FireflyIII\Events\Event;
use Illuminate\Queue\SerializesModels;

class WebhookMessagesRequestSending extends Event
{
    use SerializesModels;
}

### tests/unit/Support/Calendar/CalculatorProvider.php
<?php

/*
 * CalculatorProvider.php
 * Copyright (c) 2023 Antonio Spinelli <https://github.com/tonicospinelli>
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace Tests\unit\Support\Calendar;

use Carbon\Carbon;
use FireflyIII\Support\Calendar\Periodicity;
use Generator;
use Tests\unit\Support\Calendar\Periodicity\IntervalProvider;

readonly class CalculatorProvider
{
    public string $label;

    private function __construct(
        public IntervalProvider $intervalProvider,
        public Periodicity $periodicity,
        public int $skip = 0
    ) {
        $this->label = "{$this->periodicity->name} {$this->intervalProvider->label}";
    }

    public static function from(Periodicity $periodicity, IntervalProvider $interval, int $skip = 0): self
    {
        return new self($interval, $periodicity, $skip);
    }

    public static function providePeriodicityWithSkippedIntervals(): Generator
    {
        $intervals = [
            self::from(Periodicity::Daily, new IntervalProvider(Carbon::now(), Carbon::now()->addDays(2)), 1),
            self::from(Periodicity::Daily, new IntervalProvider(Carbon::now(), Carbon::now()->addDays(3)), 2),
            self::from(Periodicity::Daily, new IntervalProvider(Carbon::parse('2023-01-31'), Carbon::parse('2023-02-11')), 10),

            self::from(Periodicity::Weekly, new IntervalProvider(Carbon::now(), Carbon::now()->addWeeks(3)), 2),
            self::from(Periodicity::Weekly, new IntervalProvider(Carbon::parse('2023-01-31'), Carbon::parse('2023-02-14')), 1),

            self::from(Periodicity::Fortnightly, new IntervalProvider(Carbon::now(), Carbon::now()->addWeeks(4)), 1),
            self::from(Periodicity::Fortnightly, new IntervalProvider(Carbon::parse('2023-01-29'), Carbon::parse('2023-02-26')), 1),
            self::from(Periodicity::Fortnightly, new IntervalProvider(Carbon::parse(
...[truncated]...

### app/Validation/Account/LiabilityValidation.php
<?php

/*
 * LiabilityValidation.php
 * Copyright (c) 2021 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Validation\Account;

use FireflyIII\Enums\AccountTypeEnum;
use FireflyIII\Models\Account;
use FireflyIII\Models\AccountType;
use Illuminate\Support\Facades\Log;

/**
 * Trait LiabilityValidation
 */
trait LiabilityValidation
{
    protected function validateLCDestination(array $array): bool
    {
        Log::debug('Now in validateLCDestination', $array);
        $result      = null;
        $accountId   = $array['id'] ?? null;
        $accountName = $array['name'] ?? null;
        $validTypes  = config('firefly.valid_liabilities');

        // if the ID is not null the source account should be a dummy account of the type liability credit.
        // the ID of the destination must belong to a liability.
        if (null !== $accountId) {
            if (AccountTypeEnum::LIABILITY_CREDIT->value !== $this->source?->accountType?->type) {
                Log::error('Source account is not a liability.');

                return false;
            }
            $result = $this->findExistingAccount($validTypes, $array);
            if (null === $result) {
                Log::error('Destination account is not a liability.');

                return false;
            }

            return true;
        }

        if (null !== $accountName && '' !== $accountName) {
            Log::debug('Destination ID is null, now we can assume the destination is a (new) liability credit account.');

            return true;
        }
        Log::error('Destination ID is null, but destination name is also NULL.');

        return false;
    }

    /**
     * Source of a liability credit must be a liability or liability credit account.
     */
    protected function validateLCSource(array $array): bool
    {
        
...[truncated]...

### app/Api/V1/Controllers/Models/BudgetLimit/ShowController.php
<?php

/*
 * ShowController.php
 * Copyright (c) 2021 james@firefly-iii.org
 *
 * This file is part of Firefly III (https://github.com/firefly-iii).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Controllers\Models\BudgetLimit;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Api\V1\Requests\DateRangeRequest;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Models\Budget;
use FireflyIII\Models\BudgetLimit;
use FireflyIII\Repositories\Budget\BudgetLimitRepositoryInterface;
use FireflyIII\Repositories\Budget\BudgetRepositoryInterface;
use FireflyIII\Support\JsonApi\Enrichments\BudgetEnrichment;
use FireflyIII\Support\JsonApi\Enrichments\BudgetLimitEnrichment;
use FireflyIII\Transformers\BudgetLimitTransformer;
use FireflyIII\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Pagination\LengthAwarePaginator;
use League\Fractal\Pagination\IlluminatePaginatorAdapter;
use League\Fractal\Resource\Collection as FractalCollection;
use League\Fractal\Resource\Item;

/**
 * Class ShowController
 */
final class ShowController extends Controller
{
    private BudgetLimitRepositoryInterface $blRepository;
    private BudgetRepositoryInterface $repository;

    /**
     * BudgetLimitController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            /** @var User $user */
            $user               = auth()->user();
            $this->repository   = app(BudgetRepositoryInterface::class);
            $this->blRepository = app(BudgetLimitRepositoryInterface::class);
            $this->repository->setUser($user);
            $this->blRepository->setUser($user);

            return $next($request);
     
...[truncated]...