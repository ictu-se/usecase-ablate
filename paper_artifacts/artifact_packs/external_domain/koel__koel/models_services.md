# Models/services
### app/Providers/RouteServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\Route;
use Webmozart\Assert\Assert;

class RouteServiceProvider extends ServiceProvider
{
    public static function loadVersionAwareRoutes(string $type): void
    {
        Assert::oneOf($type, ['web', 'api']);

        Route::group([], base_path(sprintf('routes/%s.base.php', $type)));

        $apiVersion = self::getApiVersion();
        $routeFile = $apiVersion ? base_path(sprintf('routes/%s.%s.php', $type, $apiVersion)) : null;

        if ($routeFile && File::exists($routeFile)) {
            Route::group([], $routeFile);
        }
    }

    private static function getApiVersion(): ?string
    {
        // In the test environment, the route service provider is loaded _before_ the request is made,
        // so we can't rely on the header.
        // Instead, we manually set the API version as an env variable in applicable test cases.
        return app()->runningUnitTests() ? env('X_API_VERSION') : request()->header('X-Api-Version');
    }
}

### app/Http/Controllers/API/FetchAlbumInformationController.php
<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Album;
use App\Services\Integrations\EncyclopediaService;

class FetchAlbumInformationController extends Controller
{
    public function __invoke(Album $album, EncyclopediaService $encyclopediaService)
    {
        return response()->json($encyclopediaService->getAlbumInformation($album));
    }
}

### app/Http/Controllers/API/Artist/FetchArtistInformationController.php
<?php

namespace App\Http\Controllers\API\Artist;

use App\Http\Controllers\Controller;
use App\Models\Artist;
use App\Services\Integrations\EncyclopediaService;

class FetchArtistInformationController extends Controller
{
    public function __invoke(Artist $artist, EncyclopediaService $encyclopediaService)
    {
        return response()->json($encyclopediaService->getArtistInformation($artist));
    }
}

### tests/Unit/Models/UserTest.php
<?php

namespace Tests\Unit\Models;

use App\Enums\Acl\Role;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_admin;
use function Tests\create_manager;
use function Tests\create_user;

class UserTest extends TestCase
{
    /**
     * In CE, MANAGER is filtered out by Role::available() (Plus-only). The admin can manage
     * USER and ADMIN via canManage(), and getAssignableRoles() returns them ordered by level()
     * ascending — hence [USER, ADMIN].
     */
    #[Test]
    public function adminCanAssignAvailableRolesOrderedByLevel(): void
    {
        $admin = create_admin();

        self::assertSame([Role::USER, Role::ADMIN], $admin->getAssignableRoles()->all());
    }

    /**
     * Two filters apply for a manager (created via create_manager()): canManage() excludes
     * ADMIN (level 3 > manager's level 2), and Role::available() also filters out MANAGER
     * itself in CE. Net result of getAssignableRoles() is [USER] only.
     */
    #[Test]
    public function managerCannotAssignRolesAboveTheirLevel(): void
    {
        $manager = create_manager();

        self::assertSame([Role::USER], $manager->getAssignableRoles()->all());
    }

    #[Test]
    public function userWithoutManageAbilityCannotAssignAnyRoles(): void
    {
        $user = create_user();

        self::assertSame([], $user->getAssignableRoles()->all());
    }
}

### tests/Integration/Services/UserServiceTest.php
<?php

namespace Tests\Integration\Services;

use App\Enums\Acl\Role;
use App\Exceptions\UserProspectUpdateDeniedException;
use App\Services\UserService;
use App\Values\User\UserCreateData;
use App\Values\User\UserUpdateData;
use Illuminate\Support\Facades\Hash;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_admin;
use function Tests\create_user;
use function Tests\create_user_prospect;
use function Tests\minimal_base64_encoded_image;

class UserServiceTest extends TestCase
{
    private UserService $service;

    public function setUp(): void
    {
        parent::setUp();

        $this->service = app(UserService::class);
    }

    #[Test]
    public function createUser(): void
    {
        $user = $this->service->createUser(UserCreateData::make(
            name: 'Bruce Dickinson',
            email: 'bruce@dickison.com',
            plainTextPassword: 'FearOfTheDark',
            role: Role::ADMIN,
            avatar: minimal_base64_encoded_image(),
        ));

        $this->assertModelExists($user);
        self::assertTrue(Hash::check('FearOfTheDark', $user->password));
        self::assertSame(Role::ADMIN, $user->role);
        self::assertFileExists(image_storage_path($user->getRawOriginal('avatar')));
    }

    #[Test]
    public function createUserWithEmptyAvatarHasGravatar(): void
    {
        $user = $this->service->createUser(UserCreateData::make(
            name: 'Bruce Dickinson',
            email: 'bruce@dickison.com',
            plainTextPassword: 'FearOfTheDark',
        ));

        $this->assertModelExists($user);
        self::assertTrue(Hash::check('FearOfTheDark', $user->password));
        self::assertSame(Role::USER, $user->role);
        self::assertStringStartsWith('https://www.gravatar.com/avatar/', $user->avatar);
    }

    #[Test]
    public function createUserWithNoPassword(): void
    {
        $user = $this->service->createUser(UserCreateData::make(
            name: 'Bruce Dickinson',
            email: 'bruce@dickison.com',
            plainTextPassword: '',
        ));

        $this->assertModelExists($user);
        self::assertEmpty($user->password);
    }

    #[Test]
    public function updateUser(): void
    {
        $user = create_user();

        $this->service->updateUser($user, UserUpdateData::make(
            name: 'Steve Harris',
            email: 'steve@iron.com',
            plainTextPassword: 'TheTrooper',
            role: Role::ADMIN,
            avatar: minimal_base64_encoded_image(),
        ));

        $user->refresh();

        self::assertSame('
...[truncated]...

### tests/Integration/Services/LibraryManagerTest.php
<?php

namespace Tests\Integration\Services;

use App\Models\Album;
use App\Models\Artist;
use App\Models\Song;
use App\Services\LibraryManager;
use Laravel\Scout\EngineManager;
use Laravel\Scout\Engines\Engine;
use Mockery;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class LibraryManagerTest extends TestCase
{
    private LibraryManager $libraryManager;

    public function setUp(): void
    {
        parent::setUp();

        $this->libraryManager = app(LibraryManager::class);
    }

    #[Test]
    public function prunesEmptyAlbumsAndArtists(): void
    {
        $emptyAlbum = Album::factory()->createOne();
        $emptyArtist = Artist::factory()->createOne();

        $albumWithSongs = Album::factory()->createOne();
        Song::factory()->for($albumWithSongs)->createOne();

        $this->libraryManager->prune();

        self::assertModelMissing($emptyAlbum);
        self::assertModelMissing($emptyArtist);
        self::assertModelExists($albumWithSongs);
    }

    #[Test]
    public function dryRunDoesNotDelete(): void
    {
        $emptyAlbum = Album::factory()->createOne();
        $emptyArtist = Artist::factory()->createOne();

        $this->libraryManager->prune(dryRun: true);

        self::assertModelExists($emptyAlbum);
        self::assertModelExists($emptyArtist);
    }

    #[Test]
    public function flushesEmptyAlbumsAndArtistsFromSearchIndex(): void
    {
        $engine = Mockery::spy(Engine::class);
        $manager = Mockery::mock(EngineManager::class);
        $manager->shouldReceive('engine')->andReturn($engine);
        $this->app->instance(EngineManager::class, $manager);

        Album::factory()->createOne();
        Artist::factory()->createOne();

        $this->libraryManager->prune();

        $engine->shouldHaveReceived('delete')->twice(); // @phpstan-ignore-line
    }

    #[Test]
    public function dryRunDoesNotTouchSearchIndex(): void
    {
        $engine = Mockery::spy(Engine::class);
        $manager = Mockery::mock(EngineManager::class);
        $manager->shouldReceive('engine')->andReturn($engine);
        $this->app->instance(EngineManager::class, $manager);

        Album::factory()->createOne();

        $this->libraryManager->prune(dryRun: true);

        $engine->shouldNotHaveReceived('delete');
    }
}

### tests/Integration/Services/UserInvitationServiceTest.php
<?php

namespace Tests\Integration\Services;

use App\Enums\Acl\Role;
use App\Exceptions\InvitationNotFoundException;
use App\Mail\UserInvite;
use App\Models\User;
use App\Services\UserInvitationService;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Str;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_admin;

class UserInvitationServiceTest extends TestCase
{
    private UserInvitationService $service;

    public function setUp(): void
    {
        parent::setUp();

        $this->service = app(UserInvitationService::class);
    }

    #[Test]
    public function invite(): void
    {
        Mail::fake();

        $emails = ['foo@bar.com', 'bar@baz.io'];
        $user = create_admin();

        $this->service
            ->invite($emails, Role::ADMIN, $user)
            ->each(static function (User $prospect) use ($user): void {
                self::assertSame(Role::ADMIN, $prospect->role);
                self::assertTrue($prospect->invitedBy->is($user));
                self::assertTrue($prospect->is_prospect);
                self::assertNotNull($prospect->invitation_token);
                self::assertNotNull($prospect->invited_at);
                self::assertNull($prospect->invitation_accepted_at);
            });

        Mail::assertQueued(UserInvite::class, 2);
    }

    #[Test]
    public function getUserProspectByToken(): void
    {
        $token = Str::uuid()->toString();
        $user = create_admin();

        $prospect = User::factory()->for($user, 'invitedBy')->createOne([
            'invitation_token' => $token,
            'invited_at' => now(),
        ]);

        self::assertTrue($this->service->getUserProspectByToken($token)->is($prospect));
    }

    #[Test]
    public function getUserProspectByTokenThrowsIfTokenNotFound(): void
    {
        $this->expectException(InvitationNotFoundException::class);
        $this->service->getUserProspectByToken(Str::uuid()->toString());
    }

    #[Test]
    public function revokeByEmail(): void
    {
        $user = create_admin();
        $prospect = User::factory()->for($user, 'invitedBy')->createOne([
            'invitation_token' => Str::uuid()->toString(),
            'invited_at' => now(),
        ]);

        $this->service->revokeByEmail($prospect->email);

        $this->assertModelMissing($prospect);
    }

    #[Test]
    public function accept(): void
    {
        $admin = create_admin();
        $prospect = User::factory()->for($admin, 'invitedBy')->admin()->prospect()->createOne();


...[truncated]...

### tests/Unit/KoelPlus/Models/UserTest.php
<?php

namespace Tests\Unit\KoelPlus\Models;

use App\Enums\Acl\Role;
use PHPUnit\Framework\Attributes\Test;
use Tests\PlusTestCase;

use function Tests\create_admin;
use function Tests\create_manager;

class UserTest extends PlusTestCase
{
    /**
     * In Plus, Role::available() admits MANAGER and GUEST. The admin's canManage() permits every
     * role, so getAssignableRoles() returns all four ordered by level() ascending.
     */
    #[Test]
    public function adminCanAssignAllRolesOrderedByLevel(): void
    {
        $admin = create_admin();

        self::assertSame([Role::GUEST, Role::USER, Role::MANAGER, Role::ADMIN], $admin->getAssignableRoles()->all());
    }

    /**
     * In Plus, MANAGER passes Role::available() and the manager satisfies canManage(MANAGER)
     * since 2 >= 2; only ADMIN is filtered out by canManage() (level 3 > manager's 2). Net
     * result of getAssignableRoles() is [GUEST, USER, MANAGER].
     */
    #[Test]
    public function managerCannotAssignAdminRole(): void
    {
        $manager = create_manager();

        self::assertSame([Role::GUEST, Role::USER, Role::MANAGER], $manager->getAssignableRoles()->all());
    }
}

### tests/Integration/KoelPlus/Services/UserServiceTest.php
<?php

namespace Tests\Integration\KoelPlus\Services;

use App\Enums\Acl\Role;
use App\Models\User;
use App\Services\UserService;
use App\Values\User\SsoUser;
use App\Values\User\UserCreateData;
use App\Values\User\UserUpdateData;
use Illuminate\Support\Facades\Hash;
use Laravel\Socialite\Two\User as SocialiteUser;
use Mockery;
use PHPUnit\Framework\Attributes\Test;
use Tests\PlusTestCase;

use function Tests\create_user;

class UserServiceTest extends PlusTestCase
{
    private UserService $service;

    public function setUp(): void
    {
        parent::setUp();

        $this->service = app(UserService::class);
    }

    #[Test]
    public function createUserViaSsoProvider(): void
    {
        $user = $this->service->createUser(UserCreateData::make(
            name: 'Bruce Dickinson',
            email: 'bruce@dickison.com',
            plainTextPassword: '',
            role: Role::ADMIN,
            avatar: 'https://lh3.googleusercontent.com/a/vatar',
            ssoId: '123',
            ssoProvider: 'Google',
        ));

        $this->assertModelExists($user);
        self::assertSame('Google', $user->sso_provider);
        self::assertSame('123', $user->sso_id);
        self::assertSame('https://lh3.googleusercontent.com/a/vatar', $user->avatar);
    }

    #[Test]
    public function createUserFromSso(): void
    {
        $this->assertDatabaseMissing(User::class, ['email' => 'bruce@iron.com']);

        $socialiteUser = Mockery::mock(SocialiteUser::class, [
            'getId' => '123',
            'getEmail' => 'bruce@iron.com',
            'getName' => 'Bruce Dickinson',
            'getAvatar' => 'https://lh3.googleusercontent.com/a/vatar',
        ]);

        $user = $this->service->createOrUpdateUserFromSso(SsoUser::fromSocialite($socialiteUser, 'Google'));

        $this->assertModelExists($user);

        self::assertSame('Google', $user->sso_provider);
        self::assertSame('Bruce Dickinson', $user->name);
        self::assertSame('bruce@iron.com', $user->email);
        self::assertSame('123', $user->sso_id);
        self::assertSame('https://lh3.googleusercontent.com/a/vatar', $user->avatar);
    }

    #[Test]
    public function updateUserFromSsoId(): void
    {
        $user = create_user([
            'email' => 'bruce@iron.com',
            'name' => 'Bruce Dickinson',
            'sso_id' => '123',
            'sso_provider' => 'Google',
        ]);

        $socialiteUser = Mockery::mock(SocialiteUser::class, [
            'getId' => '123',
            'getEmail' => 'steve@iron.com',
            'getName' => 'Steve Ha
...[truncated]...

### tests/Fakes/FakePlusLicenseService.php
<?php

namespace Tests\Fakes;

use App\Exceptions\MethodNotImplementedException;
use App\Models\License;
use App\Services\License\Contracts\LicenseServiceInterface;
use App\Values\License\LicenseStatus;

class FakePlusLicenseService implements LicenseServiceInterface
{
    public function activate(string $key): License
    {
        throw MethodNotImplementedException::method(__METHOD__);
    }

    public function deactivate(License $license): void
    {
        throw MethodNotImplementedException::method(__METHOD__);
    }

    public function getStatus(bool $checkCache = true): LicenseStatus
    {
        throw MethodNotImplementedException::method(__METHOD__);
    }

    public function isPlus(): bool
    {
        return true;
    }

    public function isCommunity(): bool
    {
        return false;
    }
}

### tests/Feature/AlbumInformationTest.php
<?php

namespace Tests\Feature;

use App\Models\Album;
use App\Services\Integrations\EncyclopediaService;
use App\Values\Album\AlbumInformation;
use Mockery;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class AlbumInformationTest extends TestCase
{
    #[Test]
    public function getInformation(): void
    {
        config(['koel.services.lastfm.key' => 'foo']);
        config(['koel.services.lastfm.secret' => 'geheim']);
        $album = Album::factory()->createOne();

        $lastfm = $this->mock(EncyclopediaService::class);
        $lastfm
            ->expects('getAlbumInformation')
            ->with(Mockery::on(static fn (Album $a) => $a->is($album)))
            ->andReturn(AlbumInformation::make(
                url: 'https://lastfm.com/album/foo',
                cover: 'https://lastfm.com/cover/foo',
                wiki: [
                    'summary' => 'foo',
                    'full' => 'bar',
                ],
                tracks: [
                    [
                        'title' => 'foo',
                        'length' => 123,
                        'url' => 'https://lastfm.com/track/foo',
                    ],
                    [
                        'title' => 'bar',
                        'length' => 456,
                        'url' => 'https://lastfm.com/track/bar',
                    ],
                ],
            ));

        $this->getAs("api/albums/{$album->id}/information")->assertJsonStructure(AlbumInformation::JSON_STRUCTURE);
    }

    #[Test]
    public function getWithoutLastfmStillReturnsValidStructure(): void
    {
        config(['koel.services.lastfm.key' => null]);
        config(['koel.services.lastfm.secret' => null]);

        $this->getAs(
            'api/albums/' . Album::factory()->createOne()->id . '/information',
        )->assertJsonStructure(AlbumInformation::JSON_STRUCTURE);
    }
}

### tests/Feature/ArtistInformationTest.php
<?php

namespace Tests\Feature;

use App\Models\Artist;
use App\Services\Integrations\EncyclopediaService;
use App\Values\Artist\ArtistInformation;
use Mockery;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class ArtistInformationTest extends TestCase
{
    #[Test]
    public function getInformation(): void
    {
        config(['koel.services.lastfm.key' => 'foo']);
        config(['koel.services.lastfm.secret' => 'geheim']);
        $artist = Artist::factory()->createOne();

        $lastfm = $this->mock(EncyclopediaService::class);
        $lastfm
            ->expects('getArtistInformation')
            ->with(Mockery::on(static fn (Artist $a) => $a->is($artist)))
            ->andReturn(ArtistInformation::make(
                url: 'https://lastfm.com/artist/foo',
                image: 'https://lastfm.com/image/foo',
                bio: [
                    'summary' => 'foo',
                    'full' => 'bar',
                ],
            ));

        $this->getAs("api/artists/{$artist->id}/information")->assertJsonStructure(ArtistInformation::JSON_STRUCTURE);
    }

    #[Test]
    public function getWithoutLastfmStillReturnsValidStructure(): void
    {
        config(['koel.services.lastfm.key' => null]);
        config(['koel.services.lastfm.secret' => null]);

        $this->getAs(
            'api/artists/' . Artist::factory()->createOne()->id . '/information',
        )->assertJsonStructure(ArtistInformation::JSON_STRUCTURE);
    }
}

### tests/Unit/Models/SongTest.php
<?php

namespace Tests\Unit\Models;

use App\Enums\SongStorageType;
use App\Models\Genre;
use App\Models\Song;
use App\Values\SongStorageMetadata\S3CompatibleMetadata;
use App\Values\SongStorageMetadata\S3LambdaMetadata;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class SongTest extends TestCase
{
    #[Test]
    public function retrievedLyricsPreserveTimestamps(): void
    {
        $song = Song::factory()->createOne(['lyrics' => "[00:00.00]Line 1\n[00:01.00]Line 2\n[00:02.00]Line 3"]);

        self::assertSame("[00:00.00]Line 1\n[00:01.00]Line 2\n[00:02.00]Line 3", $song->lyrics);
        self::assertSame("[00:00.00]Line 1\n[00:01.00]Line 2\n[00:02.00]Line 3", $song->getAttributes()['lyrics']);
    }

    #[Test]
    public function syncGenres(): void
    {
        $song = Song::factory()->createOne();
        $song->syncGenres('Pop, Rock');

        self::assertCount(2, $song->genres);
        self::assertEqualsCanonicalizing(['Pop', 'Rock'], $song->genres->pluck('name')->all());
    }

    /** @return array<mixed> */
    public static function provideGenreData(): array
    {
        return [
            ['Rock, Pop',    true],
            ['Pop, Rock',    true],
            ['Rock,   Pop ', true],
            ['Rock',         false],
            ['Jazz, Pop',    false],
        ];
    }

    #[Test]
    #[DataProvider('provideGenreData')]
    public function genreEqualsTo(string $target, bool $isEqual): void
    {
        $song = Song::factory()
            ->hasAttached(Genre::factory()->createOne(['name' => 'Pop']))
            ->hasAttached(Genre::factory()->createOne(['name' => 'Rock']))
            ->create()
            ->refresh();

        self::assertSame($isEqual, $song->genreEqualsTo($target));
    }

    #[Test]
    public function s3StorageMetadataHandlesNestedKeys(): void
    {
        $song = Song::factory()->createOne([
            'path' => 's3://my-bucket/path/to/nested/file.mp3',
            'storage' => SongStorageType::S3,
        ]);

        $metadata = $song->storage_metadata;

        self::assertInstanceOf(S3CompatibleMetadata::class, $metadata);
        self::assertSame('my-bucket', $metadata->bucket);
        self::assertSame('path/to/nested/file.mp3', $metadata->key);
    }

    #[Test]
    public function s3LambdaStorageMetadataHandlesNestedKeys(): void
    {
        $song = Song::factory()->createOne([
            'path' => 's3://my-bucket/path/to/nested/file.mp3',
            'storage' => SongStorageType::S3_LAMBDA,
        ]);

        $metadata = $song->
...[truncated]...

### tests/Unit/Models/AlbumTest.php
<?php

namespace Tests\Unit\Models;

use App\Models\Album;
use App\Models\Artist;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class AlbumTest extends TestCase
{
    #[Test]
    public function existingAlbumCanBeRetrievedUsingArtistAndName(): void
    {
        $artist = Artist::factory()->createOne();
        $album = Album::factory()->for($artist)->for($artist->user)->createOne();

        self::assertTrue(Album::getOrCreate($artist, $album->name)->is($album));
    }

    #[Test]
    public function newAlbumIsAutomaticallyCreatedWithUserAndArtistAndName(): void
    {
        $artist = Artist::factory()->createOne();
        $name = 'Foo';

        self::assertNull(Album::query()->whereBelongsTo($artist)->where('name', $name)->first());

        $album = Album::getOrCreate($artist, $name);
        self::assertSame('Foo', $album->name);
        self::assertTrue($album->artist->is($artist));
    }

    /** @return array<mixed> */
    public static function provideEmptyAlbumNames(): array
    {
        return [
            [''],
            ['  '],
            [null],
            [false],
        ];
    }

    #[DataProvider('provideEmptyAlbumNames')]
    #[Test]
    public function newAlbumWithoutNameIsCreatedAsUnknownAlbum($name): void
    {
        $artist = Artist::factory()->createOne();

        $album = Album::getOrCreate($artist, $name);

        self::assertSame('Unknown Album', $album->name);
    }
}

### tests/Unit/Models/ArtistTest.php
<?php

namespace Tests\Unit\Models;

use App\Models\Artist;
use Illuminate\Support\Facades\File;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_user;
use function Tests\test_path;

class ArtistTest extends TestCase
{
    #[Test]
    public function existingArtistCanBeRetrievedUsingName(): void
    {
        $artist = Artist::factory()->createOne(['name' => 'Foo']);

        self::assertTrue(Artist::getOrCreate($artist->user, 'Foo')->is($artist));
    }

    #[Test]
    public function newArtistIsCreatedWithName(): void
    {
        self::assertNull(Artist::query()->where('name', 'Foo')->first());
        self::assertSame('Foo', Artist::getOrCreate(create_user(), 'Foo')->name);
    }

    /** @return array<mixed> */
    public static function provideEmptyNames(): array
    {
        return [
            [''],
            ['  '],
            [null],
            [false],
        ];
    }

    #[DataProvider('provideEmptyNames')]
    #[Test]
    public function gettingArtistWithEmptyNameReturnsUnknownArtist($name): void
    {
        self::assertTrue(Artist::getOrCreate(create_user(), $name)->is_unknown);
    }

    #[Test]
    public function artistsWithNameInUtf16EncodingAreRetrievedCorrectly(): void
    {
        $name = File::get(test_path('fixtures/utf16'));
        $artist = Artist::getOrCreate(create_user(), $name);

        self::assertTrue(Artist::getOrCreate($artist->user, $name)->is($artist));
    }

    #[Test]
    public function nameAccessorIsNullSafe(): void
    {
        // Scout's database engine calls toSearchableArray() on a fresh model instance
        // to introspect searchable columns; that read of $this->name hits the accessor
        // with a null value.
        self::assertSame(Artist::UNKNOWN_NAME, (new Artist())->name);
    }
}

### tests/Unit/Models/SettingTest.php
<?php

namespace Tests\Unit\Models;

use App\Models\Setting;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class SettingTest extends TestCase
{
    #[Test]
    public function setKeyValuePair(): void
    {
        Setting::set('foo', 'bar');

        $this->assertDatabaseHas(Setting::class, [
            'key' => 'foo',
            'value' => json_encode('bar'),
        ]);
    }

    #[Test]
    public function supportAssociativeArray(): void
    {
        $settings = [
            'foo' => 'bar',
            'baz' => 'qux',
        ];

        Setting::set($settings);

        $this->assertDatabaseHas(Setting::class, [
            'key' => 'foo',
            'value' => json_encode('bar'),
        ])->assertDatabaseHas(Setting::class, [
            'key' => 'baz',
            'value' => json_encode('qux'),
        ]);
    }

    #[Test]
    public function updateSettings(): void
    {
        Setting::set('foo', 'bar');
        Setting::set('foo', 'baz');

        self::assertSame('baz', Setting::get('foo'));
    }

    #[Test]
    public function getSettings(): void
    {
        Setting::factory()->createOne([
            'key' => 'foo',
            'value' => 'bar',
        ]);

        self::assertSame('bar', Setting::get('foo'));
    }
}

### tests/fixtures/wikidata/entity.json
{
  "entities": {
    "Q461269": {
      "pageid": 435092,
      "ns": 0,
      "title": "Q461269",
      "lastrevid": 2347365745,
      "modified": "2025-05-11T10:03:09Z",
      "type": "item",
      "id": "Q461269",
      "labels": "****OBJECT REDACTED****",
      "descriptions": "****OBJECT REDACTED****",
      "aliases": "****OBJECT REDACTED****",
      "claims": "****OBJECT REDACTED****",
      "sitelinks": {
        "dewiki": {
          "site": "dewiki",
          "title": "Skid Row",
          "badges": [],
          "url": "https://de.wikipedia.org/wiki/Skid_Row"
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Skid Row (American band)",
          "badges": [],
          "url": "https://en.wikipedia.org/wiki/Skid_Row_(American_band)"
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Skid Row",
          "badges": [],
          "url": "https://es.wikipedia.org/wiki/Skid_Row"
        },
        "simplewiki": {
          "site": "simplewiki",
          "title": "Skid Row (American band)",
          "badges": [],
          "url": "https://simple.wikipedia.org/wiki/Skid_Row_(American_band)"
        },
        "ukwiki": {
          "site": "ukwiki",
          "title": "Skid Row (хеві-метал-гурт)",
          "badges": [],
          "url": "https://uk.wikipedia.org/wiki/Skid_Row_(%D1%85%D0%B5%D0%B2%D1%96-%D0%BC%D0%B5%D1%82%D0%B0%D0%BB-%D0%B3%D1%83%D1%80%D1%82)"
        }
      }
    }
  }
}

### tests/Unit/Services/DotenvEditorTest.php
<?php

namespace Tests\Unit\Services;

use App\Services\DotenvEditor;
use Illuminate\Filesystem\Filesystem;
use LogicException;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class DotenvEditorTest extends TestCase
{
    private string $envPath;
    private DotenvEditor $editor;

    public function setUp(): void
    {
        parent::setUp();

        $this->envPath = tempnam(sys_get_temp_dir(), 'dotenv_test_');
        file_put_contents($this->envPath, "APP_NAME=Koel\nDB_HOST=localhost\n");

        $this->editor = new DotenvEditor($this->envPath, new Filesystem());
    }

    public function tearDown(): void
    {
        if (file_exists($this->envPath)) {
            unlink($this->envPath);
        }

        parent::tearDown();
    }

    #[Test]
    public function setKeyOverwritesExistingValue(): void
    {
        $this->editor->setKey('APP_NAME', 'NewName');

        self::assertStringContainsString('APP_NAME=NewName', file_get_contents($this->envPath));
    }

    #[Test]
    public function setKeyAppendsWhenKeyDoesNotExist(): void
    {
        $this->editor->setKey('NEW_KEY', 'NewValue');

        self::assertStringContainsString('NEW_KEY=NewValue', file_get_contents($this->envPath));
    }

    #[Test]
    public function setKeysWritesMultipleVariables(): void
    {
        $this->editor->setKeys([
            'DB_HOST' => '127.0.0.1',
            'DB_PORT' => '5432',
        ]);

        $contents = file_get_contents($this->envPath);
        self::assertStringCon
...[truncated]...