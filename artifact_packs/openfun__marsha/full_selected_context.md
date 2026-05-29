# README
## README.md
# Marsha, a self-hosted open source video and document provider 🐠

[![CircleCI](https://circleci.com/gh/openfun/marsha/tree/master.svg?style=svg)](https://circleci.com/gh/openfun/marsha/tree/master)

## Overview

`Marsha` is a video management & playback service. It is intended to be operated independently: it's like having your very own YouTube for education.

Marsha also supports hosting documents and distribute them on all your courses.

Instructors & organizations can use Marsha to upload and manage their videos (and associated files, such as subtitles or transcripts) or documents directly from a course as they are creating it.

Once the course is published, learners simply see a video player or documents in the course.

This seamless integration works with any LMS ([`Open edX`](https://open.edx.org), [`Moodle`](https://moodle.org), ...) thanks to the [LTI](https://en.wikipedia.org/wiki/Learning_Tools_Interoperability) standard for interoperability.

Here is what `Marsha` offers out of the box:

Video:

- automatic transcoding of videos to all suitable formats from a single video file uploaded by the instructor;
- adaptive-bitrate streaming playback (both HLS and DASH);
- accessibility through the player itself and support for subtitles, closed captions and transcripts;

Document:

- upload any type of documents;
- prevent disk storage quota by using AWS S3;

Moreover, Marsha provides:

- access control to resources through LTI authentication;
- easy deployment & management of environments through `Terraform`;

## Architecture

`Marsha` is made up of 3 building blocks: a **container-native** `Django` backend, an `AWS` transcoding and file storage environment, and a `React` frontend application.

### The `Django` backend

The `Django` backend is tasked with serving the LTI pages that are integrated into the LMS. It also manages all the objects with their relationships, user accounts and all authentication concerns. It exposes a JSON API to communicate with the `React` frontend.

It is defined using a [docker-compose file](../docker-compose.yml) for development, and can be deployed on any container environment (such as `Kubernetes`) for production.

### The storage & transcoding environment

Source files (video, documents, subtitles,...) are directly uploaded to an `S3` bucket by instructors. Depending the uploaded resource, Celery tasks will be triggered to do different jobs:
- Transcode videos using Peertube runners to generate all necessary video files (various formats and fragments & manifests for adaptive-bitrate streaming) into a destination `S3` bucket. Those files are then served through the `Scaleway Edge service` CDN.
- Convert any kind of subtitles (also captions and transcripts) in [WebVTT](https://www.w3.org/TR/webvtt1/) format and encode them properly.
- Resize thumbnails in many formats.

### The `React` frontend

The `React` frontend is responsible for the interfaces with which users interact in the LTI Iframes. It gets an authenticated token with permissions
from the view and interacts with the `Django` backend to manage objects and directly with `AWS s3` to upload files.

It also powers the same resource view when loaded by a learner to display a video player (thanks to [videojs](https://videojs.com/)) or a document reader.

⚠️ **Iframe management**

To have the best possible user experience for instructors, we need to be able to change the size of the `<iframe>` depending on its contents. This can be done through the [iframe-resizer](https://github.com/davidjbradshaw/iframe-resizer) library.

`iframe-resizer` requires to run some JS inside the `<iframe>` (which we include with our `React` frontend bundle) and some JS inside the host page. It then communicates through message-passing to adjust the size of the `<iframe>`.

This means that to have the best interfaces for instructors, you need to include the host-side `iframe-resizer` JS in your LMS pages. For Open edX, this is already done in our [custom LTI consumer Xblock](https://github.com/openfun/xblock-configurable-lti-consumer).

If you cannot or do not want to include this host-side JS, you can still run `Marsha`. It will work exactly the same for learners (provided you adjust the size of the LTI `<iframe>` for video), and instructors will only have to scroll inside the `<iframe>` on some occasions.

## Getting started

Make sure you have a recent version of Docker and
[Docker Compose](https://docs.docker.com/compose/install) installed on your laptop:

```bash
$ docker -v
  Docker version 19.03.6, build 369ce74a3c

$ docker-compose --version
  docker-compose version 1.24.1, build 4667896b
```

⚠️ You may need to run the following commands with `sudo` but this can be avoided by assigning your user to the `docker` group.

### The storage & transcoding environment

All tasks related to this environment are run from the `./src/aws` directory. We use `Terraform` to keep this infrastructure configuration as code and easily manage several independent deployments of the whole `AWS` infrastructure.

> Note for Mac users: Marsha's AWS development setup uses `getopt`. The version that comes with macOS is not suitable for our use case. You need to install the GNU version and add it to your path so it is used by default.
>
> `brew install gnu-getopt`
>
> `echo 'export PATH="/usr/local/opt/gnu-getopt/bin:$PATH"' >> ~/.zshrc`

There are 2 Terraform projects in Marsha with two different purposes:

- `./src/aws/shared_resources`: this project manages resources common to all marsha environments on the same AWS account. These resources must not live in different workspaces so you must work in the `default` workspace. To ease the use of this project, a dedicated script is available in `./src/aws/bin/shared-resources` which uses and configures the `Terraform` docker image. You have to run a Terraform command as if you were using the terraform cli. (eg: `./bin/shared-resources plan` will execute Terraform's "plan" command).
- `./src/aws`: this is the main project we use, most of the infrastructure is managed here (in all `*.tf` files). This project must use [`Terraform` workspaces](https://www.terraform.io/docs/state/workspaces.html) and we highly recommand you to not use the default one. With multiple workspaces, you can manage multiple environments for your Marsha instance with a single AWS account. To ease the use of this project, a dedicated script is available in `./src/aws/bin/terraform` which uses and configures the `Terraform` docker image. You have to run a Terraform command as if you were using the terraform cli. (eg: `./bin/terraform plan` will execute Terraform's "plan" command).

#### Terraform state management

Terraform manages a [state](https://www.terraform.io/docs/state/index.html) of your infrastructure. By default this state is stored locally on your machine but it is highly recommanded to use a [remote backend](https://www.terraform.io/docs/state/remote.html).

You will find all you need to configure a remote backend in the Terraform documentation: https://www.terraform.io/docs/configuration/blocks/backends/index.html

⚠ You must configure your state management before running any of the commands hereafter. The first `init` will initiate your state and after that you will have to deal with state migration if you want to modify it. You can create a file `src/aws/state.tf` and `src/aws/shared-resources/state.tf` to configure a backend, there is an example in each project (`state.tf.dist` file).

🔧 **Before you go further**, you need to create `./src/aws/env.d/development` and replace the relevant values with your own. You can take a look at the [environment documentation](https://github.com/openfun/marsha/blob/master/docs/env.md#2-environment-to-deploy-marsha-to-aws) for more details on this topic. You should use this command to create the file from the existing model:

    $ cp ./src/aws/env.d/development.dist ./src/aws/env.d/development

Initialize your `Terraform` config:

    $ cd src/aws
    $ make init

The `make init` command will also create an [ECR](https://aws.amazon.com/ecr/) repository. Before going further you have to build and publish the lambda docker image. Unfortunately AWS doesn't allow to use a public image, so you have to host this one on a private ECR instance. Copy the output of the `init` command, you will use them in the next step.

#### Apply all terraform plans

Terraform is split in two parts. The main one, directly in `src/aws` can work on multiple [`Terraform` workspaces](https://www.terraform.io/docs/state/workspaces.html). You will use this feature if you want separate environments (development, staging, preprod and production). We also need some resources available across all workspaces. For this we have an other terraform in `src/aws/shared_resources`.
To apply all plans at once run this command in the `src/aws` directory.

    $ make apply-all

Everything should be set up! You can check on your `AWS` management console.

You may have noticed that the `AWS` development environment requires a URL where the `Django` backend is running. You can easily get a URL that points to your locally running `Django` app using a tool such as [`ngrok`](https://ngrok.com).

### The `Django` Backend

All tasks related to the `Django` backend are run from the project root (where this `README.md` is located).

The easiest way to start working on the project is to use our `Makefile`:

    $ make bootstrap

This command builds the `app` container, installs back-end dependencies and performs database migrations. It's a good idea to use this command each time you are pulling code from the project repository to avoid dependency-related or migration-related issues.

🔧 **Before you go further**, you should take a look at the newly created `./env.d/development` file and replace the relevant values with your own. You can take a look at the [environment documentation](https://github.com/openfun/marsha/blob/master/docs/env.md#1-django-
...[truncated]...

# File tree
.circleci
  config.yml
CHANGELOG.md
CONTRIBUTORS.md
README.md
UPGRADE.md
arnold.yml
crowdin
  config.yml
docker
  files
    usr
      local
        etc
          gunicorn
docker-compose.yml
docs
  adr
    0001-actors.md
    0002-videos-languages.md
    0003-content-organization-and-accesses.md
    0004-soft-deletion.md
    README.md
  cache.md
  dev.md
  env.md
  i18n.md
  live_sessions.md
  lti.md
  moodle.md
  p2p-video-player.md
  peertube-runner.md
  permissions.md
  renater_federation_saml.md
  sprint-reviews
    2022-09-16-sprint-review.md
    2022-09-30-sprint-review.md
    2022-11-07-sprint-review.md
    2022-12-01-sprint-review.md
    2023-01-27-sprint-review#6.md
lib
  gitlint
    gitlint_emoji.py
readthedocs.yml
renovate.json
src
  .prettierrc.js
  backend
    manage.py
    marsha
      .cookiecutter
        cookiecutter.json
        {{cookiecutter.app_name}}
          __init__.py
          admin.py
          api.py
          apps.py
          defaults.py
          factories.py
          forms.py
          lti_select.py
          models.py
          serializers.py
          tests
          urls.py
          views.py
      __init__.py
      account
        __init__.py
        api.py
        apps.py
        backends
          saml_fer.py
        checks.py
        factories.py
        management
          __init__.py
          commands
        middleware.py
        models.py
        serializers.py
        social_pipeline
          __init__.py
          organization.py
          playlist.py
          social_auth.py
        tests
          __init__.py
          api
          backends
          dedupe_accounts
          test_checks.py
          test_middleware.py
          test_models.py
          test_social_pipeline_organization.py
          test_social_pipeline_playlist.py
          test_social_pipeline_social_auth.py
          test_views.py
          utils.py
        urls.py
        utils
          __init__.py
          dedupe_accounts
        views.py
      asgi.py
      bbb
        __init__.py
        admin.py
        api.py
        apps.py
        defaults.py
        factories.py
        forms.py
        lti_select.py
        management
          commands
        metadata.py
        models.py
        permissions.py
        serializers.py
        signals.py
        tests
          __init__.py
          api
          bbb_utils
          signals
          test_command_refresh_bbb_recordings.py
          test_command_rename_classroom_documents.py
          test_command_update_pending_classroom_sessions.py
          test_delete_outdated_classrooms.py
          test_models.py
          test_utils_tokens.py
          test_views_lti.py
          test_views_lti_config.py
          test_views_lti_select.py
        urls.py
        utils
          __init__.py
          bbb_utils.py
          tokens.py
        views.py
      celery_app.py
      core
        __init__.py
        admin.py
        admin_site.py
        api
          __init__.py
          account.py
          base.py
          file.py
          live_session.py
          lti_user_association.py
          pairing_challenge.py
          playlist.py
          playlist_access.py
          portability_request.py
          schema.py
          shared_live_media.py
          thumbnail.py
          timed_text_track.py
          video.py
          xapi.py
        apps.py
        cache.py
        defaults.py
        factories.py
        fields.py
        forms.py
        lti
          __init__.py
          common.py
          user_association.py
          utils.py
          validator.py
        lti_select.py
        management
          __init__.py
          commands
        metadata.py
        models
          __init__.py
          account.py
          base.py
          file.py
          playlist.py
          portability_request.py
          site.py
          video.py
        permissions
          __init__.py
          base.py
          organization.py
          playlist.py
          token.py
        routers.py
        sentry.py
        serializers
          __init__.py
          account.py
          base.py
          file.py
          live_session.py
          pairing_challenge.py
          playlist.py
          playlist_access.py
          portability_request.py
          shared_live_media.py
          thumbnail.py
          timed_text_track.py
          video.py
          xapi.py
        services
          __init__.py
          live_session.py
          video_participants.py
          video_recording.py
        signals.py
        simple_jwt
          __init__.py
          authentication.py
          factories.py
          permissions.py
          tokens.py
          utils.py
        static.py
        stats.py
        tasks
        tests
        urls
        utils
        views.py
        xapi.py
      deposit
      development
      e2e
      markdown
      page
      settings.py
      urls.py
      websocket
      workers.py
    setup.py
  frontend

# Selected code and test snippets
### src/backend/marsha/bbb/tests/api/classroom/test_service_end.py
"""Tests for the classroom API."""

from unittest import mock

from django.test import TestCase, override_settings

from marsha.bbb import api
from marsha.bbb.factories import ClassroomFactory
from marsha.core import factories as core_factories
from marsha.core.factories import (
    OrganizationAccessFactory,
    PlaylistAccessFactory,
    PlaylistFactory,
)
from marsha.core.models import ADMINISTRATOR
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)
from marsha.core.tests.testing_utils import reload_urlconf


# We don't enforce arguments documentation in tests
# pylint: disable=unused-argument


@override_settings(BBB_API_ENDPOINT="https://10.7.7.1/bigbluebutton/api")
@override_settings(BBB_API_SECRET="SuperSecret")
@override_settings(BBB_ENABLED=True)
class ClassroomServiceEndAPITest(TestCase):
    """Test for the Classroom API."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Force URLs reload to use BBB_ENABLED
        reload_urlconf()

    @mock.patch.object(api, "end")
    def test_api_bbb_end_classroom_anonymous(self, mock_end_request):
        """An anonymous should not be able to end a classroom."""
        classroom = ClassroomFactory()

        response = self.client.patch(
            f"/api/classrooms/{classroom.id}/end/",
        )
        self.assertEqual(response.status_code, 401)
        mock_end_request.assert_not_called()

    @mock.patch.object(api, "end")
    def test_api_bbb_end_classroom_user_logged_in(self, mock_end_request):
        """A logged-in user should not be able to end a classroom."""
        user = core_factories.UserFactory(
            first_name="Jane", last_name="Doe", email="jane.doe@example.com"
        )
        classroom = ClassroomFactory()
        self.client.force_login(user)

        response = self.client.patch(
            f"/api/classrooms/{classroom.id}/end/",
        )
        self.assertEqual(response.status_code, 401)
        mock_end_request.assert_not_called()

    @mock.patch.object(api, "end")
    def test_api_bbb_end_classroom_student(self, mock_end_request):
        """A student should not be able to end a classroom."""
        classroom = ClassroomFactory()

        jwt_token = StudentLtiTokenFactory(playlist=classroom.playlist)

        response = self.client.patch(
            f"/api/classrooms/{classroom.id}/end/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(response.status_code, 403)
        mock_
...[truncated]...

### src/backend/marsha/bbb/tests/api/classroom/test_service_join.py
"""Tests for the classroom API."""

import json
from unittest import mock

from django.test import TestCase, override_settings

from marsha.bbb import api
from marsha.bbb.factories import ClassroomFactory
from marsha.core import factories as core_factories
from marsha.core.factories import (
    OrganizationAccessFactory,
    PlaylistAccessFactory,
    PlaylistFactory,
)
from marsha.core.models import ADMINISTRATOR
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)
from marsha.core.tests.testing_utils import reload_urlconf


# We don't enforce arguments documentation in tests
# pylint: disable=unused-argument


@override_settings(BBB_API_ENDPOINT="https://10.7.7.1/bigbluebutton/api")
@override_settings(BBB_API_SECRET="SuperSecret")
@override_settings(BBB_ENABLED=True)
class ClassroomServiceJoinAPITest(TestCase):
    """Test for the Classroom API."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Force URLs reload to use BBB_ENABLED
        reload_urlconf()

    @mock.patch.object(api, "join")
    def test_api_bbb_join_classroom_anonymous(self, mock_join_request):
        """An anonymous should not be able to join a classroom."""
        classroom = ClassroomFactory()

        response = self.client.patch(
            f"/api/classrooms/{classroom.id}/join/",
        )
        self.assertEqual(response.status_code, 401)
        mock_join_request.assert_not_called()

    @mock.patch.object(api, "join")
    def test_api_bbb_join_classroom_user_logged_in(self, mock_join_request):
        """A logged-in user should not be able to join a classroom."""
        user = core_factories.UserFactory(
            first_name="Jane", last_name="Doe", email="jane.doe@example.com"
        )
        classroom = ClassroomFactory()
        self.client.force_login(user)

        response = self.client.patch(f"/api/classrooms/{classroom.id}/join/")
        self.assertEqual(response.status_code, 401)
        mock_join_request.assert_not_called()

    def test_api_bbb_join_student(self):
        """Joining a classroom as student should return an attendee classroom url."""
        classroom = ClassroomFactory(
            meeting_id="21e6634f-ab6f-4c77-a665-4229c61b479a",
            title="Classroom 1",
        )

        jwt_token = StudentLtiTokenFactory(
            playlist=classroom.playlist,
            consumer_site="consumer_site",
            user__id="user_id",
        )

        response = self.client.patch(
            f"/
...[truncated]...

### src/backend/marsha/bbb/tests/api/classroom/test_service_create.py
"""Tests for the classroom API."""

from unittest import mock

from django.test import TestCase, override_settings

from marsha.bbb import api
from marsha.bbb.factories import ClassroomFactory
from marsha.bbb.utils.bbb_utils import ApiMeetingException
from marsha.core import factories as core_factories
from marsha.core.factories import (
    OrganizationAccessFactory,
    PlaylistAccessFactory,
    PlaylistFactory,
)
from marsha.core.models import ADMINISTRATOR
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)
from marsha.core.tests.testing_utils import reload_urlconf


# We don't enforce arguments documentation in tests
# pylint: disable=unused-argument


@override_settings(BBB_API_ENDPOINT="https://10.7.7.1/bigbluebutton/api")
@override_settings(BBB_API_SECRET="SuperSecret")
@override_settings(BBB_ENABLED=True)
class ClassroomServiceCreateAPITest(TestCase):
    """Test for the Classroom API."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Force URLs reload to use BBB_ENABLED
        reload_urlconf()

    @mock.patch.object(api, "create")
    def test_api_bbb_create_anonymous(self, mock_create_request):
        """An anonymous should not be able to create a classroom."""
        classroom = ClassroomFactory()

        response = self.client.patch(f"/api/classrooms/{classroom.id}/create/")
        self.assertEqual(response.status_code, 401)
        mock_create_request.assert_not_called()

    @mock.patch.object(api, "create")
    def test_api_bbb_create_user_logged_in(self, mock_create_request):
        """A logged-in user should not be able to create a classroom."""
        user = core_factories.UserFactory(
            first_name="Jane", last_name="Doe", email="jane.doe@example.com"
        )
        classroom = ClassroomFactory()
        self.client.force_login(user)

        response = self.client.patch(f"/api/classrooms/{classroom.id}/create/")
        self.assertEqual(response.status_code, 401)
        mock_create_request.assert_not_called()

    @mock.patch.object(api, "create")
    def test_api_bbb_create_student(self, mock_create_request):
        """A student should not be able to create a classroom."""
        classroom = ClassroomFactory()

        jwt_token = StudentLtiTokenFactory(playlist=classroom.playlist)

        response = self.client.patch(
            f"/api/classrooms/{classroom.id}/create/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(res
...[truncated]...

### src/backend/marsha/development/tests/test_api_schema.py
"""Tests for the Schema endpoint on the API of the Marsha project."""

from django.test import TestCase, override_settings

from rest_framework.permissions import BasePermission

from marsha.core.api.schema import (
    clean_permission,
    extract_permission_docstring,
    format_permissions_and_docstring,
)
from marsha.core.tests.testing_utils import reload_urlconf


@override_settings(DEBUG=True)
class SchemaAPITest(TestCase):
    """Test the API route for the schema."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Force URLs reload to use DEBUG=true settings in this test suite.
        reload_urlconf()

    def test_api_schema(self):
        """The API has a schema route that answers."""
        response = self.client.get("/api/schema/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get("Content-Type"), "application/vnd.oai.openapi; charset=utf-8"
        )
        self.assertEqual(
            response.get("Content-Disposition"), 'inline; filename="Marsha API.yaml"'
        )


class PermissionA(BasePermission):
    """Permission A."""


class PermissionB(BasePermission):
    """Permission B."""


class PermissionC(BasePermission):
    """Permission C."""


class PermissionForSchemaAPITest(TestCase):
    """Test case dedicated to the permission formatting/display in the Swagger UI."""

    def test_clean_permission(self):
        """Test the `clean_permission` expected behavior."""
        for permission, expected_string in [
            (
                PermissionA & PermissionB,
                " **(** PermissionA **AND** PermissionB **)** ",
            ),
            (
                PermissionA | PermissionB,
                " **(** PermissionA **OR** PermissionB **)** ",
            ),
            (
                ~PermissionA,
                " **(NOT** PermissionA **)** ",
            ),
            (
                PermissionA,
                "PermissionA",
            ),
            (
                (PermissionA & PermissionB) | ~PermissionC,
                (
                    " **(**  **(** PermissionA **AND** PermissionB **)**  "
                    "**OR**  **(NOT** PermissionC **)**  **)** "
                ),
            ),
        ]:
            with self.subTest(permission=permission):
                self.assertEqual(
                    # mimic `get_permissions` by calling permission
                    clean_permission(permission()),
                    expected_string,
                )

    def test_extract_permission_docstring(
...[truncated]...

### src/backend/marsha/core/tests/serializers/test_xapi_statement.py
"""Tests for the XAPIStatementSerializer serializer of the Marsha project."""

from django.test import TestCase

from marsha.core.serializers import (
    ExtensionSerializer,
    VerbSerializer,
    XAPIStatementSerializer,
)


class VerbSerializerTest(TestCase):
    """Test the serializer validating a xAPI verb."""

    def test_verb_serializer_with_valid_data(self):
        """The VerbSerializer should be valid with valid data."""
        data = {"id": "http://url.tld", "display": {"foo": "bar"}}

        serializer = VerbSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_verb_serializer_with_missing_id_property(self):
        """Property id is mandatory. If missing it should fail."""
        data = {"display": {"foo": "bar"}}

        serializer = VerbSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("id", serializer.errors)
        error = serializer.errors.get("id").pop(0)
        self.assertEqual(error.code, "required")

    def test_verb_serializer_with_invalid_id_property(self):
        """Id property should be a valid URL."""
        data = {"id": "foo", "display": {"foo": "bar"}}

        serializer = VerbSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("id", serializer.errors)
        error = serializer.errors.get("id").pop(0)
        self.assertEqual(error.code, "invalid")

    def test_verb_serializer_with_missing_display_property(self):
        """Property display is mandatory. If missing it should fail."""
        data = {"id": "http://url.tld"}

        serializer = VerbSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("display", serializer.errors)
        error = serializer.errors.get("display").pop(0)
        self.assertEqual(error.code, "required")

    def test_verb_serializer_with_invalid_display_property(self):
        """Display property only accept Dictionary."""
        data = {"id": "http://url.tld", "display": "foo"}

        serializer = VerbSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("display", serializer.errors)
        error = serializer.errors.get("display").pop(0)
        self.assertEqual(error.code, "not_a_dict")


class ExtensionSerializerTest(TestCase):
    """Test the serializer validating a xAPI context."""

    def test_extension_serializer_with_valid_data(self):
        """The ContextSerializer should be valid with valid data."""
        data = {"extensions": {"foo": "bar"}}

        serializer = Extension
...[truncated]...

### src/backend/marsha/core/api/schema.py
"""Module to provide a custom implementation of the DRF spectacular schema generator."""

from drf_spectacular.openapi import AutoSchema
from rest_framework.permissions import AND, NOT, OR


def clean_permission(permission):
    """
    Convert recursively permission classes to strings.

    This allows to convert OR and AND and NOT permission classes to strings
    for the swagger documentation (Markdown).
    """
    if isinstance(permission, OR):
        return (
            f" **(** {clean_permission(permission.op1)}"
            f" **OR** {clean_permission(permission.op2)} **)** "
        )
    if isinstance(permission, AND):
        return (
            f" **(** {clean_permission(permission.op1)}"
            f" **AND** {clean_permission(permission.op2)} **)** "
        )
    if isinstance(permission, NOT):
        return f" **(NOT** {clean_permission(permission.op1)} **)** "
    return permission.__class__.__name__


def extract_permission_docstring(permission):
    """Return the used permission classes and their docstring as a dict."""
    if isinstance(permission, (OR, AND)):
        return extract_permission_docstring(
            permission.op1
        ) | extract_permission_docstring(permission.op2)
    if isinstance(permission, NOT):
        return extract_permission_docstring(permission.op1)

    return {permission.__class__.__name__: permission.__class__.__doc__}


def format_permissions_and_docstring(permissions, docstring_dict):
    """Format permissions and docstring for the swagger documentation (Markdown)."""
    permission_formatted_docstring = "\n- " + "\n- ".join(
        [f"**{perm}** : {docstring}" for perm, docstring in docstring_dict.items()]
    )

    if len(permissions) == 1:
        # Most of (all?) the time we are in this case
        return (
            "## Permissions\n\n"
            f"{permissions[0]}\n"
            "### Permission description\n"
            f"{permission_formatted_docstring}"
        )

    formatted_permissions = "\n- ".join(permissions)
    formatted_permissions = (
        "## Permissions\n\n"
        f"- {formatted_permissions}\n"
        "### Permission description\n"
        f"{permission_formatted_docstring}"
    )
    return formatted_permissions


class MarshaAutoSchema(AutoSchema):
    """Marsha specific AutoSchema to add the permission to the schema description."""

    def get_permission_description(self):
        """Get the permission description."""
        action_or_method = getattr(
            self.view, getattr(self.view, "action", self.method.lower()), None
        )

        if no
...[truncated]...

### src/backend/marsha/core/serializers/xapi.py
"""Structure of our XAPI responses with Django Rest Framework serializers."""

import re
import uuid

from django.core.exceptions import ValidationError

from rest_framework import serializers

from marsha.core.serializers.base import UUID_REGEX


class ExtensionSerializer(serializers.Serializer):
    """Validate the context in a xAPI statement."""

    extensions = serializers.DictField()


class VerbSerializer(serializers.Serializer):
    """Validate the verb in a xAPI statement."""

    id = serializers.URLField()

    display = serializers.DictField()


class XAPIStatementSerializer(serializers.Serializer):
    """A serializer to validate a xAPI statement."""

    verb = VerbSerializer()
    context = ExtensionSerializer()
    result = ExtensionSerializer(required=False)

    id = serializers.RegexField(
        re.compile(f"^{UUID_REGEX}$"),
        required=False,
        default=str(uuid.uuid4()),
    )

    def validate(self, attrs):
        """Check if there is no extra arguments in the submitted payload."""
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise ValidationError(f"Got unknown fields: {unknown_keys}")
        return attrs

### src/frontend/packages/lib_video/src/components/common/VideoWizard/CreateVOD/UploadVideoForm/UploadVideoPreview/index.tsx
import { Stack } from 'grommet';
import { BinSVG, Box } from 'lib-components';
import React, { useEffect, useRef, useState } from 'react';
import { defineMessages, useIntl } from 'react-intl';

import { BigDashedBox } from '../BigDashedBox';

const messages = defineMessages({
  removeVideoButtonLabel: {
    defaultMessage: 'Click on this button to remove the selected video.',
    description: 'Label of the video remove button.',
    id: 'components.UploadVideoPreview.removeVideoButtonLabel',
  },
});

interface UploadVideoPreviewProps {
  onClickRemoveButton: () => void;
  videoSrc: string;
}

export const UploadVideoPreview = ({
  onClickRemoveButton,
  videoSrc,
}: UploadVideoPreviewProps) => {
  const intl = useIntl();

  const videoRef = useRef<HTMLVideoElement>(null);
  const [isHovering, setIsHovering] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.addEventListener('play', () => setIsPlaying(true));
      videoRef.current.addEventListener('pause', () => setIsPlaying(false));
    }
  }, []);

  return (
    <BigDashedBox
      pad="0px"
      onMouseEnter={() => setIsHovering(true)}
      onMouseLeave={() => setIsHovering(false)}
    >
      <Stack anchor="top-right" fill>
        <Box overflow="hidden" round="small">
          <video controls ref={videoRef} src={videoSrc} width="100%" />
        </Box>
        {(!isPlaying || isHovering) && (
          <BinSVG
            aria-label={intl.formatMessage(messages.removeVideoButtonLabel)}
            className="m-b"
            height="18px"
            iconColor="white"
            onClick={() => onClickRemoveButton()}
            width="14px"
          />
        )}
      </Stack>
    </BigDashedBox>
  );
};

### src/frontend/packages/lib_video/src/components/common/VideoWizard/CreateVOD/UploadVideoForm/UploadVideoPreview/index.spec.tsx
/* eslint-disable testing-library/no-node-access */
/* eslint-disable testing-library/no-container */
import { fireEvent, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { render } from 'lib-tests';

import { UploadVideoPreview } from '.';

const mockedOnClickRemoveButton = jest.fn();

describe('<UploadVideoPreview />', () => {
  beforeEach(() => {
    jest.resetAllMocks();
  });

  it('renders UploadVideoPreview and clicks on the remove button', async () => {
    const { container } = render(
      <UploadVideoPreview
        onClickRemoveButton={mockedOnClickRemoveButton}
        videoSrc="/data/blob/video"
      />,
    );

    const video = container.getElementsByTagName('video')[0];
    expect(video).toHaveAttribute('controls');
    expect(video).toHaveAttribute('src', '/data/blob/video');
    const removeButton = screen.getByRole('button', {
      name: 'Click on this button to remove the selected video.',
    });

    await userEvent.click(removeButton);

    expect(mockedOnClickRemoveButton).toHaveBeenCalledTimes(1);
  });

  it('renders UploadVideoPreview, plays the video and then hovers it', async () => {
    const { container } = render(
      <UploadVideoPreview
        onClickRemoveButton={mockedOnClickRemoveButton}
        videoSrc="/data/blob/video"
      />,
    );

    const video = container.getElementsByTagName('video')[0];
    screen.getByRole('button', {
      name: 'Click on this button to remove the selected video.',
    });
    fireEvent.play(video);
    expect(
      screen.queryByRole('button', {
        name: 'Click on this button to remove the selected video.',
      }),
    ).not.toBeInTheDocument();

    await userEvent.hover(video);

    screen.getByRole('button', {
      name: 'Click on this button to remove the selected video.',
    });

    await userEvent.unhover(video);

    expect(
      screen.queryByRole('button', {
        name: 'Click on this button to remove the selected video.',
      }),
    ).not.toBeInTheDocument();
  });
});

### src/backend/marsha/core/tests/api/users/test_list.py
"""Tests for the User list API of the Marsha project."""

from django.test import TestCase

from marsha.core import factories, models
from marsha.core.simple_jwt.factories import UserAccessTokenFactory


class UserListAPITest(TestCase):
    """Test the list API for users objects."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        """Create dataset for all tests."""
        super().setUpClass()
        cls.organization = factories.OrganizationFactory()

        cls.user_1 = factories.OrganizationAccessFactory(
            organization=cls.organization,
            user__first_name="Arnold",
            user__last_name="Richardson",
            user__email="a.richardson@example.com",
        ).user
        cls.user_2 = factories.OrganizationAccessFactory(
            organization=cls.organization,
            user__first_name="Christian",
            user__last_name="Miller",
            user__email="c.miller@example.com",
        ).user
        cls.user_3 = factories.OrganizationAccessFactory(
            organization=cls.organization,
            user__first_name="Benoît",
            user__last_name="Hubert",
            user__email="b.hubert@example.com",
        ).user
        cls.user_4 = factories.OrganizationAccessFactory(
            organization=cls.organization,
            user__first_name="Damien",
            user__last_name="Bouvier",
            user__email="d.bouvier@example.com",
        ).user

        cls.other_organization = factories.OrganizationFactory()
        cls.user_5 = factories.OrganizationAccessFactory(
            organization=cls.other_organization,
            user__first_name="John",
            user__last_name="Parker",
        ).user

        # Never listed users
        factories.UserFactory()
        factories.OrganizationAccessFactory()

    def assert_user_cant_list_user(self, user):
        """Assert that a GET request returns an empty list."""
        jwt_token = UserAccessTokenFactory(user=user)

        response = self.client.get(
            "/api/users/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {"count": 0, "next": None, "previous": None, "results": []},
        )

    def assertGetReturnsOrderedUserList(self, user, expected_users):
        """Assert that a GET request returns a list of `expected_access`."""
        jwt_token = UserAccessTokenFactory(user=user)

        response = self.client.get(
            "/api/users/",
            HTTP_AU
...[truncated]...

### src/backend/marsha/core/tests/api/users/test_update.py
"""Tests for the User update API of the Marsha project."""

from django.test import TestCase

from marsha.core import factories, models
from marsha.core.simple_jwt.factories import UserAccessTokenFactory


class UserUpdateAPITest(TestCase):
    """Test the update API for user objects."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        """Create dataset for all tests."""
        super().setUpClass()
        cls.organization = factories.OrganizationFactory()

        cls.user_to_update = factories.OrganizationAccessFactory(
            organization=cls.organization,
            user__first_name="Arnold",
            user__last_name="Richardson",
            user__email="a.richardson@example.com",
            role=models.INSTRUCTOR,
        ).user

    def assert_user_cant_update_user(self, user):
        """Assert a user cannot update a user with a PUT request."""
        jwt_token = UserAccessTokenFactory(user=user)

        response = self.client.put(
            f"/api/users/{str(self.user_to_update.pk)}/",
            {"email": "a.richardson+test@example.com"},
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)

    def assert_user_can_update_user(self, user):
        """Assert a user can update a user with a PUT request."""
        jwt_token = UserAccessTokenFactory(user=user)

        response = self.client.put(
            f"/api/users/{str(self.user_to_update.pk)}/",
            {"email": "a.richardson+test@example.com"},
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

        self.user_to_update.refresh_from_db()
        self.assertEqual(
            response.json(),
            {
                "id": str(self.user_to_update.pk),
                "date_joined": self.user_to_update.date_joined.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
                "email": "a.richardson+test@example.com",
                "full_name": self.user_to_update.get_full_name(),
                "is_staff": False,
                "is_superuser": False,
                "organization_accesses": [
                    {
                        "organization": str(self.organization.pk),
                        "organization_name": self.organization.name,
                        "role": "instructor",
                        "user": str(self.user_to_update.pk),
                        "inactive_features":
...[truncated]...

### src/backend/marsha/core/tests/api/users/test_whoami.py
"""Tests for the User API of the Marsha project."""

from django.test import TestCase

from marsha.core import factories
from marsha.core.simple_jwt.factories import UserAccessTokenFactory


class UserWhoAmIAPITest(TestCase):
    """Test the API endpoint to get the current user."""

    # WHOAMI TESTS
    def test_whoami_by_anonymous_user(self):
        """
        Anonymous users can make `whoami` requests.

        They receive a 401 response confirming they are not logged in.
        """
        response = self.client.get("/api/users/whoami/")
        self.assertEqual(response.status_code, 401)

    def test_whoami_by_logged_in_user(self):
        """
        Logged-in users can make `whoami` requests.

        They receive their own user object.
        """
        user = factories.UserFactory(
            first_name="Jane", last_name="Doe", email="jane.doe@example.com"
        )
        org_1 = factories.OrganizationFactory()
        org_access_1 = factories.OrganizationAccessFactory(
            user=user, organization=org_1
        )
        org_2 = factories.OrganizationFactory()
        org_access_2 = factories.OrganizationAccessFactory(
            user=user, organization=org_2
        )

        jwt_token = UserAccessTokenFactory(user=user)

        with self.assertNumQueries(3):
            response = self.client.get(
                "/api/users/whoami/",
                HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["date_joined"],
            user.date_joined.isoformat()[:-6] + "Z",  # NB: DRF literally does this
        )
        self.assertEqual(response.json()["email"], "jane.doe@example.com")
        self.assertEqual(response.json()["full_name"], "Jane Doe")
        self.assertEqual(response.json()["id"], str(user.id))
        self.assertEqual(response.json()["is_staff"], False)
        self.assertEqual(response.json()["is_superuser"], False)

        resp_accesses = response.json()["organization_accesses"]
        resp_org_access_1 = (
            resp_accesses.pop(0)
            if resp_accesses[0]["organization"] == str(org_1.id)
            else resp_accesses.pop(1)
        )
        self.assertEqual(
            resp_org_access_1,
            {
                "organization": str(org_1.id),
                "organization_name": org_1.name,
                "role": org_access_1.role,
                "user": str(user.id),
                "inactive_features": [],
                "inactive_resources": [],
            },
   
...[truncated]...

### src/backend/marsha/bbb/tests/api/classroom/test_list.py
"""Tests for the classroom API."""

from django.test import TestCase, override_settings

from marsha.bbb.factories import ClassroomFactory
from marsha.core.factories import (
    OrganizationAccessFactory,
    PlaylistAccessFactory,
    PlaylistFactory,
    UserFactory,
)
from marsha.core.models import ADMINISTRATOR
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)
from marsha.core.tests.testing_utils import reload_urlconf


# We don't enforce arguments documentation in tests
# pylint: disable=unused-argument


@override_settings(BBB_API_ENDPOINT="https://10.7.7.1/bigbluebutton/api")
@override_settings(BBB_API_SECRET="SuperSecret")
@override_settings(BBB_ENABLED=True)
class ClassroomListAPITest(TestCase):
    """Test for the Classroom API."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Force URLs reload to use BBB_ENABLED
        reload_urlconf()

    def test_api_classroom_fetch_list_anonymous(self):
        """An anonymous should not be able to fetch a list of classroom."""
        response = self.client.get("/api/classrooms/")
        self.assertEqual(response.status_code, 401)

    def test_api_classroom_fetch_list_student(self):
        """A student should not be able to fetch a list of classroom."""
        classroom = ClassroomFactory()

        jwt_token = StudentLtiTokenFactory(
            playlist=classroom.playlist,
            permissions__can_update=True,
        )

        response = self.client.get(
            "/api/classrooms/", HTTP_AUTHORIZATION=f"Bearer {jwt_token}"
        )
        self.assertEqual(response.status_code, 403)

    def test_api_fetch_list_instructor(self):
        """An instructor should not be able to fetch a classroom list."""
        classroom = ClassroomFactory()

        jwt_token = InstructorOrAdminLtiTokenFactory(playlist=classroom.playlist)

        response = self.client.get(
            "/api/classrooms/", HTTP_AUTHORIZATION=f"Bearer {jwt_token}"
        )
        self.assertEqual(response.status_code, 403)

    def test_api_fetch_list_user_access_token_playlist_admin(self):
        """
        A user with UserAccessToken should be able to fetch a classroom list from playlist
        he is admin
        """
        user = UserFactory()
        playlist_access = PlaylistAccessFactory(user=user, role=ADMINISTRATOR)
        classrooms = ClassroomFactory.create_batch(3, playlist=playlist_access.playlist)
        ClassroomFactory()

        jwt_token = UserAccess
...[truncated]...

### src/backend/marsha/core/tests/api/users/test_retrieve.py
"""Tests for the User retrieve API of the Marsha project."""

from django.test import TestCase

from marsha.core import factories, models
from marsha.core.simple_jwt.factories import UserAccessTokenFactory


class UserRetrieveAPITest(TestCase):
    """Test the retrieve API for user objects."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        """Create dataset for all tests."""
        super().setUpClass()
        cls.organization = factories.OrganizationFactory()

        cls.user_to_retrieve = factories.OrganizationAccessFactory(
            organization=cls.organization,
            user__first_name="Arnold",
            user__last_name="Richardson",
            user__email="a.richardson@example.com",
            role=models.INSTRUCTOR,
        ).user

    def assert_user_cant_retrieve_user(self, user):
        """Assert a user cannot retrieve a user with a GET request."""
        jwt_token = UserAccessTokenFactory(user=user)

        response = self.client.get(
            f"/api/users/{str(self.user_to_retrieve.pk)}/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(response.status_code, 404)

    def assert_user_can_retrieve_user(self, user):
        """Assert a user can retrieve a user with a GET request."""
        jwt_token = UserAccessTokenFactory(user=user)

        response = self.client.get(
            f"/api/users/{str(self.user_to_retrieve.pk)}/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.json(),
            {
                "id": str(self.user_to_retrieve.pk),
                "date_joined": self.user_to_retrieve.date_joined.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
                "email": self.user_to_retrieve.email,
                "full_name": self.user_to_retrieve.get_full_name(),
                "is_staff": False,
                "is_superuser": False,
                "organization_accesses": [
                    {
                        "organization": str(self.organization.pk),
                        "organization_name": self.organization.name,
                        "role": "instructor",
                        "user": str(self.user_to_retrieve.pk),
                        "inactive_features": [],
                        "inactive_resources": [],
                    }
                ],
            },
        )

    def test_retrieve_user_by_anonymous_user(self):
        """Anonymous users cannot retrieve user.""
...[truncated]...

### src/backend/marsha/bbb/tests/api/classroom/test_create.py
"""Tests for the classroom API."""

from django.test import TestCase, override_settings

from marsha.bbb.factories import ClassroomFactory
from marsha.bbb.models import Classroom
from marsha.core import factories as core_factories
from marsha.core.factories import (
    OrganizationAccessFactory,
    PlaylistAccessFactory,
    PlaylistFactory,
)
from marsha.core.models import ADMINISTRATOR, INSTRUCTOR
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)
from marsha.core.tests.testing_utils import reload_urlconf


# We don't enforce arguments documentation in tests
# pylint: disable=unused-argument


@override_settings(BBB_API_ENDPOINT="https://10.7.7.1/bigbluebutton/api")
@override_settings(BBB_API_SECRET="SuperSecret")
@override_settings(BBB_ENABLED=True)
class ClassroomCreateAPITest(TestCase):
    """Test for the Classroom API."""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Force URLs reload to use BBB_ENABLED
        reload_urlconf()

    def test_api_classroom_create_anonymous(self):
        """An anonymous should not be able to create a classroom."""
        response = self.client.post("/api/classrooms/")
        self.assertEqual(response.status_code, 401)

    def test_api_classroom_create_student(self):
        """A student should not be able to create a classroom."""
        classroom = ClassroomFactory()

        jwt_token = StudentLtiTokenFactory(
            playlist=classroom.playlist,
            permissions__can_update=True,
        )

        response = self.client.post(
            "/api/classrooms/", HTTP_AUTHORIZATION=f"Bearer {jwt_token}"
        )
        self.assertEqual(response.status_code, 403)

    def test_api_classroom_create_instructor(self):
        """An instructor should be able to create a classroom."""
        playlist = core_factories.PlaylistFactory()

        jw
...[truncated]...