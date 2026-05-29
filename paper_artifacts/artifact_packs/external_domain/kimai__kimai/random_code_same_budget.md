# Deterministic random code snippets
### src/Export/Spreadsheet/AnnotatedObjectExporter.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Export\Spreadsheet;

use App\Export\Spreadsheet\Extractor\AnnotationExtractor;
use PhpOffice\PhpSpreadsheet\Spreadsheet;

final class AnnotatedObjectExporter
{
    public function __construct(private SpreadsheetExporter $spreadsheetExporter, private AnnotationExtractor $annotationExtractor)
    {
    }

    public function export(string $class, array $entries): Spreadsheet
    {
        $columns = $this->annotationExtractor->extract($class);

        return $this->spreadsheetExporter->export($columns, $entries);
    }
}

### tests/DependencyInjection/Compiler/TwigContextCompilerPassTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\DependencyInjection\Compiler;

use App\DependencyInjection\Compiler\TwigContextCompilerPass;
use App\Export\ServiceExport;
use App\Twig\Configuration;
use App\Twig\Context;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\DependencyInjection\Definition;

#[CoversClass(TwigContextCompilerPass::class)]
class TwigContextCompilerPassTest extends TestCase
{
    private function getContainer(): ContainerBuilder
    {
        $container = new ContainerBuilder();
        $container->setParameter('kimai.invoice.documents', []); // TODO we could test that as well
        $container->setParameter('kimai.export.documents', []); // TODO we could test that as well

        $definition = new Definition('twig');
        $container->setDefinition('twig', $definition);

        $definition = new Definition('twig.loader.native_filesystem');
        $container->setDefinition('twig.loader.native_filesystem', $definition);

        $definition = new Definition(ServiceExport::class);
        $container->setDefinition(ServiceExport::class, $definition);

        $definition = new Definition(Context::class);
        $container->setDefinition(Context::class, $definition);

        $definition = new Definition(Configuration::class);
        $container->setDefinition(Configuration::class, $definition);

        return $container;
    }

    public function testCallsAreAdded(): void
    {
        $container = $this->getContainer();
        $sut = new TwigContextCompilerPass();
        $sut->process($container);

        $definition = $container->findDefinition('twig');
        $methods = $definition->getMethodCalls();

        self::assertCount(2, $methods);
        self::assertTrue($definition->hasMethodCall('addGlobal'));
        self::assertEquals('addGlobal', $methods[0][0]);
        self::assertEquals('kimai_context', $methods[0][1][0]);
        self::assertEquals('addGlobal', $methods[1][0]);
        self::assertEquals('kimai_config', $methods[1][1][0]);
    }
}

### src/Invoice/NumberGenerator/ConfigurableNumberGenerator.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Invoice\NumberGenerator;

use App\Configuration\SystemConfiguration;
use App\Invoice\InvoiceModel;
use App\Invoice\NumberGeneratorInterface;
use App\Repository\InvoiceRepository;
use App\Utils\NumberGenerator;

final class ConfigurableNumberGenerator implements NumberGeneratorInterface
{
    private ?InvoiceModel $model = null;

    public function __construct(
        private readonly InvoiceRepository $repository,
        private readonly SystemConfiguration $configuration
    )
    {
    }

    public function getId(): string
    {
        return 'default';
    }

    public function setModel(InvoiceModel $model): void
    {
        $this->model = $model;
    }

    public function getInvoiceNumber(): string
    {
        $format = $this->configuration->find('invoice.number_format');
        if (empty($format) || !\is_string($format)) {
            $format = '{Y}/{cy,3}';
        }

        $invoiceDate = $this->model->getInvoiceDate();

        $loops = 0;
        $increaseBy = 0;

        $numberGenerator = new NumberGenerator($format, function (string $originalFormat, string $format, int $increaseBy) use ($invoiceDate): string|int {
            if ($this->model === null) {
                throw new \InvalidArgumentException('Missing invoice model, cannot calculate invoice number');
            }

            if ($format === 'cname' && $this->model->getCustomer()->getName() === null) {
                throw new \InvalidArgumentException('Customer has no name, replacer {cname} failed evaluation');
            }

            if ($format === 'cnumber' && $this->model->getCustomer()->getNumber() === null) {
                throw new \InvalidArgumentException('Customer has no number, replacer {cnumber} failed evaluation');
            }

            return match ($format) {
                'Y' => $invoiceDate->format('Y'),
                'y' => $invoiceDate->format('y'),
                'M' => $invoiceDate->format('m'),
                'm' => $invoiceDate->format('n'),
                'D' => $invoiceDate->format('d'),
                'd' => $invoiceDate->format('j'),
                'YY' => (int) $invoiceDate->format('Y') + $increaseBy,
                'yy' => (int) $invoiceDate->format('y') + $increaseBy,
                'MM' => (int) $invoiceDate->format('m') + $increaseBy,
                'DD' => (int) $invoiceDate->format('d') + $increaseBy,
...[truncated]...

### src/Form/Type/BudgetType.php
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

/**
 * Custom form field type to select the type of budget.
 */
final class BudgetType extends AbstractType
{
    public const TYPE_MONTH = 'month';

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'label' => 'budgetType',
            // not yet translated in enough languages
            //'placeholder' => 'budgetType_full',
            'required' => false,
            'search' => false,
            'choices' => [
                'budgetType_month' => self::TYPE_MONTH,
            ],
            'documentation' => [
                'description' => 'The type of budget. Only submit if you want to use a monthly budget.',
            ],
        ]);
    }

    public function getParent(): string
    {
        return ChoiceType::class;
    }
}

### tests/Repository/Query/TagFormTypeQueryTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Repository\Query;

use App\Repository\Query\BaseFormTypeQuery;
use App\Repository\Query\TagFormTypeQuery;
use PHPUnit\Framework\Attributes\CoversClass;

#[CoversClass(TagFormTypeQuery::class)]
#[CoversClass(BaseFormTypeQuery::class)]
class TagFormTypeQueryTest extends AbstractBaseFormTypeQueryTestCase
{
    public function testQuery(): void
    {
        $sut = new TagFormTypeQuery();

        $this->assertBaseQuery($sut);
    }
}

### src/Event/RevenueStatisticEvent.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Event;

use Symfony\Contracts\EventDispatcher\Event;

/**
 * Used to display the full revenue information for a certain date-range.
 */
final class RevenueStatisticEvent extends Event
{
    /**
     * @var array<string, float>
     */
    private array $revenue = [];

    public function __construct(private ?\DateTimeInterface $begin, private ?\DateTimeInterface $end)
    {
    }

    public function getBegin(): ?\DateTimeInterface
    {
        return $this->begin;
    }

    public function getEnd(): ?\DateTimeInterface
    {
        return $this->end;
    }

    public function getRevenue(): array
    {
        return $this->revenue;
    }

    public function addRevenue(string $currency, float $revenue): void
    {
        if (!\array_key_exists($currency, $this->revenue)) {
            $this->revenue[$currency] = 0.0;
        }

        $this->revenue[$currency] += $revenue;
    }
}

### tests/Event/TimesheetStatisticsQueryEventTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Event;

use App\Event\TimesheetStatisticsQueryEvent;
use Doctrine\ORM\EntityManager;
use Doctrine\ORM\QueryBuilder;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(TimesheetStatisticsQueryEvent::class)]
class TimesheetStatisticsQueryEventTest extends TestCase
{
    public function testGetter(): void
    {
        $qb = new QueryBuilder($this->createMock(EntityManager::class));
        self::assertCount(0, $qb->getParameters());
        $sut = new TimesheetStatisticsQueryEvent($qb);
        $qb->setParameter('foo', 'bar');

        self::assertSame($qb, $sut->getQueryBuilder());
        self::assertCount(1, $sut->getQueryBuilder()->getParameters());
    }
}

### tests/Plugin/Fixtures/TestPlugin2/TestPlugin2.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Plugin\Fixtures\TestPlugin2;

use App\Plugin\PluginInterface;

class TestPlugin2 implements PluginInterface
{
    public function getName(): string
    {
        return 'TestPlugin';
    }

    public function getPath(): string
    {
        return __DIR__;
    }
}

### src/Form/API/DateTimeApiType.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\API;

use App\API\BaseApiController;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\DateTimeType;
use Symfony\Component\OptionsResolver\OptionsResolver;

final class DateTimeApiType extends AbstractType
{
    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'documentation' => [
                'type' => 'string',
                'format' => 'date-time',
                'example' => (new \DateTime())->format(BaseApiController::DATE_FORMAT_PHP),
            ],
            'widget' => 'single_text',
            'html5' => true, // for the correct format
            'with_seconds' => false,
        ]);
    }

    public function getParent(): string
    {
        return DateTimeType::class;
    }
}

### src/Invoice/Hydrator/InvoiceModelUserHydrator.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Invoice\Hydrator;

use App\Invoice\InvoiceModel;
use App\Invoice\InvoiceModelHydrator;

final class InvoiceModelUserHydrator implements InvoiceModelHydrator
{
    public function hydrate(InvoiceModel $model): array
    {
        $user = $model->getUser();

        if (null === $user) {
            return [];
        }

        $values = [
            'user.name' => $user->getUserIdentifier(),
            'user.email' => $user->getEmail(),
            'user.title' => $user->getTitle() ?? '',
            'user.alias' => $user->getAlias() ?? '',
            'user.display' => $user->getDisplayName(),
        ];

        foreach ($user->getPreferences() as $metaField) {
            $values = array_merge($values, [
                'user.meta.' . $metaField->getName() => $metaField->getValue(),
            ]);
        }

        return $values;
    }
}

### tests/Event/InvoiceTemplateMetaDefinitionEventTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Event;

use App\Entity\InvoiceTemplate;
use App\Event\InvoiceTemplateMetaDefinitionEvent;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(InvoiceTemplateMetaDefinitionEvent::class)]
class InvoiceTemplateMetaDefinitionEventTest extends TestCase
{
    public function testGetterAndSetter(): void
    {
        $invoiceTemplate = new InvoiceTemplate();
        $sut = new InvoiceTemplateMetaDefinitionEvent($invoiceTemplate);
        self::assertSame($invoiceTemplate, $sut->getEntity());
    }
}

### src/Reporting/YearByUser/YearByUserForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Reporting\YearByUser;

use App\Form\Type\ReportSumType;
use App\Form\Type\UserType;
use App\Form\Type\YearPickerType;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

/**
 * @extends AbstractType<YearByUser>
 */
final class YearByUserForm extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder->add('date', YearPickerType::class, [
            'model_timezone' => $options['timezone'],
            'view_timezone' => $options['timezone'],
            'start_date' => $options['start_date'],
        ]);

        if ($options['include_user']) {
            $builder->add('user', UserType::class, [
                'width' => false,
                'include_current_user_if_system_account' => true,
            ]);
        }
        $builder->add('sumType', ReportSumType::class);
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => YearByUser::class,
            'timezone' => date_default_timezone_get(),
            'start_date' => new \DateTime(),
            'include_user' => false,
            'csrf_protection' => false,
            'method' => 'GET',
        ]);
    }
}

### src/EventSubscriber/Actions/TeamsSubscriber.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\EventSubscriber\Actions;

use App\Event\PageActionsEvent;

final class TeamsSubscriber extends AbstractActionsSubscriber
{
    public static function getActionName(): string
    {
        return 'teams';
    }

    public function onActions(PageActionsEvent $event): void
    {
        if ($this->isGranted('create_team')) {
            $event->addCreate($this->path('admin_team_create'));
        }
    }
}

### tests/Twig/Runtime/EncoreExtensionTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Twig\Runtime;

use App\Twig\Runtime\EncoreExtension;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;
use Symfony\Component\DependencyInjection\Container;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBag;
use Symfony\WebpackEncoreBundle\Asset\EntrypointLookupInterface;
use Twig\Error\RuntimeError;

#[CoversClass(EncoreExtension::class)]
class EncoreExtensionTest extends TestCase
{
    protected function getSut(array $files = [], bool $expectsReset = true): EncoreExtension
    {
        $entryLookup = $this->createMock(EntrypointLookupInterface::class);
        $entryLookup->expects($this->any())->method('getCssFiles')->willReturn($files);
        $entryLookup->expects($expectsReset ? $this->once() : $this->never())->method('reset');

        $container = new Container(new ParameterBag([]));
        $container->set(EntrypointLookupInterface::class, $entryLookup);

        return new EncoreExtension($container, __DIR__ . '/../');
    }

    public function testGetSubscribedServices(): void
    {
        self::assertEquals([EntrypointLookupInterface::class], EncoreExtension::getSubscribedServices());
    }

    public function testGetEncoreEntryCssSource(): void
    {
        $sut = $this->getSut(['test.css', 'test1.css']);
        $css = 'body { margin: 0; }p
{
    color: red; font-style: italic; }';
        self::assertEquals($css, $sut->getEncoreEntryCssSource('invoice'));
    }

    public function testGetEncoreEntryCssSourceIgnoresNonCssFiles(): void
    {
        $sut = $this->getSut(['test.css', 'test.js', 'test1.css', 'build/app.css.map']);
        $css = 'body { margin: 0; }p
{
    color: red; font-style: italic; }';

        self::assertEquals($css, $sut->getEncoreEntryCssSource('invoice-pdf'));
    }

    public function testGetEncoreEntryCssSourceIgnoresDirectoryTraversalPaths(): void
    {
        $sut = $this->getSut(['../composer.json', 'test.css', 'foo/../test1.css', '../ContextTest.php']);

        self::assertSame('body { margin: 0; }', $sut->getEncoreEntryCssSource('export-pdf'));
    }

    public function testGetEncoreEntryCssSourceRejectsUnknownPackage(): void
    {
        $this->expectException(RuntimeError::class);
        $this->expectExceptionMessage('Unknown CSS package requested: blub');

        $sut = $this->getSut([], false);
        $sut->getEncoreEntryCssSource('
...[truncated]...

### tests/Event/WorkingTimeQueryStatsEventTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Event;

use App\Entity\User;
use App\Event\WorkingTimeQueryStatsEvent;
use Doctrine\ORM\EntityManager;
use Doctrine\ORM\QueryBuilder;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(WorkingTimeQueryStatsEvent::class)]
class WorkingTimeQueryStatsEventTest extends TestCase
{
    public function testGetter(): void
    {
        $qb = new QueryBuilder($this->createMock(EntityManager::class));
        self::assertCount(0, $qb->getParameters());

        $user = new User();
        $begin = new \DateTime('2004-02-13');
        $end = new \DateTime('2099-12-31');

        $sut = new WorkingTimeQueryStatsEvent($qb, $user, $begin, $end);
        $qb->setParameter('foo', 'bar');

        self::assertSame($qb, $sut->getQueryBuilder());
        self::assertCount(1, $sut->getQueryBuilder()->getParameters());
        self::assertSame($user, $sut->getUser());
        self::assertSame($begin, $sut->getBegin());
        self::assertSame($end, $sut->getEnd());
    }
}

### tests/Event/CalendarDragAndDropSourceEventTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Event;

use App\Calendar\DragAndDropSource;
use App\Entity\User;
use App\Event\CalendarDragAndDropSourceEvent;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(CalendarDragAndDropSourceEvent::class)]
class CalendarDragAndDropSourceEventTest extends TestCase
{
    public function testGetterAndSetter(): void
    {
        $user = new User();
        $user->setAlias('foo');

        $sut = new CalendarDragAndDropSourceEvent($user, 10);

        $hello = new TestDragAndDropSource('hello');
        $tmp1 = new TestDragAndDropSource('foo');
        $tmp2 = new TestDragAndDropSource('bar');
        $tmp3 = new TestDragAndDropSource('hello');

        self::assertSame($user, $sut->getUser());
        self::assertIsArray($sut->getSources());
        self::assertEmpty($sut->getSources());
        self::assertInstanceOf(CalendarDragAndDropSourceEvent::class, $sut->addSource($tmp1));
        self::assertInstanceOf(CalendarDragAndDropSourceEvent::class, $sut->addSource($tmp2));
        self::assertInstanceOf(CalendarDragAndDropSourceEvent::class, $sut->addSource($hello));
        self::assertInstanceOf(CalendarDragAndDropSourceEvent::class, $sut->addSource($tmp3));
        self::assertCount(4, $sut->getSources());
        self::assertEquals([$tmp1, $tmp2, $hello, $tmp3], $sut->getSources());
        self::assertEquals(10, $sut->getMaxEntries());

        self::assertFalse($sut->removeSource(new TestDragAndDropSource('foo')));
        self::assertTrue($sut->removeSource($hello));
        self::assertFalse($sut->removeSource(new TestDragAndDropSource('world')));
        self::assertCount(3, $sut->getSources());
        self::assertEquals([$tmp1, $tmp2, $tmp3], $sut->getSources());
    }
}

class TestDragAndDropSource implements DragAndDropSource
{
    private $title;

    public function __construct(string $title)
    {
        $this->title = $title;
    }

    public function getTitle(): string
    {
        return $this->title;
    }

    public function getTranslationDomain(): string
    {
        return 'messages';
    }

    public function getRoute(): string
    {
        return '';
    }

    public function getRouteParams(): array
    {
        return [];
    }

    public function getRouteReplacer(): array
    {
        return [];
    }

    public function getMethod(): string
    {
        return '';
 
...[truncated]...

### tests/Validator/Constraints/TimesheetDeactivatedTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Validator\Constraints;

use App\Validator\Constraints\TimesheetConstraint;
use App\Validator\Constraints\TimesheetDeactivated;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(TimesheetDeactivated::class)]
class TimesheetDeactivatedTest extends TestCase
{
    public function testIsTimesheetConstraint(): void
    {
        self::assertInstanceOf(TimesheetConstraint::class, new TimesheetDeactivated());
    }
}

### tests/Controller/Reporting/UserYearControllerTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Controller\Reporting;

use PHPUnit\Framework\Attributes\Group;

#[Group('integration')]
class UserYearControllerTest extends AbstractUserPeriodControllerTestCase
{
    protected function getReportUrl(): string
    {
        return '/reporting/user/year';
    }

    protected function getExportUrl(): string
    {
        return '/reporting/user/year_export';
    }

    protected function getBoxId(): string
    {
        return 'user-year-reporting-box';
    }
}

### src/API/Serializer/ValidationFailedExceptionErrorHandler.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\API\Serializer;

use App\Entity\User;
use App\Validator\ValidationFailedException;
use FOS\RestBundle\Serializer\Normalizer\FlattenExceptionHandler;
use JMS\Serializer\Context;
use JMS\Serializer\GraphNavigatorInterface;
use JMS\Serializer\Handler\SubscribingHandlerInterface;
use JMS\Serializer\JsonSerializationVisitor;
use Symfony\Bundle\SecurityBundle\Security;
use Symfony\Component\ErrorHandler\Exception\FlattenException;
use Symfony\Component\Validator\ConstraintViolationInterface;
use Symfony\Contracts\Translation\TranslatorInterface;

final class ValidationFailedExceptionErrorHandler implements SubscribingHandlerInterface
{
    public function __construct(
        private readonly TranslatorInterface $translator,
        private readonly FlattenExceptionHandler $exceptionHandler, // @phpstan-ignore-line
        private readonly Security $security
    )
    {
    }

    public static function getSubscribingMethods(): array
    {
        return [[
            'direction' => GraphNavigatorInterface::DIRECTION_SERIALIZATION,
            'type' => FlattenException::class,
            'format' => 'json',
            'method' => 'serializeExceptionToJson',
            'priority' => -1
        ], [
            'direction' => GraphNavigatorInterface::DIRECTION_SERIALIZATION,
            'type' => ValidationFailedException::class,
            'format' => 'json',
            'method' => 'serializeValidationExceptionToJson',
            'priority' => -1
        ]];
    }

    public function serializeExceptionToJson(JsonSerializationVisitor $visitor, FlattenException $exception, array $type, Context $context)
    {
        if ($exception->getClass() !== ValidationFailedException::class) {
            return $this->exceptionHandler->serializeToJson($visitor, $exception, $type, $context); // @phpstan-ignore method.internalClass
        }

        $original = $context->getAttribute('exception');
        if ($original instanceof ValidationFailedException) {
            return $this->serializeValidationExceptionToJson($visitor, $original, $type, $context);
        }

        return $this->exceptionHandler->serializeToJson($visitor, $exception, $type, $context); // @phpstan-ignore method.internalClass
    }

    public function serializeValidationExceptionToJson(JsonSerializationVisitor $visitor, ValidationFailedException $exception, array $type, Context $co
...[truncated]...

### src/Event/TeamCreatePreEvent.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Event;

/**
 * Triggered for team instances, which are just about to being saved.
 */
final class TeamCreatePreEvent extends AbstractTeamEvent
{
}

### src/Event/ProjectDetailControllerEvent.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Event;

/**
 * Triggered for project detail pages, to add additional content boxes.
 *
 * @see https://symfony.com/doc/5.4/templates.html#embedding-controllers
 */
final class ProjectDetailControllerEvent extends AbstractProjectEvent
{
    /**
     * @var array<string>
     */
    private array $controller = [];

    public function addController(string $controller): void
    {
        $this->controller[] = $controller;
    }

    /**
     * @return string[]
     */
    public function getController(): array
    {
        return $this->controller;
    }
}

### tests/Event/TeamUpdatePreEventTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Event;

use App\Entity\Team;
use App\Event\AbstractTeamEvent;
use App\Event\TeamUpdatePreEvent;
use PHPUnit\Framework\Attributes\CoversClass;

#[CoversClass(AbstractTeamEventTestCase::class)]
#[CoversClass(TeamUpdatePreEvent::class)]
class TeamUpdatePreEventTest extends AbstractTeamEventTestCase
{
    protected function createTeamEvent(Team $team): AbstractTeamEvent
    {
        return new TeamUpdatePreEvent($team);
    }
}