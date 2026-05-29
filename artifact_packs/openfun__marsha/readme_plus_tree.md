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