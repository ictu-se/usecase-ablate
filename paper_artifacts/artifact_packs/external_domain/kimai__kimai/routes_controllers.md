# Routes/controllers
### tests/API/Model/VersionTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\API\Model;

use App\API\Model\Version;
use App\Constants;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(Version::class)]
class VersionTest extends TestCase
{
    public function testValues(): void
    {
        $sut = new Version();

        self::assertEquals(Constants::VERSION, $sut->version);
        self::assertEquals(Constants::VERSION_ID, $sut->versionId);
        self::assertEquals(Constants::SOFTWARE . ' ' . Constants::VERSION . ' by Kevin Papst.', $sut->copyright);
    }
}

### tests/API/Model/PageActionTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\API\Model;

use App\API\Model\PageAction;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(PageAction::class)]
class PageActionTest extends TestCase
{
    public function testEmptySettings(): void
    {
        $options = [];

        $sut = new PageAction('foo', $options);

        $obj = new \ReflectionClass($sut);

        self::assertEquals('foo', $obj->getProperty('id')->getValue($sut));
        self::assertEquals('foo', $obj->getProperty('title')->getValue($sut));
        self::assertEquals('', $obj->getProperty('url')->getValue($sut));
        self::assertEquals('', $obj->getProperty('class')->getValue($sut));
        self::assertFalse($obj->getProperty('divider')->getValue($sut));
        self::assertIsArray($obj->getProperty('attr')->getValue($sut));
    }

    public function testWithSettings(): void
    {
        $options = [
            'title' => 'bar',
            'url' => 'http://sdkfjhaslkdjfhaskljh',
            'class' => 'btn-primary',
        ];

        $sut = new PageAction('trash', $options);

        $obj = new \ReflectionClass($sut);

        self::assertEquals('trash', $obj->getProperty('id')->getValue($sut));
        self::assertEquals('bar', $obj->getProperty('title')->getValue($sut));
        self::assertEquals('http://sdkfjhaslkdjfhaskljh', $obj->getProperty('url')->getValue($sut));
        self::assertEquals('btn-primary', $obj->getProperty('class')->getValue($sut));
        self::assertTrue($obj->getProperty('divider')->getValue($sut));
        self::assertIsArray($obj->getProperty('attr')->getValue($sut));
    }

    public function testDivider(): void
    {
        $options = [
            'title' => 'bar',
            'url' => null,
            'class' => 'btn-primary',
        ];

        $sut = new PageAction('divider0', $options);

        $obj = new \ReflectionClass($sut);

        self::assertEquals('divider0', $obj->getProperty('id')->getValue($sut));
        self::assertEquals('bar', $obj->getProperty('title')->getValue($sut));
        self::assertNull($obj->getProperty('url')->getValue($sut));
        self::assertEquals('btn-primary', $obj->getProperty('class')->getValue($sut));
        self::assertTrue($obj->getProperty('divider')->getValue($sut));
        self::assertIsArray($obj->getProperty('attr')->getValue($sut));
    }
}

### tests/API/Model/TimesheetConfigTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\API\Model;

use App\API\Model\TimesheetConfig;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(TimesheetConfig::class)]
class TimesheetConfigTest extends TestCase
{
    public function testSetter(): void
    {
        $sut = new TimesheetConfig();
        $sut->setIsAllowFutureTimes(false);
        $sut->setIsAllowOverlapping(false);
        $sut->setDefaultBeginTime('08:00');
        $sut->setTrackingMode('punch');
        $sut->setActiveEntriesHardLimit(3);

        $obj = new \ReflectionClass($sut);

        self::assertFalse($obj->getProperty('isAllowFutureTimes')->getValue($sut));
        self::assertFalse($obj->getProperty('isAllowOverlapping')->getValue($sut));
        self::assertEquals('08:00', $obj->getProperty('defaultBeginTime')->getValue($sut));
        self::assertEquals('punch', $obj->getProperty('trackingMode')->getValue($sut));
        self::assertEquals(3, $obj->getProperty('activeEntriesHardLimit')->getValue($sut));
    }
}

### tests/Form/Type/CalendarViewTypeTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Form\Type;

use App\Form\Type\CalendarViewType;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\Attributes\DataProvider;
use Symfony\Component\Form\Extension\Core\Type\FormType;
use Symfony\Component\Form\Test\TypeTestCase;

#[CoversClass(CalendarViewType::class)]
class CalendarViewTypeTest extends TypeTestCase
{
    /**
     * @return iterable<int, array<int, string>>
     */
    public static function getTestData(): iterable
    {
        yield ['month', 'month'];
        yield ['week', 'week'];
        yield ['day', 'day'];
    }

    #[DataProvider('getTestData')]
    public function testSubmitValidData(string $value, string $expected): void
    {
        $data = ['view' => $value];
        $model = new TypeTestModel(['view' => 'some']);

        $form = $this->factory->createBuilder(FormType::class, $model);
        $form->add('view', CalendarViewType::class);
        $form = $form->getForm();

        $expected = new TypeTestModel([
            'view' => $expected
        ]);

        $form->submit($data);

        self::assertTrue($form->isSynchronized());
        self::assertEquals($expected, $model);
    }
}

### tests/Reporting/ProjectView/ProjectViewModelTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\Reporting\ProjectView;

use App\Entity\Project;
use App\Model\ProjectBudgetStatisticModel;
use App\Model\Statistic\BudgetStatistic;
use App\Reporting\ProjectView\ProjectViewModel;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;

#[CoversClass(ProjectViewModel::class)]
class ProjectViewModelTest extends TestCase
{
    public function testDefaults(): void
    {
        $project = new Project();
        $model = new ProjectBudgetStatisticModel($project);
        $total = new BudgetStatistic();
        $model->setStatisticTotal($total);
        $sut = new ProjectViewModel($model);

        self::assertSame($project, $sut->getProject());
        self::assertSame(0, $sut->getDurationDay());
        self::assertSame(0, $sut->getDurationMonth());
        self::assertSame(0, $sut->getDurationTotal());
        self::assertSame(0, $sut->getDurationWeek());
        self::assertSame(0, $sut->getNotExportedDuration());
        self::assertSame(0.0, $sut->getNotExportedRate());
        self::assertSame(0.0, $sut->getRateTotal());
        self::assertNull($sut->getLastRecord());
        self::assertNull($sut->getLastRecord());
        self::assertSame(0.0, $sut->getBillableRate());
        self::assertSame(0, $sut->getBillableDuration());
    }

    public function testSetterGetter(): void
    {
        $project = new Project();

        $model = new ProjectBudgetStatisticModel($project);
        $total = new BudgetStatistic();
        $total->setCounter(123);
        $total->setDuration(3456789);
        $total->setDurationBillable(3456789);
        $total->setDurationBillableExported(3400000);
        $total->setRate(789.0);
        $total->setRateBillable(16789.0);
        $total->setRateBillableExported(10000.0);
        $model->setStatisticTotal($total);

        $sut = new ProjectViewModel($model);

        $date = new \DateTime();

        $sut->setDurationDay(123456789);
        $sut->setDurationMonth(23456789);
        $sut->setDurationWeek(456789);
        $sut->setLastRecord($date);

        self::assertSame(123456789, $sut->getDurationDay());
        self::assertSame(23456789, $sut->getDurationMonth());
        self::assertSame(3456789, $sut->getDurationTotal());
        self::assertSame(456789, $sut->getDurationWeek());
        self::assertSame(56789, $sut->getNotExportedDuration());
        self::assertSame(6789.
...[truncated]...

### tests/API/Serializer/ValidationFailedExceptionErrorHandlerTest.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Tests\API\Serializer;

use App\API\Serializer\ValidationFailedExceptionErrorHandler;
use App\Validator\ValidationFailedException;
use FOS\RestBundle\Serializer\Normalizer\FlattenExceptionHandler;
use JMS\Serializer\GraphNavigatorInterface;
use JMS\Serializer\JsonSerializationVisitor;
use JMS\Serializer\SerializationContext;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;
use Symfony\Bundle\SecurityBundle\Security;
use Symfony\Component\ErrorHandler\Exception\FlattenException;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Validator\ConstraintViolation;
use Symfony\Component\Validator\ConstraintViolationList;
use Symfony\Contracts\Translation\TranslatorInterface;

#[CoversClass(ValidationFailedExceptionErrorHandler::class)]
class ValidationFailedExceptionErrorHandlerTest extends TestCase
{
    public function testSubscribingMethods(): void
    {
        self::assertEquals([[
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
        ]], ValidationFailedExceptionErrorHandler::getSubscribingMethods());
    }

    public function testWithEmptyConstraintsList(): void
    {
        $security = $this->createMock(Security::class);
        $translator = $this->createMock(TranslatorInterface::class);
        $handler = $this->createMock(FlattenExceptionHandler::class);
        $sut = new ValidationFailedExceptionErrorHandler($translator, $handler, $security);

        $constraints = new ConstraintViolationList();
        $validations = new ValidationFailedException($constraints, 'Uuups, that is broken');

        $expected = [
            'code' => Response::HTTP_BAD_REQUEST,
            'message' => null,
            'errors' => [
                'children' => []
            ]
        ];
        self::assertEquals($expected, $sut->serializeValidationExceptionToJson(new JsonSerializationVisitor(), $validations, [], new SerializationContext()));
    }

    pub
...[truncated]...

### src/Form/UserApiPasswordType.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form;

use App\Entity\User;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\PasswordType;
use Symfony\Component\Form\Extension\Core\Type\RepeatedType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

/**
 * Defines the form used to set the users API password.
 * @extends AbstractType<User>
 */
final class UserApiPasswordType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('plainApiToken', RepeatedType::class, [
                'type' => PasswordType::class,
                'first_options' => ['label' => 'api_token'],
                'second_options' => ['label' => 'api_token_repeat'],
            ])
        ;
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'validation_groups' => ['ApiTokenUpdate'],
            'data_class' => User::class,
            'csrf_protection' => true,
            'csrf_field_name' => '_token',
            'csrf_token_id' => 'edit_user_password_token',
        ]);
    }
}

### src/Repository/ApiUserRepository.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Repository;

use App\Entity\User;
use Symfony\Bridge\Doctrine\Security\User\UserLoaderInterface;
use Symfony\Component\Security\Core\Exception\UserNotFoundException;
use Symfony\Component\Security\Core\User\PasswordAuthenticatedUserInterface;
use Symfony\Component\Security\Core\User\PasswordUpgraderInterface;
use Symfony\Component\Security\Core\User\UserInterface;

/**
 * @deprecated since 2.54 - see https://www.kimai.org/en/blog/2026/removing-api-passwords
 */
class ApiUserRepository implements UserLoaderInterface, PasswordUpgraderInterface
{
    public function __construct(private readonly UserRepository $userRepository)
    {
    }

    public function loadUserByIdentifier(string $identifier): ?UserInterface
    {
        try {
            return $this->userRepository->loadUserByIdentifier($identifier);
        } catch (UserNotFoundException $ex) {
            return null;
        }
    }

    public function upgradePassword(PasswordAuthenticatedUserInterface|UserInterface $user, string $newHashedPassword): void
    {
        if (!($user instanceof User)) {
            return;
        }

        try {
            $user->setApiToken($newHashedPassword);
            $this->userRepository->saveUser($user);
        } catch (\Exception $ex) {
            // happens during login: if it fails, ignore it!
        }
    }
}

### src/Form/API/UserApiEditForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\API;

use App\Form\Type\UserRoleType;
use App\Form\UserEditType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

final class UserApiEditForm extends UserEditType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        parent::buildForm($builder, $options);

        if ($options['include_roles']) {
            $builder->add('roles', UserRoleType::class, [
                'label' => 'roles',
                'required' => false,
                'multiple' => true,
                'expanded' => false,
            ]);
        }
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        parent::configureOptions($resolver);

        $resolver->setDefaults([
            'csrf_protection' => false,
            'include_roles' => true,
        ]);
    }
}

### src/Form/API/UserApiCreateForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\API;

use App\Form\Type\UserRoleType;
use App\Form\UserCreateType;
use Symfony\Component\Form\Extension\Core\Type\PasswordType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

final class UserApiCreateForm extends UserCreateType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        parent::buildForm($builder, $options);

        if ($builder->has('plainPassword')) {
            $builder->remove('plainPassword');
        }

        $builder->add('plainPassword', PasswordType::class, [
            'required' => true,
            'label' => 'password',
            'documentation' => [
                'type' => 'string',
                'description' => 'Plain text password',
            ],
        ]);

        if ($builder->has('plainApiToken')) {
            $builder->remove('plainApiToken');
        }

        $builder->add('plainApiToken', PasswordType::class, [
            'required' => false,
            'label' => 'api_token',
            'documentation' => [
                'type' => 'string',
                'description' => 'Plain API token',
            ],
        ]);

        if ($options['include_roles']) {
            $builder->add('roles', UserRoleType::class, [
                'label' => 'roles',
                'required' => false,
                'multiple' => true,
                'expanded' => false,
            ]);
        }
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        parent::configureOptions($resolver);

        $resolver->setDefaults([
            'csrf_protection' => false,
            'include_roles' => true,
        ]);
    }
}

### src/API/Model/Plugin.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\API\Model;

use App\Plugin\Plugin as CorePlugin;
use JMS\Serializer\Annotation as Serializer;

#[Serializer\ExclusionPolicy('all')]
final class Plugin
{
    /**
     * The plugin name, eg. "ExpensesBundle"
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    private ?string $name = null;
    /**
     * The plugin version, eg. "1.14"
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    private ?string $version = null;

    public function __construct(CorePlugin $plugin)
    {
        $this->name = $plugin->getId();
        $this->version = $plugin->getMetadata()->getVersion();
    }
}

### src/API/Model/Version.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\API\Model;

use App\Constants;
use JMS\Serializer\Annotation as Serializer;

#[Serializer\ExclusionPolicy('all')]
final class Version
{
    /**
     * Kimai Version, eg. "2.0.0"
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    public readonly string $version;
    /**
     * Kimai Version as integer, eg. 20000
     *
     * Follows the same logic as PHP_VERSION_ID, see https://www.php.net/manual/de/function.phpversion.php
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'integer')]
    public readonly int $versionId;
    /**
     * A full copyright notice
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    public readonly string $copyright;

    public function __construct()
    {
        $this->version = Constants::VERSION;
        $this->versionId = Constants::VERSION_ID;
        $this->copyright = Constants::SOFTWARE . ' ' . Constants::VERSION . ' by Kevin Papst.';
    }
}

### src/API/Model/PageAction.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\API\Model;

use JMS\Serializer\Annotation as Serializer;

/**
 * @internal
 */
#[Serializer\ExclusionPolicy('all')]
final class PageAction
{
    /**
     * ID of the action
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    public readonly string $id;
    /**
     * Translated title to show the user
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    public readonly string $title;
    /**
     * URL of the action
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    public readonly ?string $url;
    /**
     * HTML classes to be used
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    public readonly ?string $class;
    /**
     * HTML (data) attributes to render the action
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'array<string, string>')]
    public readonly array $attr;
    /**
     * Whether to render a divider before this item
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'boolean')]
    public readonly bool $divider;

    public function __construct(string $title, array $settings = [])
    {
        $this->id = $title;
        $this->title = $settings['title'] ?? $title;
        $this->url = $settings['url'] ?? null;
        $this->class = $settings['class'] ?? null;
        $this->attr = $settings['attr'] ?? [];

        $this->divider = ($title === 'trash' || (str_contains($title, 'divider') && ($this->url === null || $this->url === '')));
    }
}

### src/API/Model/CalendarEvent.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\API\Model;

use App\Utils\Color;
use JMS\Serializer\Annotation as Serializer;

#[Serializer\ExclusionPolicy('all')]
final class CalendarEvent
{
    /**
     * Calendar entry title
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    private string $title; // @phpstan-ignore-line
    /**
     * Calendar background color
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    private ?string $color = null; // @phpstan-ignore-line
    /**
     * Calendar text color
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'string')]
    private ?string $textColor = null;
    /**
     * If this entry is all-day long
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'boolean')]
    private bool $allDay = false; // @phpstan-ignore-line
    /**
     * Calendar entry start date
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'DateTimeImmutable')]
    private \DateTimeImmutable $start; // @phpstan-ignore-line
    /**
     * Calendar entry end date
     */
    #[Serializer\Expose]
    #[Serializer\Groups(['Default'])]
    #[Serializer\Type(name: 'DateTimeImmutable')]
    private \DateTimeImmutable $end; // @phpstan-ignore-line

    public function setTitle(string $title): void
    {
        $this->title = $title;
    }

    public function setStart(\DateTimeInterface $start): void
    {
        $this->start = \DateTimeImmutable::createFromInterface($start);
    }

    public function setEnd(\DateTimeInterface $end): void
    {
        $this->end = \DateTimeImmutable::createFromInterface($end);
    }

    public function setColor(?string $color): void
    {
        $this->color = $color;
        if ($color !== null && $this->textColor === null) {
            $this->textColor = (new Color())->getFontContrastColor($color);
        }
    }

    public function setAllDay(bool $allDay): void
    {
        $this->allDay = $allDay;
    }

    public function setTextColor(?string $textColor): void
    {
        $this->textColor = $textColor;
    }
}

### src/Form/API/CommentApiForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\API;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\CheckboxType;
use Symfony\Component\Form\Extension\Core\Type\TextareaType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

final class CommentApiForm extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder->add('pinned', CheckboxType::class, [
            'required' => false,
            'documentation' => [
                'default' => false,
                'description' => 'Pinned comments always appear first'
            ],
        ]);

        $builder->add('message', TextareaType::class, [
            'label' => false,
            'documentation' => [
                'description' => 'The actual comment (markdown is supported)'
            ],
        ]);
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'csrf_protection' => false,
        ]);
    }
}

### src/Form/API/TagApiEditForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\API;

use App\Form\TagEditForm;

final class TagApiEditForm extends TagEditForm
{
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

### src/Form/API/TeamApiEditForm.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Form\API;

use App\Form\TeamEditForm;
use Symfony\Component\Form\FormBuilderInterface;

final class TeamApiEditForm extends TeamEditForm
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        parent::buildForm($builder, $options);
        $builder->remove('users');
    }
}