# Routes/controllers
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

### tests/Feature/OverviewTest.php
<?php

namespace Tests\Feature;

use App\Http\Resources\AlbumResource;
use App\Http\Resources\ArtistResource;
use App\Http\Resources\SongResource;
use App\Models\Artist;
use App\Models\Interaction;
use App\Models\Song;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_user;

class OverviewTest extends TestCase
{
    #[Test]
    public function index(): void
    {
        $user = create_user();
        $artist = Artist::factory()->createOne();

        // Create songs by the same artist so that similar_songs has results
        $songs = Song::factory()->for($artist)->createMany(10);

        foreach ($songs as $song) {
            Interaction::factory()->for($user)->for($song)->createOne();
        }

        $this->getAs('api/overview', $user)->assertJsonStructure([
            'most_played_songs' => [0 => SongResource::JSON_STRUCTURE],
            'recently_played_songs' => [0 => SongResource::JSON_STRUCTURE],
            'recently_added_albums' => [0 => AlbumResource::JSON_STRUCTURE],
            'recently_added_artists' => [0 => ArtistResource::JSON_STRUCTURE],
            'recently_added_songs' => [0 => SongResource::JSON_STRUCTURE],
            'most_played_artists' => [0 => ArtistResource::JSON_STRUCTURE],
            'most_played_albums' => [0 => AlbumResource::JSON_STRUCTURE],
            'least_played_songs' => [0 => SongResource::JSON_STRUCTURE],
            'random_songs' => [0 => SongResource::JSON_STRUCTURE],
            'similar_songs' => [0 => SongResource::JSON_STRUCTURE],
        ]);
    }
}

### tests/fixtures/musicbrainz/artist-rel-urls.json
{
  "gender": null,
  "name": "Skid Row",
  "relations": [
    {
      "direction": "forward",
      "begin": null,
      "attributes": [],
      "ended": false,
      "attribute-ids": {
      },
      "source-credit": "",
      "target-type": "url",
      "type-id": "08db8098-c0df-4b78-82c3-c8697b4bba7f",
      "end": null,
      "target-credit": "",
      "attribute-values": {
      },
      "type": "last.fm",
      "url": {
        "resource": "https://www.last.fm/music/Skid+Row",
        "id": "bc7e1a9a-6958-460a-a69a-441b633b3ba9"
      }
    },
    {
      "target-credit": "",
      "end": null,
      "attribute-values": {
      },
      "type": "lyrics",
      "url": {
        "resource": "http://muzikum.eu/en/122-8835/skid-row/lyrics.html",
        "id": "a15e35c6-c4d0-4177-8c37-86289be6dc3b"
      },
      "attribute-ids": {
      },
      "direction": "forward",
      "attributes": [],
      "begin": null,
      "ended": false,
      "target-type": "url",
      "type-id": "e4d73442-3762-45a8-905c-401da65544ed",
      "source-credit": ""
    },
    {
      "attribute-ids": {
      },
      "direction": "forward",
      "ended": false,
      "attributes": [],
      "begin": null,
      "target-type": "url",
      "type-id": "fe33d22f-c3b0-4d68-bd53-a856badf2b15",
      "source-credit": "",
      "target-credit": "",
      "end": null,
      "attribute-values": {
      },
      "type": "official homepage",
      "url": {
        "id": "46051885-1e7b-4223-8c2c-87a909e0f375",
        "resource": "http://www.skidrow.com/"
      }
    },
    {
      "target-credit": "",
      "end": null,
      "url": {
        "id": "3fe674a9-d3d1-4202-9fae-4f0d49e18b50",
        "resource": "https://www.facebook.com/OfficialSkidRow"
      },
      "type": "social network",
      "attribute-values": {
      },
      "attribute-ids": {
      },
      "attributes": [],
      "begin": null,
      "ended": false,
      "direction": "forward",
      "type-id": "99429741-f3f6-484b-84f8-23af51991770",
      "target-type": "url",
      "source-credit": ""
    },
    {
      "end": null,
      "target-credit": "",
      "type": "social network",
      "attribute-values": {
      },
      "url": {
        "resource": "https://www.instagram.com/officialskidrow/",
        "id": "da5bc84c-4114-4733-8539-6dedacb77466"
      },
      "direction": "forward",
      "ended": false,
      "begin": null,
      "attributes": [],
      "attribute-ids": {
      },
      "source-credit": "",
      "target-type": "url",
      "type-id": "99429741-f3f6-484b-84f8-23af51991770"
    },
    {
   
...[truncated]...

### tests/Feature/Subsonic/ShowApiKeyCommandTest.php
<?php

namespace Tests\Feature\Subsonic;

use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

use function Tests\create_user;

class ShowApiKeyCommandTest extends TestCase
{
    #[Test]
    public function printsApiKeyForExistingUser(): void
    {
        $user = create_user(['email' => 'alice@example.com']);

        $this
            ->artisan('koel:subsonic:apikey', ['email' => 'alice@example.com'])
            ->expectsOutput($user->subsonic_api_key)
            ->assertSuccessful();
    }

    #[Test]
    public function failsWhenUserNotFound(): void
    {
        $this->artisan('koel:subsonic:apikey', ['email' => 'ghost@example.com'])->assertFailed();
    }
}

### tests/fixtures/musicbrainz/release-group-rel-urls.json
{
  "primary-type": "Album",
  "disambiguation": "",
  "relations": [
    {
      "end": null,
      "ended": false,
      "begin": null,
      "type": "allmusic",
      "type-id": "a50a1d20-2b20-4d2c-9a29-eb771dd78386",
      "attributes": [],
      "attribute-values": {
      },
      "target-credit": "",
      "source-credit": "",
      "target-type": "url",
      "direction": "forward",
      "url": {
        "id": "557c80f7-7b63-42fd-97b7-1a01fadd5a2e",
        "resource": "https://www.allmusic.com/album/mw0000264528"
      },
      "attribute-ids": {
      }
    },
    {
      "attribute-ids": {
      },
      "url": {
        "id": "91ed2994-fd27-4ddf-b966-a5b83027a1d5",
        "resource": "https://www.discogs.com/master/94196"
      },
      "direction": "forward",
      "source-credit": "",
      "target-type": "url",
      "target-credit": "",
      "attribute-values": {
      },
      "attributes": [],
      "type-id": "99e550f3-5ab4-3110-b5b9-fe01d970b126",
      "type": "discogs",
      "begin": null,
      "ended": false,
      "end": null
    },
    {
      "type": "lyrics",
      "end": null,
      "ended": false,
      "begin": null,
      "attribute-values": {
      },
      "type-id": "156344d3-da8b-40c6-8b10-7b1c22727124",
      "attributes": [],
      "target-credit": "",
      "direction": "forward",
      "source-credit": "",
      "target-type": "url",
      "url": {
        "id": "ae6e9f1b-8c66-43bf-b8f5-8412cf7385f1",
        "resource": "https://genius.com/albums/Skid-row/Slave-to-the-grind"
      },
      "attribute-ids": {
      }
    },
    {
      "attribute-values": {
      },
      "attributes": [],
      "type-id": "38320e40-9f4a-3ae7-8cb2-3f3c9c5d856d",
      "type": "other databases",
      "begin": null,
      "ended": false,
      "end": null,
      "attribute-ids": {
      },
      "url": {
        "resource": "https://rateyourmusic.com/release/album/skid-row/slave-to-the-grind/",
        "id": "71dfe6ce-f3bd-41d0-92e5-7fac7b71f2c4"
      },
      "source-credit": "",
      "direction": "forward",
      "target-type": "url",
      "target-credit": ""
    },
    {
      "type-id": "38320e40-9f4a-3ae7-8cb2-3f3c9c5d856d",
      "attributes": [],
      "attribute-values": {
      },
      "ended": false,
      "begin": null,
      "end": null,
      "type": "other databases",
      "attribute-ids": {
      },
      "url": {
        "resource": "https://www.musik-sammler.de/album/15577/",
        "id": "c9de5478-147e-4853-ae1c-a9ce4a7f7dae"
      },
      "target-credit": "",
      "target-type": "url",
      "source-cr
...[truncated]...

### tests/Feature/KoelPlus/Ai/AiControllerTest.php
<?php

namespace Tests\Feature\KoelPlus\Ai;

use App\Ai\Agents\KoelAssistant;
use PHPUnit\Framework\Attributes\Test;
use Tests\PlusTestCase;

use function Tests\create_user;

class AiControllerTest extends PlusTestCase
{
    #[Test]
    public function promptsTheAgent(): void
    {
        KoelAssistant::fake(['Hello, how can I help you with your music?']);

        $user = create_user();

        $this
            ->postAs(
                'api/ai/prompt',
                [
                    'prompt' => 'Play some jazz',
                ],
                $user,
            )
            ->assertSuccessful()
            ->assertJsonStructure(['message', 'action', 'data', 'conversation_id']);

        KoelAssistant::assertPrompted(static fn ($prompt) => $prompt->contains('Play some jazz'));
    }

    #[Test]
    public function requiresAuthentication(): void
    {
        KoelAssistant::fake();

        $this->postJson('api/ai/prompt', [
            'prompt' => 'Play some jazz',
        ])->assertUnauthorized();

        KoelAssistant::assertNeverPrompted();
    }

    #[Test]
    public function validatesPromptIsRequired(): void
    {
        KoelAssistant::fake();

        $user = create_user();

        $this->postAs('api/ai/prompt', [], $user)->assertUnprocessable();

        KoelAssistant::assertNeverPrompted();
    }

    #[Test]
    public function validatesPromptMaxLength(): void
    {
        KoelAssistant::fake();

        $user = create_user();

        $this->postAs(
            'api/ai/prompt',
            [
                'prompt' => str_repeat('a', 501),
            ],
            $user,
        )->assertUnprocessable();

        KoelAssistant::assertNeverPrompted();
    }
}

### app/Http/Requests/API/UserLoginRequest.php
<?php

namespace App\Http\Requests\API;

/**
 * @property string $email
 * @property string $password
 */
class UserLoginRequest extends Request
{
    /** @inheritdoc */
    public function rules(): array
    {
        return [
            'email' => ['required', 'email'],
            'password' => 'required',
        ];
    }
}

### app/Http/Requests/API/UserStoreRequest.php
<?php

namespace App\Http\Requests\API;

use App\Enums\Acl\Role;
use App\Rules\AvailableRole;
use App\Rules\UserCanManageRole;
use App\Values\User\UserCreateData;
use Illuminate\Validation\Rule;
use Illuminate\Validation\Rules\Password;

/**
 * @property-read string $password
 * @property-read string $name
 * @property-read string $email
 */
class UserStoreRequest extends Request
{
    /** @inheritdoc */
    public function rules(): array
    {
        return [
            'name' => 'required',
            'email' => ['required', 'email', 'unique:users'],
            'password' => ['required', Password::defaults()],
            'role' => [
                'required',
                Rule::enum(Role::class),
                new AvailableRole(),
                new UserCanManageRole($this->user()),
            ],
        ];
    }

    public function toDto(): UserCreateData
    {
        return UserCreateData::make(
            name: $this->name,
            email: $this->email,
            plainTextPassword: $this->password,
            role: $this->enum('role', Role::class),
        );
    }
}

### app/Http/Controllers/API/UserController.php
<?php

namespace App\Http\Controllers\API;

use App\Exceptions\UserProspectUpdateDeniedException;
use App\Http\Controllers\Controller;
use App\Http\Requests\API\UserStoreRequest;
use App\Http\Requests\API\UserUpdateRequest;
use App\Http\Resources\UserResource;
use App\Models\User;
use App\Repositories\UserRepository;
use App\Services\UserService;
use Illuminate\Http\Response;

class UserController extends Controller
{
    public function __construct(
        private readonly UserRepository $userRepository,
        private readonly UserService $userService,
    ) {}

    public function index()
    {
        $this->authorize('manage', User::class);

        return UserResource::collection($this->userRepository->getAll());
    }

    public function store(UserStoreRequest $request)
    {
        $this->authorize('manage', User::class);

        return UserResource::make($this->userService->createUser($request->toDto()));
    }

    public function update(UserUpdateRequest $request, User $user)
    {
        $this->authorize('update', $user);

        try {
            return UserResource::make($this->userService->updateUser($user, $request->toDto()));
        } catch (UserProspectUpdateDeniedException) {
            abort(Response::HTTP_FORBIDDEN, 'Cannot update a user prospect.');
        }
    }

    public function destroy(User $user)
    {
        $this->authorize('destroy', $user);
        $this->userService->deleteUser($user);

        return response()->noContent();
    }
}

### app/Http/Requests/API/InviteUserRequest.php
<?php

namespace App\Http\Requests\API;

use App\Enums\Acl\Role;
use App\Rules\AvailableRole;
use App\Rules\UserCanManageRole;
use Illuminate\Validation\Rule;

/**
 * @property-read array<string> $emails
 */
class InviteUserRequest extends Request
{
    /**
     * @inheritdoc
     */
    public function rules(): array
    {
        return [
            'emails.*' => ['required', 'email', 'unique:users,email'],
            'role' => [
                'required',
                Rule::enum(Role::class),
                new AvailableRole(),
                new UserCanManageRole($this->user()),
            ],
        ];
    }

    /**
     * @inheritdoc
     */
    public function messages(): array
    {
        return [
            'emails.*.unique' => 'The email :input is already registered.',
        ];
    }
}

### app/Http/Requests/API/UserUpdateRequest.php
<?php

namespace App\Http\Requests\API;

use App\Enums\Acl\Role;
use App\Models\User;
use App\Rules\AvailableRole;
use App\Rules\UserCanManageRole;
use App\Values\User\UserUpdateData;
use Illuminate\Validation\Rule;
use Illuminate\Validation\Rules\Password;

/**
 * @property-read string $password
 * @property-read string $name
 * @property-read string $email
 */
class UserUpdateRequest extends Request
{
    /** @inheritdoc */
    public function rules(): array
    {
        /** @var User $target */
        $target = $this->route('user');

        return [
            'name' => 'required',
            'email' => 'required|email|unique:users,email,' . $target->id,
            'password' => ['sometimes', Password::defaults()],
            'role' => [
                'required',
                Rule::enum(Role::class),
                new AvailableRole(),
                new UserCanManageRole($this->user()),
            ],
        ];
    }

    public function toDto(): UserUpdateData
    {
        return UserUpdateData::make(
            name: $this->name,
            email: $this->email,
            plainTextPassword: $this->password,
            role: $this->enum('role', Role::class),
        );
    }
}

### resources/views/emails/users/invite.blade.php
<x-mail::message>
Hey hey,

{{ $invitee->invitedBy->name }} has invited you to join them on {{ config('app.name') }}.
Click the button below to accept the invitation.

<x-mail::button :url="$url">
    Accept Invitation
</x-mail::button>

Enjoy!
</x-mail::message>

### app/Http/Requests/API/GetUserInvitationRequest.php
<?php

namespace App\Http\Requests\API;

/**
 * @property-read string $token
 */
class GetUserInvitationRequest extends Request
{
    /**
     * @inheritdoc
     */
    public function rules(): array
    {
        return [
            'token' => ['required', 'string'],
        ];
    }
}

### app/Http/Controllers/API/UserInvitationController.php
<?php

namespace App\Http\Controllers\API;

use App\Enums\Acl\Role;
use App\Exceptions\InvitationNotFoundException;
use App\Http\Controllers\Controller;
use App\Http\Requests\API\AcceptUserInvitationRequest;
use App\Http\Requests\API\GetUserInvitationRequest;
use App\Http\Requests\API\InviteUserRequest;
use App\Http\Requests\API\RevokeUserInvitationRequest;
use App\Http\Resources\UserProspectResource;
use App\Models\User;
use App\Services\Auth\AuthenticationService;
use App\Services\UserInvitationService;
use Illuminate\Contracts\Auth\Authenticatable;
use Illuminate\Http\Response;

class UserInvitationController extends Controller
{
    public function __construct(
        private readonly UserInvitationService $invitationService,
        private readonly AuthenticationService $auth,
    ) {}

    /** @param User $invitor */
    public function invite(InviteUserRequest $request, Authenticatable $invitor)
    {
        $this->authorize('manage', $invitor);

        $invitees = $this->invitationService->invite($request->emails, $request->enum('role', Role::class), $invitor);

        return UserProspectResource::collection($invitees);
    }

    public function get(GetUserInvitationRequest $request)
    {
        try {
            return UserProspectResource::make($this->invitationService->getUserProspectByToken($request->token));
        } catch (InvitationNotFoundException) {
            abort(Response::HTTP_NOT_FOUND, 'The invitation token is invalid.');
        }
    }

    public function accept(AcceptUserInvitationRequest $request)
    {
        try {
            $user = $this->invitationService->accept($request->token, $request->name, $request->password);

            return response()->json($this->auth->login($user->email, $request->password)->toArray());
        } catch (InvitationNotFoundException) {
            abort(Response::HTTP_NOT_FOUND, 'The invitation token is invalid.');
        }
    }

    public function revoke(RevokeUserInvitationRequest $request)
    {
        $this->authorize('manage', User::class);

        try {
            $this->invitationService->revokeByEmail($request->email);

            return response()->noContent();
        } catch (InvitationNotFoundException) {
            abort(Response::HTTP_NOT_FOUND, 'The invitation token is invalid.');
        }
    }
}

### app/Http/Requests/API/AcceptUserInvitationRequest.php
<?php

namespace App\Http\Requests\API;

use Illuminate\Validation\Rules\Password;

/**
 * @property-read string $token
 * @property-read string $name
 * @property-read string $password
 */
class AcceptUserInvitationRequest extends Request
{
    /** @inheritdoc */
    public function rules(): array
    {
        return [
            'name' => 'required',
            'token' => 'required',
            'password' => ['required', Password::defaults()],
        ];
    }
}

### app/Http/Requests/API/RevokeUserInvitationRequest.php
<?php

namespace App\Http\Requests\API;

/**
 * @property-read string $email
 */
class RevokeUserInvitationRequest extends Request
{
    /** @inheritdoc */
    public function rules(): array
    {
        return ['email' => ['required', 'email']];
    }
}