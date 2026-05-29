# README-derived retrieval query
openfun marsha ## README.md
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

- `./src/aws/shared_resources`: this project manages resources common to all marsha environments on the same AWS account. These resources must not live in different workspaces so you must work in the `default` workspace. To ease the use of this project, a dedicated script is available in `./src/aws/bin/shared-resources` which uses and configures the `Terraform` docker image. You have to run a Terraform command as if you were using the terraform cli. (eg: `./bin/shared-resources plan` will execute Terraform'
...[truncated]...

# BM25 selected code snippets
### README.md
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
- Transcode videos using Peertube runners to generate all necessary video files (various formats and fragments & manifests for adaptive-bitrate streaming) into a destination `S3`
...[truncated]...

### UPGRADE.md
# Upgrade

All instructions to upgrade this project from one release to the next will be
documented in this file. Upgrades must be run sequentially, meaning you should
not skip minor/major releases while upgrading (fix releases can be skipped).

The format is inspired from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### 5.10.0 to 5.11.0

Cloudfront signed URLs are not used anymore in the project, make sure to remove the following environment variables:
- CLOUDFRONT_PRIVATE_KEY_PATH
- CLOUDFRONT_SIGNED_URLS_ACTIVE
- CLOUDFRONT_SIGNED_URLS_VALIDITY
- CLOUDFRONT_SIGNED_URL_CACHE_DURATION
- CLOUDFRONT_SIGNED_PUBLIC_KEY_ID
- CLOUDFRONT_DOMAIN = values.Value(None)

### 5.7.x to 5.8.0

Environment variables previously prefixed with `DJANGO_VIDEOS_STORAGE_` are now prefixed with `DJANGO_STORAGE_`. Make sure to update your configuration accordingly.

### 4.2.x to 4.3.0

`DJANGO_STATICFILES_STORAGE` environment variable is not used anymore. You have to replace it by `DJANGO_STORAGES_STATICFILES_BACKEND`.

## 3.27.x to 4.0.x

### Before deploying

First you have to install `hashicorp/tls` provider by running `./bin/terraform init` in the `src/aws` directory.

Then the new terraform plan must be applied:

```bash
$ cd src/aws
$ make apply
```

Once done, a new ssh key pair has been generated. The public key is in the cloudfront management public keys and you have to use the corresponding ssh private key in your marsha installation. You have to retrieve it and replace your actual ssh private key by this one.

```bash
$ ./bin/terraform output cloudfront_ssh_private_key
```

You also have to remove the `DJANGO_CLOUDFRONT_ACCESS_KEY_ID` environment variable and add the new one `DJANGO_CLOUDFRONT_SIGNED_PUBLIC_KEY_ID`. It's value can be retrieve in the terraform output:

```bash
$ /bin/terraform output cloudfront_publick_key_id
```

## 3.0.0 to 3.1.0

### After deploying

- If you run the AWS migration, remove the variable `TF_VAR_migrations`,

### Before deploying


- An AWS migration should be run. This migration escapes all existing timed text
  tracks in the source bucket. This migration is called `0001_encode_timed_text_tracks` and you
  should set the environment variable `TF_VAR_migrations` with the value
  `0001_encode_timed_text_tracks`.
- Deploy first the AWS stack using terraform.

## 2.10.x to 3.0.x

### Before switching

- The deprecated route `/lti-video/` is removed. You must move all your existing
  link using this route to the route `/lti/videos/{id}` w
...[truncated]...

### docs/peertube-runner.md
# PeerTube Runner

This document describes how to use [django-peertube-runner-connector](https://github.com/openfun/django-peertube-runner-connector) library in order to use a [PeerTube runner](https://docs.joinpeertube.org/admin/remote-runners) on Marsha. The goal is to replace the current AWS transcoding to use PeerTube runner hosted on your own infrastructure instead.

## Marsha integration

### The SocketIO problem

`django-peertube-runner-connector` is using the [socketIO](https://socket.io/) library. To make this works with Marsha, we needed to support its websocket endpoint, so we added this to the `websocket_urlpatterns`.


```Python
from django_peertube_runner_connector.socket import sio
from socketio import ASGIApp

websocket_urlpatterns += re_path(r"^socket.io/", ASGIApp(sio)),
```

Marsha is already using a websocket library and has a middleware verifying the JWT token in each websocket connection. So we needed to disable it for socket.io usage because our runner do not send the JWT token. It's a server to server connection.

```Python
# In case of a socket.io connection do not validate the token
if scope["path"] != "/socket.io/":
    token = self.validate_jwt(scope)
    scope["token"] = token
```

Doing this is enough to make PeerTube runner and Marsha work together without breaking change.

### Peertube Pipeline

In Marsha app, anything that should be done through Peertube runners should have the property `transcode_pipeline` set to `PEERTUBE`. Doing so, change the way video's urls are generated and enable the launch of transcoding jobs. Moreover, everything related to Peertube transcoding will use the [Scaleway](https://www.scaleway.com/en/object-storage/) object storage. The goal is to progressively use this new storage for any new video object.

### Storages

`django-peertube-runner-connector` uses [django-storages](https://django-storages.readthedocs.io/en/latest/) library to transcode and store videos. We take advantage of this library to store videos in different storage backends depending on our use case and environment.

In our case we need to set the `STORAGES["videos"]["BACKEND"]` setting with the right storage class, and the `STORAGE_BACKEND` setting with the right value. See [storage](#storage), to understand why we need this second setting.

#### S3FileStorage

A storage used to store files in a S3 like bucket. It can be used locally, and should be used in production.

```Python
STORAGES = {
    "videos": {
        "BACKEND": values.Value(
            "marsha.core.storage.s3.S3FileStorage",
            environ_name="STORAGES_BA
...[truncated]...

### docs/sprint-reviews/2023-01-27-sprint-review#6.md
# Marsha sprint review #5 of January 27, 2023

## Achievements

- Issues on the service worker for handling of JWT token: remove it and replace it by a wrapper
  around fetch that catches 401 and renews the token
- Improved Shibboleth authentication:
    * refresh tokens
    * add image to organizations in Shibboleth select list
- BBB:
    - Added recordings
    - Added LTI links for easy integration to a LMS from the website
    - Added maximum size to uploaded documents
- Prepared the VOD/Live for the standalone site
- Added permissions to allow instructors to create playlists

## Next

- Document permissions and add description of permissions to each endpoint
- Banner image and text should be customizable (by a developper for now)
- Add VOD/Live to the standalone site as soon as available
- Start using [Cunningham](https://github.com/openfun/cunningham) as soon as possible
- Add footer with legal mentions and general conditions
- Display home page even when anonymous
- Fix date picker issue
- Rework Markdown module
- Continue extracting remaining modules to standalone site: Documents, Deposits, Markdown
- Refactor to differentiate Course (= LTI context) from Playlists and allow multiple playlists
   for a resource
- C&P to add user documentation to Zendesk
- Allow teachers to download the subtitles on the dashboard of their own videos
- Blocking point for VOD in Moodle: must be able to embed a video to WYSIWYG content:
    * Allow embedding iframes (permission to be given on a per consumer site basis)
    * Finalize generic LTI plugins for Moodle (activity and WYSIWYG)
- Solve Shibboleth issues:
    * Security configuration
    * Presence/quality of fields => handle all cases and display information pages instead of failing with 500
- Add student consent for recording:
  * check what already exists for consent on the BBB API
  * checkbox for the teacher to activate recording
  * input text for the teacher to explain what the recording is for, and how long the recording
    will be kept when recording is activated
  * explanation + checkbox for the student each time recording is activated
  * store recordings for a limited time

# Also discussed

- Allow activating/deactivating modules for each organization
- Allow mass uploads
- Organize design workshop on the deposit module to see how it can evolve toward a full homework
  submission app.
- Integrate downloading videos in the videojs skin
- LRS configuration: should be consumer site OR organization. Is this exclusive? Is the event
  sent twice?
- Improve onboarding of new backend developpers:
  * Per
...[truncated]...

### docs/sprint-reviews/2022-11-07-sprint-review.md
# Marsha sprint review #3 of November 7, 2022

## Achievements

- Allow targeting LTI select endpoints to one resource
- Incidents with Jitsi due to Jibri breaking upgrade
  We now run Jibri's default image instead of our own
- Refactorings to make standalone site work
- Fixed Django's Management commands that were broken in production
- Deployed the standalone site to the staging environment
- Add playlist and profile pages
- Make LTI components compatible with the site
- Add a form to create a new classroom
- Port webinar apps to VOD: documents, transcripts, download video
- Sharing between playlists (portability)

## Next sprint

- Change french translation "En direct" to "webinaire"
- Rename playlist to course
- Port attendance to VOD when it comes from a live
- Port Chat to VOD
- Port Webinar and video to website
- Finalize sharing between playlists
- On each user login:
  * if the organization does not exists: create it on the fly
  * if the organization already exists, but the user has no access role on it: create it according to what Shibboleth says: teacher or student
  * if the organization already exists and the user already has an access role: update it with what
  Shibboleth says: teacher or student
- Create playlist: don't ask consumer site and LTI ID

## Discussed

- We could create a personal playlist (to be renamed to context asap) on the fly when creating a
  user to use as default or we could allow the playlist to be empty on a resource
- A teacher in an organization is allowed by default to create a playlist
  and becomes admin of the playlist s.he creates
- Handling organizations: created on the fly from Shibboleth
- Should organization be a context as in github
- Chat in VOD should be either hidden, readonly or open for discussion
- How to display shared documents in VOD?
- How can we add tests to avoid breaking the command line again in the future (cost consequences)

### docs/env.md
# Environment variables

`marsha` contains several projects, three of which are configured through environment variables.

First, there is our Django backend. We try to follow [12 factors app](https://12factor.net/) and so use environment variables for configuration. It looks for environment variables in `env.d/{environment}`.

Then, there is our AWS deployment configurations in the `src/aws` folder. Terraform looks for environment variables in `src/aws/env.d/{environment}`:

- A small side Terraform project located in `src/aws/create_state_bucket` is responsible just for creating an S3 bucket in AWS that Terraform will use to record the state of the main Marsha project with encryption and versioning.
- The main Terraform project in charge of deploying Marsha,

## 1. Django backend environment

Specified in `{REPO_ROOT}/env.d/{environment}`.

### General Django settings

#### DJANGO_ALLOWED_HOSTS

A string of comma separated domains that Django should accept and answer to. See [Django documentation](https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts) for more details about this setting.

- Type: String
- Required: Varies depending on the environment.
  - No in development, this setting is not available and its value is forced to accept any originating domain;
  - Yes otherwise.
- Default: Varies depending on the environment.
  - ["*"] in development: all originating domains are accepted;
  - None otherwise: all originating domains are rejected.

#### DJANGO_CONFIGURATION

Define the environment in which the application should run. It conditions which version of the settings will be loaded.

- Type: `String`
- Required: Yes
- Default: `Development`
- Choices: One of `Development`, `Test`, `Staging`, `Preprod` or `Production`.

#### DJANGO_DEBUG

Turns on/off debug mode.

- Type: Boolean
- Required: No
- Default: `True` if `DJANGO_CONFIGURATION` is set to `Development`, `False` otherwise
- Choices: `True` or `False`

#### DJANGO_SECRET_KEY

Standard Django secret key used to make the instance unique and generate hashes such as CSRF tokens or auth keys.

See [Django documentation](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key) for more information about this setting.

- Type: String
- Required: Yes
- Default: None

#### DJANGO_SETTINGS_MODULE

Define the settings file to use, relative to `src/backend`.

- Type: `String`
- Required: Yes
- Default: `marsha.settings`
- Choices: Must be set to `marsha.settings`.

### Marsha specific settings

#### DJANGO_BYPASS_LTI_VERIFICATION

Whether to skip all LTI-related checks and accept a
...[truncated]...

### .circleci/config.yml
# CircleCI's configuration for Marsha
#
# Reference: https://circleci.com/docs/2.0/configuration-reference/

parameters:
  cache-version:
    type: string
    default: '{{ .Environment.CACHE_VERSION }}.0'

aliases:
  - &docker_login
    # Login to DockerHub
    #
    # Nota bene: you'll need to define the following secrets environment vars
    # in CircleCI interface:
    #
    #   - DOCKER_HUB_USER
    #   - DOCKER_HUB_PASS
    run:
      name: Login to DockerHub
      command: echo "$DOCKER_HUB_PASS" | docker login -u "$DOCKER_HUB_USER" --password-stdin

  - &count_cpus
    run:
      name: Count the number of available cpu cores
      command: echo "export NB_CPUS=$(cat /proc/cpuinfo | grep processor | wc -l)" >> $BASH_ENV
# Configuration file anchors
generate-version-file: &generate-version-file
  run:
    name: Create a version.json
    command: |
      # Create a version.json à-la-mozilla
      # https://github.com/mozilla-services/Dockerflow/blob/master/docs/version_object.md
      printf '{"commit":"%s","version":"%s","source":"https://github.com/%s/%s","build":"%s"}\n' \
        "$CIRCLE_SHA1" \
        "${CIRCLE_TAG:-$CIRCLE_SHA1}" \
        "$CIRCLE_PROJECT_USERNAME" \
        "$CIRCLE_PROJECT_REPONAME" \
        "$CIRCLE_BUILD_URL" > src/backend/marsha/version.json

version: 2.1
commands:
  get_last_frontend_commit:
    description: 'Get last commit that modified the frontend and stores it in File. File is used as checksum source for part of frontend caching key.'
    parameters:
      filename:
        type: string
    steps:
      - run:
          name: Get last commit that modified frontend
          command: git log -n 1 --pretty=format:%H -- . > << parameters.filename >>
jobs:
  # Git jobs
  # Check that the git history is clean and complies with our expectations
  lint-git:
    docker:
      # stay in python 3.8
      - image: cimg/python:3.8
        auth:
          username: $DOCKER_HUB_USER
          password: $DOCKER_HUB_PASS
    working_directory: ~/marsha
    steps:
      - checkout
      - run:
          name: Check presence of all commit authors in CONTRIBUTORS.md file
          command: |
            for contributor in $(git log --pretty="format:%ae" 33587e4faee29ef55d0c8e8dd96eaa4989ea714a.. | sort | uniq ); do grep -F $contributor CONTRIBUTORS.md; done
      - run:
          name: Check absence of fixup commits
          command: |
            ! git log | grep 'fixup!'
      - run:
          name: Install gitlint
          command: |
            pip install requests
            pip install --user gitlint
      - run:
         
...[truncated]...

### docs/sprint-reviews/2022-09-30-sprint-review.md
# Marsha sprint review #2 of September 30, 2022

## To be discussed

- Refactor folders in `src/backend/marsha

## Achievements

- Rename BBB to `classrooms`
- Upload document to a BBB classroom
- Add API permissions for the site
- Splitting test files that are too long
- Started the website: authentication, i18n, menu, navigation, playlists page
- Refactoring to extract components that we can use in the site
- Started work on link between LTI users and site users
- Started work on asking for a portability from the LTI site
- Started work on the student view for the VOD (let chat and shared document follow from a live)

## Next sprint

- Add deposit to the green button in OpenEdX
- Use deposits in a course in production
- Add playlists and BBB classrooms to the site 
- Work on deep linking to show to a teacher everything he has access to
- Debug switch "everybody on stage" to "streaming"
- Set max file deposit to 1,5Go
- Go live for markdown and deposits: on fun-campus.fr and fun-mooc.fr
- deploy the site frontend to staging
- Configure Shibboleth access
- Continue work on marketing documents

## Discussed

- Review resource names:
  > Ok: Videos, Webinars, Virtual Classrooms
  > To be renamed: Lessons
- We will need to rename the existing `Playlist` to `Context` and introduce a real
  collection feature.
- Remove title and tabs from the student view for the VOD
- Activate token (need to activate Magnify first)
- Jitsi configuration in LMS too small > link
- Allow screen sharing on fun-campus.Fr

### src/frontend/packages/lib_components/src/types/tracks.ts
import { Nullable } from 'lib-common';

import { JitsiMeetExternalAPI } from '@lib-components/types/libs/JitsiMeetExternalAPI';

import { ConsumerSite } from './ConsumerSite';
import { Participant } from './Participant';
import { XMPP } from './XMPP';
import { Classroom, ClassroomDocument } from './apps/classroom/models';
import { DepositedFile } from './apps/deposit/models';
import { MarkdownDocument, MarkdownImage } from './apps/markdown/models';
import { Document } from './file';

/** Base shape for all resources to extend. */
export interface Resource {
  id: string;
}

/** Possible states for a track upload, whether video or other such as timed text.
 *
 * NB: PENDING, PROCESSING, READY and ERROR are the actual possible values
 * for the state field on a video record.
 *
 * UPLOADING does not exist as a track state on the backend side, as during
 * upload the model value for the state is still PENDING. However, here
 * on the frontend, they are two different states as far as the user is concerned,
 * especially when it comes to videos which might take a long time to upload.
 *
 * We add it in to make it easier to work with those states. It should not actually be
 * applied on any Video or other track record but will be used as a stand-in in our local
 * track representations and whenever we might need to pass such state information around.
 */
export enum uploadState {
  DELETED = 'deleted',
  INITIALIZED = 'initialized',
  ERROR = 'error',
  PENDING = 'pending',
  PROCESSING = 'processing',
  READY = 'ready',
}

export enum liveState {
  IDLE = 'idle',
  STARTING = 'starting',
  RUNNING = 'running',
  STOPPING = 'stopping',
  STOPPED = 'stopped',
  HARVESTING = 'harvesting',
  HARVESTED = 'harvested',
  ENDED = 'ended',
}

/** Possible modes for a timed text track.
 *
 * We're using modes instead of different objects to represent subtitles, transcripts and closed captions
 * as they're both the same types of files that go through the same pipelines, and have the same kinds
 * of relations to video tracks.
 */
export enum timedTextMode {
  SUBTITLE = 'st',
  TRANSCRIPT = 'ts',
  CLOSED_CAPTIONING = 'cc',
}

export interface PlaylistLite extends Resource {
  title?: string | Nullable<Extract<Playlist, 'title'>>;
  lti_id?: string | Nullable<Extract<Playlist, 'lti_id'>>;
}

export interface Playlist extends Resource {
  consumer_site: Nullable<ConsumerSite>;
  created_by: Nullable<string>;
  created_on: string;
  duplicated_from: Nullable<string>;
  is_portable_to_playlist: boolean;
  is_portable_to_consumer_site: boolean;
  is_public: boolean;
  lti_
...[truncated]...

### src/backend/marsha/settings.py
"""Django settings for marsha project.

Uses django-configurations to manage environments inheritance and the loading of some
config from the environment

"""

# pylint: disable=abstract-class-instantiated,too-many-lines

from datetime import timedelta
import json
import os

from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _

from configurations import Configuration, values
from corsheaders.defaults import default_headers
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from marsha.account.social_pipeline import MARSHA_DEFAULT_AUTH_PIPELINE


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_release():
    """
    Get the current release of the application.

    By release, we mean the release from the version.json file à la Mozilla [1]
    (if any). If this file has not been found, it defaults to "NA".
    [1]
    https://github.com/mozilla-services/Dockerflow/blob/master/docs/version_object.md
    """
    # Try to get the current release from the version.json file generated by the
    # CI during the Docker image build
    try:
        with open(os.path.join(BASE_DIR, "version.json"), encoding="utf8") as version:
            return json.load(version)["version"]
    except FileNotFoundError:
        return "NA"  # Default: not available


class Base(Configuration):
    """Base configuration every configuration (aka environment) should inherit from.

    It depends on an environment variable that SHOULD be defined:
    - DJANGO_SECRET_KEY

    You may also want to override default configuration by setting the following
    environment variables:
    - DJANGO_DEBUG
    """

    DATA_DIR = values.Value(os.path.join("/", "data"))

    # Static files (CSS, JavaScript, Images)
    BASE_STATIC_DIR = os.path.join(BASE_DIR, "static")
    STATICFILES_DIRS = (BASE_STATIC_DIR,)
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"
    # Allow to configure location of static/media files for non-Docker installation
    MEDIA_ROOT = values.Value(os.path.join(str(DATA_DIR), "media"))
    STATIC_ROOT = values.Value(os.path.join(str(DATA_DIR), "static"))
    FILES_ROOT = values.Value(os.path.join(str(DATA_DIR), "files"))

    SECRET_KEY = values.SecretValue()

    DEBUG = values.BooleanValue(False)

    DATABASES = {
        "default": {
            "ENGINE": values.Value(
                "django.db.backends.postgresql",
                environ_name="DATABASE_ENGINE",
                environ_prefix=None,
            ),
            "NAME": values.Value(
                "
...[truncated]...

### docs/adr/0002-videos-languages.md
# 'ADR 0002 - Videos languages'

## Status

Accepted

## Context

We want to think Marsha as accessible from the beginning. At least from
the point of view of the videos, which are the main content available.

We can think about a video as a main content, with many auxiliary
contents.

### Auxiliary contents

#### Audio

We have a main video, with an audio track included. The author could
propose many other audio tracks, as audio files, and in the player the
viewer can change the one to use.

#### Timed texts

In addition to audio tracks, many timed text tracks can be available.

#### Sign language

Some people with disabilities could want a video with the sign language
transcript. For this it can be a video incorporated in the original one,
or an other video displayed on the site.

As sign languages are not the same for every spoken language, there can
be several sign languages videos for a single video.

## Decision

We decided to take all these elements into account right from the
beginning.

So we have a main Django model named `Video`, from an author, with the
link to the main video file, including the default audio track.

For the other audio tracks, we have an `AudioTrack` Django model, with a
`ForeignKey` to the `Video` instance, named `video`, and a `language`
field (with only one audio track for each video+language)

It's the same for timed text tracks, we have a `TimedTextTrack` Django model,
with the same `video` and `language` fields, but with an additional `mode`
field to indicate that this timed text track is either a simple subtitle,
a "[closed
captioning](https://en.wikipedia.org/wiki/Closed_captioning)" ie subtitles
for deaf or hard of hearing viewers, or a transcript. So there can be up to 
3 timed text tracks for each video+language: one for each mode.

And finally, for sign-languages videos, it's the same as for audio
tracks: a Django model named `SignTrack` with the same `video` and
`language` field.

## Consequences

Accessibility is implemented from the start. Even if we decide to hide
some things, the main concepts are here.

### docs/dev.md
# Development

At the time of writing, **Marsha** is developed with **Python** 3.6 for
**Django 2.0**.

## Code quality

We enforce good code by using some linters and auto code formatting tools.

To run all linters at once, run the command:

```bash
make lint
```

You can also run each linter one by one. We have ones for the following
tools:

### Black

We use [Black](https://github.com/ambv/black) to automatically format python
files to produce [pep8](https://www.python.org/dev/peps/pep-0008/) compliant
code.

The best is to [configure your editor to automatically update the files
when saved](https://github.com/ambv/black#editor-integration).

If you want to do this manually, run the command:

```bash
make lint-black
```

And to check if all is correct without actually modifying the files:

```bash
make check-black
```

### Flake8

In addition to section-black auto-formatting, we pass the code through
[flake8](http://flake8.pycqa.org/en/latest/) to check for a lot of
rules. In addition to the default `flake8` rules, we use these plugins:

-   [flake8-bugbear](https://pypi.org/project/flake8-bugbear/) to find
    likely bugs and design problems.
-   [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/)
    to helps write better list/set/dict comprehensions.
-   [flake8-imports](https://pypi.org/project/flake8-imports/) to check
    imports order via `isort`.
-   [flake8-mypy](https://pypi.org/project/flake8-mypy/) to check typing
    inconsistencies via `mypy` (see section-mypy).
-   [flake8-docstrings](https://pypi.org/project/flake8-docstrings/) to
    check docstrings (see section-docstrings)

To check your code, run the command:

```bash
make lint-flake8
```

### Pylint


To enforce even more rules than the ones provided by section-flake8, we
use [pylint](https://www.pylint.org/) (with the help of
[pylint-django](https://pypi.org/project/pylint-django/)).

`pylint` may report some violations not found by `flake8`, and
vice-versa. More often, both will report the same ones.

To check your code, run the command:

```bash
make lint-pylint
```


## Docstrings

section-flake8 is configured to enforce docstrings rule defined in the
[pep 257](https://www.python.org/dev/peps/pep-0257/)

In addition, we document function arguments, return types, etc... using
the ["NumPy" style
documentation](https://numpydoc.readthedocs.io/en/latest/format.html),
which will be validated by section-flake8.

## Django

### Opinionated choices

We made the opinionated choice of following [this document, "Tips for
Building High-Quality Django Apps at
Scale"](h
...[truncated]...

### docker-compose.yml
services:
  db:
    image: postgres:16.4
    env_file: env.d/db
    volumes:
      - ./docker/files/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d
    ports:
      - "5452:5432"

  # We use our production image as a basis for the development image, hence, we
  # define a "base" service upon which the "app" service depends to force
  # marsha:latest build.
  base:
    build: .
    image: marsha:latest
    # Override the default command so that the container exists immediately when
    # it is run (no server).
    command: echo "I should exit now. Bye."

  app:
    build:
      context: .
      dockerfile: ./docker/images/dev/Dockerfile
      args:
        DOCKER_USER: ${DOCKER_USER:-1000}
    image: marsha:dev
    env_file:
      - env.d/db
      - env.d/${ENV_FILE:-development}
    # Override production container command that runs gunicorn in favor of the
    # django development server
    command: >
      python manage.py runserver 0.0.0.0:8000
    ports:
      - "8060:8000"
    volumes:
      - .:/app
      - ./data/static:/data/static
      - ./data/media:/data/media
      - ./data/files:/data/files
    depends_on:
      - "base"
      - "db"
      - "redis"
      - "mailcatcher"
    stdin_open: true
    tty: true

  celery:
    image: marsha:dev
    env_file:
      - env.d/db
      - env.d/${ENV_FILE:-development}
    command: >
      python -m celery -A marsha.celery_app worker -l info
    volumes:
      - .:/app
      - ./data/static:/data/static
      - ./data/media:/data/media
      - ./data/files:/data/files
    depends_on:
      - "base"
      - "db"
      - "redis"
      - "mailcatcher"
    stdin_open: true
    tty: true

  peertube-runner:
    image: fundocker/peertube-runner:latest-whisper_ctranslate2
    env_file:
      - env.d/peertube_runner

  webtorrent:
    image: node:20
    environment:
      - APP_PORT=3000
      - JWT_SIGNING_KEY=ThisIsAnExampleKeyForDevPurposeOnly
    ports:
      - "8080:3000"
    working_dir: /app
    command: ["yarn", "run", "dev"]
    volumes:
      - ./src/webtorrent:/app

  redis:
    image: redis:5

  e2e:
    build:
      context: .
      dockerfile: ./docker/images/e2e/Dockerfile
    image: marsha:e2e
    env_file:
      - env.d/db
      - env.d/${ENV_FILE:-development}
    ports:
      - "8070:8000"
    volumes:
      - .:/app
      - ./data/static:/data/static
      - ./src/backend/marsha/e2e/media:/data/media/e2e
    depends_on:
      - "app"
    stdin_open: true
    tty: true

  crowdin:
    image: crowdin/cli:3.7.10
    volumes:
      - ".:/app"
    env_file:
      - env.d/development
    wo
...[truncated]...

### docs/adr/0001-actors.md
# 'ADR 0001 - Actors'


## Status

Accepted

## Context

There are different kinds of actors that need to interact with Marsha.

First we have the people managing a Marsha instance.

Then we have people linking their own website (this website is a
"consumer site") to a Marsha instance, to host videos.

These consumer sites can host many publishers. We call these
"organizations". And these organizations have managers that can
administrate some things about authors, video sharing between authors...

Next we have the video authors, belonging to the organizations.

And finally we have the users coming to watch videos.

## Decision

Let's separate those 5 actors / roles:

### "staff"

#### Purpose

To manage a Marsha instance

#### Implementation

These are simply instances of the Django `User` model, with the flag
`is_staff` set to `True`.

### "admins"

#### Purpose

To manage the link between a consumer site and a Marsha instance, and
the organizations allowed to access this consumer site on the instance.

#### Implementation

To represent a consumer site on a Marsha instance, we have a
`ConsumerSite` Django model. With a `ManyToMany` link to the `User`
model, named `admins` (not a single admin, to avoid having no admin if
the only one existing is not available anymore)).

### "managers"

#### Purpose

To manage the authors in the organization (an organization could be
present on many consumer sites). To allow videos to be private to
authors or public for all authors. And create courses.

#### Implementation

To represent an organization on a Marsha instance, we have an
`Organization` Django model. With a `ManyToMany` link to the `User`
model, named `managers`.

### "authors"

#### Purpose

To post videos on a Marsha instance to be used on a consumer site.

#### Implementation

An author is simply an instance of the `User` model, but has a link to
an `Organization` via a `ManyToMany` link, named `organizations` (we can
imagine an author working for many organizations).

### "viewers"

#### Purpose

To watch videos hosted on a Marsha instance.

#### Implementation

For the viewers we don't need to save anything in the database, so there
is no instances of the `User` Django model for them.

Each time a user does an action to view a video, they access it via a
url containing a unique token, with a limited life span. It's this token
that grant them access to the video.

This is not the scope of this document to address token generations.

To store the user preferences regarding languages, video resolution,
etc, it can simply be done via a cookie.

## Consequen
...[truncated]...

### src/backend/marsha/core/management/commands/clean_aws_elemental_stack.py
"""Check every existing medialive channel and check if the related video is still usable."""

from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from marsha.core.defaults import DELETED, ENDED
from marsha.core.models import Video
from marsha.core.utils.medialive_utils import (
    delete_medialive_stack,
    list_medialive_channels,
)
from marsha.core.utils.time_utils import to_datetime


def generate_expired_date():
    """Generate a datetime object NB_DAYS_BEFORE_DELETING_AWS_ELEMENTAL_STACK days in the past."""
    return timezone.now() - timedelta(
        days=settings.NB_DAYS_BEFORE_DELETING_AWS_ELEMENTAL_STACK
    )


class Command(BaseCommand):
    """
    Once a live started, all AWS elemental stack are created. Once stopped, the
    instructor must do an action. Restart it and/or convert it in VOD. If
    nothing is done, the AWS element resources are leaved unused and use the quota
    we have on our AWS account.
    These unused resources must be removed after several days of inactivity and the video
    move in 
...[truncated]...