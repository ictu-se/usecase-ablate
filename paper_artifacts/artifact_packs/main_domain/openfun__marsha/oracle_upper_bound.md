# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

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

# Oracle-selected code and test snippets
### src/backend/marsha/urls.py
"""Marsha URLs configuration."""

import re

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, register_converter
from django.views.decorators.cache import cache_page

from django_peertube_runner_connector.urls import (
    urlpatterns as django_peertube_runner_connector_urls,
)
from rest_framework.routers import DefaultRouter

from marsha.core import models
from marsha.core.api import (
    ChallengeAuthenticationView,
    DocumentViewSet,
    LiveSessionViewSet,
    OrganizationViewSet,
    PlaylistAccessViewSet,
    PlaylistViewSet,
    PortabilityResourceViewSet,
    SharedLiveMediaViewSet,
    ThumbnailViewSet,
    TimedTextTrackViewSet,
    UserViewSet,
    VideoViewSet,
    XAPIStatementView,
    get_frontend_configuration,
    pairing_challenge,
    recording_slices_manifest,
    recording_slices_state,
    update_state,
)
from marsha.core.api.lti_user_association import LtiUserAssociationViewSet
from marsha.core.routers import MarshaDefaultRouter
from marsha.core.urls.converters import XAPIResourceKindConverter
from marsha.core.utils.lti_select_utils import get_lti_select_resources
from marsha.core.views import (
    DocumentLTIView,
    DocumentView,
    LTIConfigView,
    LTIRespondView,
    LTISelectView,
    RemindersCancelView,
    SiteView,
    VideoLTIView,
    VideoView,
)
from marsha.development.api import (
    dummy_document_upload,
    dummy_video_upload,
    local_classroom_document_upload,
    local_deposited_file_upload,
    local_document_upload,
    local_markdown_image_upload,
    local_videos_storage_upload,
)


register_converter(XAPIResourceKindConverter, "xapi_resource_kind")

LTI_SELECT_ROUTE_PATTERN = (
    rf"lti/select/((?P<resource_kind>{'|'.join(get_lti_select_resources().keys())})/)?$"
)

router = MarshaDefaultRouter()
router.register(models.Video.RESOURCE_NAME, VideoViewSet, basename="videos")
router.register(models.Document.RESOURCE_NAME, DocumentViewSet, basename="documents")
router.register("organizations", OrganizationViewSet, basename="organizations")
router.register("playlists", PlaylistViewSet, basename="playlists")
router.register(
    "playlist-accesses", PlaylistAccessViewSet, basename="playlist_accesses"
)
router.register(
    "portability-requests", PortabilityResourceViewSet, basename="portability_requests"
)
router.register("users", UserViewSet, basename="users")
router.register(
    "lti-user-associations", LtiUserAssociationViewSet, basename="lti_user_associations"
)

# Video related resources (
...[truncated]...

### src/backend/marsha/core/api/video.py
"""Declare API endpoints for videos with Django RestFramework viewsets."""

# pylint: disable=too-many-lines
from copy import deepcopy
from http import HTTPStatus
import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db import IntegrityError, OperationalError, transaction
from django.db.models import F, Func, Q, Value
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.module_loading import import_string

from boto3.exceptions import Boto3Error
import django_filters
from django_peertube_runner_connector.models import RunnerJob
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, MethodNotAllowed
from rest_framework.response import Response

from marsha.core import defaults, forms, permissions, serializers, storage
from marsha.core.api.base import APIViewMixin, BulkDestroyModelMixin, ObjectPkMixin
from marsha.core.defaults import ENDED, JITSI
from marsha.core.metadata import VideoMetadata
from marsha.core.models import (
    ADMINISTRATOR,
    INSTRUCTOR,
    LivePairing,
    LiveSession,
    SharedLiveMedia,
    TimedTextTrack,
    Video,
)
from marsha.core.services.video_participants import (
    VideoParticipantsException,
    add_participant_asking_to_join,
    move_participant_to_discussion,
    remove_participant_asking_to_join,
    remove_participant_from_discussion,
)
from marsha.core.services.video_recording import (
    VideoRecordingError,
    start_recording,
    stop_recording,
)
from marsha.core.tasks.video import launch_video_transcoding, launch_video_transcript
from marsha.core.utils import jitsi_utils
from marsha.core.utils.api_utils import validate_signature
from marsha.core.utils.medialive_utils import (
    ManifestMissingException,
    create_live_stream,
    create_mediapackage_harvest_job,
    delete_aws_element_stack,
    delete_mediapackage_channel,
    start_live_channel,
    stop_live_channel,
    update_id3_tags,
    wait_medialive_channel_is_created,
)
from marsha.core.utils.send_emails import (
    send_ready_to_convert_notification,
    send_vod_ready_notification,
)
from marsha.core.utils.time_utils import to_datetime, to_timestamp
from marsha.core.utils.xmpp_utils import close_room, create_room, reopen_room_for_vod
from marsha.websocket.utils import channel_layers_utils

...[truncated]...

### src/backend/marsha/core/models/video.py
"""This module holds the models for the marsha project."""

import secrets

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import OuterRef
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.functional import lazy
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _

from safedelete import HARD_DELETE_NOCASCADE
from safedelete.managers import SafeDeleteManager
from safedelete.queryset import SafeDeleteQueryset

from marsha.core.defaults import (
    APPROVAL,
    AWS_STORAGE_BASE_DIRECTORY,
    CELERY_PIPELINE,
    DELETED,
    DELETED_STORAGE_BASE_DIRECTORY,
    ENDED,
    ERROR,
    HARVESTED,
    IDLE,
    JOIN_MODE_CHOICES,
    LICENCES_CHOICES,
    LIVE_CHOICES,
    LIVE_TYPE_CHOICES,
    PENDING,
    PROCESS_PIPELINE_CHOICES,
    RUNNING,
    STOPPING,
    STORAGE_BASE_DIRECTORY,
    TRANSCODE_PIPELINE_CHOICES,
    UPLOAD_ERROR_REASON_CHOICES,
    VOD_STORAGE_BASE_DIRECTORY,
)
from marsha.core.models.account import ADMINISTRATOR, INSTRUCTOR, OrganizationAccess
from marsha.core.models.base import BaseModel
from marsha.core.models.file import AbstractImage, BaseFile, UploadableFileMixin
from marsha.core.models.playlist import PlaylistAccess, RetentionDateObjectMixin
from marsha.core.utils.api_utils import generate_salted_hmac
from marsha.core.utils.time_utils import to_timestamp


# pylint: disable=too-many-lines


class VideoQueryset(SafeDeleteQueryset):
    """A queryset to provide helper for querying videos."""

    def annotate_can_edit(self, user_id, force_value=None):
        """
        Annotate the queryset with a boolean indicating if the user can act
        on the video.
        Required for the VideoSerializer serializer.

        Parameters
        ----------
        user_id : str
            The user ID determine rights on video.
            We use the user ID here because it can be provided from UserToken

        force_value : optional[bool]
            If set, force the value of the annotation to `force_value`.
            Useful to avoid heavy request when we already know the answer.

        Returns
        -------
        QuerySet
            The annotated queryset.
        """
        if force_value is not None:
            return self.annotate(
                can_edit=models.Value(force_value, output_field=models.BooleanField()),
            )

        organi
...[truncated]...

### src/backend/marsha/core/serializers/video.py
"""Structure of Video related models API responses with Django Rest Framework serializers."""

import datetime
from datetime import timedelta
from hashlib import sha256
from inspect import signature

from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from rest_framework import serializers
from sentry_sdk import capture_message

from marsha.core.defaults import (
    AWS_PIPELINE,
    AWS_STORAGE_BASE_DIRECTORY,
    ENDED,
    HARVESTED,
    IDLE,
    JITSI,
    LIVE_CHOICES,
    LIVE_TYPE_CHOICES,
    PEERTUBE_PIPELINE,
    RUNNING,
    STOPPED,
    TMP_STORAGE_BASE_DIRECTORY,
)
from marsha.core.models import TimedTextTrack, Video
from marsha.core.serializers.base import TimestampField
from marsha.core.serializers.playlist import PlaylistLiteSerializer
from marsha.core.serializers.shared_live_media import (
    SharedLiveMediaId3TagsSerializer,
    SharedLiveMediaSerializer,
)
from marsha.core.serializers.thumbnail import ThumbnailSerializer
from marsha.core.serializers.timed_text_track import TimedTextTrackSerializer
from marsha.core.storage.storage_class import file_storage
from marsha.core.utils import jitsi_utils, time_utils, xmpp_utils
from marsha.core.utils.time_utils import to_datetime


MAX_DATETIME = timezone.datetime.max.replace(tzinfo=datetime.timezone.utc)


class UpdateLiveStateSerializer(serializers.Serializer):
    """A serializer to validate data submitted on the UpdateLiveState API endpoint."""

    state = serializers.ChoiceField(
        tuple(c for c in LIVE_CHOICES if c[0] in (RUNNING, STOPPED, HARVESTED))
    )
    logGroupName = serializers.CharField()
    requestId = serializers.CharField()
    extraParameters = serializers.DictField(allow_null=True, required=False)


class VideosStorageUploadEndedSerializer(serializers.Serializer):
    """A serializer to validate data submitted on the UploadEnded API endpoint."""

    file_key = serializers.CharField()

    def validate_file_key(self, value):
        """Check if the file_key is valid."""

        stamp = value.split("/")[-1]

        try:
            to_datetime(stamp)
        except serializers.ValidationError as error:
            raise serializers.ValidationError("file_key is not valid") from error

        if (
            self.context["obj"].get_storage_prefix(stamp, TMP_STORAGE_BASE_DIRECTORY)
            != value
        ):
            raise serializers.ValidationError("file_key is not valid")
        return value


class InitLiveStateSerializer(serializers.Serializer):
    """A serializer to validate data submitted on the i
...[truncated]...

### src/backend/marsha/core/tests/api/video/test_create.py
"""Tests for the Video create API of the Marsha project."""

from datetime import timedelta
import random
import uuid

from django.test import TestCase

from marsha.core import factories, models
from marsha.core.api import timezone
from marsha.core.defaults import INITIALIZED, STATE_CHOICES
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)


class VideoCreateAPITest(TestCase):
    """Test the create API of the video object."""

    maxDiff = None

    def test_api_video_create_anonymous(self):
        """Anonymous users should not be able to create a new video."""
        response = self.client.post("/api/videos/")
        self.assertEqual(response.status_code, 401)
        self.assertFalse(models.Video.objects.exists())

    def test_api_video_create_token_user_playlist_preexists(self):
        """A token user should not be able to create a video."""
        jwt_token = UserAccessTokenFactory()
        response = self.client.post(
            "/api/videos/", HTTP_AUTHORIZATION=f"Bearer {jwt_token}"
        )
        # Te user is authenticated, but action is forbidden => 403
        self.assertEqual(response.status_code, 403)
        self.assertFalse(models.Video.objects.exists())

    def test_api_video_create_student(self):
        """Student users should not be able to create videos."""
        video = factories.VideoFactory()
        jwt_token = StudentLtiTokenFactory(playlist=video.playlist)
        response = self.client.post(
            "/api/videos/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(models.Video.objects.count(), 1)

    def test_api_video_create_staff_or_user(self):
        """Users authenticated via a session should not be able to create videos."""
        for user in [factories.UserFactory(), factories.UserFactory(is_staff=True)]:
            self.client.login(username=user.username, password="test")
            response = self.client.post("/api/videos/")
            self.assertEqual(response.status_code, 401)
            self.assertFalse(models.Video.objects.exists())

    def test_api_video_create_by_playlist_admin(self):
        """
        Create video with playlist admin access.

        Users with an administrator role on a playlist should be able to create videos
        for it.
        """
        user = factories.UserFactory()
        playlist = factories.PlaylistFactory()
        factories.PlaylistAccessFactory(
            role=models
...[truncated]...

### src/frontend/packages/lib_video/src/components/common/VideoWizard/CreateVOD/index.spec.tsx
/* eslint-disable testing-library/no-node-access */
/* eslint-disable testing-library/no-container */
import { screen, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import fetchMock from 'fetch-mock';
import {
  AppConfig,
  UploadManagerContext,
  UploadManagerStatus,
  modelName,
  uploadState,
  useAppConfig,
  useJwt,
  useUploadManager,
  useVideo,
} from 'lib-components';
import { videoMockFactory } from 'lib-components/tests';
import { Deferred, render } from 'lib-tests';
import { PropsWithChildren } from 'react';

import { CreateVOD } from '.';

jest.mock('lib-components', () => ({
  ...jest.requireActual('lib-components'),
  useAppConfig: jest.fn(),
  report: jest.fn(),
  useVideo: jest.fn(),
  useUploadManager: jest.fn(),
  UploadManagerContext: {
    Provider: ({ children }: PropsWithChildren<{}>) => children,
  },
}));

const mockedUseAppConfig = useAppConfig as jest.MockedFunction<
  typeof useAppConfig
>;

const licenseChoices = [
  { display_name: 'Creative Common By Attribution', value: 'CC_BY' },
  {
    display_name: 'Creative Common By Attribution Share Alike',
    value: 'CC_BY-SA',
  },
  {
    display_name: 'Creative Common By Attribution Non Commercial No Derivates',
    value: 'CC_BY-NC-ND',
  },
  { display_name: 'Public Domain Dedication ', value: 'CC0' },
  { display_name: 'All rights reserved', value: 'NO_CC' },
];

URL.createObjectURL = () => '/blob/path/to/video';

const mockUseUploadManager = useUploadManager as jest.MockedFunction<
  typeof useUploadManager
>;

const mockedUseVideo = useVideo as jest.MockedFunction<typeof useVideo>;

describe('<CreateVOD />', () => {
  beforeEach(() => {
    useJwt.setState({
      jwt: 'json web token',
    });
    jest.resetAllMocks();
  });

  afterEach(() => {
    fetchMock.restore();
  });

  it('renders CreateVOD with empty fields', async () => {
    const mockedVideo = videoMockFactory({
      id: 'videoId',
      title: null,
      description: null,
      upload_state: uploadState.PENDING,
      is_ready_to_show: false,
    });

    mockedUseVideo.mockReturnValue(mockedVideo);

    mockedUseAppConfig.mockReturnValue({
      static: {
        img: {
          videoWizardBackground: 'img/path/videoWizardBackground',
        },
      },
    } as any);

    fetchMock.mock(
      `/api/videos/`,
      {
        actions: { POST: { license: { choices: licenseChoices } } },
      },
      { method: 'OPTIONS' },
    );

    mockUseUploadManager.mockReturnValue({
      addUpload: jest.fn(),
      resetUpload: jest.fn(),
      uploadMan
...[truncated]...

### src/backend/marsha/core/tests/api/video/test_list.py
"""Tests for the Video list API of the Marsha project."""

from datetime import datetime, timezone

from django.test import TestCase

from marsha.core import factories
from marsha.core.models import ADMINISTRATOR
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    UserAccessTokenFactory,
)


# pylint: disable=too-many-lines


class VideoListAPITest(TestCase):
    """Test the list API of the video object."""

    maxDiff = None

    def test_api_video_read_list_anonymous(self):
        """Anonymous users should not be able to read a list of videos."""
        factories.VideoFactory()
        response = self.client.get("/api/videos/")
        self.assertEqual(response.status_code, 401)

    def test_api_video_read_list_token_user(self):
        """
        Token user lists videos.

        A token user associated to a video should be able to read a list of videos.
        It should however be empty as they have no rights on lists of videos.
        """
        video = factories.VideoFactory()
        jwt_token = InstructorOrAdminLtiTokenFactory(
            playlist=video.playlist,
            permissions__can_update=False,
        )

        response = self.client.get(
            "/api/videos/", HTTP_AUTHORIZATION=f"Bearer {jwt_token}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"count": 0, "next": None, "previous": None, "results": []}
        )

    def test_api_video_read_list_user_with_no_access(self):
        """
        Token user lists videos.

        A user with a user token, with no playlist or organization access should not
        get any videos in response to video list requests.
        """
        # An organization with a playlist and one video
        organization = factories.OrganizationFactory()
        organization_playlist = factories.PlaylistFactory(organization=organization)
        factories.VideoFactory(playlist=organization_playlist)
        # A playlist with a video but no organization
        other_playlist = factories.PlaylistFactory()
        factories.VideoFactory(playlist=other_playlist)

        jwt_token = UserAccessTokenFactory()

        response = self.client.get(
            "/api/videos/", HTTP_AUTHORIZATION=f"Bearer {jwt_token}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"count": 0, "next": None, "previous": None, "results": []}
        )

    def test_api_video_read_list_user_with_playlist_access(self):
        """
        Token use
...[truncated]...

### src/backend/marsha/core/tests/api/video/test_retrieve.py
"""Tests for the Video retrieve API of the Marsha project."""

from datetime import datetime, timedelta, timezone as baseTimezone
import json
import random
from unittest import mock

from django.test import TestCase, override_settings

from marsha.core import factories, models
from marsha.core.api import timezone
from marsha.core.defaults import (
    AWS_PIPELINE,
    CC_BY,
    IDLE,
    JITSI,
    JOIN_MODE_CHOICES,
    PENDING,
    RAW,
    READY,
    RUNNING,
)
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)
from marsha.core.tests.testing_utils import RSA_KEY_MOCK


# This test module is quite long...
# pylint: disable=too-many-lines,duplicate-code,line-too-long
# flake8: noqa: E501


class VideoRetrieveAPITest(TestCase):
    """Test the retrieve API of the video object."""

    maxDiff = None

    def test_api_video_read_detail_anonymous(self):
        """Anonymous users should not be allowed to read a video detail."""
        video = factories.VideoFactory()
        response = self.client.get(f"/api/videos/{video.id}/")
        self.assertEqual(response.status_code, 401)
        content = json.loads(response.content)
        self.assertEqual(
            content, {"detail": "Authentication credentials were not provided."}
        )

    def test_api_video_read_detail_student(self):
        """Student users should be allowed to read a video detail."""
        video = factories.VideoFactory()
        jwt_token = StudentLtiTokenFactory(playlist=video.playlist)
        # Get the video linked to the JWT token
        response = self.client.get(
            f"/api/videos/{video.id}/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(response.status_code, 200)

    def test_api_video_read_detail_scheduled_video_student(self):
        """Student users should be allowed to read a scheduled video detail."""
        starting_at = timezone.now() + timedelta(days=100)
        video = factories.VideoFactory(
            live_state=IDLE, live_type=RAW, starting_at=starting_at
        )
        self.assertTrue(video.is_scheduled)
        jwt_token = StudentLtiTokenFactory(playlist=video.playlist)
        # Get the video linked to the JWT token
        response = self.client.get(
            f"/api/videos/{video.id}/",
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(response.status_code, 200)

    def test_api_video_read_detail_scheduled_past_video_student(self):
        """Student users can
...[truncated]...

### src/frontend/apps/lti_site/components/VideoWizard/index.spec.tsx
import { screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import fetchMock from 'fetch-mock';
import {
  LiveModeType,
  builderDashboardRoute,
  liveState,
  modelName,
  useFlags,
} from 'lib-components';
import { videoMockFactory } from 'lib-components/tests';
import { render } from 'lib-tests';
import React from 'react';

import {
  VIDEO_WIZARD_ROUTE,
  builderVideoWizzardRoute,
} from 'components/routes';

import VideoWizard from '.';

const mockedVideo = videoMockFactory({ live_state: null });
jest.mock('lib-components', () => ({
  ...jest.requireActual('lib-components'),
  WizardLayout: ({ children }: { children: React.ReactNode }) => (
    <div>{children}</div>
  ),
  useAppConfig: () => ({
    static: {
      img: {
        liveBackground: 'path/to/image.png',
      },
    },
    video: mockedVideo,
  }),
}));

useFlags.getState().setFlags({
  video: true,
  document: true,
  webinar: true,
  classroom: true,
  deposit: true,
});

describe('<VideoWizard />', () => {
  beforeEach(() => {
    jest.resetAllMocks();

    fetchMock.mock(
      `/api/videos/`,
      {
        actions: { POST: { license: { options: [] } } },
      },
      { method: 'OPTIONS' },
    );
  });

  afterEach(() => {
    fetchMock.restore();
  });

  it('renders VideoWizard and clicks on CreateVODButton', async () => {
    render(<VideoWizard />, {
      routerOptions: {
        componentPath: `/${VIDEO_WIZARD_ROUTE.all}`,
        history: [builderVideoWizzardRoute()],
      },
    });

    await screen.findByText(
      'You can choose how you want to share your content using the options below.',
    );
    screen.getByText('What would you like to do?');
    const createVODButton = screen.getByRole('button', {
      name: 'Create a video',
    });
    screen.getByRole('button', { name: 'Start a live' });

    await userEvent.click(createVODButton);

    expect(
      await screen.findByText(
        'Use this wizard to create a new video, that you will be able to share with your students.',
      ),
    ).toBeInTheDocument();
  });

  it('renders VideoWizard and clicks on ConfigureLiveButton', async () => {
    fetchMock.mock(
      `/api/videos/${mockedVideo.id}/initiate-live/`,
      JSON.stringify({
        ...mockedVideo,
        live_state: liveState.IDLE,
        live_type: LiveModeType.JITSI,
      }),
      { method: 'POST' },
    );

    render(<VideoWizard />, {
      routerOptions: {
        componentPath: `/${VIDEO_WIZARD_ROUTE.all}`,
        history: [builderVideoWizzardRoute()],
        routes: [
          {
      
...[truncated]...

### src/backend/marsha/core/serializers/file.py
"""Structure of Document related models API responses with Django Rest Framework serializers."""

import mimetypes
from os.path import splitext

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse

from rest_framework import serializers

from marsha.core.defaults import AWS_STORAGE_BASE_DIRECTORY, SCW_S3
from marsha.core.models import Document
from marsha.core.serializers.base import (
    TimestampField,
    UploadableFileWithExtensionSerializerMixin,
)
from marsha.core.serializers.playlist import PlaylistLiteSerializer
from marsha.core.storage.storage_class import file_storage


class DocumentSerializer(
    UploadableFileWithExtensionSerializerMixin, serializers.ModelSerializer
):
    """A serializer to display a Document resource."""

    class Meta:  # noqa
        model = Document
        fields = (
            "active_stamp",
            "extension",
            "filename",
            "id",
            "is_ready_to_show",
            "title",
            "upload_state",
            "url",
            "show_download",
            "playlist",
        )
        read_only_fields = (
            "active_stamp",
            "extension",
            "filename",
            "id",
            "is_ready_to_show",
            "upload_state",
            "url",
        )

    active_stamp = TimestampField(
        source="uploaded_on", required=False, allow_null=True, read_only=True
    )
    filename = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    is_ready_to_show = serializers.BooleanField(read_only=True)
    playlist = PlaylistLiteSerializer(read_only=True)

    def _get_extension_string(self, obj):
        """Document extension with the leading dot.

        Parameters
        ----------
        obj : Type[models.Document]
            The document that we want to serialize

        Returns
        -------
        String
            The document with the leading dot if the document has an extension
            An empty string otherwise

        """
        return "." + obj.extension if obj.extension else ""

    def get_filename(self, obj):
        """Filename of the Document.

        Parameters
        ----------
        obj : Type[models.Document]
            The document that we want to serialize

        Returns
        -------
        String
            The document's filename

        """
        return obj.filename

    def get_url(self, obj):
        """Url of the Document.

        Parameters
        ----------
        obj : Type[models.D
...[truncated]...

### src/backend/marsha/core/tests/api/video/test_initiate_upload.py
"""Tests for the Video initiate upload API of the Marsha project."""

from datetime import datetime, timezone as baseTimezone
import json
import random
from unittest import mock

from django.test import TestCase, override_settings

from marsha.core import factories, models
from marsha.core.api import timezone
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    UserAccessTokenFactory,
)


class VideoInitiateUploadAPITest(TestCase):
    """Test the "initiate upload" API of the video object."""

    maxDiff = None

    def test_api_video_initiate_upload_anonymous_user(self):
        """Anonymous users are not allowed to initiate an upload."""
        video = factories.VideoFactory()

        response = self.client.post(
            f"/api/videos/{video.id}/initiate-upload/",
            {"filename": "video_file", "mimetype": "", "size": 100},
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.json(), {"detail": "Authentication credentials were not provided."}
        )

    def test_api_video_instructor_initiate_upload_in_read_only(self):
        """An instructor with read_only set to true should not be able to initiate an upload."""
        video = factories.VideoFactory()
        jwt_token = InstructorOrAdminLtiTokenFactory(
            playlist=video.playlist,
            permissions__can_update=False,
        )

        response = self.client.post(
            f"/api/videos/{video.id}/initiate-upload/",
            {"filename": "video_file", "mimetype": "", "size": 100},
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
        )
        self.assertEqual(response.status_code, 403)

    def test_api_video_initiate_upload_token_user(self):
        """A token user associated to a video should be able to retrieve an upload policy."""
        video = factories.VideoFactory(
            id="27a23f52-3379-46a2-94fa-697b59cfe3c7",
            upload_state=random.choice(["ready", "error"]),
        )
        jwt_token = InstructorOrAdminLtiTokenFactory(playlist=video.playlist)

        # Create another video to check that its upload state is unaffected
        other_video = factories.VideoFactory(
            upload_state=random.choice(["ready", "error"])
        )

        # Get the upload policy for this video
        # It should generate a key file with the Unix timestamp of the present time
        now = datetime(2018, 8, 8, tzinfo=baseTimezone.utc)
        with mock.patch.object(timezone, "now", return_value=now), mock.patch(
            "datetime.datetime"
 
...[truncated]...

### src/frontend/packages/lib_video/src/components/common/VideoWizard/CreateVOD/UploadVideoForm/index.spec.tsx
/* eslint-disable testing-library/no-node-access */
/* eslint-disable testing-library/no-container */
import { screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import fetchMock from 'fetch-mock';
import {
  UploadManagerStatus,
  modelName,
  uploadState,
  useUploadManager,
} from 'lib-components';
import { videoMockFactory } from 'lib-components/tests';
import { render } from 'lib-tests';
import { PropsWithChildren } from 'react';

import { wrapInVideo } from '@lib-video/utils/wrapInVideo';

import { UploadVideoForm } from '.';

jest.mock('lib-components', () => ({
  ...jest.requireActual('lib-components'),
  useUploadManager: jest.fn(),
  UploadManagerContext: {
    Provider: ({ children }: PropsWithChildren<{}>) => children,
  },
}));
const mockUseUploadManager = useUploadManager as jest.MockedFunction<
  typeof useUploadManager
>;

const mockedOnRetry = jest.fn();
const mockedSetVideoFile = jest.fn();

URL.createObjectURL = () => '/blob/path/to/video';

describe('<UploadVideoForm />', () => {
  beforeEach(() => {
    jest.resetAllMocks();
  });
  afterEach(() => {
    fetchMock.restore();
  });

  it('renders UploadVideoForm when there is no file selected', () => {
    const mockedVideo = videoMockFactory({ upload_state: uploadState.PENDING });

    mockUseUploadManager.mockReturnValue({
      addUpload: jest.fn(),
      resetUpload: jest.fn(),
      uploadManagerState: {},
    });

    render(
      wrapInVideo(
        <UploadVideoForm
          onRetry={mockedOnRetry}
          setVideoFile={mockedSetVideoFile}
        />,
        mockedVideo,
      ),
    );

    expect(
      screen.getByText('Add a video or drag & drop it'),
    ).toBeInTheDocument();
  });

  it('renders UploadVideoForm with a file selected and then removes the file', async () => {
    const mockedVideo = videoMockFactory({ upload_state: uploadState.PENDING });

    mockUseUploadManager.mockReturnValue({
      addUpload: jest.fn(),
      resetUpload: jest.fn(),
      uploadManagerState: {
        [mockedVideo.id]: { status: UploadManagerStatus.SUCCESS } as any,
      },
    });

    const { container } = render(
      wrapInVideo(
        <UploadVideoForm
          onRetry={mockedOnRetry}
          setVideoFile={mockedSetVideoFile}
        />,
        mockedVideo,
      ),
    );

    const file = new File(['(⌐□_□)'], 'course.mp4', { type: 'video/mp4' });
    const hiddenInput = screen.getByTestId('input-video-test-id');

    await userEvent.upload(hiddenInput, file);

    await waitFor(() =>
      expect(mockedSetVideoFile
...[truncated]...

### src/frontend/packages/lib_video/src/components/common/VideoWizard/CreateVOD/UploadVideoForm/UploadVideoDropzone/index.spec.tsx
/* eslint-disable testing-library/no-container */
/* eslint-disable testing-library/no-node-access */
import { fireEvent, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { colorsTokens } from 'lib-common';
import { render } from 'lib-tests';

import { UploadVideoDropzone } from '.';

const mockedSetVideoFile = jest.fn();

describe('<UploadVideoDropzone />', () => {
  beforeEach(() => {
    jest.resetAllMocks();
  });

  it('renders UploadVideoDropzone and uploads a file', async () => {
    const { container } = render(
      <UploadVideoDropzone setVideoFile={mockedSetVideoFile} />,
    );

    const dashedBox =
      container.firstElementChild!.children[1].firstElementChild;
    expect(dashedBox).toHaveStyle(
      `background-color: ${colorsTokens['info-150']}}`,
    );

    const svg = container.getElementsByTagName('path')[0];
    expect(svg).toHaveStyle(`fill: #b4cff2`);

    const text = screen.getByText('Add a video or drag & drop it');
    expect(text).toHaveStyle('color: #b4cff2');

    const file = new File(['(⌐□_□)'], 'course.mp4', { type: 'video/mp4' });
    const hiddenInput = screen.getByTestId('input-video-test-id');

    await userEvent.upload(hiddenInput, file);

    await waitFor(() => expect(mockedSetVideoFile).toHaveBeenCalledTimes(1));
    expect(mockedSetVideoFile).toHaveBeenCalledWith(file);
  });

  it('renders UploadVideoDropzone and drags a file over', async () => {
    const { container } = render(
      <UploadVideoDropzone setVideoFile={mockedSetVideoFile} />,
    );

    const dashedBox =
      container.firstElementChild!.children[1].firstElementChild;
    const svg = container.getElementsByTagName('path')[0];
    const text = screen.getByText('Add a video or drag & drop it');

    expect(dashedBox).toHaveStyle(
      `background-color: ${colorsTokens['info-150']}`,
    );
    expect(svg).toHaveStyle('fill: #b4cff2');
    expect(text).toHaveStyle('color: #b4cff2');

    fireEvent.dragEnter(
      container.querySelector('input[type="file"]')!,
      new File(['(⌐□_□)'], 'course.mp4', { type: 'video/mp4' }),
    );
    await waitFor(() =>
      expect(dashedBox).toHaveStyle('background-color: #b4cff2'),
    );
    expect(svg).toHaveStyle(`fill: white`);
    expect(text).toHaveStyle(`color: white`);

    fireEvent.dragLeave(
      container.querySelector('input[type="file"]')!,
      new File(['(⌐□_□)'], 'course.mp4', { type: 'video/mp4' }),
    );
    await waitFor(() =>
      expect(dashedBox).toHaveStyle(
        `background-color: ${colorsTokens['info-150']}`,

...[truncated]...

### src/frontend/packages/lib_video/src/components/common/VideoWizard/CreateVOD/UploadVideoForm/BigDashedBox/index.spec.tsx
import { screen } from '@testing-library/react';
import { render } from 'lib-tests';
import React from 'react';

import { BigDashedBox } from '.';

const GenericComponent1 = () => <p>generic component 1</p>;
const GenericComponent2 = () => <p>generic component 2</p>;
const GenericComponent3 = () => <p>generic component 3</p>;

describe('<BigDashedBox>', () => {
  it('renders BigDashedBox with one child', () => {
    render(
      <BigDashedBox>
        <GenericComponent1 />
      </BigDashedBox>,
    );

    expect(screen.getByText('generic component 1')).toBeInTheDocument();
  });

  it('renders BigDashedBox with 3 children', () => {
    render(
      <BigDashedBox>
        <GenericComponent1 />
        <GenericComponent2 />
        <GenericComponent3 />
      </BigDashedBox>,
    );

    expect(screen.getByText('generic component 1')).toBeInTheDocument();
    expect(screen.getByText('generic component 2')).toBeInTheDocument();
    expect(screen.getByText('generic component 3')).toBeInTheDocument();
  });
});

### src/backend/marsha/core/tests/api/video/test_upload_ended.py
"""Tests for the Video upload ended API of the Marsha project."""

import json
from unittest import mock

from django.test import TestCase

from marsha.core import factories, models
from marsha.core.defaults import PEERTUBE_PIPELINE, PROCESSING
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)


class VideoUploadEndedAPITest(TestCase):
    """Test the "upload-ended" API of the video object."""

    maxDiff = None

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.some_organization = factories
...[truncated]...