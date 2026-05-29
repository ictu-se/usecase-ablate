# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

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

# Oracle-selected code and test snippets
### app/Http/Controllers/Account/IndexController.php
<?php

/**
 * IndexController.php
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

namespace FireflyIII\Http\Controllers\Account;

use Carbon\Carbon;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Models\Account;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\Support\Http\Controllers\BasicDataSupport;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\Request;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Support\Facades\Log;
use Illuminate\View\View;
use Psr\Container\ContainerExceptionInterface;
use Psr\Container\NotFoundExceptionInterface;

/**
 * Class IndexController
 */
final class IndexController extends Controller
{
    use BasicDataSupport;

    private AccountRepositoryInterface $repository;

    /**
     * IndexController constructor.
     */
    public function __construct()
    {
        parent::__construct();

        // translations:
        $this->middleware(function ($request, $next) {
            app('view')->share('mainTitleIcon', 'fa-credit-card');
            app('view')->share('title', (string) trans('firefly.accounts'));

            $this->repository = app(AccountRepositoryInterface::class);

            return $next($request);
        });
    }

    /**
     * @return Factory|View
     *
     * @throws ContainerExceptionInterface
     * @throws NotFoundExceptionInterface
     */
    public function inactive(Request $request, string $objectType): Factory|\Illuminate\Contracts\View\View
    {
        $inactivePage                  = true;
        $subTitle                      = (string) trans(sprintf('firefly.%s_accounts_inactive', $objectType));
        $subTitleIcon                  = config(sprintf('firefly.subIconsByIdentifi
...[truncated]...

### app/Http/Controllers/Account/CreateController.php
<?php

/**
 * CreateController.php
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

namespace FireflyIII\Http\Controllers\Account;

use FireflyIII\Enums\AccountTypeEnum;
use FireflyIII\Helpers\Attachments\AttachmentHelperInterface;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Http\Requests\AccountFormRequest;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Http\Controllers\ModelInformation;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Illuminate\View\View;

/**
 * Class CreateController
 */
final class CreateController extends Controller
{
    use ModelInformation;

    private AttachmentHelperInterface $attachments;
    private AccountRepositoryInterface $repository;

    /**
     * CreateController constructor.
     */
    public function __construct()
    {
        parent::__construct();

        // translations:
        $this->middleware(function ($request, $next) {
            app('view')->share('mainTitleIcon', 'fa-credit-card');
            app('view')->share('title', (string) trans('firefly.accounts'));

            $this->repository  = app(AccountRepositoryInterface::class);
            $this->attachments = app(AttachmentHelperInterface::class);

            return $next($request);
        });
    }

    /**
     * Create a new account.
     *
     * @return Factory|View
     */
    public function create(Request $request, string $objectType): Factory|\Illuminate\Contracts\View\View
    {
        $subTitleIcon        = config(sprintf('firefly.subIconsByIdentifier.%s', $objectType));
        $subTitle            = (string) trans(sprintf('firefly.make_new_%s_account', $objectType));
        $roles 
...[truncated]...

### app/Http/Controllers/Account/EditController.php
<?php

/**
 * EditController.php
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

namespace FireflyIII\Http\Controllers\Account;

use FireflyIII\Helpers\Attachments\AttachmentHelperInterface;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Http\Requests\AccountFormRequest;
use FireflyIII\Models\Account;
use FireflyIII\Models\Location;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\Support\Http\Controllers\ModelInformation;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Routing\Redirector;
use Illuminate\Support\Facades\Log;
use Illuminate\View\View;

/**
 * Class EditController
 */
final class EditController extends Controller
{
    use ModelInformation;

    private AttachmentHelperInterface $attachments;
    private AccountRepositoryInterface $repository;

    /**
     * EditController constructor.
     */
    public function __construct()
    {
        parent::__construct();

        // translations:
        $this->middleware(function ($request, $next) {
            app('view')->share('mainTitleIcon', 'fa-credit-card');
            app('view')->share('title', (string) trans('firefly.accounts'));

            $this->repository  = app(AccountRepositoryInterface::class);
            $this->attachments = app(AttachmentHelperInterface::class);

            return $next($request);
        });
    }

    /**
     * Edit account overview. It's complex, but it just has a lot of if/then/else.
     *
     * @SuppressWarnings("PHPMD.NPathComplexity")
     *
     * @return Factory|RedirectResponse|View
     */
    public function edit(
        Request $request,
        Account $account,
        AccountRepositoryIn
...[truncated]...

### app/Http/Controllers/Account/ReconcileController.php
<?php

/**
 * ReconcileController.php
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

namespace FireflyIII\Http\Controllers\Account;

use Carbon\Carbon;
use FireflyIII\Enums\AccountTypeEnum;
use FireflyIII\Enums\TransactionTypeEnum;
use FireflyIII\Exceptions\DuplicateTransactionException;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Factory\TransactionGroupFactory;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Http\Requests\ReconciliationStoreRequest;
use FireflyIII\Models\Account;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use FireflyIII\Repositories\Journal\JournalRepositoryInterface;
use FireflyIII\Support\Facades\Navigation;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\User;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\RedirectResponse;
use Illuminate\Routing\Redirector;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Log;
use Illuminate\View\View;

/**
 * Class ReconcileController.
 */
final class ReconcileController extends Controller
{
    private AccountRepositoryInterface $accountRepos;
    private JournalRepositoryInterface $repository;

    /**
     * ReconcileController constructor.
     */
    public function __construct()
    {
        parent::__construct();

        // translations:
        $this->middleware(function ($request, $next) {
            app('view')->share('mainTitleIcon', 'fa-credit-card');
            app('view')->share('title', (string) trans('firefly.accounts'));
            $this->repository   = app(JournalRepositoryInterface::class);
            $this->accountRepos = app(AccountRepositoryInterface::class);

            return $next($request);
        });
    }

    /**
     * Reconciliation overview.
     *
     * @return Factory|Redirect
...[truncated]...

### app/Repositories/Account/AccountRepository.php
<?php

/**
 * AccountRepository.php
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

namespace FireflyIII\Repositories\Account;

use Carbon\Carbon;
use FireflyIII\Enums\AccountTypeEnum;
use FireflyIII\Enums\TransactionTypeEnum;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Factory\AccountFactory;
use FireflyIII\Models\Account;
use FireflyIII\Models\AccountMeta;
use FireflyIII\Models\AccountType;
use FireflyIII\Models\Attachment;
use FireflyIII\Models\Location;
use FireflyIII\Models\TransactionCurrency;
use FireflyIII\Models\TransactionGroup;
use FireflyIII\Models\TransactionJournal;
use FireflyIII\Services\Internal\Destroy\AccountDestroyService;
use FireflyIII\Services\Internal\Update\AccountUpdateService;
use FireflyIII\Support\Facades\Amount;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\Support\Repositories\UserGroup\UserGroupInterface;
use FireflyIII\Support\Repositories\UserGroup\UserGroupTrait;
use Illuminate\Database\Eloquent\Builder as EloquentBuilder;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Storage;
use Override;

use function Safe\json_encode;

/**
 * Class AccountRepository.
 */
class AccountRepository implements AccountRepositoryInterface, UserGroupInterface
{
    use UserGroupTrait;

    public function count(array $types): int
    {
        return $this->user->accounts()->accountTypeIn($types)->count();
    }

    /**
     * Moved here from account CRUD.
     */
    public function destroy(Account $account, ?Account $moveTo): bool
    {
        /** @var AccountDestroyService $service */
        $service = app(AccountDestroyService::class);
        $service->destroy($account, $moveTo);

        return true;
    }

    /**
     * Find account with same name
...[truncated]...

### app/Http/Controllers/Transaction/CreateController.php
<?php

/**
 * CreateController.php
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

namespace FireflyIII\Http\Controllers\Transaction;

use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Models\TransactionGroup;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use FireflyIII\Repositories\TransactionGroup\TransactionGroupRepositoryInterface;
use FireflyIII\Services\Internal\Update\GroupCloneService;
use FireflyIII\Support\Facades\FireflyConfig;
use FireflyIII\Support\Facades\Preferences;
use Illuminate\Contracts\View\Factory;
use Illuminate\Contracts\View\View;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Psr\Container\ContainerExceptionInterface;
use Psr\Container\NotFoundExceptionInterface;
use Safe\Exceptions\UrlException;

use function Safe\parse_url;

/**
 * Class CreateController
 */
final class CreateController extends Controller
{
    private TransactionGroupRepositoryInterface $repository;

    /**
     * CreateController constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->middleware(function ($request, $next) {
            app('view')->share('title', (string) trans('firefly.transactions'));
            app('view')->share('mainTitleIcon', 'fa-exchange');
            $this->repository = app(TransactionGroupRepositoryInterface::class);

            return $next($request);
        });
    }

    public function cloneGroup(Request $request): JsonResponse
    {
        $groupId = (int) $request->get('id');
        if (0 !== $groupId) {
            $group = $this->repository->find($groupId);
            if ($group instanceof TransactionGroup) {
                /** @var GroupCloneService $service */
                $service  = app(GroupCloneService::class);
                $newGroup = $service->clon
...[truncated]...

### app/Http/Controllers/Transaction/EditController.php
<?php

/**
 * EditController.php
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

namespace FireflyIII\Http\Controllers\Transaction;

use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Models\TransactionGroup;
use FireflyIII\Models\TransactionJournal;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use FireflyIII\Repositories\Journal\JournalRepositoryInterface;
use FireflyIII\Support\Facades\FireflyConfig;
use FireflyIII\Support\Facades\Preferences;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Routing\Redirector;
use Illuminate\View\View;
use Psr\Container\ContainerExceptionInterface;
use Psr\Container\NotFoundExceptionInterface;
use Safe\Exceptions\UrlException;

use function Safe\parse_url;

/**
 * Class EditController
 */
final class EditController extends Controller
{
    private JournalRepositoryInterface $repository;

    /**
     * IndexController constructor.
     */
    public function __construct()
    {
        parent::__construct();

        // translations:
        $this->middleware(function ($request, $next) {
            app('view')->share('title', (string) trans('firefly.transactions'));
            app('view')->share('mainTitleIcon', 'fa-exchange');

            $this->repository = app(JournalRepositoryInterface::class);

            return $next($request);
        });
    }

    /**
     * @return Factory|RedirectResponse|View
     *
     * @throws ContainerExceptionInterface
     * @throws NotFoundExceptionInterface
     * @throws UrlException
     */
    public function edit(TransactionGroup $transactionGroup): Factory|\Illuminate\Contracts\View\View|Redirector|RedirectResponse
    {
        Preferences::mark();

        if (!$this->isEditableGroup($transactionGroup)) {
      
...[truncated]...

### app/Http/Controllers/Transaction/IndexController.php
<?php

/**
 * IndexController.php
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

namespace FireflyIII\Http\Controllers\Transaction;

use Carbon\Carbon;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Helpers\Collector\GroupCollectorInterface;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Models\TransactionJournal;
use FireflyIII\Repositories\Journal\JournalRepositoryInterface;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Http\Controllers\PeriodOverview;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\Request;
use Illuminate\View\View;
use Psr\Container\ContainerExceptionInterface;
use Psr\Container\NotFoundExceptionInterface;

/**
 * Class IndexController
 */
final class IndexController extends Controller
{
    use PeriodOverview;

    private JournalRepositoryInterface $repository;

    /**
     * IndexController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        app('view')->share('showCategory', true);
        // translations:
        $this->middleware(function ($request, $next) {
            app('view')->share('mainTitleIcon', 'fa-exchange');
            app('view')->share('title', (string) trans('firefly.transactions'));

            $this->repository = app(JournalRepositoryInterface::class);

            return $next($request);
        });
    }

    /**
     * Index for a range of transactions.
     *
     * @return Factory|View
     *
     * @throws ContainerExceptionInterface
     * @throws FireflyException
     * @throws NotFoundExceptionInterface
     */
    public function index(Request $request, string $objectType, ?Carbon $start = null, ?Carbon $end = null): Factory|\Illuminate\Contracts\View\View
    {
        if ('transfers' === $objectType) {
            $objectType = 'transfe
...[truncated]...

### app/Repositories/TransactionGroup/TransactionGroupRepository.php
<?php

/**
 * TransactionGroupRepository.php
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

namespace FireflyIII\Repositories\TransactionGroup;

use Carbon\Carbon;
use Exception;
use FireflyIII\Enums\TransactionTypeEnum;
use FireflyIII\Events\Model\TransactionGroup\CreatedSingleTransactionGroup;
use FireflyIII\Events\Model\TransactionGroup\TransactionGroupEventFlags;
use FireflyIII\Events\Model\TransactionGroup\TransactionGroupEventObjects;
use FireflyIII\Events\Model\Webhook\WebhookMessagesRequestSending;
use FireflyIII\Exceptions\DuplicateTransactionException;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Factory\TransactionGroupFactory;
use FireflyIII\Models\AccountMeta;
use FireflyIII\Models\Attachment;
use FireflyIII\Models\Location;
use FireflyIII\Models\Note;
use FireflyIII\Models\PiggyBankEvent;
use FireflyIII\Models\Transaction;
use FireflyIII\Models\TransactionGroup;
use FireflyIII\Models\TransactionJournal;
use FireflyIII\Models\TransactionJournalLink;
use FireflyIII\Repositories\Attachment\AttachmentRepositoryInterface;
use FireflyIII\Services\Internal\Destroy\TransactionGroupDestroyService;
use FireflyIII\Services\Internal\Update\GroupUpdateService;
use FireflyIII\Support\Facades\Amount;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\Support\NullArrayObject;
use FireflyIII\Support\Repositories\UserGroup\UserGroupInterface;
use FireflyIII\Support\Repositories\UserGroup\UserGroupTrait;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

use function Safe\json_decode;

/**
 * Class TransactionGroupRepository
 */
class TransactionGroupRepository implements TransactionGroupRepositoryInterface, UserGroupInterface
{
    use UserGroupT
...[truncated]...

### app/Http/Controllers/Budget/IndexController.php
<?php

/**
 * IndexController.php
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

namespace FireflyIII\Http\Controllers\Budget;

use Carbon\Carbon;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Models\AvailableBudget;
use FireflyIII\Models\Budget;
use FireflyIII\Models\BudgetLimit;
use FireflyIII\Models\TransactionCurrency;
use FireflyIII\Repositories\Budget\AvailableBudgetRepositoryInterface;
use FireflyIII\Repositories\Budget\BudgetLimitRepositoryInterface;
use FireflyIII\Repositories\Budget\BudgetRepositoryInterface;
use FireflyIII\Repositories\Budget\OperationsRepositoryInterface;
use FireflyIII\Repositories\Currency\CurrencyRepositoryInterface;
use FireflyIII\Support\Facades\Navigation;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\Support\Http\Api\ExchangeRateConverter;
use FireflyIII\Support\Http\Controllers\DateCalculation;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Log;
use Illuminate\View\View;
use Spatie\Period\Boundaries;
use Spatie\Period\Period;
use Spatie\Period\Precision;

/**
 * Class IndexController
 */
final class IndexController extends Controller
{
    use DateCalculation;

    private AvailableBudgetRepositoryInterface $abRepository;
    private BudgetLimitRepositoryInterface $blRepository;
    private CurrencyRepositoryInterface $currencyRepository;
    private OperationsRepositoryInterface $opsRepository;
    private BudgetRepositoryInterface $repository;

    /**
     * IndexController constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->middleware(function ($request, $next) {
            ap
...[truncated]...

### app/Http/Controllers/Budget/CreateController.php
<?php

/**
 * CreateController.php
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

namespace FireflyIII\Http\Controllers\Budget;

use FireflyIII\Enums\AutoBudgetType;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Helpers\Attachments\AttachmentHelperInterface;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Http\Requests\BudgetFormStoreRequest;
use FireflyIII\Repositories\Budget\BudgetRepositoryInterface;
use FireflyIII\Support\Facades\Preferences;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Illuminate\View\View;

/**
 * Class CreateController
 */
final class CreateController extends Controller
{
    private AttachmentHelperInterface $attachments;
    private BudgetRepositoryInterface $repository;

    /**
     * CreateController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            app('view')->share('title', (string) trans('firefly.budgets'));
            app('view')->share('mainTitleIcon', 'fa-pie-chart');
            $this->repository  = app(BudgetRepositoryInterface::class);
            $this->attachments = app(AttachmentHelperInterface::class);

            return $next($request);
        });
    }

    /**
     * Form to create a budget.
     *
     * @return Factory|View
     */
    public function create(Request $request): Factory|\Illuminate\Contracts\View\View
    {
        $hasOldInput       = null !== $request->old('_token');

        // auto budget types
        $autoBudgetTypes   = [
            0                                           => (string) trans('firefly.auto_budget_none'),
            AutoBudgetType::AUTO_BUDGET_RESET->value    => (string) trans(
...[truncated]...

### app/Http/Controllers/Budget/BudgetLimitController.php
<?php

/**
 * BudgetLimitController.php
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

namespace FireflyIII\Http\Controllers\Budget;

use Carbon\Carbon;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Http\Controllers\Controller;
use FireflyIII\Models\Budget;
use FireflyIII\Models\BudgetLimit;
use FireflyIII\Models\TransactionCurrency;
use FireflyIII\Repositories\Budget\BudgetLimitRepositoryInterface;
use FireflyIII\Repositories\Budget\BudgetRepositoryInterface;
use FireflyIII\Repositories\Budget\OperationsRepositoryInterface;
use FireflyIII\Repositories\Currency\CurrencyRepositoryInterface;
use FireflyIII\Support\Facades\Amount;
use FireflyIII\Support\Facades\Preferences;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\Support\Http\Controllers\DateCalculation;
use Illuminate\Contracts\View\Factory;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Log;
use Illuminate\View\View;
use Spatie\Period\Boundaries;
use Spatie\Period\Period;
use Spatie\Period\Precision;

/**
 * Class BudgetLimitController
 */
final class BudgetLimitController extends Controller
{
    use DateCalculation;

    private BudgetLimitRepositoryInterface $blRepository;
    private CurrencyRepositoryInterface $currencyRepos;
    private OperationsRepositoryInterface $opsRepository;
    private BudgetRepositoryInterface $repository;

    /**
     * AmountController constructor.
     */
    public function __construct()
    {
        parent::__construct();
        $this->middleware(function ($request, $next) {
            app('view')->share('title', (string) trans('firefly.budgets'));
            app('view')->share('mainTitleIcon', 'fa-pie-chart');
            $this->repository    = app(BudgetReposito
...[truncated]...

### app/Repositories/Budget/BudgetRepository.php
<?php

/**
 * BudgetRepository.php
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

namespace FireflyIII\Repositories\Budget;

use Carbon\Carbon;
use FireflyIII\Enums\AutoBudgetType;
use FireflyIII\Enums\TransactionTypeEnum;
use FireflyIII\Events\Model\Budget\CreatedBudget;
use FireflyIII\Events\Model\Budget\UpdatedBudget;
use FireflyIII\Events\Model\Webhook\WebhookMessagesRequestSending;
use FireflyIII\Exceptions\FireflyException;
use FireflyIII\Helpers\Collector\GroupCollectorInterface;
use FireflyIII\Models\Account;
use FireflyIII\Models\Attachment;
use FireflyIII\Models\AutoBudget;
use FireflyIII\Models\Budget;
use FireflyIII\Models\BudgetLimit;
use FireflyIII\Models\Note;
use FireflyIII\Models\RecurrenceTransactionMeta;
use FireflyIII\Models\RuleAction;
use FireflyIII\Models\RuleTrigger;
use FireflyIII\Repositories\Account\AccountRepositoryInterface;
use FireflyIII\Repositories\Currency\CurrencyRepositoryInterface;
use FireflyIII\Services\Internal\Destroy\BudgetDestroyService;
use FireflyIII\Support\Facades\Amount;
use FireflyIII\Support\Facades\Navigation;
use FireflyIII\Support\Facades\Steam;
use FireflyIII\Support\Http\Api\ExchangeRateConverter;
use FireflyIII\Support\Repositories\UserGroup\UserGroupInterface;
use FireflyIII\Support\Repositories\UserGroup\UserGroupTrait;
use FireflyIII\Support\Singleton\PreferencesSingleton;
use Illuminate\Database\QueryException;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Storage;

/**
 * Class BudgetRepository.
 */
class BudgetRepository implements BudgetRepositoryInterface, UserGroupInterface
{
    use UserGroupTrait;

    public function budgetedInPeriod(Carbon $start, Carbon $end): array
   
...[truncated]...