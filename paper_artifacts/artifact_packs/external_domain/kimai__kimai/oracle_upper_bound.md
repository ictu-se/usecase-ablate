# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

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

# Oracle-selected code and test snippets
### src/Controller/TimesheetController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Entity\Timesheet;
use App\Event\TimesheetMetaDisplayEvent;
use App\Export\ServiceExport;
use App\Form\TimesheetEditForm;
use Symfony\Component\Form\FormInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;

/**
 * No permission check on controller level, only for single routes.
 *
 * There was "view_own_timesheet" here once, but it is a bug, as some companies (rarely, but existing) want their
 * employees to enter time, but not to see it afterward.
 *
 * It is legit to only own "create_own_timesheet" without "view_own_timesheet".
 */
#[Route(path: '/timesheet')]
final class TimesheetController extends TimesheetAbstractController
{
    #[Route(path: '/', defaults: ['page' => 1], name: 'timesheet', methods: ['GET'])]
    #[Route(path: '/page/{page}', requirements: ['page' => '[1-9]\d*'], name: 'timesheet_paginated', methods: ['GET'])]
    #[IsGranted('view_own_timesheet')]
    public function indexAction(int $page, Request $request): Response
    {
        $query = $this->createDefaultQuery();
        $query->setPage($page);

        return $this->index($query, $request, 'timesheet', 'timesheet_paginated', TimesheetMetaDisplayEvent::TIMESHEET);
    }

    #[Route(path: '/export/{exporter}', name: 'timesheet_export', methods: ['GET', 'POST'])]
    #[IsGranted('export_own_timesheet')]
    public function exportAction(string $exporter, Request $request, ServiceExport $serviceExport): Response
    {
        return $this->export($exporter, $request, $serviceExport);
    }

    #[Route(path: '/{id}/edit', name: 'timesheet_edit', methods: ['GET', 'POST'])]
    #[IsGranted('edit', 'entry')]
    public function editAction(Timesheet $entry, Request $request): Response
    {
        return $this->edit($entry, $request);
    }

    #[Route(path: '/{id}/duplicate', name: 'timesheet_duplicate', methods: ['GET', 'POST'])]
    #[IsGranted('duplicate', 'entry')]
    public function duplicateAction(Timesheet $entry, Request $request): Response
    {
        return $this->duplicate($entry, $request);
    }

    #[Route(path: '/multi-update', name: 'timesheet_multi_update', methods: ['POST'])]
    #[IsGranted('edit_own_timesheet')]
    public function multiUpdateAction(Request $request): Response
...[truncated]...

### src/Controller/TimesheetAbstractController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Configuration\SystemConfiguration;
use App\Entity\MetaTableTypeInterface;
use App\Entity\Timesheet;
use App\Event\TimesheetDuplicatePostEvent;
use App\Event\TimesheetDuplicatePreEvent;
use App\Event\TimesheetMetaDefinitionEvent;
use App\Event\TimesheetMetaDisplayEvent;
use App\Export\ServiceExport;
use App\Form\MultiUpdate\MultiUpdateTable;
use App\Form\MultiUpdate\MultiUpdateTableDTO;
use App\Form\MultiUpdate\TimesheetMultiUpdate;
use App\Form\MultiUpdate\TimesheetMultiUpdateDTO;
use App\Form\TimesheetEditForm;
use App\Form\TimesheetPreCreateForm;
use App\Form\Toolbar\TimesheetToolbarForm;
use App\Repository\Query\BaseQuery;
use App\Repository\Query\TimesheetQuery;
use App\Repository\TagRepository;
use App\Repository\TimesheetRepository;
use App\Timesheet\TimesheetService;
use App\Timesheet\TrackingMode\TrackingModeInterface;
use App\Utils\DataTable;
use App\Utils\PageSetup;
use Psr\EventDispatcher\EventDispatcherInterface;
use Symfony\Component\Form\FormInterface;
use Symfony\Component\Form\FormTypeInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

abstract class TimesheetAbstractController extends AbstractController
{
    public function __construct(
        protected readonly TimesheetRepository $repository,
        protected readonly EventDispatcherInterface $dispatcher,
        protected readonly TimesheetService $service,
        protected readonly SystemConfiguration $configuration,
        protected readonly TagRepository $tagRepository
    ) {
    }

    protected function getTrackingMode(): TrackingModeInterface
    {
        return $this->service->getActiveTrackingMode();
    }

    protected function index(TimesheetQuery $query, Request $request, string $route, string $paginationRoute, string $location): Response
    {
        $form = $this->getToolbarForm($query);
        if ($this->handleSearch($form, $request)) {
            return $this->redirectToRoute($route);
        }

        $canSeeRate = $this->canSeeRate();
        $canSeeUsername = $this->canSeeUsername();

        $this->prepareQuery($query);

        $result = $this->repository->getTimesheetResult($query);
        $metaColumns = $this->findMetaColumns($query, $location);

        $table = new DataTable($this->getTableName(), $query);
        $table->setPagination($result->getPagerfanta());
     
...[truncated]...

### src/Form/TimesheetEditForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form;

use App\Configuration\SystemConfiguration;
use App\Entity\Customer;
use App\Entity\Timesheet;
use App\Form\Type\CustomerType;
use App\Form\Type\DatePickerType;
use App\Form\Type\DescriptionType;
use App\Form\Type\DurationType;
use App\Form\Type\FixedRateType;
use App\Form\Type\HourlyRateType;
use App\Form\Type\InternalRateType;
use App\Form\Type\MetaFieldsCollectionType;
use App\Form\Type\TagsType;
use App\Form\Type\TimePickerType;
use App\Form\Type\TimesheetBillableType;
use App\Form\Type\UserType;
use App\Form\Type\YesNoType;
use App\Repository\CustomerRepository;
use App\Repository\Query\CustomerFormTypeQuery;
use App\Timesheet\Calculator\BillableCalculator;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\CallbackTransformer;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\Form\FormEvent;
use Symfony\Component\Form\FormEvents;
use Symfony\Component\OptionsResolver\OptionsResolver;
use Symfony\Component\Validator\Constraints\NotBlank;

/**
 * Defines the form used to manipulate Timesheet entries.
 */
class TimesheetEditForm extends AbstractType
{
    use FormTrait;

    public function __construct(
        private readonly CustomerRepository $customers,
        private readonly SystemConfiguration $systemConfiguration
    )
    {
    }

    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $activity = null;
        $project = null;
        $customer = null;
        $currency = false;
        $timezone = $options['timezone'];
        $isNew = true;

        if (isset($options['data']) && $options['data'] instanceof Timesheet) {
            $entry = $options['data'];

            $activity = $entry->getActivity();
            $project = $entry->getProject();
            $customer = $project?->getCustomer();

            if (null !== $entry->getId()) {
                $isNew = false;
            }

            if (null === $project && null !== $activity) {
                $project = $activity->getProject();
            }

            if (null !== $customer) {
                $currency = $customer->getCurrency();
            }

            if (null !== ($begin = $entry->getBegin())) {
                $timezone = $begin->getTimezone()->getName();
            }
        }

        $dateTimeOptions = [
            'model_timezone' => $timezone,
            'vie
...[truncated]...

### src/Repository/TimesheetRepository.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Repository;

use App\Entity\ActivityRate;
use App\Entity\CustomerRate;
use App\Entity\Project;
use App\Entity\ProjectRate;
use App\Entity\RateInterface;
use App\Entity\Team;
use App\Entity\Timesheet;
use App\Entity\TimesheetMeta;
use App\Entity\User;
use App\Model\Revenue;
use App\Model\TimesheetStatistic;
use App\Repository\Loader\TimesheetLoader;
use App\Repository\Paginator\LoaderQueryPaginator;
use App\Repository\Paginator\PaginatorInterface;
use App\Repository\Query\TimesheetQuery;
use App\Repository\Query\TimesheetQueryHint;
use App\Repository\Result\TimesheetResult;
use App\Repository\Search\SearchConfiguration;
use App\Repository\Search\SearchHelper;
use App\Utils\Pagination;
use DateInterval;
use DateTime;
use Doctrine\DBAL\Types\Types;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\Mapping\ClassMetadata;
use Doctrine\ORM\Query;
use Doctrine\ORM\Query\Expr\Join;
use Doctrine\ORM\QueryBuilder;
use Exception;
use InvalidArgumentException;

/**
 * @extends EntityRepository<Timesheet>
 */
class TimesheetRepository extends EntityRepository
{
    /** @deprecated since 2.0.35 */
    public const STATS_QUERY_DURATION = 'duration';
    /** @deprecated since 2.0.35 */
    public const STATS_QUERY_RATE = 'rate';
    /** @deprecated since 2.0.35 */
    public const STATS_QUERY_USER = 'users';
    /** @deprecated since 2.0.35 */
    public const STATS_QUERY_AMOUNT = 'amount';
    /** @deprecated since 2.0.35 */
    public const STATS_QUERY_ACTIVE = 'active';

    /**
     * Fetches the raw data of a timesheet, to allow comparison e.g. of submitted and previously stored data.
     *
     * @param int $id
     * @return array
     */
    public function getRawData(int $id): array
    {
        $qb = $this->createQueryBuilder('t');
        $qb
            ->select([
                't.rate',
                't.begin',
                't.end',
                't.duration',
                't.hourlyRate',
                't.billable',
                'IDENTITY(p.customer) as customer',
                'IDENTITY(t.project) as project',
                'IDENTITY(t.activity) as activity',
                'IDENTITY(t.user) as user'
            ])
            ->leftJoin(Project::class, 'p', Join::WITH, 'p.id = t.project')
            ->andWhere($qb->expr()->eq('t.id', ':id'))
            ->setParameter('id', $id)
        ;

        return $qb->getQuery()-
...[truncated]...

### src/Controller/QuickEntryController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Configuration\SystemConfiguration;
use App\Event\QuickEntryMetaDisplayEvent;
use App\Form\QuickEntryForm;
use App\Form\WeekByUserForm;
use App\Model\QuickEntryWeek;
use App\Reporting\WeekByUser\WeekByUser;
use App\Repository\Query\TimesheetQuery;
use App\Repository\TimesheetRepository;
use App\Timesheet\FavoriteRecordService;
use App\Timesheet\TimesheetService;
use App\Utils\PageSetup;
use App\WorkingTime\WorkingTimeService;
use Psr\EventDispatcher\EventDispatcherInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;

/**
 * Controller used to enter times in weekly form.
 */
#[IsGranted('quick-entry')]
final class QuickEntryController extends AbstractController
{
    public function __construct(
        private readonly SystemConfiguration $configuration,
        private readonly TimesheetService $timesheetService,
        private readonly TimesheetRepository $repository,
        private readonly FavoriteRecordService $favoriteRecordService,
        private readonly EventDispatcherInterface $dispatcher,
        private readonly WorkingTimeService $workingTimeService,
    )
    {
    }

    #[Route(path: '/quick_entry/', name: 'quick_entry', methods: ['GET', 'POST'])]
    public function quickEntry(Request $request): Response
    {
        $user = $this->getUser();
        $factory = $this->getDateTimeFactory($user);
        $defaultDate = $factory->createDateTime();

        $values = new WeekByUser();
        $values->setUser($user);
        $values->setDate($defaultDate);

        $weeklyForm = $this->createFormForGetRequest(WeekByUserForm::class, $values, [
            'include_user' => $this->isGranted('view_other_timesheet'),
            'timezone' => $factory->getTimezone()->getName(),
            'start_date' => $values->getDate(),
            'attr' => ['name' => 'quick_entry_weekrange_form']
        ]);

        $weeklyForm->submit($request->query->all(), false);

        $user = $values->getUser() ?? $user;
        $factory = $this->getDateTimeFactory($user);

        $begin = $values->getDate();

        if ($begin === null) {
            $begin = $factory->createDateTime();
        }

        $startWeek = $factory->getStartOfWeek($begin);
        $endWeek = $facto
...[truncated]...

### src/Form/Type/QuickEntryTimesheetType.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\Type;

use App\Entity\Timesheet;
use Symfony\Bundle\SecurityBundle\Security;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\Form\FormError;
use Symfony\Component\Form\FormEvent;
use Symfony\Component\Form\FormEvents;
use Symfony\Component\OptionsResolver\OptionsResolver;

final class QuickEntryTimesheetType extends AbstractType
{
    public function __construct(private readonly Security $security)
    {
    }

    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $durationOptions = [
            'label' => false,
            'required' => false,
            'attr' => [
                'placeholder' => '0:00',
            ],
            'icon' => null,
        ];

        $duration = $options['duration_minutes'];
        if ($duration !== null && (int) $duration > 0) {
            $durationOptions = array_merge($durationOptions, [
                'preset_minutes' => $duration
            ]);
        }

        $duration = $options['duration_hours'];
        if ($duration !== null && (int) $duration > 0) {
            $durationOptions = array_merge($durationOptions, [
                'preset_hours' => $duration,
            ]);
        }

        $builder->add('duration', DurationType::class, $durationOptions);

        $builder->addEventListener(
            FormEvents::POST_SET_DATA,
            function (FormEvent $event) use ($durationOptions): void {
                /** @var Timesheet|null $data */
                $data = $event->getData();
                if (null === $data || $data->isRunning()) {
                    $event->getForm()->get('duration')->setData(null);
                }

                if ($data instanceof Timesheet && !$this->security->isGranted('edit', $data)) {
                    // do not call $event->getForm()->remove() this would change the field order
                    $event->getForm()->add('duration', DurationType::class, array_merge(['disabled' => true], $durationOptions));

                    $mainForm = $event->getForm()->getParent()?->getParent();
                    if ($mainForm === null) {
                        return;
                    }

                    $isNew = $data->getId() === null;

                    foreach($mainForm->all() as $key => $child) {
                        if ($key 
...[truncated]...

### src/Validator/Constraints/QuickEntryTimesheetValidator.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Validator\Constraints;

use App\Entity\Timesheet as TimesheetEntity;
use App\Validator\Constraints\QuickEntryTimesheet as QuickEntryTimesheetConstraint;
use Symfony\Component\DependencyInjection\Attribute\TaggedIterator;
use Symfony\Component\Validator\Constraint;
use Symfony\Component\Validator\ConstraintValidator;
use Symfony\Component\Validator\Exception\UnexpectedTypeException;

final class QuickEntryTimesheetValidator extends ConstraintValidator
{
    /**
     * @param TimesheetConstraint[] $constraints
     */
    public function __construct(
        #[TaggedIterator(TimesheetConstraint::class)]
        private iterable $constraints
    )
    {
    }

    public function validate(mixed $value, Constraint $constraint): void
    {
        if (!$constraint instanceof QuickEntryTimesheetConstraint) {
            throw new UnexpectedTypeException($constraint, QuickEntryTimesheetConstraint::class);
        }

        if (!\is_object($value) || !($value instanceof TimesheetEntity)) {
            throw new UnexpectedTypeException($value, TimesheetEntity::class);
        }

        if ($value->getId() === null && $value->getDuration(false) === null) {
            return;
        }

        foreach ($this->constraints as $innerConstraint) {
            $this->context
                ->getValidator()
                ->inContext($this->context)
                ->atPath('duration')
                ->validate($value, $innerConstraint, [Constraint::DEFAULT_GROUP]);
        }
    }
}

### src/Controller/CustomerController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Customer\CustomerService;
use App\Customer\CustomerStatisticService;
use App\Entity\Customer;
use App\Entity\CustomerComment;
use App\Entity\CustomerRate;
use App\Event\CustomerDetailControllerEvent;
use App\Event\CustomerMetaDisplayEvent;
use App\Export\Spreadsheet\EntityWithMetaFieldsExporter;
use App\Export\Spreadsheet\Writer\BinaryFileResponseWriter;
use App\Export\Spreadsheet\Writer\XlsxWriter;
use App\Form\CustomerCommentForm;
use App\Form\CustomerEditForm;
use App\Form\CustomerRateForm;
use App\Form\CustomerTeamPermissionForm;
use App\Form\Toolbar\CustomerToolbarForm;
use App\Form\Type\CustomerType;
use App\Repository\CustomerRateRepository;
use App\Repository\CustomerRepository;
use App\Repository\ProjectRepository;
use App\Repository\Query\CustomerQuery;
use App\Repository\Query\ProjectQuery;
use App\Repository\Query\TeamQuery;
use App\Repository\Query\TimesheetQuery;
use App\Repository\Query\VisibilityInterface;
use App\Repository\TeamRepository;
use App\Utils\DataTable;
use App\Utils\PageSetup;
use Psr\EventDispatcher\EventDispatcherInterface;
use Symfony\Component\ExpressionLanguage\Expression;
use Symfony\Component\Form\FormInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;

/**
 * Controller used to manage customers.
 */
#[Route(path: '/admin/customer')]
final class CustomerController extends AbstractController
{
    public function __construct(private readonly CustomerRepository $repository)
    {
    }

    #[Route(path: '/', defaults: ['page' => 1], name: 'admin_customer', methods: ['GET'])]
    #[Route(path: '/page/{page}', requirements: ['page' => '[1-9]\d*'], name: 'admin_customer_paginated', methods: ['GET'])]
    #[IsGranted(new Expression("is_granted('listing', 'customer')"))]
    public function indexAction(int $page, Request $request, EventDispatcherInterface $dispatcher): Response
    {
        $query = new CustomerQuery();
        $query->loadTeams();
        $query->setCurrentUser($this->getUser());
        $query->setPage($page);

        $form = $this->getToolbarForm($query, $request);
        if ($this->handleSearch($form, $request)) {
            return $this->redirectToRoute('admin_customer');
        }

        $entries = $this->repositor
...[truncated]...

### src/Controller/ProjectController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Configuration\SystemConfiguration;
use App\Entity\Customer;
use App\Entity\Project;
use App\Entity\ProjectComment;
use App\Entity\ProjectRate;
use App\Event\ProjectDetailControllerEvent;
use App\Event\ProjectMetaDisplayEvent;
use App\Export\Spreadsheet\EntityWithMetaFieldsExporter;
use App\Export\Spreadsheet\Writer\BinaryFileResponseWriter;
use App\Export\Spreadsheet\Writer\XlsxWriter;
use App\Form\ProjectCommentForm;
use App\Form\ProjectEditForm;
use App\Form\ProjectRateForm;
use App\Form\ProjectTeamPermissionForm;
use App\Form\Toolbar\ProjectToolbarForm;
use App\Form\Type\ProjectType;
use App\Project\ProjectDuplicationService;
use App\Project\ProjectService;
use App\Project\ProjectStatisticService;
use App\Repository\ActivityRepository;
use App\Repository\ProjectRateRepository;
use App\Repository\ProjectRepository;
use App\Repository\Query\ActivityQuery;
use App\Repository\Query\ProjectQuery;
use App\Repository\Query\TeamQuery;
use App\Repository\Query\TimesheetQuery;
use App\Repository\Query\VisibilityInterface;
use App\Repository\TeamRepository;
use App\Utils\Context;
use App\Utils\DataTable;
use App\Utils\PageSetup;
use Psr\EventDispatcher\EventDispatcherInterface;
use Symfony\Component\ExpressionLanguage\Expression;
use Symfony\Component\Form\FormInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Csrf\CsrfToken;
use Symfony\Component\Security\Csrf\CsrfTokenManagerInterface;
use Symfony\Component\Security\Http\Attribute\IsGranted;

/**
 * Controller used to manage projects.
 */
#[Route(path: '/admin/project')]
final class ProjectController extends AbstractController
{
    public function __construct(private readonly ProjectRepository $repository)
    {
    }

    #[Route(path: '/', defaults: ['page' => 1], name: 'admin_project', methods: ['GET'])]
    #[Route(path: '/page/{page}', requirements: ['page' => '[1-9]\d*'], name: 'admin_project_paginated', methods: ['GET'])]
    #[IsGranted(new Expression("is_granted('listing', 'project')"))]
    public function indexAction(int $page, Request $request, EventDispatcherInterface $dispatcher): Response
    {
        $query = new ProjectQuery();
        $query->loadTeams();
        $query->setCurrentUser($this->getUser());
        $query->setPage($page
...[truncated]...

### src/Controller/ActivityController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Activity\ActivityService;
use App\Activity\ActivityStatisticService;
use App\Configuration\SystemConfiguration;
use App\Entity\Activity;
use App\Entity\ActivityRate;
use App\Entity\Project;
use App\Event\ActivityDetailControllerEvent;
use App\Event\ActivityMetaDisplayEvent;
use App\Export\Spreadsheet\EntityWithMetaFieldsExporter;
use App\Export\Spreadsheet\Writer\BinaryFileResponseWriter;
use App\Export\Spreadsheet\Writer\XlsxWriter;
use App\Form\ActivityEditForm;
use App\Form\ActivityRateForm;
use App\Form\ActivityTeamPermissionForm;
use App\Form\Toolbar\ActivityToolbarForm;
use App\Form\Type\ActivityType;
use App\Repository\ActivityRateRepository;
use App\Repository\ActivityRepository;
use App\Repository\Query\ActivityQuery;
use App\Repository\Query\TeamQuery;
use App\Repository\Query\TimesheetQuery;
use App\Repository\TeamRepository;
use App\Utils\DataTable;
use App\Utils\PageSetup;
use Exception;
use Psr\EventDispatcher\EventDispatcherInterface;
use Symfony\Component\ExpressionLanguage\Expression;
use Symfony\Component\Form\FormInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;

/**
 * Controller used to manage activities.
 */
#[Route(path: '/admin/activity')]
final class ActivityController extends AbstractController
{
    public function __construct(private readonly ActivityRepository $repository)
    {
    }

    #[Route(path: '/', defaults: ['page' => 1], name: 'admin_activity', methods: ['GET'])]
    #[Route(path: '/page/{page}', requirements: ['page' => '[1-9]\d*'], name: 'admin_activity_paginated', methods: ['GET'])]
    #[IsGranted(new Expression("is_granted('listing', 'activity')"))]
    public function indexAction(int $page, Request $request, EventDispatcherInterface $dispatcher, SystemConfiguration $configuration): Response
    {
        $query = new ActivityQuery();
        $query->loadTeams();
        $query->setCurrentUser($this->getUser());
        $query->setPage($page);

        $form = $this->getToolbarForm($query);
        if ($this->handleSearch($form, $request)) {
            return $this->redirectToRoute('admin_activity');
        }

        $entries = $this->repository->getPagerfantaForQuery($query);

        $event = new ActivityMetaDisplayEvent
...[truncated]...

### src/Repository/CustomerRepository.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Repository;

use App\Entity\Customer;
use App\Entity\CustomerComment;
use App\Entity\CustomerMeta;
use App\Entity\Project;
use App\Entity\Team;
use App\Entity\User;
use App\Repository\Loader\CustomerLoader;
use App\Repository\Paginator\LoaderQueryPaginator;
use App\Repository\Paginator\PaginatorInterface;
use App\Repository\Query\CustomerFormTypeQuery;
use App\Repository\Query\CustomerQuery;
use App\Repository\Query\CustomerQueryHydrate;
use App\Repository\Search\SearchConfiguration;
use App\Repository\Search\SearchHelper;
use App\Utils\Pagination;
use Doctrine\DBAL\ParameterType;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\Mapping\ClassMetadata;
use Doctrine\ORM\Query;
use Doctrine\ORM\Query\Expr\Andx;
use Doctrine\ORM\QueryBuilder;

/**
 * @extends EntityRepository<Customer>
 */
class CustomerRepository extends EntityRepository
{
    /**
     * @param array<int, string|int> $customerIDs
     * @return array<Customer>
     */
    public function findByIds(array $customerIDs): array
    {
        $ids = array_filter(
            array_unique($customerIDs),
            function ($value) {
                return $value > 0;
            }
        );

        if (\count($ids) === 0) {
            return [];
        }

        $qb = $this->createQueryBuilder('c');
        $qb
            ->where($qb->expr()->in('c.id', ':id'))
            ->setParameter('id', $ids)
        ;

        return $this->getCustomers($this->prepareCustomerQuery($qb->getQuery()), new CustomerQuery());
    }

    public function saveCustomer(Customer $customer): void
    {
        $entityManager = $this->getEntityManager();
        $entityManager->persist($customer);
        $entityManager->flush();
    }

    public function countCustomer(bool $visible = false): int
    {
        if ($visible) {
            return $this->count(['visible' => $visible]);
        }

        return $this->count([]);
    }

    /**
     * @param array<Team> $teams
     */
    public function addPermissionCriteria(QueryBuilder $qb, ?User $user = null, array $teams = []): void
    {
        $permissions = $this->getPermissionCriteria($qb, $user, $teams);
        if ($permissions->count() > 0) {
            $qb->andWhere($permissions);
        }
    }

    /**
     * @param array<Team> $teams
     */
    private function getPermissionCriteria(QueryBuilder $qb, ?User $user = null, array $teams
...[truncated]...

### src/Repository/ProjectRepository.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Repository;

use App\Entity\Activity;
use App\Entity\Project;
use App\Entity\ProjectComment;
use App\Entity\ProjectMeta;
use App\Entity\Team;
use App\Entity\Timesheet;
use App\Entity\User;
use App\Repository\Loader\ProjectLoader;
use App\Repository\Paginator\LoaderQueryPaginator;
use App\Repository\Paginator\PaginatorInterface;
use App\Repository\Query\ProjectFormTypeQuery;
use App\Repository\Query\ProjectQuery;
use App\Repository\Query\ProjectQueryHydrate;
use App\Repository\Search\SearchConfiguration;
use App\Repository\Search\SearchHelper;
use App\Utils\Pagination;
use DateTime;
use Doctrine\DBAL\ParameterType;
use Doctrine\DBAL\Types\Types;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\Mapping\ClassMetadata;
use Doctrine\ORM\Query;
use Doctrine\ORM\Query\Expr\Andx;
use Doctrine\ORM\QueryBuilder;

/**
 * @extends EntityRepository<Project>
 */
class ProjectRepository extends EntityRepository
{
    /**
     * @param array<int, string|int> $projectIds
     * @return array<Project>
     */
    public function findByIds(array $projectIds): array
    {
        $ids = array_filter(
            array_unique($projectIds),
            function ($value) {
                return $value > 0;
            }
        );

        if (\count($ids) === 0) {
            return [];
        }

        $qb = $this->createQueryBuilder('p');
        $qb
            ->where($qb->expr()->in('p.id', ':id'))
            ->setParameter('id', $ids)
        ;

        return $this->getProjects($this->prepareProjectQuery($qb->getQuery()));
    }

    public function saveProject(Project $project): void
    {
        $entityManager = $this->getEntityManager();
        $entityManager->persist($project);
        $entityManager->flush();
    }

    /**
     * @return int<0, max>
     */
    public function countProject(?bool $visible = null): int
    {
        if (null !== $visible) {
            return $this->count(['visible' => $visible]);
        }

        return $this->count([]);
    }

    /**
     * @param array<Team> $teams
     */
    public function addPermissionCriteria(QueryBuilder $qb, ?User $user = null, array $teams = []): void
    {
        $permissions = $this->getPermissionCriteria($qb, $user, $teams);
        if ($permissions->count() > 0) {
            $qb->andWhere($permissions);
        }
    }

    /**
     * @param array<Team> $teams
     */
    privat
...[truncated]...

### src/Repository/ActivityRepository.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Repository;

use App\Entity\Activity;
use App\Entity\ActivityMeta;
use App\Entity\Project;
use App\Entity\Team;
use App\Entity\Timesheet;
use App\Entity\User;
use App\Repository\Loader\ActivityLoader;
use App\Repository\Paginator\LoaderQueryPaginator;
use App\Repository\Paginator\PaginatorInterface;
use App\Repository\Query\ActivityFormTypeQuery;
use App\Repository\Query\ActivityQuery;
use App\Repository\Query\ActivityQueryHydrate;
use App\Repository\Search\SearchConfiguration;
use App\Repository\Search\SearchHelper;
use App\Utils\Pagination;
use Doctrine\DBAL\ParameterType;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\Mapping\ClassMetadata;
use Doctrine\ORM\Query;
use Doctrine\ORM\Query\Expr\Andx;
use Doctrine\ORM\QueryBuilder;

/**
 * @extends EntityRepository<Activity>
 */
class ActivityRepository extends EntityRepository
{
    /**
     * @param array<int, string|int> $activityIds
     * @return array<Activity>
     */
    public function findByIds(array $activityIds): array
    {
        $ids = array_filter(
            array_unique($activityIds),
            function ($value) {
                return $value > 0;
            }
        );

        if (\count($ids) === 0) {
            return [];
        }

        $qb = $this->createQueryBuilder('a');
        $qb
            ->where($qb->expr()->in('a.id', ':id'))
            ->setParameter('id', $ids)
        ;

        return $this->getActivities($this->prepareActivityQuery($qb->getQuery()));
    }

    public function saveActivity(Activity $activity): void
    {
        $entityManager = $this->getEntityManager();
        $entityManager->persist($activity);
        $entityManager->flush();
    }

    public function countActivity(?bool $visible = null): int
    {
        if (null !== $visible) {
            return $this->count(['visible' => $visible]);
        }

        return $this->count([]);
    }

    /**
     * @param array<Team> $teams
     */
    private function addPermissionCriteria(QueryBuilder $qb, ?User $user = null, array $teams = [], bool $globalsOnly = false): void
    {
        $permissions = $this->getPermissionCriteria($qb, $user, $teams, $globalsOnly);
        if ($permissions->count() > 0) {
            $qb->andWhere($permissions);
        }
    }

    /**
     * @param array<Team> $teams
     */
    private function getPermissionCriteria(QueryBuilder $qb, ?User $
...[truncated]...

### src/Controller/ExportController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Configuration\SystemConfiguration;
use App\Entity\ExportableItem;
use App\Entity\ExportTemplate;
use App\Export\Base\DispositionInlineInterface;
use App\Export\ServiceExport;
use App\Export\TooManyItemsExportException;
use App\Form\ExportTemplateSpreadsheetForm;
use App\Form\Toolbar\ExportToolbarForm;
use App\Repository\ExportTemplateRepository;
use App\Repository\Query\ExportQuery;
use App\Utils\PageSetup;
use Symfony\Component\Form\FormInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;

/**
 * Controller used to export timesheet data.
 */
#[Route(path: '/export')]
#[IsGranted('create_export')]
final class ExportController extends AbstractController
{
    public function __construct(private readonly ServiceExport $export)
    {
    }

    #[Route(path: '/', name: 'export', methods: ['GET'])]
    public function indexAction(Request $request): Response
    {
        $query = $this->getDefaultQuery();

        $showPreview = false;
        $tooManyResults = false;
        $maxItemsPreview = 500;
        $entries = [];

        $form = $this->getToolbarForm($query, 'GET');
        if ($this->handleSearch($form, $request)) {
            return $this->redirectToRoute('export');
        }

        $byCustomer = [];

        if ($form->isValid() && ($query->hasBookmark() || $request->query->has('performSearch'))) {
            try {
                $showPreview = true;
                $entries = $this->getEntries($query);
                foreach ($entries as $entry) {
                    $cid = $entry->getProject()->getCustomer()->getId();
                    if (!isset($byCustomer[$cid])) {
                        $byCustomer[$cid] = [
                            'customer' => $entry->getProject()->getCustomer(),
                            'rate' => 0,
                            'internalRate' => 0,
                            'duration' => 0,
                        ];
                    }
                    $byCustomer[$cid]['rate'] += $entry->getRate();
                    $byCustomer[$cid]['internalRate'] += $entry->getInternalRate() ?? 0.0;
                    $byCustomer[$cid]['duration'] += $entry->getDuration() ?? 0;
                }
            } catch (TooManyIte
...[truncated]...

### src/Form/Toolbar/TimesheetToolbarForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\Toolbar;

use App\Repository\Query\TimesheetQuery;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

/**
 * Defines the form used for filtering the timesheet.
 * @extends AbstractType<TimesheetQuery>
 */
final class TimesheetToolbarForm extends AbstractType
{
    use ToolbarFormTrait;

    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $newOptions = [];
        if ($options['ignore_date'] === true) {
            $newOptions['ignore_date'] = true;
        }

        $this->addSearchTermInputField($builder);
        $this->addDateRange($builder, ['timezone' => $options['timezone']]);
        $this->addCustomerMultiChoice($builder, $newOptions, true);
        $this->addProjectMultiChoice($builder, $newOptions, true, true);
        $this->addActivityMultiChoice($builder, [], true);
        $this->addTagInputField($builder);
        if ($options['include_user']) {
            $this->addUsersChoice($builder);
            $this->addTeamsChoice($builder);
        }
        $this->addTimesheetStateChoice($builder);
        $this->addBillableChoice($builder);
        $this->addExportStateChoice($builder);
        $this->addPageSizeChoice($builder);
        $this->addHiddenPagination($builder);

        $query = $options['data'];
        if ($query instanceof TimesheetQuery) {
            $this->addOrder($builder);
            $this->addOrderBy($builder, $query->getAllowedOrderColumns());
        }
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => TimesheetQuery::class,
            'csrf_protection' => false,
            'include_user' => false,
            'ignore_date' => true,
            'timezone' => date_default_timezone_get(),
        ]);
    }
}

### src/Repository/Query/ExportQuery.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Repository\Query;

class ExportQuery extends TimesheetQuery
{
    private ?string $renderer = null;
    private bool $markAsExported = false;

    public function __construct()
    {
        parent::__construct();
        $this->setDefaults([
            'order' => BaseQuery::ORDER_ASC,
            'state' => TimesheetQuery::STATE_STOPPED,
            'exported' => TimesheetQuery::STATE_NOT_EXPORTED,
        ]);
    }

    public function getRenderer(): ?string
    {
        return $this->renderer;
    }

    public function setRenderer(string $renderer): ExportQuery
    {
        $this->renderer = $renderer;

        return $this;
    }

    public function isMarkAsExported(): bool
    {
        return $this->markAsExported;
    }

    public function setMarkAsExported(?bool $markAsExported): ExportQuery
    {
        if ($markAsExported === null) {
            $markAsExported = false;
        }
        $this->markAsExported = $markAsExported;

        return $this;
    }
}

### src/Form/Type/ExportRendererType.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\Type;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;
use Symfony\Component\OptionsResolver\OptionsResolver;

final class ExportRendererType extends AbstractType
{
    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'choices' => [
                'csv' => 'csv',
                'xlsx' => 'xlsx',
                'pdf' => 'pdf'
            ],
        ]);
    }

    public function getParent(): string
    {
        return ChoiceType::class;
    }
}

### src/Controller/InvoiceController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For t
...[truncated]...