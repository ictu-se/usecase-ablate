# Deterministic random code snippets
### app/Services/Scanners/IndividualFileHandler.php
<?php

namespace App\Services\Scanners;

use App\Repositories\SongRepository;
use App\Services\SongService;
use App\Values\Scanning\ScanConfiguration;
use App\Values\Scanning\ScanResult;
use Illuminate\Support\Facades\File;
use Throwable;

class IndividualFileHandler
{
    public function __construct(
        private readonly SongService $songService,
        private readonly SongRepository $songRepository,
        private readonly FileScanner $fileScanner,
    ) {}

    public function handle(string $path, ScanConfiguration $config): ScanResult
    {
        try {
            $song = $this->songRepository->findOneByPath($path);

            if (!$config->force && $song && !$song->isFileModified(File::lastModified($path))) {
                return ScanResult::skipped($path);
            }

            $info = $this->fileScanner->scan($path);
            $this->songService->createOrUpdateSongFromScan($info, $config, $song);

            return ScanResult::success($info->path);
        } catch (Throwable $e) {
            return ScanResult::error($path, $e->getMessage());
        }
    }
}

### tests/Feature/KoelPlus/SongVisibilityTest.php
<?php

namespace Tests\Feature\KoelPlus;

use App\Models\Song;
use PHPUnit\Framework\Attributes\Test;
use Tests\PlusTestCase;

use function Tests\create_user;

class SongVisibilityTest extends PlusTestCase
{
    #[Test]
    public function makingSongPublic(): void
    {
        $currentUser = create_user();
        $anotherUser = create_user();

        $externalSongs = Song::factory()->for($anotherUser, 'owner')->private()->createMany(2);

        // We can't make public songs that are not ours.
        $this->putAs('api/songs/publicize', ['songs' => $externalSongs->modelKeys()], $currentUser)->assertForbidden();

        // But we can our own songs.
        $ownSongs = Song::factory()->for($currentUser, 'owner')->createMany(2);

        $this->putAs('api/songs/publicize', ['songs' => $ownSongs->modelKeys()], $currentUser)->assertSuccessful();

        $ownSongs->each(static fn (Song $song) => self::assertTrue($song->refresh()->is_public));
    }

    #[Test]
    public function makingSongPrivate(): void
    {
        $currentUser = create_user();
        $anotherUser = create_user();

        $externalSongs = Song::factory()->for($anotherUser, 'owner')->public()->createMany(2);

        // We can't Mark as Private songs that are not ours.
        $this->putAs('api/songs/privatize', ['songs' => $externalSongs->modelKeys()], $currentUser)->assertForbidden();

        // But we can our own songs.
        $ownSongs = Song::factory()->for($currentUser, 'owner')->createMany(2);

        $this->putAs('api/songs/privatize', ['songs' => $ownSongs->modelKeys()], $currentUser)->assertSuccessful();

        $ownSongs->each(static fn (Song $song) => self::assertFalse($song->refresh()->is_public));
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
        self::assertStringContainsString('DB_HOST="127.0.0.1"', $contents);
        self::assertStringContainsString('DB_PORT=5432', $contents);
    }

    #[Test]
    public function backupRestoreRoundTripsTheFile(): void
    {
        $original = file_get_contents($this->envPath);

        $this->editor
            ->backup()
            ->setKeys([
                'APP_NAME' => 'Mutated',
                'DB_HOST' => 'mutated',
            ]);

        self::assertNotSame($original, file_get_contents($this->envPath));

        $this->editor->restore();

        self::assertSame($original, file_get_contents($this->envPath));
    }

    #[Test]
    public function restoreThrowsWhenNoBackupCaptured(): void
    {
        $this->expectException(LogicException::class);

        $this->editor->restore();
    }

    #[Test]
    public function restoreClearsTheBackupSoItCannotBeReused(): void
    {
        $this->editor->backup()->restore();

        $this->expectException(LogicException::class);

        $this->editor->restore();
    }

    #[Test]
    public function setKeyReturnsSelfForChaining(): voi
...[truncated]...

### tests/Feature/KoelPlus/UserTest.php
<?php

namespace Tests\Feature\KoelPlus;

use PHPUnit\Framework\Attributes\Test;
use Tests\PlusTestCase;

use function Tests\create_admin;

class UserTest extends PlusTestCase
{
    #[Test]
    public function creatingManagersIsOk(): void
    {
        $this->postAs(
            'api/users',
            [
                'name' => 'Manager',
                'email' => 'foo@bar.com',
                'password' => 'secret',
                'role' => 'manager',
            ],
            create_admin(),
        )->assertSuccessful();
    }

    #[Test]
    public function updatingUsersToManagersIsOk(): void
    {
        $user = create_admin();

        $this->putAs(
            "api/users/{$user->public_id}",
            [
                'name' => 'Manager',
                'email' => 'foo@bar.com',
                'role' => 'manager',
            ],
            create_admin(),
        )->assertSuccessful();
    }
}

### tests/Feature/RadioStationTest.php
<?php

namespace Tests\Feature;

use App\Helpers\Ulid;
use App\Http\Resources\RadioStationResource;
use App\Models\Organization;
use App\Models\RadioStation;
use Illuminate\Support\Facades\Http;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_admin;
use function Tests\create_user;
use function Tests\minimal_base64_encoded_image;

class RadioStationTest extends TestCase
{
    public function setUp(): void
    {
        parent::setUp();

        Http::fake(['*' => Http::response('', 200, ['Content-Type' => 'audio/mpeg'])]);
    }

    #[Test]
    public function create(): void
    {
        $user = create_user();

        $ulid = Ulid::freeze();

        $this
            ->postAs(
                '/api/radio/stations',
                [
                    'url' => 'https://example.com/stream',
                    'name' => 'Test Radio Station',
                    'logo' => minimal_base64_encoded_image(),
                    'description' => 'A test radio station',
                    'is_public' => true,
                ],
                $user,
            )
            ->assertCreated()
            ->assertJsonStructure(RadioStationResource::JSON_STRUCTURE);

        $this->assertDatabaseHas(RadioStation::class, [
            'url' => 'https://example.com/stream',
            'name' => 'Test Radio Station',
            'logo' => "$ulid.webp",
            'description' => 'A test radio station',
            'is_public' => true,
            'user_id' => $user->id,
        ]);
    }

    #[Test]
    public function updateKeepingLogoIntact(): void
    {
        $station = RadioStation::factory()->createOne([
            'logo' => 'neat-logo.webp',
        ]);

        $this
            ->putAs(
                "/api/radio/stations/{$station->id}",
                [
                    'url' => 'https://example.com/updated-stream',
                    'name' => 'Updated Radio Station',
                    'description' => 'An updated test radio station',
                    'is_public' => false,
                ],
                $station->user,
            )
            ->assertOk()
            ->assertJsonStructure(RadioStationResource::JSON_STRUCTURE);

        $station->refresh();

        self::assertEquals('neat-logo.webp', $station->logo);
        self::assertEquals('https://example.com/updated-stream', $station->url);
        self::assertEquals('Updated Radio Station', $station->name);
        self::assertEquals('An updated test radio station', $station->description);
        self::assertFalse($station->is_publ
...[truncated]...

### app/Http/Requests/API/PlaylistFolder/PlaylistFolderPlaylistDestroyRequest.php
<?php

namespace App\Http\Requests\API\PlaylistFolder;

use App\Http\Requests\API\Request;
use App\Models\Playlist;
use App\Rules\AllPlaylistsAreAccessibleBy;
use Illuminate\Validation\Rule;

/**
 * @property-read array<int>|int $playlists
 */
class PlaylistFolderPlaylistDestroyRequest extends Request
{
    /** @inheritdoc */
    public function rules(): array
    {
        return [
            'playlists' => [
                'required',
                'array',
                new AllPlaylistsAreAccessibleBy($this->user()),
                Rule::exists(Playlist::class, 'id'),
            ],
        ];
    }
}

### app/Http/Controllers/API/LikeMultipleSongsController.php
<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Http\Requests\API\InteractWithMultipleSongsRequest;
use App\Models\Song;
use App\Models\User;
use App\Services\FavoriteService;
use Illuminate\Contracts\Auth\Authenticatable;
use Illuminate\Support\Collection;

class LikeMultipleSongsController extends Controller
{
    /** @param User $user */
    public function __invoke(
        InteractWithMultipleSongsRequest $request,
        FavoriteService $favoriteService,
        Authenticatable $user,
    ) {
        /** @var Collection<int, Song> $songs */
        $songs = Song::query()->findMany($request->songs);
        $songs->each(fn (Song $song) => $this->authorize('access', $song));

        $favoriteService->batchFavorite($songs, $user); // @phpstan-ignore-line

        return response()->noContent();
    }
}

### app/Values/User/Preferences/AlbumsSortFieldPreference.php
<?php

namespace App\Values\User\Preferences;

use Webmozart\Assert\Assert;

class AlbumsSortFieldPreference extends Preference
{
    public function getDefaultValue(): string
    {
        return 'name';
    }

    public function assert(): void
    {
        Assert::oneOf($this->value, ['name', 'artist_name', 'year', 'created_at']);
    }
}

### app/Helpers/TestableIdentifier.php
<?php

namespace App\Helpers;

abstract class TestableIdentifier
{
    protected static ?string $frozenValue = null;

    abstract protected static function newIdentifier(): string;

    public static function generate(): string
    {
        return static::$frozenValue ?: static::newIdentifier();
    }

    /**
     * Freeze the identifier value for testing purposes.
     *
     * @param ?string $value A value to freeze, or null to generate a new one.
     */
    public static function freeze(?string $value = null): string
    {
        static::$frozenValue = $value ?? static::newIdentifier();

        return static::$frozenValue;
    }

    public static function unfreeze(): void
    {
        static::$frozenValue = null;
    }
}

### tests/Unit/Helpers/QueryStringParserTest.php
<?php

namespace Tests\Unit\Helpers;

use App\Helpers\QueryStringParser;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

class QueryStringParserTest extends TestCase
{
    #[Test]
    public function preservesDuplicateKeys(): void
    {
        self::assertSame(['songId' => ['a', 'b', 'c']], QueryStringParser::parse('songId=a&songId=b&songId=c'));
    }

    #[Test]
    public function singleValueKeyStillBecomesList(): void
    {
        self::assertSame(['name' => ['Mix']], QueryStringParser::parse('name=Mix'));
    }

    #[Test]
    public function urlDecodesKeysAndValues(): void
    {
        self::assertSame(['my key' => ['hello world']], QueryStringParser::parse('my%20key=hello%20world'));
    }

    #[Test]
    public function skipsBracketSuffixedKeys(): void
    {
        self::assertSame(['plain' => ['x']], QueryStringParser::parse('plain=x&things%5B%5D=a&things%5B%5D=b'));
    }

    #[Test]
    public function skipsPairsWithoutEquals(): void
    {
        self::assertSame(['ok' => ['1']], QueryStringParser::parse('flag&ok=1'));
    }

    #[Test]
    public function emptyStringReturnsEmptyArray(): void
    {
        self::assertSame([], QueryStringParser::parse(''));
    }
}

### tests/Feature/Commands/CleanUpDuplicateUploadsCommandTest.php
<?php

namespace Tests\Feature\Commands;

use App\Models\DuplicateUpload;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_user;

class CleanUpDuplicateUploadsCommandTest extends TestCase
{
    #[Test]
    public function removesStaleEntries(): void
    {
        $user = create_user();

        DuplicateUpload::factory()->for($user)->createOne([
            'created_at' => now()->subDays(10),
        ]);
        DuplicateUpload::factory()->for($user)->createOne([
            'created_at' => now()->subDays(8),
        ]);
        $recent = DuplicateUpload::factory()->for($user)->createOne([
            'created_at' => now()->subDays(3),
        ]);

        $this
            ->artisan('koel:clean-up-duplicate-uploads')
            ->expectsOutputToContain('2 stale duplicate upload(s) removed')
            ->assertSuccessful();

        self::assertSame(1, DuplicateUpload::query()->count());
        $this->assertDatabaseHas('duplicate_uploads', ['id' => $recent->id]);
    }

    #[Test]
    public function reportsNothingWhenNoStaleEntries(): void
    {
        $user = create_user();

        DuplicateUpload::factory()->for($user)->createOne([
            'created_at' => now()->subDays(2),
        ]);

        $this
            ->artisan('koel:clean-up-duplicate-uploads')
            ->expectsOutputToContain('No stale duplicate uploads found')
            ->assertSuccessful();

        self::assertSame(1, DuplicateUpload::query()->count());
    }

    #[Test]
    public function respectsCustomDaysOption(): void
    {
        $user = create_user();

        DuplicateUpload::factory()->for($user)->createOne([
            'created_at' => now()->subDays(4),
        ]);
        DuplicateUpload::factory()->for($user)->createOne([
            'created_at' => now()->subDays(2),
        ]);

        $this
            ->artisan('koel:clean-up-duplicate-uploads --days=3')
            ->expectsOutputToContain('1 stale duplicate upload(s) removed')
            ->assertSuccessful();

        self::assertSame(1, DuplicateUpload::query()->count());
    }

    #[Test]
    public function rejectsInvalidDaysOption(): void
    {
        $this
            ->artisan('koel:clean-up-duplicate-uploads --days=0')
            ->expectsOutputToContain('must be a positive integer')
            ->assertFailed();

        $this
            ->artisan('koel:clean-up-duplicate-uploads --days=abc')
            ->expectsOutputToContain('must be a positive integer')
            ->assertFailed();
    }
}

### app/Services/Playlist/PlaylistCollaborationService.php
<?php

namespace App\Services\Playlist;

use App\Events\NewPlaylistCollaboratorJoined;
use App\Exceptions\CannotRemoveOwnerFromPlaylistException;
use App\Exceptions\NotAPlaylistCollaboratorException;
use App\Exceptions\OperationNotApplicableForSmartPlaylistException;
use App\Exceptions\PlaylistCollaborationTokenExpiredException;
use App\Models\Playlist;
use App\Models\PlaylistCollaborationToken;
use App\Models\User;
use App\Values\Playlist\PlaylistCollaborator;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\DB;
use SensitiveParameter;

class PlaylistCollaborationService
{
    public function createToken(Playlist $playlist): PlaylistCollaborationToken
    {
        throw_if($playlist->is_smart, OperationNotApplicableForSmartPlaylistException::class);

        return $playlist->collaborationTokens()->create();
    }

    public function acceptUsingToken(#[SensitiveParameter] string $token, User $user): Playlist
    {
        /** @var PlaylistCollaborationToken $collaborationToken */
        $collaborationToken = PlaylistCollaborationToken::query()->where('token', $token)->firstOrFail();

        throw_if($collaborationToken->expired, PlaylistCollaborationTokenExpiredException::class);

        if ($collaborationToken->playlist->ownedBy($user)) {
            return $collaborationToken->playlist;
        }

        $collaborationToken->playlist->addCollaborator($user);

        // Now that we have at least one external collaborator, the songs in the playlist should be made public.
        // Here we dispatch an event for that to happen.
        event(new NewPlaylistCollaboratorJoined($user, $collaborationToken));

        return $collaborationToken->playlist;
    }

    /** @return Collection<array-key, PlaylistCollaborator> */
    public function getCollaborators(Playlist $playlist, bool $includingOwner = false): Collection
    {
        $collaborators = $includingOwner ? $playlist->users : $playlist->collaborators;

        return $collaborators->map(PlaylistCollaborator::fromUser(...));
    }

    public function removeCollaborator(Playlist $playlist, User $user): void
    {
        throw_if($playlist->ownedBy($user), CannotRemoveOwnerFromPlaylistException::class);
        throw_if(!$playlist->hasCollaborator($user), NotAPlaylistCollaboratorException::class);

        DB::transaction(static function () use ($playlist, $user): void {
            $playlist->collaborators()->detach($user);
            $playlist->playables()->wherePivot('user_id', $user->id)->detach();
        });
    }
}

### config/scout.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Search Engine
    |--------------------------------------------------------------------------
    |
    | This option controls the default search connection that gets used while
    | using Laravel Scout. This connection is used when syncing all models
    | to the search service. You should adjust this based on your needs.
    |
    | Supported: "algolia", "null"
    |
    */

    'driver' => env('SCOUT_DRIVER', 'tntsearch'),

    /*
    |--------------------------------------------------------------------------
    | Index Prefix
    |--------------------------------------------------------------------------
    |
    | Here you may specify a prefix that will be applied to all search index
    | names used by Scout. This prefix may be useful if you have multiple
    | "tenants" or applications sharing the same search infrastructure.
    |
    */

    'prefix' => env('SCOUT_PREFIX', ''),

    /*
    |--------------------------------------------------------------------------
    | Queue Data Syncing
    |--------------------------------------------------------------------------
    |
    | This option allows you to control if the operations that sync your data
    | with your search engines are queued. When this is set to "true" then
    | all automatic data syncing will get queued for better performance.
    |
    */

    'queue' => env('SCOUT_QUEUE', false),

    /*
    |--------------------------------------------------------------------------
    | Chunk Sizes
    |--------------------------------------------------------------------------
    |
    | These options allow you to control the maximum chunk size when you are
    | mass importing data into the search engine. This allows you to fine
    | tune each of these chunk sizes based on the power of the servers.
    |
    */

    'chunk' => [
        'searchable' => 500,
        'unsearchable' => 500,
    ],

    /*
    |--------------------------------------------------------------------------
    | Soft Deletes
    |--------------------------------------------------------------------------
    |
    | This option allows to control whether to keep soft deleted records in
    | the search indexes. Maintaining soft deleted records can be useful
    | if your application still needs to search for the records later.
    |
    */

    'soft_delete' => false,

    /*
    |--------------------------------------------------------------------------
    | Identify User
    |------------------
...[truncated]...

### app/Values/User/Preferences/IncludePublicMediaPreference.php
<?php

namespace App\Values\User\Preferences;

class IncludePublicMediaPreference extends BooleanPreference
{
    public function getDefaultValue(): true
    {
        return true;
    }
}

### app/Console/Commands/DoctorCommand.php
<?php

namespace App\Console\Commands;

use App\Enums\DoctorResult;
use App\Enums\SongStorageType;
use App\Facades\License;
use App\Helpers\Ulid;
use App\Http\Integrations\Lastfm\LastfmConnector;
use App\Http\Integrations\Lastfm\Requests\GetArtistInfoRequest;
use App\Http\Integrations\Spotify\SpotifyClient;
use App\Http\Integrations\YouTube\Requests\SearchVideosRequest;
use App\Http\Integrations\YouTube\YouTubeConnector;
use App\Models\Setting;
use App\Models\Song;
use App\Models\User;
use App\Services\Image\ImageWriter;
use App\Services\Integrations\LastfmService;
use App\Services\Integrations\SpotifyService;
use App\Services\Integrations\YouTubeService;
use App\Services\SongStorages\SongStorage;
use Closure;
use Exception;
use Illuminate\Console\Command;
use Illuminate\Mail\Message;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Mail;
use InvalidArgumentException;
use Throwable;
use TiBeN\CrontabManager\CrontabAdapter;
use TiBeN\CrontabManager\CrontabRepository;

// @mago-ignore lint:too-many-methods,cyclomatic-complexity,kan-defect
class DoctorCommand extends Command
{
    protected $signature = 'koel:doctor';
    protected $description = 'Check Koel setup';

    private array $errors = [];

    public function handle(): int
    {
        if (PHP_OS_FAMILY === 'Windows' || PHP_OS_FAMILY === 'Unknown') {
            $this->components->error('This command is only available on Linux systems.');

            return self::FAILURE;
        }

        $this->components->alert('Checking Koel setup...');
        $this->line('');

        if (exec('whoami') === 'root') {
            $this->components->error('This command cannot be run as root.');

            return self::FAILURE;
        }

        $this->checkDirectoryPermissions();

        if ($this->checkDatabaseConnection() === DoctorResult::SUCCESS) {
            $this->checkMediaStorage();
        } else {
            $this->reportWarning('Storage type.', 'UNKNOWN');
        }

        $this->checkFullTextSearch();
        $this->checkApiHealth();
        $this->checkFFMpeg();
        $this->checkImageWriting();
        $this->checkPhpExtensions();
        $this->checkPhpConfiguration();
        $this->checkStreamingMethod();
        $this->checkServiceIntegrations();
        $this->checkMailConfiguration();
        $this->checkScheduler();
        $this->checkPlusLicense();

        if ($this->errors) {
            $this->reportErroneousResult();
        } else {
         
...[truncated]...

### routes/api.base.php
<?php

use App\Facades\YouTube;
use App\Helpers\Uuid;
use App\Http\Controllers\API\ActivateLicenseController;
use App\Http\Controllers\API\AiController;
use App\Http\Controllers\API\AlbumController;
use App\Http\Controllers\API\AlbumSongController;
use App\Http\Controllers\API\Artist\ArtistAlbumController;
use App\Http\Controllers\API\Artist\ArtistController;
use App\Http\Controllers\API\Artist\ArtistSongController;
use App\Http\Controllers\API\Artist\FetchArtistEventsController;
use App\Http\Controllers\API\Artist\FetchArtistInformationController;
use App\Http\Controllers\API\AuthController;
use App\Http\Controllers\API\DisconnectFromLastfmController;
use App\Http\Controllers\API\Embed\EmbedController;
use App\Http\Controllers\API\Embed\EmbedOptionsController;
use App\Http\Controllers\API\EqualizerPresetController;
use App\Http\Controllers\API\ExcerptSearchController;
use App\Http\Controllers\API\FavoriteController;
use App\Http\Controllers\API\FetchAlbumInformationController;
use App\Http\Controllers\API\FetchAlbumThumbnailController;
use App\Http\Controllers\API\FetchDemoCreditsController;
use App\Http\Controllers\API\FetchFavoriteSongsController;
use App\Http\Controllers\API\FetchInitialDataController;
use App\Http\Controllers\API\FetchOverviewController;
use App\Http\Controllers\API\FetchRecentlyPlayedSongController;
use App\Http\Controllers\API\FetchSongsByIdsController;
use App\Http\Controllers\API\FetchSongsForQueueController;
use App\Http\Controllers\API\FetchSongsToQueueByGenreController;
use App\Http\Controllers\API\ForgotPasswordController;
use App\Http\Controllers\API\GenreController;
use App\Http\Controllers\API\GetOneTimeTokenController;
use App\Http\Controllers\API\LambdaSongController as S3SongController;
use App\Http\Controllers\API\LikeMultipleSongsController;
use App\Http\Controllers\API\MediaBrowser\FetchFolderSongsController;
use App\Http\Controllers\API\MediaBrowser\FetchRecursiveFolderSongsController;
use App\Http\Controllers\API\MediaBrowser\FetchSubfoldersController;
use App\Http\Controllers\API\MediaBrowser\PaginateFolderSongsController;
use App\Http\Controllers\API\MoveFavoriteSongsController;
use App\Http\Controllers\API\MovePlaylistSongsController;
use App\Http\Controllers\API\PaginateSongsByGenreController;
use App\Http\Controllers\API\PlaylistCollaboration\AcceptPlaylistCollaborationInviteController;
use App\Http\Controllers\API\PlaylistCollaboration\CreatePlaylistCollaborationTokenController;
use App\Http\Controllers\API\PlaylistCollaboration\PlaylistCollaboratorController;
use App\Http\Controllers\API\PlaylistController;
...[truncated]...

### app/Http/Controllers/Subsonic/GetMusicFoldersController.php
<?php

namespace App\Http\Controllers\Subsonic;

use App\Http\Controllers\Controller;
use App\Http\Responses\Subsonic\SubsonicResponse;

class GetMusicFoldersController extends Controller
{
    public function __invoke()
    {
        return SubsonicResponse::ok([
            'musicFolders' => [
                'musicFolder' => [
                    ['id' => 1, 'name' => 'Music'],
                ],
            ],
        ]);
    }
}

### app/Http/Controllers/Subsonic/CreatePlaylistController.php
<?php

namespace App\Http\Controllers\Subsonic;

use App\Http\Controllers\Controller;
use App\Http\Requests\Subsonic\CreatePlaylistRequest;
use App\Http\Responses\Subsonic\Resources\PlaylistResource;
use App\Http\Responses\Subsonic\Resources\SongResource;
use App\Http\Responses\Subsonic\SubsonicResponse;
use App\Models\User;
use App\Services\Playlist\PlaylistService;
use App\Values\Playlist\PlaylistCreateData;
use Illuminate\Contracts\Auth\Authenticatable;

class CreatePlaylistController extends Controller
{
    public function __construct(
        private readonly PlaylistService $playlistService,
    ) {}

    /** @param User $user */
    public function __invoke(CreatePlaylistRequest $request, Authenticatable $user)
    {
        $playlist = $this->playlistService->createPlaylist(
            PlaylistCreateData::make(name: $request->name, playableIds: $request->songId),
            $user,
        );

        $playlist->loadCount('playables')->loadSum('playables', 'length');

        return SubsonicResponse::ok([
            'playlist' => PlaylistResource::toArray($playlist)
                + [
                    'entry' => $playlist->playables->map(SongResource::toArray(...))->all(),
                ],
        ]);
    }
}

### routes/channels.php
<?php

use App\Models\User;
use Illuminate\Support\Facades\Broadcast;

Broadcast::channel('user.{publicId}', static function (User $user, $publicId): bool {
    return $user->is(User::query()->where('public_id', $publicId)->firstOrFail());
});

### app/Ai/Tools/PlayLeastPlayed.php
<?php

namespace App\Ai\Tools;

use App\Ai\AiRequestContext;
use App\Ai\Services\PlaybackService;
use App\Enums\PlayableType;
use App\Repositories\SongRepository;
use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Contracts\Tool;
use Laravel\Ai\Tools\Request;
use Stringable;

class PlayLeastPlayed implements Tool
{
    public function __construct(
        private readonly AiRequestContext $context,
        private readonly SongRepository $songRepository,
        private readonly PlaybackService $playbackService,
    ) {}

    public function description(): Stringable|string
    {
        return (
            'Play songs the user has rarely or never listened to. '
            . 'Use this when the user wants to rediscover songs, listen to something they haven\'t heard, '
            . 'or play their least played tracks.'
        );
    }

    public function schema(JsonSchema $schema): array
    {
        return [
            ...PlaybackService::limitSchema($schema, 'Number of songs to play. Default 50'),
            ...PlaybackService::queueSchema($schema),
        ];
    }

    public function handle(Request $request): Stringable|string
    {
        $songs = $this->songRepository->getLeastPlayed(
            PlaybackService::extractLimit($request),
            $this->context->user,
            type: PlayableType::SONG,
        );

        if ($songs->isEmpty()) {
            return 'No songs found in the library.';
        }

        $queue = $this->playbackService->queueSongs($songs, $request);
        $verb = $queue ? 'Added' : 'Playing';
        $suffix = $queue ? ' to the queue' : '';

        return "{$verb} {$songs->count()} rarely or never played song(s){$suffix}.";
    }
}

### app/Rules/SafeUrl.php
<?php

namespace App\Rules;

use App\Helpers\Network;
use Closure;
use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Uri;
use Illuminate\Translation\PotentiallyTranslatedString;
use Throwable;

/**
 * Validates that a URL does not resolve to a private or reserved IP address,
 * preventing SSRF attacks against internal services.
 * Also follows redirects and validates the effective URL.
 */
class SafeUrl implements ValidationRule
{
    private const array ALLOWED_SCHEMES = ['http', 'https'];

    public function __construct(
        private ?Network $network = null,
    ) {
        $this->network ??= app(Network::class);
    }

    /** @param Closure(string, ?string=): PotentiallyTranslatedString $fail */
    public function validate(string $attribute, mixed $value, Closure $fail): void
    {
        try {
            $uri = Uri::of((string) $value);
        } catch (Throwable) {
            $fail('The :attribute is not a valid URL.');

            return;
        }

        if (!in_array($uri->scheme(), self::ALLOWED_SCHEMES, true)) {
            $fail('The :attribute must use HTTP or HTTPS.');

            return;
        }

        if (!$this->network->isPublicHost($uri->host())) {
            $fail('The :attribute must point to a public URL.');

            return;
        }

        try {
            $response = Http::head((string) $value);
        } catch (Throwable) {
            // Some streaming servers don't support HEAD — try GET
            try {
                $response = Http::withOptions(['stream' => true])->get((string) $value);
            } catch (Throwable) {
                $fail("The $attribute couldn't be reached.");

                return;
            }
        }

        $effectiveHost = $response->effectiveUri()?->getHost();

        if ($effectiveHost && !$this->network->isPublicHost($effectiveHost)) {
            $fail('The :attribute must point to a public URL.');
        }
    }
}

### app/Ai/Tools/PlayMostPlayedAlbum.php
<?php

namespace App\Ai\Tools;

use App\Ai\AiRequestContext;
use App\Ai\Services\PlaybackService;
use App\Repositories\AlbumRepository;
use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Contracts\Tool;
use Laravel\Ai\Tools\Request;
use Stringable;

class PlayMostPlayedAlbum implements Tool
{
    public function __construct(
        private readonly AiRequestContext $context,
        private readonly AlbumRepository $albumRepository,
        private readonly PlaybackService $playbackService,
    ) {}

    public function description(): Stringable|string
    {
        return (
            'Play the user\'s most played (top) album. '
            . 'Use this when the user wants to listen to their favorite or most listened-to album.'
        );
    }

    public function schema(JsonSchema $schema): array
    {
        return PlaybackService::queueSchema($schema);
    }

    public function handle(Request $request): Stringable|string
    {
        $albums = $this->albumRepository->getMostPlayed(1, $this->context->user);

        if ($albums->isEmpty()) {
            return 'No play history found yet.';
        }

        return $this->playbackService->playAlbum($albums->first(), $this->context->user, $request);
    }
}