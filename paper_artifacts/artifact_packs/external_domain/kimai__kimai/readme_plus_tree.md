# README
## README.md
<p align="center">
    <img src="https://raw.githubusercontent.com/kimai/images/main/repository-header.png" alt="Kimai logo">
</p>

<p align="center">
    <a href="https://github.com/kimai/kimai/actions"><img alt="CI Status" src="https://github.com/kimai/kimai/actions/workflows/testing.yaml/badge.svg"></a>
    <a href="https://codecov.io/gh/kimai/kimai"><img alt="Code Coverage" src="https://codecov.io/gh/kimai/kimai/branch/main/graph/badge.svg"></a>
    <a href="https://packagist.org/packages/kimai/kimai"><img alt="Latest stable version" src="https://poser.pugx.org/kimai/kimai/v/stable"></a>
</p>

<h1 align="center">Kimai<br>#1 Open-Source Time-Tracker</h1>

Kimai is a professional grade time-tracking application, free and open-source. 
It handles use-cases of freelancers as well as companies with dozens or hundreds of users. 
Kimai was build to track your project times and ships with many advanced features, including but not limited to:

JSON API, invoicing, data exports, multi-timer and punch-in punch-out mode, tagging, multi-user - multi-timezones - multi-language ([over 30 translations existing](https://hosted.weblate.org/projects/kimai/)!),
authentication via SAML/LDAP/Database, two-factor authentication (2FA) with TOTP, customizable role and team permissions, responsive design,
user/customer/project specific rates, advanced search & filtering, money and time budgets, advanced reporting, support for [plugins](https://www.kimai.org/store/)
and so much more.

### Links

- [Home](https://www.kimai.org) — Kimai project homepage
- [Blog](https://www.kimai.org/blog/) — Read the latest news
- [Documentation](https://www.kimai.org/documentation/) — Learn how to use Kimai
- [Newsletter](https://www.kimai.org/en/newsletter) - Subscribe and get notified about new releases and important updates


### Requirements

- PHP 8.2 minimum with support for 8.3, 8.4, 8.5
- MariaDB / MySQL: oldest maintained LTS release (MariaDB >= [10.6](https://endoflife.date/mariadb) or MySQL >= [8.4](https://endoflife.date/mysql)) or newer
- A webserver and subdomain (subdirectory is not supported)
- PHP extensions: `gd`, `intl`, `json`, `mbstring`, `pdo`, `tokenizer`, `xml`, `xsl`, `zip`

## Installation

- Caddy with Docker-Compose at [Hetzner](https://www.kimai.org/documentation/hosting-hetzner-cloud.html) and [DigitalOcean](https://www.kimai.org/documentation/hosting-digital-ocean.html)
- [SSH setup](https://www.kimai.org/documentation/installation.html) with Git and Composer
- [Docker images](https://hub.docker.com/r/kimai/kimai2) with FPM only or incl. Apache
- [Synology](https://www.kimai.org/documentation/synology.html) user can host the Docker version 
- [Developer setups](https://www.kimai.org/documentation/developers.html) if you want to create Kimai integrations

There are more documented ways for [on-premise hosting](https://www.kimai.org/documentation/chapter-on-premise.html). 

And if you don't want to host Kimai, you can use the [Cloud version](https://www.kimai.cloud/) of it.

### Updating Kimai

- [Update Kimai](https://www.kimai.org/documentation/updates.html) — get the latest version
- [UPGRADING guide](UPGRADING.md) — version specific steps

### Plugins

- [Plugins](https://www.kimai.org/store/) — paid and free plugin marketplace
- [Developer documentation](https://www.kimai.org/documentation/developers.html) — how to create a plugin

## Roadmap and releases

You can see a rough development [roadmap](https://github.com/orgs/kimai/projects/2), which is open for changes and input from the community, your [ideas](https://github.com/kimai/kimai/issues) are welcome.

Release versions will be created on a regular basis, every couple of weeks latest.
Every code change, whether it's a new feature or a bugfix, will be done on the `main` branch.

## Contributing

You want to contribute to this repository? This is so great!
The best way to start is to [open a new issue](https://github.com/kimai/kimai/issues) for bugs or feature requests or a [discussion](https://github.com/kimai/kimai/discussions) for questions, support and such.

In case you want to contribute, but you wouldn't know how, here are some suggestions:

- Spread the word: Please [write a testimonial for our Wall of love](https://love.kimai.org), vote for Kimai on any software platform, you can toot or tweet about it, share it on LinkedIn, Reddit and any other social media platform!
- [Translate Kimai into your language](https://hosted.weblate.org/engage/kimai/), or help to improve the existing translations, many languages look for a contributor
- Answer questions: You know the answer to another user's problem? Share your knowledge.
- Something can be done better? An essential feature is missing? Create a feature request.
- Report bugs makes Kimai better for everyone.
- You don't have to be programmer, the documentation and translation could always use some attention.
- Sponsor the project: free software costs money to create!

There is one simple rule in our "Code of conduct": Don't be an ass!

## Follow Kimai

- Mastodon: [@kimai](https://phpc.social/@kimai)
- Youtube: [@kimai_org](https://www.youtube.com/@kimai_org)
- LinkedIn: [@kimai-org](https://www.linkedin.com/company/kimai-org/)
- Reddit: [r/kimai](https://www.reddit.com/r/kimai/)

### Credits

Kimai is based on modern technologies and frameworks such as [PHP](https://www.php.net/),
[Symfony](https://github.com/symfony/symfony) and [Doctrine](https://github.com/doctrine/),
[Bootstrap](https://github.com/twbs/bootstrap) and [Tabler](https://tabler.io/),
and [countless](composer.json) [others](package.json).

# File tree
.codecov.yml
.docker
  dbtest.php
  monolog.yaml
.php-cs-fixer.dist.php
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
README.md
SECURITY.md
UPGRADING-1.md
UPGRADING-3.md
UPGRADING.md
composer.json
config
  bundles.php
  locales.php
  packages
    assets.yaml
    cache.yaml
    doctrine.yaml
    doctrine_migrations.yaml
    fos_rest.yaml
    framework.yaml
    jms_serializer.yaml
    kimai.yaml
    monolog.yaml
    nelmio_api_doc.yaml
    nelmio_cors.yaml
    rate_limiter.yaml
    routing.yaml
    scheb_2fa.yaml
    security.yaml
    tabler.yaml
    translation.yaml
    twig.yaml
    web_profiler.yaml
    webpack_encore.yaml
  preload.php
  routes
    dev
      twig.yaml
      web_profiler.yaml
    test
      test_routes.yaml
  routes.yaml
  services.yaml
  services_test.yaml
package.json
pnpm-lock.yaml
src
  API
    ActionsController.php
    ActivityController.php
    Authentication
      AccessTokenHandler.php
      AccessTokenSuccessHandler.php
      ApiRequestMatcher.php
      ApiTokenMigratingListener.php
      ApiTokenUpgradeBadge.php
      TokenAuthenticator.php
    BaseApiController.php
    ConfigurationController.php
    CustomerController.php
    ExportController.php
    InvoiceController.php
    Model
      CalendarEvent.php
      PageAction.php
      Plugin.php
      TimesheetConfig.php
      Version.php
    NotFoundException.php
    ProjectController.php
    Serializer
      ValidationFailedExceptionErrorHandler.php
    StatusController.php
    TagController.php
    TeamController.php
    TimesheetController.php
    UserController.php
    ViewHandler.php
  Activity
    ActivityService.php
    ActivityStatisticService.php
  Audit
    Loggable.php
    Versioned.php
  Calendar
    CalendarQuery.php
    CalendarService.php
    CalendarSource.php
    CalendarSourceType.php
    DragAndDropEntry.php
    DragAndDropSource.php
    Google.php
    GoogleSource.php
    RecentActivitiesSource.php
    TimesheetEntry.php
  Command
    AbstractBundleInstallerCommand.php
    AbstractResetCommand.php
    AbstractRoleCommand.php
    AbstractUserCommand.php
    ActivateUserCommand.php
    ChangePasswordCommand.php
    CreateUserCommand.php
    DeactivateUserCommand.php
    DemoteUserCommand.php
    ExportCreateCommand.php
    InstallCommand.php
    InvoiceCreateCommand.php
    ListUserCommand.php
    MailTestCommand.php
    PluginCommand.php
    PromoteUserCommand.php
    RegenerateLocalesCommand.php
    ReloadCommand.php
    ResetDevelopmentCommand.php
    ResetTestCommand.php
    TimesheetStopAllCommand.php
    TranslationCommand.php
    UserLoginLinkCommand.php
    VersionCommand.php
  Configuration
    ConfigLoaderInterface.php
    ConfigurationService.php
    LdapConfiguration.php
    LocaleService.php
    MailConfiguration.php
    SamlConfiguration.php
    SamlConfigurationInterface.php
    SystemConfiguration.php
  ConsoleApplication.php
  Constants.php
  Controller
    AboutController.php
    AbstractController.php
    ActivityController.php
    Auth
      SamlController.php
    BookmarkController.php
    CalendarController.php
    ContractController.php
    CustomerController.php
    DashboardController.php
    DoctorController.php
    ExportController.php
    FavoriteController.php
    HelpController.php
    HomepageController.php
    InvoiceController.php
    PermissionController.php
    PluginController.php
    ProfileController.php
    ProjectController.php
    QuickEntryController.php
    Reporting
      AbstractUserReportController.php
      CustomerMonthlyProjectsController.php
      ProjectDateRangeController.php
      ProjectDetailsController.php
      ProjectInactiveController.php
      ProjectViewController.php
      ReportUsersMonthController.php
      ReportUsersWeekController.php
      ReportUsersYearController.php
      UserMonthController.php
      UserWeekController.php
      UserYearController.php
    ReportingController.php
    Security
      LoginLinkController.php
      PasswordResetController.php
      SecurityController.php
      SelfRegistrationController.php
    SystemConfigurationController.php
    TagController.php
    TeamController.php
    TimesheetAbstractController.php
    TimesheetController.php
    TimesheetTeamController.php
    UserController.php
    WidgetController.php
    WizardController.php
  Customer
    CustomerService.php
    CustomerStatisticService.php
  DataFixtures
    AllFixtures.php
    CustomerFixtures.php
    InvoiceFixtures.php
    TagFixtures.php
    TeamFixtures.php
    TimesheetFixtures.php
    UserFixtures.php
  DependencyInjection
    AppExtension.php
    Compiler
      ExportServiceCompilerPass.php
      InvoiceServiceCompilerPass.php
      TwigContextCompilerPass.php
      WidgetCompilerPass.php
    Configuration.php
  Doctrine
    AbstractMigration.php
    Behavior
      CreatedAt.php
      CreatedTrait.php
      ModifiedAt.php
      ModifiedTrait.php
    DataSubscriberInterface.php
    DsnParserFactory.php
    Extensions
      Date.php
      Day.php
      Month.php
      Year.php
    ModifiedSubscriber.php
    TimesheetSubscriber.php
    UTCDateTimeImmutableType.php
    UTCDateTimeType.php
  Entity
  Event
  EventSubscriber
  Export
  Form
  Invoice
  Kernel.php
  Ldap
  Logger
  Mail
  Model
  Pdf
  Plugin
  Project
  Reporting
  Repository
  Saml
  Security
  Timesheet
  Twig
  User
  Utils
  Validator
  Voter
  Webhook
  Widget
  WorkingTime
tests
webpack.config.js