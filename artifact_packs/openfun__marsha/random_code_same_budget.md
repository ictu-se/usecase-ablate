# Deterministic random code snippets
### src/frontend/packages/lib_video/src/components/common/VideoWidgetProvider/widgets/UploadTranscripts/index.tsx
import { FoldableItem, timedTextMode } from 'lib-components';
import React from 'react';
import { defineMessages, useIntl } from 'react-intl';

import { LocalizedTimedTextTrackUpload } from '../../LocalizedTimedTextTrackUpload';

const messages = defineMessages({
  info: {
    defaultMessage: `This widget allows you upload transcripts for the video.
    Accepted formats : MicroDVD SUB (.sub) - SubRip (.srt) - SubViewer (.sbv)
      - WebVTT (.vtt) - SubStation Alpha (.ssa and .ass) - SAMI (.smi) aka Synchronized 
      Accessible Media Interchange
      - LRC (.lrc) aka LyRiCs - JSON (.json)`,
    description: 'Info of the widget used for uploading transcripts.',
    id: 'components.UploadTranscripts.info',
  },
  title: {
    defaultMessage: 'Transcripts',
    description: 'Title of the widget used for uploading transcripts.',
    id: 'components.UploadTranscripts.title',
  },
});

export const UploadTranscripts = () => {
  const intl = useIntl();

  return (
    <FoldableItem
      infoText={intl.formatMessage(messages.info)}
      initialOpenValue
      title={intl.formatMessage(messages.title)}
    >
      <LocalizedTimedTextTrackUpload
        timedTextModeWidget={timedTextMode.TRANSCRIPT}
      />
    </FoldableItem>
  );
};

### src/frontend/apps/standalone_site/src/features/Playlist/features/UpdatePlaylist/components/AddUserAccessButton.tsx
import { Button } from '@openfun/cunningham-react';
import { Modal } from 'lib-components';
import { Fragment, useState } from 'react';
import { defineMessages, useIntl } from 'react-intl';

import { AddUserAccessForm } from './AddUserAccessForm';

const messages = defineMessages({
  buttonLabel: {
    defaultMessage: 'Add people',
    description: 'Add member to playlist button label.',
    id: 'features.Playlist.features.UpdatePlaylist.components.AddUserAccessButton.buttonLabel',
  },
});

interface AddUserAccessButtonProps {
  playlistId: string;
  excludedUsers?: string[];
}

export const AddUserAccessButton = ({
  playlistId,
  excludedUsers,
}: AddUserAccessButtonProps) => {
  const intl = useIntl();
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <Fragment>
      <Modal
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
        }}
      >
        <AddUserAccessForm
          playlistId={playlistId}
          excludedUsers={excludedUsers}
          onUserAdded={() => {
            setIsModalOpen(false);
          }}
        />
      </Modal>

      <Button
        aria-label={intl.formatMessage(messages.buttonLabel)}
        onClick={() => {
          setIsModalOpen(true);
        }}
      >
        {intl.formatMessage(messages.buttonLabel)}
      </Button>
    </Fragment>
  );
};

### src/frontend/packages/lib_common/src/cunningham/cunningham-tokens.ts
export const tokens = {
  themes: {
    default: {
      theme: {
        colors: {
          'secondary-text': '#555F6B',
          'secondary-100': '#F2F7FC',
          'secondary-200': '#EBF3FA',
          'secondary-300': '#E2EEF8',
          'secondary-400': '#DDEAF7',
          'secondary-500': '#D4E5F5',
          'secondary-600': '#C1D0DF',
          'secondary-700': '#97A3AE',
          'secondary-800': '#757E87',
          'secondary-900': '#596067',
          'info-text': '#FFFFFF',
          'info-100': '#EBF2FC',
          'info-200': '#8CB5EA',
          'info-300': '#5894E1',
          'info-400': '#377FDB',
          'info-500': '#055FD2',
          'info-600': '#0556BF',
          'info-700': '#044395',
          'info-800': '#033474',
          'info-900': '#022858',
          'greyscale-100': '#FAFAFB',
          'greyscale-200': '#F3F4F4',
          'greyscale-300': '#E7E8EA',
          'greyscale-400': '#C2C6CA',
          'greyscale-500': '#9EA3AA',
          'greyscale-600': '#79818A',
          'greyscale-700': '#555F6B',
          'greyscale-800': '#303C4B',
          'greyscale-900': '#0C1A2B',
          'greyscale-000': '#FFFFFF',
          'primary-100': '#EDF5FA',
          'primary-200': '#8CB5EA',
          'primary-300': '#5894E1',
          'primary-400': '#377FDB',
          'primary-500': '#055FD2',
          'primary-600': '#0556BF',
          'primary-700': '#044395',
          'primary-800': '#033474',
          'primary-900': '#022858',
          'success-100': '#EFFCD3',
          'success-200': '#DBFAA9',
          'success-300': '#BEF27C',
          'success-400': '#A0E659',
          'success-500': '#76D628',
          'success-600': '#5AB81D',
          'success-700': '#419A14',
          'success-800': '#2C7C0C',
          'success-900': '#1D6607',
          'warning-100': '#FFF8CD',
          'warning-200': '#FFEF9B',
          'warning-300': '#FFE469',
          'warning-400': '#FFDA43',
          'warning-500': '#FFC805',
          'warning-600': '#DBA603',
          'warning-700': '#B78702',
          'warning-800': '#936901',
          'warning-900': '#7A5400',
          'danger-100': '#F4B0B0',
          'danger-200': '#EE8A8A',
          'danger-300': '#E65454',
          'danger-400': '#E13333',
          'danger-500': '#DA0000',
          'danger-600': '#C60000',
          'danger-700': '#9B0000',
          'danger-800': '#780000',
          'danger-900': '#5C0000',
          'primary-text': '#FFFFFF',
          'success-text': '#FFFFFF',
          'warning-text': '#FFFFFF',
          'danger-text': '
...[truncated]...

### src/frontend/packages/lib_components/src/common/ProgressionBar/index.tsx
import { Meter } from 'grommet';

import { Box } from '../Box';
import { Text } from '../Text';

interface ProgressionBarProps {
  progressPercentage: number;
}

export const ProgressionBar = ({ progressPercentage }: ProgressionBarProps) => {
  return (
    <Box direction="row" style={{ position: 'relative' }}>
      <Meter round size="xlarge" type="bar" value={progressPercentage} />
      <Text
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
        }}
        color={progressPercentage < 48 ? undefined : 'white'}
        size="small"
      >
        {progressPercentage} %
      </Text>
    </Box>
  );
};

### src/backend/marsha/core/utils/api_utils.py
"""Utils used by the api module."""

from functools import cache
import hashlib
import hmac

import django.apps
from django.conf import settings
from django.utils.crypto import salted_hmac


def validate_signature(signature, message):
    """Check if the provided signature is valid against any secret in our list.

    We need to do this to support 2 or more versions of our infrastructure at the same time.
    It then enables us to do updates and change the secret without incurring downtime.

    Parameters
    ----------
    signature: string
        The signature to validate.

    message: string
        The signed message to compare with the signature.

    Return
    ------
    Boolean
        Return true if the signature is valid. False otherwise.
    """
    return any(
        signature == generate_hash(secret, message)
        for secret in settings.UPDATE_STATE_SHARED_SECRETS
    )


def generate_hash(secret, message):
    """Generate a hash given a secret and a message.

    Parameters
    ----------
    secret: string
        The secret to use.

    message: string
        The message to hash.

    Return
    ------
    String
       Return a computed hash
    """
    return hmac.new(
        secret.encode("utf-8"), msg=message, digestmod=hashlib.sha256
    ).hexdigest()


def generate_salted_hmac(secret, key):
    """Generate a salted_hmac with secret and key"""
    return salted_hmac(secret, key, algorithm="sha256").hexdigest()


@cache
def get_uploadable_models_s3_mapping():
    """
    Generates a map between the S3 key model identifier and Django models.
    Used in the update_state API called when the lamda "convert" notify us it has done its job

    This must always be used after all applications are loaded
    (`django.apps.apps.get_models` takes care of that assertion).

    Return
    ------
    dict
        The returned dict looks like

        ```
        {
            "document": marsha.core.models.Document,
            "sharedlivemedia": marsha.core.models.SharedLiveMedia,
            "thumbnail": marsha.core.models.Thumbnail,
            "timedtexttrack": marsha.core.models.TimedTextTrack,
            "video": marsha.core.models.Video,
        }
        ```
    """
    all_models = django.apps.apps.get_models()
    return {
        model.S3_IDENTIFIER: model
        for model in all_models
        if getattr(model, "S3_IDENTIFIER", None) is not None
    }

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

### src/frontend/packages/lib_markdown/src/utils/escapeMarkdown.spec.ts
import { escapeMarkdown } from './escapeMarkdown';

describe('escapeMarkdown', () => {
  it('escapes asterisks', () => {
    expect(escapeMarkdown('some text with *')).toEqual('some text with \\*');
  });
  it('escapes hashtag', () => {
    expect(escapeMarkdown('some text with #')).toEqual('some text with \\#');
  });
  it('escapes slashes', () => {
    expect(escapeMarkdown('some text with /')).toEqual('some text with \\/');
  });
  it('escapes opening parenthesis', () => {
    expect(escapeMarkdown('some text with (')).toEqual('some text with \\(');
  });
  it('escapes closing parenthesis', () => {
    expect(escapeMarkdown('some text with )')).toEqual('some text with \\)');
  });
  it('escapes opening square bracket', () => {
    expect(escapeMarkdown('some text with [')).toEqual('some text with \\[');
  });
  it('escapes closing square bracket', () => {
    expect(escapeMarkdown('some text with ]')).toEqual('some text with \\]');
  });
  it('escapes opening angle bracket', () => {
    expect(escapeMarkdown('some text with <')).toEqual('some text with \\<');
  });
  it('escapes closing angle bracket', () => {
    expect(escapeMarkdown('some text with >')).toEqual('some text with \\>');
  });
  it('escapes underscore', () => {
    expect(escapeMarkdown('some text with _')).toEqual('some text with \\_');
  });
});

### src/frontend/apps/standalone_site/src/features/HomePage/index.tsx
export { default as HomePage } from './components/HomePage';

### src/frontend/packages/lib_markdown/src/components/MarkdownEditor/route.ts
/**
 * Route for the `<MarkdownEditor />` component.
 */
export const MARKDOWN_EDITOR_ROUTE = () => '/editor';

### src/frontend/apps/standalone_site/src/features/Menu/components/Menu.spec.tsx
import { fireEvent, screen } from '@testing-library/react';
import { ResponsiveContext } from 'grommet';
import { render } from 'lib-tests';
import { Fragment } from 'react';

import { featureContentLoader } from 'features/Contents';
import { getFullThemeExtend } from 'styles/theme.extend';

import { useMenu } from '../store/menuStore';

import Burger from './Burger/Burger';
import Menu from './Menu';

const initialStoreState = useMenu.getState();

describe('<Menu />', () => {
  beforeEach(() => {
    useMenu.setState(initialStoreState, true);
  });

  test('renders Menu', () => {
    featureContentLoader([]);

    render(<Menu />);
    expect(
      screen.getByRole('menuitem', { name: /My playlists/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole('menuitem', { name: /My Contents/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole('menuitem', { name: /Classrooms/i }),
    ).toBeInTheDocument();
  });

  test('menu opening state', () => {
    render(
      <Fragment>
        <Burger />
        <Menu />
      </Fragment>,
    );

    const menu = screen.getByRole('menu');
    expect(menu).not.toHaveStyle('margin-left: -18.75rem;');
    fireEvent.click(screen.getByRole('button'));
    expect(menu).toHaveStyle('margin-left: -18.75rem;');
  });

  test('menu responsive small screen', () => {
    render(
      <ResponsiveContext.Provider value="small">
        <Menu />
      </ResponsiveContext.Provider>,
      {
        grommetOptions: {
          theme: getFullThemeExtend(),
        },
      },
    );

    const menu = screen.getByRole('menu');
    expect(menu).toHaveStyle('margin-left: -18.75rem;');
    expect(menu).toHaveStyle('position: fixed;');
  });
});

### src/backend/marsha/core/tests/management_commands/test_send_vod_convert_reminders.py
"""Test send_vod_convert_reminders command."""

from datetime import datetime, timedelta, timezone
from io import StringIO
from unittest import mock

from django.core import mail
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone as django_timezone

from marsha.core.defaults import HARVESTED, IDLE, JITSI, RUNNING, STOPPED
from marsha.core.factories import VideoFactory
from marsha.core.management.commands import send_vod_convert_reminders
from marsha.core.utils.time_utils import to_timestamp


# pylint: disable=too-many-locals


class SendVodConvertRemindersCommandTest(TestCase):
    """Test send_vod_convert_reminders command."""

    maxDiff = None

    def test_send_vod_convert_reminders(self):
        """Test send_vod_convert_reminders command."""
        expiration_reminder_date = datetime(2022, 11, 1, 15, 00, tzinfo=timezone.utc)

        start = django_timezone.now() - timedelta(minutes=20)
        stop = start + timedelta(minutes=10)

        # first live not started yet, should not be reminded.
        live1 = VideoFactory(
            live_state=IDLE,
            live_type=JITSI,
            starting_at=expiration_reminder_date - timedelta(days=1),
            title="live one",
            live_info=None,  # live has never been started
            recording_slices=[
                {"start": to_timestamp(start), "stop": to_timestamp(stop)}
            ],
        )
        # medialive channels not in the same AWS_BASE_NAME environment
        medialive_channel_1 = {
            "Id": "111111",
            "Name": f"foo_{live1.id}_1667490961",
            "Tags": {"environment": "foo"},
            "State": "IDLE",
        }

        # Second live, started but still running, should not be reminded
        live2 = VideoFactory(
            live_state=RUNNING,
            live_type=JITSI,
            starting_at=expiration_reminder_date - timedelta(days=1),
            title="live two",
            live_info={},
            recording_slices=[
                {"start": to_timestamp(start), "stop": to_timestamp(stop)}
            ],
        )
        medialive_channel_2 = {
            "Id": "2222222",
            "Name": f"test_{live2.id}_1667490961",
            "Tags": {"environment": "test"},
            "State": "RUNNING",
        }

        # Third live, started and stopped soon. Should not be reminded
        live3 = VideoFactory(
            live_state=STOPPED,
            live_type=JITSI,
            starting_at=expiration_reminder_date + timedelta(days=1),
            title="live
...[truncated]...

### src/frontend/packages/lib_components/src/common/SVGIcons/StopSVG.tsx
import React from 'react';

import SVGIcon, { SvgProps } from '.';

export const StopSVG = (svgProps: SvgProps) => {
  return (
    <SVGIcon viewBox={{ x: 0, y: 0, width: 18, height: 18 }} {...svgProps}>
      <g fill="none" fillRule="evenodd" stroke="none" strokeWidth="1">
        <path
          transform="translate(3 3)"
          fillRule="nonzero"
          d="M2 0h8c1.1 0 2 .9 2 2v8c0 1.1-.9 2-2 2H2c-1.1 0-2-.9-2-2V2C0 .9.9 0 2 0z"
        />
      </g>
    </SVGIcon>
  );
};

### src/backend/marsha/core/tests/management_commands/test_sync_medialive_video.py
"""Test clean_aws_elemental_stack command."""

from datetime import datetime, timezone
from io import StringIO
from unittest import mock
import uuid

from django.core.management import call_command
from django.test import TestCase

from botocore.stub import Stubber

from marsha.core.defaults import IDLE, JITSI, RUNNING, STARTING, STOPPED, STOPPING
from marsha.core.factories import VideoFactory
from marsha.core.management.commands import sync_medialive_video
from marsha.core.utils import medialive_utils, time_utils


class TestSyncMedialiveVideoCommandTest(TestCase):
    """Test sync_medialive_video command."""

    maxDiff = None

    def createLive(self, live_id, state):
        """Create a live with specified id and state."""
        return VideoFactory(
            id=live_id,
            live_state=state,
            live_type=JITSI,
            starting_at=datetime(2022, 11, 4, 13, 25, tzinfo=timezone.utc),
            title="live two",
            live_info={
                "started_at": time_utils.to_timestamp(
                    datetime(2022, 10, 14, 13, 25, tzinfo=timezone.utc)
                ),
                "medialive": {
                    "channel": {
                        "arn": "arn:aws:medialive:eu-west-1:xxx:channel:2222222",
                        "id": "2222222",
                    },
                    "input": {
                        "endpoints": [
                            f"rtmp://x.x.x.x:1935/{live_id}_1667490961-primary",
                            f"rtmp://x.x.x.x:1935/{live_id}_1667490961-secondary",
                        ],
                        "id": "2222222",
                    },
                },
                "mediapackage": {
                    "channel": {"id": f"test_{live_id}_1667490961"},
                    "endpoints": {
                        "hls": {
                            "id": f"test_{live_id}_1667490961_hls",
                            "url": (
                                "https://xxx.mediapackage.eu-west-1.amazonaws.com/out/v1/xxx/"
                                f"test_{live_id}_1667490961_hls.m3u8",
                            ),
                        }
                    },
                },
            },
        )

    def test_sync_not_used_state_medialive_on_running_video(self):
        """Not used medialive states should do nothing."""
        # running lives.
        live1_id = uuid.uuid4()
        live1 = self.createLive(live1_id, RUNNING)
        live2_id = uuid.uuid4()
        live2 = self.createLive(live2_id, RUNNING)
        live3_id = uuid.uuid4()
    
...[truncated]...

### src/frontend/packages/lib_video/src/api/usePairingVideo/index.spec.tsx
import { renderHook, waitFor } from '@testing-library/react';
import fetchMock from 'fetch-mock';
import { useJwt } from 'lib-components';
import { videoMockFactory } from 'lib-components/tests';
import { WrapperReactQuery } from 'lib-tests';

import { usePairingVideo } from '.';

jest.mock('lib-components', () => ({
  ...jest.requireActual('lib-components'),
  report: jest.fn(),
}));

describe('usePairingingVideo', () => {
  beforeEach(() => {
    useJwt.getState().setJwt('some token');
  });

  afterEach(() => {
    fetchMock.restore();
    jest.resetAllMocks();
  });

  it('updates the resource', async () => {
    const video = videoMockFactory();
    fetchMock.get(`/api/videos/${video.id}/pairing-secret/`, {
      secret: '12345',
    });

    const { result } = renderHook(() => usePairingVideo(video.id), {
      wrapper: WrapperReactQuery,
    });
    result.current.mutate();
    await waitFor(() => {
      expect(result.current.isSuccess).toBeTruthy();
    });

    expect(fetchMock.lastCall()![0]).toEqual(
      `/api/videos/${video.id}/pairing-secret/`,
    );
    expect(fetchMock.lastCall()![1]).toEqual({
      headers: {
        Authorization: 'Bearer some token',
        'Content-Type': 'application/json',
        'Accept-Language': 'en',
      },
      method: 'GET',
    });
    expect(result.current.data).toEqual({ secret: '12345' });
    expect(result.current.status).toEqual('success');
  });

  it('fails to update the resource', async () => {
    const video = videoMockFactory();
    fetchMock.get(`/api/videos/${video.id}/pairing-secret/`, 400);

    const { result } = renderHook(() => usePairingVideo(video.id), {
      wrapper: WrapperReactQuery,
    });
    result.current.mutate();
    await waitFor(() => {
      expect(result.current.isError).toBeTruthy();
    });

    expect(fetchMock.lastCall()![0]).toEqual(
      `/api/videos/${video.id}/pairing-secret/`,
    );
    expect(fetchMock.lastCall()![1]).toEqual({
      headers: {
        Authorization: 'Bearer some token',
        'Content-Type': 'application/json',
        'Accept-Language': 'en',
      },
      method: 'GET',
    });
    expect(result.current.data).toEqual(undefined);
    expect(result.current.status).toEqual('error');
  });
});

### src/frontend/packages/lib_video/src/api/createThumbnail/index.spec.ts
import fetchMock from 'fetch-mock';
import { useJwt } from 'lib-components';

import { createThumbnail } from '.';

describe('sideEffects/createThumbnail', () => {
  beforeEach(() => {
    useJwt.setState({
      jwt: 'token',
    });
  });

  afterEach(() => fetchMock.restore());

  it('creates a new thumbnail and return it', async () => {
    fetchMock.mock('/api/videos/video-id/thumbnails/', {
      id: '42',
      ready_to_display: false,
      urls: null,
    });

    const body = {
      size: 10,
      video: 'video-id',
    };
    const thumbnail = await createThumbnail(body);
    const fetchArgs = fetchMock.lastCall()![1]!;

    expect(thumbnail).toEqual({
      id: '42',
      ready_to_display: false,
      urls: null,
    });
    expect(fetchArgs.body).toEqual(
      JSON.stringify({
        size: 10,
      }),
    );
    expect(fetchArgs.headers).toEqual({
      Authorization: 'Bearer token',
      'Content-Type': 'application/json',
      'Accept-Language': 'en',
    });
    expect(fetchArgs.method).toEqual('POST');
  });

  it('throws when it fails to create the thumbnail (request failure)', async () => {
    fetchMock.mock(
      '/api/videos/video-id/thumbnails/',
      Promise.reject(new Error('Failed to perform the request')),
    );

    const body = {
      size: 10,
      video: 'video-id',
    };
    await expect(createThumbnail(body)).rejects.toThrow(
      'Failed to perform the request',
    );
  });

  it('throws when it fails to create the thumbnail (API error)', async () => {
    fetchMock.mock('/api/videos/video-id/thumbnails/', 400);

    const body = {
      size: 10,
      video: 'video-id',
    };
    await expect(createThumbnail(body)).rejects.toThrow();
  });
});

### src/backend/marsha/core/tests/test_sentry.py
"""Test for sentry module"""

from django.test import TestCase, override_settings

from marsha.core.sentry import filter_transactions


class SentryFilteringTestCase(TestCase):
    """Test about sentry filtering"""

    @override_settings(SENTRY_IGNORE_HEALTH_CHECKS=True)
    def test_filtering_without_request_in_event(self):
        """Without request parameter in the event, the event should be return directly"""

        event = {"foo": "bar"}

        filtered_event = filter_transactions(event, None)

        self.assertEqual(event, filtered_event)

    @override_settings(SENTRY_IGNORE_HEALTH_CHECKS=True)
    def test_filtering_without_url_in_the_request(self):
        """Without url in the request, the event should be return directly"""

        event = {
            "foo": "bar",
            "request": {
                "query_string": "query=foobar&page=2",
            },
        }

        filtered_event = filter_transactions(event, None)

        self.assertEqual(event, filtered_event)

    @override_settings(SENTRY_IGNORE_HEALTH_CHECKS=False)
    def test_filtering_setting_disabled_should_return_the_event(self):
        """When the SENTRY_IGNORE_HEALTH_CHECKS is set to False, the event should be return"""

        event = {
            "foo": "bar",
            "request": {
                "query_string": "query=foobar&page=2",
                "url": "https://absolute.uri/__heartbeat__/",
            },
        }

        filtered_event = filter_transactions(event, None)

        self.assertEqual(event, filtered_event)

    @override_settings(SENTRY_IGNORE_HEALTH_CHECKS=True)
    def test_filtering_url_matching_dockerflow_heartbeat_should_return_none(self):
        """When a request url matches a dockerflow heartbeat pattern, should return None"""

        event = {
            "foo": "bar",
            "request": {
                "query_string": "query=foobar&page=2",
                "url": "https://absolute.uri/__heartbeat__/",
            },
        }

        filtered_event = filter_transactions(event, None)

        self.assertIsNone(filtered_event)

    @override_settings(SENTRY_IGNORE_HEALTH_CHECKS=True)
    def test_filtering_url_matching_dockerflow_lbheartbeat_should_return_none(self):
        """When a request url matches a dockerflow lbheartbeat pattern, should return None"""

        event = {
            "foo": "bar",
            "request": {
                "query_string": "query=foobar&page=2",
                "url": "https://absolute.uri/__lbheartbeat__/",
            },
        }

        filtered_event = filter_transactions(ev
...[truncated]...

### src/frontend/packages/lib_components/src/types/XAPI.ts
import { Nullable } from 'lib-common';

export enum XapiResourceType {
  DOCUMENT = 'document',
  VIDEO = 'video',
}

export interface DataPayload {
  context?: {
    extensions: {
      [key: string]: string | boolean | number | undefined;
    };
  };
  result?: {
    extensions: {
      [key: string]: string | boolean | number | undefined;
    };
  };
  verb: {
    id: string;
    display: {
      [key: string]: string;
    };
  };
}

export interface CompletedDataPlayload extends DataPayload {
  result?: {
    extensions: {
      [key: string]: string | boolean | number | undefined;
    };
    completion: boolean;
    duration: Nullable<string>;
  };
}

export enum ContextExtensionsDefinition {
  ccSubtitleEnabled = 'https://w3id.org/xapi/video/extensions/cc-subtitle-enabled',
  ccSubtitleLanguage = 'https://w3id.org/xapi/video/extensions/cc-subtitle-lang',
  completionTreshold = 'https://w3id.org/xapi/video/extensions/completion-threshold',
  frameRate = 'https://w3id.org/xapi/video/extensions/frame-rate',
  fullScreen = 'https://w3id.org/xapi/video/extensions/full-screen',
  length = 'https://w3id.org/xapi/video/extensions/length',
  quality = 'https://w3id.org/xapi/video/extensions/quality',
  screenSize = 'https://w3id.org/xapi/video/extensions/screen-size',
  sessionId = 'https://w3id.org/xapi/video/extensions/session-id',
  speed = 'https://w3id.org/xapi/video/extensions/speed',
  track = 'https://w3id.org/xapi/video/extensions/track',
  userAgent = 'https://w3id.org/xapi/video/extensions/user-agent',
  videoPlaybackSize = 'https://w3id.org/xapi/video/extensions/video-playback-size',
  volume = 'https://w3id.org/xapi/video/extensions/volume',
}

export enum ContextDocumentExtensionsDefinition {
  sessionId = 'https://w3id.org/xapi/cmi5/context/extensions/sessionid',
}

export enum ResultExtensionsDefinition {
  playedSegment = 'https://w3id.org/xapi/video/extensions/played-segments',
  progress = 'https://w3id.org/xapi/video/extensions/progress',
  time = 'https://w3id.org/xapi/video/extensions/time',
  timeFrom = 'https://w3id.org/xapi/video/extensions/time-from',
  timeTo = 'https://w3id.org/xapi/video/extensions/time-to',
}

export enum VerbDefinition {
  completed = 'http://adlnet.gov/expapi/verbs/completed',
  downloaded = 'http://id.tincanapi.com/verb/downloaded',
  initialized = 'http://adlnet.gov/expapi/verbs/initialized',
  interacted = 'http://adlnet.gov/expapi/verbs/interacted',
  paused = 'https://w3id.org/xapi/video/verbs/paused',
  played = 'https://w3id.org/xapi/video/verbs/played',
  seeked = 'https://w3id.org/xapi/video/verbs/se
...[truncated]...

### src/frontend/packages/lib_video/src/api/useTimedTextMetadata/index.ts
import { UseQueryOptions, useQuery } from '@tanstack/react-query';
import { FetchResponseError, metadata } from 'lib-components';

import { TimedTextMetadata } from '@lib-video/types/metadata';

type UseTimedTextMetadataError = FetchResponseError<TimedTextMetadata>;
export const useTimedTextMetadata = (
  videoId: string,
  locale?: string,
  queryConfig?: UseQueryOptions<
    TimedTextMetadata,
    UseTimedTextMetadataError,
    TimedTextMetadata,
    string[]
  >,
) => {
  const key = [`videos/${videoId}/timedtexttracks`, locale || 'undefined'];
  return useQuery<
    TimedTextMetadata,
    UseTimedTextMetadataError,
    TimedTextMetadata,
    string[]
  >({
    queryKey: key,
    queryFn: metadata,
    refetchInterval: false,
    refetchIntervalInBackground: false,
    refetchOnWindowFocus: false,
    cacheTime: Infinity,
    staleTime: Infinity,
    ...queryConfig,
  });
};

### src/backend/marsha/core/tests/api/thumbnails/test_upload_ended.py
"""Tests for the thumbnail upload ended API of the Marsha project."""

from unittest import mock

from django.test import TestCase

from marsha.core import factories, models
from marsha.core.defaults import PEERTUBE_PIPELINE
from marsha.core.simple_jwt.factories import (
    InstructorOrAdminLtiTokenFactory,
    StudentLtiTokenFactory,
    UserAccessTokenFactory,
)


class ThumbnailUploadEndedAPITest(TestCase):
    """Test the "upload-ended" API of the thumbnail object."""

    maxDiff = None

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.some_organization = factories.OrganizationFactory()
        cls.some_video = factories.VideoFactory(
            playlist__organization=cls.some_organization,
            transcode_pipeline=PEERTUBE_PIPELINE,
        )
        cls.some_thumbnail = factories.ThumbnailFactory(
            video=cls.some_video,
        )

    def assert_user_cannot_end_an_upload(self, video, thumbnail, token):
        """Assert the user cannot end an upload."""

        response = self.client.post(
            f"/api/videos/{video.pk}/thumbnails/{thumbnail.pk}/upload-ended/",
            HTTP_AUTHORIZATION=f"Bearer {token}",
        )

        self.assertEqual(response.status_code, 403)

    def assert_user_can_end_an_upload(self, video, thumbnail, token):
        """Assert the user can end an upload."""
        with mock.patch(
            "marsha.core.api.thumbnail.resize_thumbnails"
        ) as mock_resize_thumbnails:
            response = self.client.post(
                f"/api/videos/{video.id}/thumbnails/{thumbnail.pk}/upload-ended/",
                {
                    "file_key": f"tmp/{video.pk}/thumbnail/4564565456",
                },
                HTTP_AUTHORIZATION=f"Bearer {token}",
            )

            mock_resize_thumbnails.delay.assert_called_once_with(
                str(thumbnail.pk), "4564565456"
            )

        self.assertEqual(response.status_code, 200)

    def test_end_upload_by_anonymous_user(self):
        """Anonymous users cannot end an upload."""
        response = self.client.post(
            f"/api/videos/{self.some_video.pk}/"
            f"thumbnails/{self.some_thumbnail.pk}/upload-ended/"
        )

        self.assertEqual(response.status_code, 401)

    def test_end_upload_by_random_user(self):
        """Authenticated user without access cannot end an upload."""
        user = factories.UserFactory()

        jwt_token = UserAccessTokenFactory(user=user)
        self.assert_user_cannot_end_an_upload(
            self.some_video, self.some
...[truncated]...

### src/backend/marsha/bbb/tests/test_delete_outdated_classrooms.py
"""Test delete_outdated_classrooms command."""

from datetime import date, datetime, timezone as baseTimezone
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from marsha.bbb.factories import ClassroomFactory
from marsha.bbb.models import Classroom


class DeleteOutdatedClassroomsTestCase(TestCase):
    """
    Test case for the delete_outdated_classrooms command.
    """

    def setUp(self):
        """
        Set up the test case with classrooms.
        """

        self.classroom_1 = ClassroomFactory(
            retention_date=date(2022, 1, 1),
        )
        self.classroom_2 = ClassroomFactory(
            retention_date=date(2021, 1, 1),
        )
        self.classroom_3 = ClassroomFactory(
            retention_date=date(2023, 1, 1),
        )
        self.classroom_4 = ClassroomFactory()

    def test_delete_outdated_videos(self):
        """
        Test the delete_outdated_classrooms command.
        """
        with patch.object(
            timezone, "now", return_value=datetime(2022, 1, 2, tzinfo=baseTimezone.utc)
        ):
            call_command("delete_outdated_classrooms")
            self.assertEqual(Classroom.objects.count(), 2)

            self.classroom_1.refresh_from_db()
            self.assertIsNotNone(self.classroom_1.deleted)

            self.classroom_2.refresh_from_db()
            self.assertIsNotNone(self.classroom_2.deleted)

            self.classroom_3.refresh_from_db()
            self.assertIsNone(self.classroom_3.deleted)

            self.classroom_4.refresh_from_db()
            self.assertIsNone(self.classroom_4.deleted)