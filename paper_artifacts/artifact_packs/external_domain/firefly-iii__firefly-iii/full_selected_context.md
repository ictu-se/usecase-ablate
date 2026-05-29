# README
## readme.md
[![Packagist][packagist-shield]][packagist-url]
[![License][license-shield]][license-url]
[![Stargazers][stars-shield]][stars-url]
[![Donate][donate-shield]][donate-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://firefly-iii.org/">
    <img src="https://raw.githubusercontent.com/firefly-iii/firefly-iii/develop/.github/assets/img/logo-small.png" alt="Firefly III" width="120" height="178">
  </a>
</p>
  <h1 align="center">Firefly III</h1>

  <p align="center">
    A free and open source personal finance manager
    <br />
    <a href="https://docs.firefly-iii.org/"><strong>Explore the documentation</strong></a>
    <br />
    <br />
    <a href="https://demo.firefly-iii.org/">View the demo</a>
    ·
    <a href="https://github.com/firefly-iii/firefly-iii/issues">Report a bug</a>
    ·
    <a href="https://github.com/firefly-iii/firefly-iii/issues">Request a feature</a>
    ·
    <a href="https://github.com/firefly-iii/firefly-iii/discussions">Ask questions</a>
  </p>

---

<p>
<img align="left" src=".github/assets/img/europe.png" alt="Flag of Europe" height="50"> Billionaires and fascists are breaking democracies and international alliances. Their profits are costing us our safety. (Digital) sovereignty is more important than ever. <strong>Firefly III</strong> is free open source software and originates from, and lives in the European Union (🇳🇱).
</p>

---

<!-- MarkdownTOC autolink="true" -->

- [About Firefly III](#about-firefly-iii)
  - [Purpose](#purpose)
- [Features](#features)
- [Who's it for?](#whos-it-for)
- [The Firefly III eco-system](#the-firefly-iii-eco-system)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Support the development of Firefly III](#support-the-development-of-firefly-iii)
- [License](#license)
- [Do you need help, or do you want to get in touch?](#do-you-need-help-or-do-you-want-to-get-in-touch)
- [Acknowledgements](#acknowledgements)

<!-- /MarkdownTOC -->

## About Firefly III

<p align="center">
	<img src="https://raw.githubusercontent.com/firefly-iii/firefly-iii/develop/.github/assets/img/imac-complete.png" alt="Firefly III on iMac" />
</p>

"Firefly III" is a (self-hosted) manager for your personal finances. It can help you keep track of your expenses and income, so you can spend less and save more. Firefly III supports the use of budgets, categories and tags. Using a bunch of external tools, you can import data. It also has many neat financial reports available.

Firefly III should give you **insight** into and **control** over your finances. Money should be useful, not scary. You should be able to *see* where it is going, to *feel* your expenses and to... wow, I'm going overboard with this aren't I?

But you get the idea: this is your money. These are your expenses. Stop them from controlling you. I built this tool because I started to dislike money. Having money, not having money, paying bills with money, you get the idea. But no more. I want to feel "safe", whatever my balance is. And I hope this tool can help you. I know it helps me.

### Purpose

<p align="center">
  <img src="https://raw.githubusercontent.com/firefly-iii/firefly-iii/develop/.github/assets/img/ipad-complete.png" alt="Firefly III on iPad" width="600">
</p>

Personal financial management is pretty difficult, and everybody has their own approach to it. Some people make budgets, other people limit their cashflow by throwing away their credit cards, others try to increase their current cashflow. There are tons of ways to save and earn money. Firefly III works on the principle that if you know where your money is going, you can stop it from going there.

By keeping track of your expenses and your income you can budget accordingly and save money. Stop living from paycheck to paycheck but give yourself the financial wiggle room you need.

You can read more about the purpose of Firefly III in the [documentation](https://docs.firefly-iii.org/).

## Features

Firefly III is pretty feature packed. Some important stuff first:

* It is completely self-hosted and isolated, and will never contact external servers until you explicitly tell it to.
* It features a REST JSON API that covers almost every part of Firefly III.

The most exciting features are:

* Create [recurring transactions to manage your money](https://docs.firefly-iii.org/explanation/financial-concepts/recurring/).
* [Rule based transaction handling](https://docs.firefly-iii.org/how-to/firefly-iii/features/rules/) with the ability to create your own rules.

Then the things that make you go "yeah OK, makes sense".

* A [double-entry](https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system) bookkeeping system.
* Save towards a goal using [piggy banks](https://docs.firefly-iii.org/explanation/financial-concepts/piggy-banks/).
* View [income and expense reports](https://docs.firefly-iii.org/how-to/firefly-iii/finances/reports/).

And the things you would hope for but not expect:

* 2 factor authentication for extra security 🔒.
* Supports [any currency you want](https://docs.firefly-iii.org/how-to/firefly-iii/features/currencies/).
* There is a [Docker image](https://docs.firefly-iii.org/how-to/firefly-iii/installation/docker/).

And to organise everything:

* Clear views that should show you how you're doing.
* Easy navigation through your records.
* Lots of charts because we all love them.

Many more features are listed in the [documentation](https://docs.firefly-iii.org/explanation/firefly-iii/about/introduction/).

## Who's it for?
<img src="https://raw.githubusercontent.com/firefly-iii/firefly-iii/develop/.github/assets/img/iphone-complete.png" alt="Firefly III on iPhone" align="left" width="250">

 This application is for people who want to track their finances, keep an eye on their money **without having to upload their financial records to the cloud**. You're a bit tech-savvy, you like open source software and you don't mind tinkering with (self-hosted) servers.
 
 <br clear="left"/>

## The Firefly III eco-system

Several users have built pretty awesome stuff around the Firefly III API. [Check out these tools in the documentation](https://docs.firefly-iii.org/references/firefly-iii/third-parties/apps/).

## Getting Started

There are many ways to run Firefly III
1. There is a [demo site](https://demo.firefly-iii.org) with an example financial administration already present.
2. You can [install it on your server](https://docs.firefly-iii.org/how-to/firefly-iii/installation/self-managed/).
3. You can [run it using Docker](https://docs.firefly-iii.org/how-to/firefly-iii/installation/docker/).
4. You can [deploy via Kubernetes](https://firefly-iii.github.io/kubernetes/).
5. You can [install it using Softaculous](https://www.softaculous.com/softaculous/apps/others/Firefly_III).
6. You can [install it using AMPPS](https://www.ampps.com/).
7. You can [install it on Cloudron](https://cloudron.io/store/org.fireflyiii.cloudronapp.html).
8. You can [install it on Lando](https://gist.github.com/ArtisKrumins/ccb24f31d6d4872b57e7c9343a9d1bf0).
9. You can [install it on Yunohost](https://github.com/YunoHost-Apps/firefly-iii).

## Contributing

You can contact me at [james@firefly-iii.org](mailto:james@firefly-iii.org), you may open an issue in the [main repository](https://github.com/firefly-iii/firefly-iii) or contact me through [gitter](https://gitter.im/firefly-iii/firefly-iii) and [Mastodon](https://fosstodon.org/@ff3).

Of course, there are some [contributing guidelines](https://docs.firefly-iii.org/explanation/support/#contributing-code) and a [code of conduct](https://github.com/firefly-iii/firefly-iii/blob/main/.github/code_of_conduct.md), which I invite you to check out.

I can always use your help [squashing bugs](https://docs.firefly-iii.org/explanation/support/), thinking about [new features](https://docs.firefly-iii.org/explanation/support/) or [translating Firefly III](https://docs.firefly-iii.org/how-to/firefly-iii/development/translations/) into other languages.

[Sonarcloud][sc-project-url] scans the code of Firefly III. If you want to help improve Firefly III, check out the latest reports and take your pick!

[![Quality Gate Status][sc-gate-shield]][sc-project-url] [![Bugs][sc-bugs-shield]][sc-project-url] [![Code Smells][sc-smells-shield]][sc-project-url] [![Vulnerabilities][sc-vuln-shield]][sc-project-url]

There is also a [security policy](https://github.com/firefly-iii/firefly-iii/security/policy).

[![CII Best Practices][bp-badge]][bp-url]

<!-- SPONSOR TEXT -->

## Support the development of Firefly III

Firefly III is a side gig. With your sponsorship or support, I can spend more time on Firefly III. So, if you like Firefly III, and if it helps you save lots of money, why not send me a dime for every dollar saved! 🥳

OK, that was a joke. But for real, when you feel Firefly III made your life better, please consider contributing as a sponsor. Please check out my [Patreon](https://www.patreon.com/jc5) and [GitHub Sponsors](https://github.com/sponsors/JC5) page for more information. You can also [buy me a ☕️ coffee at ko-fi.com](https://ko-fi.com/Q5Q5R4SH1) or send something my way using [Liberapay](https://liberapay.com/JC5). Thank you for your consideration.

### Sponsorships

Firefly III is sponsored by TestMu AI. Their support allows me to test Firefly III more easily and introduce even fewer bugs with every release.

Browser testing via:

<a href="https://www.testmuai.com/?utm_source=fireflyiii&utm_medium=sponsor" target="_blank">
<img src=".github/assets/img/testmu.png" alt="Testmu" style="vertical-align: middle;" width="250" />
</a>

<!-- END OF SPONSOR TEXT -->

## License

This work [is licensed](https://github.com/firefly-iii/firefly-iii/blob/main/LICENSE) under the [GNU Affero General Public License v3](https://www.gnu.org/licenses/agpl-3.0.html).

<!-- HELP TEXT -->

## Do you need help, or do you want to get in touch?

Do you want to contact me? You can email me at [james@firefly
...[truncated]...

# File tree
.ci
  firefly-iii-standard.yml
  php-cs-fixer
    .php-cs-fixer.php
    composer.json
  phpmd
    composer.json
    phpmd.xml
  rector.php
THANKS.md
agents.md
app
  Api
    V1
      Controllers
        Autocomplete
          AccountController.php
          BillController.php
          BudgetController.php
          CategoryController.php
          CurrencyController.php
          ObjectGroupController.php
          PiggyBankController.php
          RecurrenceController.php
          RuleController.php
          RuleGroupController.php
          TagController.php
          TransactionController.php
          TransactionTypeController.php
        Chart
          AccountController.php
          BalanceController.php
          BudgetController.php
          CategoryController.php
        Controller.php
        Data
          Bulk
          DestroyController.php
          Export
          PurgeController.php
        Insight
          Expense
          Income
          Transfer
        Models
          Account
          Attachment
          AvailableBudget
          Bill
          Budget
          BudgetLimit
          Category
          CurrencyExchangeRate
          ObjectGroup
          PiggyBank
          Recurrence
          Rule
          RuleGroup
          Tag
          Transaction
          TransactionCurrency
          TransactionLink
          TransactionLinkType
          UserGroup
        Search
          AccountController.php
          TransactionController.php
        Summary
          BasicController.php
        System
          AboutController.php
          BatchController.php
          ConfigurationController.php
          CronController.php
          UserController.php
        User
          PreferencesController.php
        Webhook
          AttemptController.php
          DestroyController.php
          MessageController.php
          ShowController.php
          StoreController.php
          SubmitController.php
          UpdateController.php
      Middleware
        ApiDemoUser.php
      Requests
        AggregateFormRequest.php
        ApiRequest.php
        Autocomplete
          AutocompleteApiRequest.php
          AutocompleteRequest.php
          AutocompleteTransactionApiRequest.php
        Chart
          ChartRequest.php
        Data
          Bulk
          DestroyRequest.php
          Export
          SameDateRequest.php
        DateRangeRequest.php
        DateRequest.php
        Generic
          ObjectTypeApiRequest.php
          PaginationDateRangeRequest.php
          QueryRequest.php
          SingleDateRequest.php
        Insight
          GenericRequest.php
        Models
          Account
          Attachment
          AvailableBudget
          Bill
          Budget
          BudgetLimit
          Category
          CurrencyExchangeRate
          ObjectGroup
          PiggyBank
          Recurrence
          Rule
          RuleGroup
          Tag
          Transaction
          TransactionCurrency
          TransactionLink
          TransactionLinkType
          UserGroup
          Webhook
        PaginationRequest.php
        Search
          CountRequest.php
          SearchQueryRequest.php
          TransactionSearchRequest.php
        Summary
          BasicRequest.php
        System
          CronRequest.php
          UpdateRequest.php
          UserStoreRequest.php
          UserUpdateRequest.php
        User
          PreferenceStoreRequest.php
          PreferenceUpdateRequest.php
  Casts
    SeparateTimezoneCaster.php
  Console
    Commands
      Correction
        ClearsEmptyForeignAmounts.php
        ConvertsDatesToUTC.php
        CorrectsAccountOrder.php
        CorrectsAccountTypes.php
        CorrectsAmounts.php
        CorrectsCurrencies.php
        CorrectsDatabase.php
        CorrectsFrontpageAccounts.php
        CorrectsGroupAccounts.php
        CorrectsGroupInformation.php
        CorrectsIbans.php
        CorrectsInvertedBudgetLimits.php
        CorrectsLongDescriptions.php
        CorrectsMetaDataFields.php
        CorrectsOpeningBalanceCurrencies.php
        CorrectsPiggyBanks.php
        CorrectsPreferences.php
        CorrectsPrimaryCurrencyAmounts.php
        CorrectsRecurringTransactions.php
        CorrectsTimezoneInformation.php
        CorrectsTransactionTypes.php
        CorrectsTransferBudgets.php
        CorrectsUnevenAmount.php
        CreatesAccessTokens.php
        CreatesGroupMemberships.php
        CreatesLinkTypes.php
        RemovesBills.php
        RemovesEmptyGroups.php
        RemovesEmptyJournals.php
        RemovesLinksToDeletedObjects.php
        RemovesOrphanedTransactions.php
        RemovesZeroAmount.php
        RestoresOAuthKeys.php
        RollbacksSingleMigration.php
        TriggersCreditCalculation.php
      Explain
        ExplainAvailableBudget.php
      Export
        ExportsData.php
      Integrity
        ReportsEmptyObjects.php
        ReportsIntegrity.php
        ReportsSums.php
        ValidatesEnvironmentVariables.php
        ValidatesFilePermissions.php
      SendTestEmail.php
      ShowsFriendlyMessages.php
      System
        CallsLaravelPassportKeys.php
        CreatesDatabase.php
        CreatesFirstUser.php
        ForcesDecimalSize.php
        ForcesMigrations.php
        OutputsInstructions.php
        OutputsVersion.php
        RecalculatesRunningBalance.php
        ResetsErrorMailLimit.php
        ScansAttachments.php
        SetsLatestVersion.php
        VerifySecurityAlerts.php
      Tools
        ApplyRules.php
        ChecksForUpdates.php
        Cron.php
        VerifiesDatabaseConnection.php
        VerifiesDatabaseConnectionTrait.php
      Upgrade
        AddsTransactionIdentifiers.php
        RemovesDatabaseDecryption.php
        RepairsAccountBalances.php
        RepairsPostgresSequences.php
        UpgradesAccountCurrencies.php
        UpgradesAccountMetaData.php
        UpgradesAttachments.php
        UpgradesBillsToRules.php
        UpgradesBudgetLimitPeriods.php
        UpgradesBudgetLimits.php
        UpgradesCreditCardLiabilities.php
        UpgradesCurrencyPreferences.php
        UpgradesDatabase.php
        UpgradesJournalMetaData.php
        UpgradesJournalNotes.php
        UpgradesLiabilities.php
        UpgradesLiabilitiesEight.php
        UpgradesMultiPiggyBanks.php
        UpgradesPrimaryCurrencyAmounts.php
        UpgradesRecurrenceMetaData.php
        UpgradesRuleActions.php
        UpgradesTagLocations.php
        UpgradesToGroups.php
        UpgradesTransferCurrencies.php
        UpgradesVariousCurrencyInformation.php
        UpgradesWebhooks.php
      VerifiesAccessToken.php
  Enums
  Events
  Exceptions
  Factory
  Generator
  Handlers
  Helpers
  Http
  Jobs
  Listeners
  Mail
  Models
  Notifications
  Providers
  Repositories
  Rules
  Services
  Support
  TransactionRules
  Transformers
  User.php
  Validation
bootstrap
changelog.md
composer.json
config
crowdin.yml
index.php
mago.toml
package-lock.json
package.json
phpunit.xml
readme.md
releases.md
resources
routes
server.php
sonar-project.properties
tests

# Selected code and test snippets
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

### resources/views/v2/partials/form/submission-options.blade.php
<!-- RETURN HERE AFTER CREATE -->
<template x-if="'create' === formBehaviour.formType">
    <div class="form-check">
        <input class="form-check-input" x-model="formStates.returnHereButton" type="checkbox" id="returnButton">
        <label class="form-check-label" for="returnButton"><em class="fa-solid fa-arrow-rotate-left"></em> {{ __('firefly.create_another') }}</label>
    </div>
</template>

<!-- RESET AFTER -->
<template x-if="'create' === formBehaviour.formType">
    <div class="form-check">
        <input class="form-check-input" x-model="formStates.resetButton" type="checkbox" id="resetButton" :disabled="!formStates.returnHereButton">
        <label class="form-check-label" for="resetButton"><em class="fa-regular fa-file"></em> {{ __('firefly.reset_after') }}</label>
    </div>
</template>
<!-- RETURN HERE AFTER UPDATE -->
<template x-if="'update' === formBehaviour.formType">
    <div class="form-check">
        <input class="form-check-input" x-model="formStates.returnHereButton" type="checkbox" id="returnButton">
        <label class="form-check-label" for="returnButton"><em class="fa-solid fa-arrow-rotate-left"></em> {{ __('firefly.after_update_create_another') }}</label>
    </div>
</template>
<!-- CLONE INSTEAD OF UPDATE -->
<template x-if="'update' === formBehaviour.formType">
    <div class="form-check">
        <input class="form-check-input" x-model="formStates.saveAsNewButton" type="checkbox" id="saveAsNewButton">
        <label class="form-check-label" for="saveAsNewButton">{{ __('firefly.store_as_new') }}</label>
    </div>
</template>

### app/Api/V1/Requests/Models/Rule/TestRequest.php
<?php

/**
 * RuleTestRequest.php
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

namespace FireflyIII\Api\V1\Requests\Models\Rule;

use Carbon\Carbon;
use FireflyIII\Support\Request\ChecksLogin;
use FireflyIII\Support\Request\ConvertsDataTypes;
use Illuminate\Foundation\Http\FormRequest;

/**
 * Class TestRequest
 */
class TestRequest extends FormRequest
{
    use ChecksLogin;
    use ConvertsDataTypes;

    protected array $acceptedRoles = [];

    public function getTestParameters(): array
    {
        return ['page' => $this->getPage(), 'start' => $this->getDate('start'), 'end' => $this->getDate('end'), 'accounts' => $this->getAccounts()];
    }

    public function rules(): array
    {
        return [
            'start'      => ['date', 'after:1970-01-02', 'before:2038-01-17'],
            'end'        => ['date', 'after_or_equal:start', 'after:1970-01-02', 'before:2038-01-17'],
            'accounts'   => '',
            'accounts.*' => ['required', 'exists:accounts,id', 'belongsToUser:accounts'],
        ];
    }

    private function getAccounts(): array
    {
        return $this->get('accounts') ?? [];
    }

    private function getDate(string $field): ?Carbon
    {
        $value = $this->query($field);
        if (is_array($value)) {
            return null;
        }
        $value = (string) $value;

        return null === $this->query($field) ? null : Carbon::createFromFormat('Y-m-d', substr($value, 0, 10));
    }

    private function getPage(): int
    {
        return 0 === (int) $this->query('page') ? 1 : (int) $this->query('page');
    }
}

### app/Api/V1/Requests/Models/Tag/StoreRequest.php
<?php

/**
 * TagStoreRequest.php
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
 * You should have received a copy of the GNU Affero 
...[truncated]...