# Models/services
### tests/integration/Api/Models/Account/ListControllerTest.php
<?php

/*
 * AccountControllerTest.php
 * Copyright (c) 2025 james@firefly-iii.org
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

namespace Tests\integration\Api\Models\Account;

use FireflyIII\Enums\AccountTypeEnum;
use FireflyIII\Factory\AttachmentFactory;
use FireflyIII\Models\Account;
use FireflyIII\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Override;
use Tests\integration\TestCase;

/**
 * @internal
 *
 * @covers \FireflyIII\Api\V1\Controllers\Models\Account\ListController
 */
final class ListControllerTest extends TestCase
{
    use RefreshDatabase;

    private User $user;
    private Account $account;

    public function testIndex(): void
    {
        $this->actingAs($this->user);
        $response = $this->getJson(route('api.v1.accounts.attachments', ['account' => $this->account->id]));
        $response->assertOk();
        $response->assertJson(['meta' => ['pagination' => ['total' => 2, 'total_pages' => 1]]]);
    }

    public function testIndexCanChangePageSize(): void
    {
        $this->actingAs($this->user);
        $response = $this->getJson(route('api.v1.accounts.attachments', ['account' => $this->account->id, 'limit' => 1]));
        $response->assertOk();
        $response->assertJson(['meta' => ['pagination' => ['total' => 2, 'total_pages' => 2]]]);
    }

    #[Override]
    protected function setUp(): void
    {
        parent::setUp();

        $this->user    = $this->createAuthenticatedUser();
        $this->actingAs($this->user);

        $this->account = Account::factory()->for($this->user)->withType(AccountTypeEnum::ASSET)->create();
        app(AttachmentFactory::class)
            ->setUser($this->user)
            ->create([
                'filename'        => 'test 1',
                'title'           => 'test 1',
                'attachable_type' => Account::class,
                'att
...[truncated]...

### tests/integration/Api/Models/Account/ShowControllerTest.php
<?php

/*
 * AccountControllerTest.php
 * Copyright (c) 2025 james@firefly-iii.org
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

namespace Tests\integration\Api\Models\Account;

use FireflyIII\Enums\AccountTypeEnum;
use FireflyIII\Models\Account;
use FireflyIII\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Override;
use Tests\integration\TestCase;

/**
 * @internal
 *
 * @covers \FireflyIII\Api\V1\Controllers\Models\Account\ShowController
 */
final class ShowControllerTest extends TestCase
{
    use RefreshDatabase;

    private User $user;

    public function testIndex(): void
    {
        $this->actingAs($this->user);
        $response = $this->getJson(route('api.v1.accounts.index'));
        $response->assertOk();
        $response->assertJson(['meta' => ['pagination' => ['total' => 5]]]);
    }

    public function testIndexCanFilterOnAccountType(): void
    {
        $this->actingAs($this->user);
        $response = $this->getJson(route('api.v1.accounts.index').'?type=asset');
        $response->assertOk();
        $response->assertJson([
            'data' => [['attributes' => ['type' => 'asset']], ['attributes' => ['type' => 'asset']]],
            'meta' => ['pagination' => ['total' => 2]],
        ]);
    }

    public function testIndexFailsOnUnknownAccountType(): void
    {
        $this->actingAs($this->user);
        $response = $this->getJson(route('api.v1.accounts.index').'?type=foobar');
        $response->assertUnprocessable();
        $response->assertJson(['errors' => ['type' => ['The selected type is invalid.']]]);
    }

    #[Override]
    protected function setUp(): void
    {
        parent::setUp();

        $this->user = $this->createAuthenticatedUser();
        $this->actingAs($this->user);

        Account::factory()->for($this->user)->withType(AccountTypeEnum::ASSET)->create();
        Account:
...[truncated]...

### app/Api/V1/Requests/Models/UserGroup/UpdateRequest.php
<?php

/*
 * UpdateRequest.php
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

namespace FireflyIII\Api\V1\Requests\Models\UserGroup;

use FireflyIII\Support\Request\ChecksLogin;
use FireflyIII\Support\Request\ConvertsDataTypes;
use Illuminate\Foundation\Http\FormRequest;

/**
 * Class UpdateRequest
 */
class UpdateRequest extends FormRequest
{
    use ChecksLogin;
    use ConvertsDataTypes;

    protected array $acceptedRoles = [];

    public function getData(): array
    {
        $fields = [
            'title'                 => ['title', 'convertString'],
            'primary_currency_id'   => ['primary_currency_id', 'convertInteger'],
            'primary_currency_code' => ['primary_currency_code', 'convertString'],
        ];

        return $this->getAllData($fields);
    }

    /**
     * Rules for this request.
     */
    public function rules(): array
    {
        return [
            'title'                 => ['required', 'min:1', 'max:255'],
            'primary_currency_id'   => 'exists:transaction_currencies,id',
            'primary_currency_code' => 'exists:transaction_currencies,code',
        ];
    }
}

### app/Api/V1/Controllers/Models/UserGroup/ShowController.php
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

namespace FireflyIII\Api\V1\Controllers\Models\UserGroup;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Models\UserGroup;
use FireflyIII\Repositories\Webhook\WebhookRepositoryInterface;
use FireflyIII\Transformers\UserGroupTransformer;
use Illuminate\Http\JsonResponse;

/**
 * Class ShowController
 */
final class ShowController extends Controller
{
    public const string RESOURCE_KEY = 'user_groups';

    private WebhookRepositoryInterface $repository;

    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            $this->repository = app(WebhookRepositoryInterface::class);
            $this->repository->setUser(auth()->user());

            return $next($request);
        });
    }

    public function show(UserGroup $userGroup): JsonResponse
    {
        $transformer = new UserGroupTransformer();
        $transformer->setParameters($this->parameters);

        return response()->api($this->jsonApiObject(self::RESOURCE_KEY, $userGroup, $transformer))->header('Content-Type', self::CONTENT_TYPE);
    }
}

### app/Api/V1/Controllers/Models/UserGroup/IndexController.php
<?php

/*
 * IndexController.php
 * Copyright (c) 2024 james@firefly-iii.org.
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
 * along with this program.  If not, see https://www.gnu.org/licenses/.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Controllers\Models\UserGroup;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Api\V1\Requests\PaginationRequest;
use FireflyIII\Repositories\UserGroup\UserGroupRepositoryInterface;
use FireflyIII\Transformers\UserGroupTransformer;
use Illuminate\Http\JsonResponse;
use Illuminate\Pagination\LengthAwarePaginator;

final class IndexController extends Controller
{
    public const string RESOURCE_KEY = 'user_groups';

    private UserGroupRepositoryInterface $repository;

    /**
     * AccountController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            $this->repository = app(UserGroupRepositoryInterface::class);

            return $next($request);
        });
    }

    public function index(PaginationRequest $request): JsonResponse
    {
        $administrations                                          = $this->repository->get();
        ['page' => $page, 'limit' => $limit, 'offset' => $offset] = $request->attributes->all();
        $count                                                    = $administrations->count();
        $administrations                                          = $administrations->slice($offset, $limit);
        $paginator                                                = new LengthAwarePaginator($administrations, $count, $limit, $page);
        $transformer                                              = new UserGroupTransformer();

        return response()->json($this->jsonApiList(self::RESOURCE_KEY, $paginator, $transformer))->header('Content-Type', self::CONTENT_TYPE);
    }
}

### app/Api/V1/Controllers/Models/UserGroup/UpdateController.php
<?php

/*
 * UpdateController.php
 * Copyright (c) 2025 james@firefly-iii.org.
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
 * along with this program.  If not, see https://www.gnu.org/licenses/.
 */

declare(strict_types=1);

namespace FireflyIII\Api\V1\Controllers\Models\UserGroup;

use FireflyIII\Api\V1\Controllers\Controller;
use FireflyIII\Api\V1\Requests\Models\UserGroup\UpdateRequest;
use FireflyIII\Models\UserGroup;
use FireflyIII\Repositories\UserGroup\UserGroupRepositoryInterface;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Transformers\UserGroupTransformer;
use Illuminate\Http\JsonResponse;
use Illuminate\Support\Facades\Log;

final class UpdateController extends Controller
{
    public const string RESOURCE_KEY = 'user_groups';

    private UserGroupRepositoryInterface $repository;

    /**
     * AccountController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            $this->repository = app(UserGroupRepositoryInterface::class);

            return $next($request);
        });
    }

    public function update(UpdateRequest $request, UserGroup $userGroup): JsonResponse
    {
        Log::debug(sprintf('Now in %s', __METHOD__));
        $data        = $request->getData();
        $userGroup   = $this->repository->update($userGroup, $data);
        $userGroup->refresh();
        Preferences::mark();

        $transformer = new UserGroupTransformer();
        $transformer->setParameters($this->parameters);

        return response()->api($this->jsonApiObject(self::RESOURCE_KEY, $userGroup, $transformer))->header('Content-Type', self::CONTENT_TYPE);
    }
}

### app/Providers/RouteServiceProvider.php
<?php

/**
 * RouteServiceProvider.php
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

namespace FireflyIII\Providers;

use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;
use Override;

/**
 * Class RouteServiceProvider
 */
class RouteServiceProvider extends ServiceProvider
{
    public const string HOME = '/';

    protected $namespace     = '';

    /**
     * Define the routes for the application.
     */
    #[Override]
    public function boot(): void
    {
        //        $this->routes(function (): void {
        //            Route::prefix('api')
        //                ->middleware('api')
        //                ->namespace($this->namespace)
        //                ->group(base_path('routes/api.php'))
        //            ;
        //            Route::prefix('api/v1/cron')
        //                ->middleware('api_basic')
        //                ->namespace($this->namespace)
        //                ->group(base_path('routes/api-noauth.php'))
        //            ;
        //            Route::middleware('web')->namespace($this->namespace)->group(base_path('routes/web.php'));
        //        });
    }
}

### app/Repositories/Journal/JournalAPIRepository.php
<?php

/**
 * JournalAPIRepository.php
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

namespace FireflyIII\Repositories\Journal;

use FireflyIII\Models\Attachment;
use FireflyIII\Models\PiggyBank;
use FireflyIII\Models\PiggyBankEvent;
use FireflyIII\Models\Transaction;
use FireflyIII\Models\TransactionJournal;
use FireflyIII\Support\Repositories\UserGroup\UserGroupInterface;
use FireflyIII\Support\Repositories\UserGroup\UserGroupTrait;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Storage;

/**
 * Class JournalAPIRepository
 */
class JournalAPIRepository implements JournalAPIRepositoryInterface, UserGroupInterface
{
    use UserGroupTrait;

    /**
     * Returns transaction by ID. Used to validate attachments.
     */
    public function findTransaction(int $transactionId): ?Transaction
    {
        return Transaction::leftJoin('transaction_journals', 'transaction_journals.id', '=', 'transactions.transaction_journal_id')
            ->where('transaction_journals.user_id', $this->user->id)
            ->where('transactions.id', $transactionId)
            ->first(['transactions.*'])
        ;
    }

    /**
     * TODO pretty sure method duplicated.
     *
     * Return all attachments for journal.
     */
    public function getAttachments(TransactionJournal $journal): Collection
    {
        $set  = $journal->attachments;

        $disk = Storage::disk('upload');

        return $set->each(static function (Attachment $attachment) use ($disk): Attachment {
            $notes                   = $attachment->notes()->first();
            $attachment->file_exists = $disk->exists($attachment->fileName());
            $attachment->notes_text  = null !== $notes ? $notes->text : ''; // TODO should not set notes like this.

            return $attachment;
        });
    }

    pub
...[truncated]...

### app/Repositories/Journal/JournalAPIRepositoryInterface.php
<?php

/**
 * JournalAPIRepositoryInterface.php
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

namespace FireflyIII\Repositories\Journal;

use FireflyIII\Enums\UserRoleEnum;
use FireflyIII\Models\Transaction;
use FireflyIII\Models\TransactionJournal;
use FireflyIII\Models\UserGroup;
use FireflyIII\User;
use Illuminate\Contracts\Auth\Authenticatable;
use Illuminate\Support\Collection;

/**
 * Interface JournalAPIRepositoryInterface
 *
 * @method setUserGroup(UserGroup $group)
 * @method getUserGroup()
 * @method getUser()
 * @method checkUserGroupAccess(UserRoleEnum $role)
 * @method setUser(null|Authenticatable|User $user)
 * @method setUserGroupById(int $userGroupId)
 */
interface JournalAPIRepositoryInterface
{
    /**
     * Returns transaction by ID. Used to validate attachments.
     */
    public function findTransaction(int $transactionId): ?Transaction;

    /**
     * Return all attachments for journal.
     */
    public function getAttachments(TransactionJournal $journal): Collection;

    /**
     * Return all journal links for journal.
     */
    public function getJournalLinks(TransactionJournal $journal): Collection;

    /**
     * Get all piggy bank events for a journal.
     */
    public function getPiggyBankEvents(TransactionJournal $journal): Collection;
}

### app/Api/V1/Requests/AggregateFormRequest.php
<?php

/*
 * Copyright (c) 2025 https://github.com/ctrl-f5
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

namespace FireflyIII\Api\V1\Requests;

use Illuminate\Contracts\Validation\Validator;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Http\Request;
use Override;
use RuntimeException;

abstract class AggregateFormRequest extends ApiRequest
{
    /**
     * @var Request[]
     */
    protected array $requests      = [];

    protected array $acceptedRoles = [];

    #[Override]
    public function initialize(
        array $query = [],
        array $request = [],
        array $attributes = [],
        array $cookies = [],
        array $files = [],
        array $server = [],
        $content = null
    ): void {
        parent::initialize($query, $request, $attributes, $cookies, $files, $server, $content);

        // instantiate all subrequests and share current requests' bags with them
        // Log::debug('Initializing AggregateFormRequest.');

        /** @var array|string $config */
        foreach ($this->getRequests() as $config) {
            $requestClass         = is_array($config) ? array_shift($config) : $config;

            if (!is_a($requestClass, Request::class, true)) {
                throw new RuntimeException('getRequests() must return class-strings of subclasses of Request');
            }
            // Log::debug(sprintf('Initializing subrequest %s', $requestClass));

            $instance             = new $requestClass();
            $this->requests[]     = $instance;
            $instance->request    = $this->request;
            $instance->query      = $this->query;
            $instance->attributes = $this->attributes;
            $instance->cookies    = $this->cookies;
            $instance->files      = $this->files;
            $instance->server     = $this->server;
            $instance->hea
...[truncated]...

### app/Support/Http/Controllers/ModelInformation.php
<?php

/**
 * ModelInformation.php
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

namespace FireflyIII\Support\Http\Controllers;

use FireflyIII\Enums\AccountTypeEnum;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Models\AccountType;
use FireflyIII\Models\Bill;
use FireflyIII\Models\Tag;
use FireflyIII\Models\Transaction;
use FireflyIII\Models\TransactionJournal;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use Illuminate\Support\Facades\Log;
use Throwable;

/**
 * Trait ModelInformation
 */
trait ModelInformation
{
    /**
     * Get actions based on a bill.
     *
     * @throws FireflyException
     */
    protected function getActionsForBill(Bill $bill): array // get info and argument
    {
        try {
            $result = view('rules.partials.action', [
                'oldAction'  => 'link_to_bill',
                'oldValue'   => $bill->name,
                'oldChecked' => false,
                'count'      => 1,
            ])->render();
        } catch (Throwable $e) {
            Log::error(sprintf('Throwable was thrown in getActionsForBill(): %s', $e->getMessage()));
            Log::error($e->getTraceAsString());
            $result = 'Could not render view. See log files.';

            throw new FireflyException($result, 0, $e);
        }

        return [$result];
    }

    /**
     * @return string[]
     *
     * @psalm-return array<int|null, string>
     */
    protected function getLiabilityTypes(): array
    {
        /** @var AccountRepositoryInterface $repository */
        $repository     = app(AccountRepositoryInterface::class);

        // types of liability:
        /** @var AccountType $debt */
        $debt           = $repository->getAccountTypeByType(AccountTypeEnum::DEBT->value);

        /** @var AccountType $loan */
        $lo
...[truncated]...

### app/Support/Http/Controllers/RequestInformation.php
<?php

/**
 * RequestInformation.php
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

namespace FireflyIII\Support\Http\Controllers;

use Carbon\Carbon;
use FireflyIII\Exceptions\ValidationException;
use FireflyIII\Http\Requests\RuleFormRequest;
use FireflyIII\Http\Requests\TestRuleFormRequest;
use FireflyIII\Support\Binder\AccountList;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\User;
use Illuminate\Contracts\Validation\Validator as ValidatorContract;
use Illuminate\Routing\Route;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Route as RouteFacade;
use Illuminate\Support\Facades\Validator;

use function Safe\parse_url;

/**
 * Trait RequestInformation
 */
trait RequestInformation
{
    /**
     * Get the domain of FF system.
     */
    final protected function getDomain(): string // get request info
    {
        $url   = url()->to('/');
        $parts = parse_url($url);

        return $parts['host'] ?? '';
    }

    final protected function getPageName(): string // get request info
    {
        return str_replace('.', '_', RouteFacade::currentRouteName());
    }

    /**
     * Get the specific name of a page for intro.
     */
    final protected function getSpecificPageName(): string // get request info
    {
        /** @var null|string $param */
        $param = RouteFacade::current()->parameter('objectType');

        return null === $param ? '' : sprintf('_%s', $param);
    }

    /**
     * Get a list of triggers.
     */
    final protected function getValidTriggerList(TestRuleFormRequest $request): array // process input
    {
        $triggers = [];
        $data     = $request->get('triggers');
        if (is_array($data)) {
            foreach ($data as $triggerInfo) {
                $current    = [
                    'type'            => $trig
...[truncated]...

### resources/views/v2/partials/form/title.blade.php
<div class="row mb-3">
    <label for="title" class="col-sm-1 col-form-label d-none d-sm-block">
        <em title="{{ __('firefly.title') }}" class="fa-solid fa-font"></em>
    </label>
    <div class="col-sm-10">
        <input type="text" class="form-control ac-title"
               id="title"
               @change="changedTitle"
               @keyup.enter="submitForm()"
               x-model="title"
               :class="{'is-invalid': errors.title.length > 0, 'form-control': true}"
               placeholder="{{ __('form.title')  }}">
        <template x-if="errors.title.length > 0">
            <div class="invalid-feedback"
                 x-text="errors.title[0]">
            </div>
        </template>
    </div>
</div>