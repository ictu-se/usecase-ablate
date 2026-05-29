# Models/services
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

### src/backend/marsha/bbb/tests/test_models.py
"""Tests for the models in the ``bbb`` app of the Marsha project."""

import json

from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from safedelete.models import SOFT_DELETE_CASCADE

from marsha.bbb.factories import (
    ClassroomFactory,
    ClassroomRecordingFactory,
    ClassroomSessionFactory,
)


class ClassroomModelsTestCase(TestCase):
    """Test our intentions about the Classroom model."""

    maxDiff = None

    def test_models_classroom_str(self):
        """The str method should display the classroom title and its eventual soft deletion."""
        classroom = ClassroomFactory(title="ça joue")
        self.assertEqual(str(classroom), "ça joue")

        classroom.delete()
        self.assertEqual(str(classroom), "ça joue [deleted]")

    def test_models_classroom_fields_lti_id_unique(self):
        """Classrooms should be unique for a given duo lti_id/playlist (see LTI specification)."""
        classroom = ClassroomFactory()

        # A classroom with a different lti_id and the same playlist can still be created
        ClassroomFactory(playlist=classroom.playlist)

        # A classroom for a different playlist and the same lti_id can still be created
        ClassroomFactory(lti_id=classroom.lti_id)

        # Trying to create a classroom with the same duo lti_id/playlist should raise a
        # database error
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ClassroomFactory(lti_id=classroom.lti_id, playlist=classroom.playlist)

        # Soft deleted classrooms should not count for unicity
        classroom.delete(force_policy=SOFT_DELETE_CASCADE)
        ClassroomFactory(lti_id=classroom.lti_id, playlist=classroom.playlist)


class ClassroomClassroomRecordingTestCase(TestCase):
    """Test the ClassroomRecording model."""

    maxDiff = None

    def test_models_classroomrecording_video_file_url(self):
        """The video_file_url method should return the video file url."""
        classroom_recording = ClassroomRecordingFactory()
        with self.assertRaises(DeprecationWarning) as deprecation:
            # pylint: disable=pointless-statement
            classroom_recording.video_file_url

        self.assertEqual(
            deprecation.exception.args[0],
            "Access denied to video_file_url: deprecated field",
        )


class ClassroomSessionTestCase(TestCase):
    """Test the ClassroomSession model."""

    maxDiff = None

    def test_models_classroomsession_str(self):
        """The str method should 
...[truncated]...

### src/backend/marsha/account/tests/test_models.py
"""Test the marsha's account models."""

from django.core.exceptions import ValidationError
from django.test import TestCase

from marsha.account.models import IdpOrganizationAssociation
from marsha.core.factories import OrganizationFactory


class IdpOrganizationAssociationTestCase(TestCase):
    """Test case for the `IdpOrganizationAssociation` model."""

    @classmethod
    def setUpClass(cls):
        """Init all tests once with an organization and an already existing association"""
        super().setUpClass()
        cls.organization = OrganizationFactory()
        cls.idp_entity_id = "https://some-idp.com/entity/id/"
        IdpOrganizationAssociation.objects.create(
            organization=cls.organization,
            idp_identifier=cls.idp_entity_id,
        )

    def test_unicity(self):
        """Asserts we can only link twice the same identity provider to the same organization"""
        with self.assertRaises(ValidationError) as exception_context_manager:
            IdpOrganizationAssociation.objects.create(
                organization=self.organization,
                idp_identifier=self.idp_entity_id,
            )

        raised_exception = exception_context_manager.exception
        self.assertListEqual(
            raised_exception.messages,
            [
                "Idp organization association with this Identity provider ID already exists.",
            ],
        )

    def test_one_organization_many_identity_providers(self):
        """Asserts the same organization can be linked to several identity providers"""
        IdpOrganizationAssociation.objects.create(
            organization=self.organization,
            idp_identifier="https://some-other-idp.com/entity/id/",
        )

        IdpOrganizationAssociation.objects.create(
            organization=self.organization,
            idp_identifier="https://my-idp.com/entity/id/",
        )

        self.assertEqual(
            IdpOrganizationAssociation.objects.filter(
                organization=self.organization
            ).count(),
            3,
        )

    def test_one_identity_provider_many_organizations(self):
        """Asserts the same identity provider cannot be linked to several organizations"""
        with self.assertRaises(ValidationError) as exception_context_manager:
            IdpOrganizationAssociation.objects.create(
                organization=OrganizationFactory(),
                idp_identifier=self.idp_entity_id,
            )
        raised_exception = exception_context_manager.exception
        self.assertListEqual(
            rais
...[truncated]...

### src/backend/marsha/core/tests/models/test_site.py
"""Tests for the models in the ``core`` app of the Marsha project."""

from django.test import TestCase

from marsha.core.factories import SiteConfigFactory


class SiteConfigModelsTestCase(TestCase):
    """Test our intentions about the SiteConfig model."""

    def test_models_marsha_site_str(self):
        """The str method should display the site name"""
        site = SiteConfigFactory(site__name="Marsha site")
        self.assertEqual(str(site), "Config associated to: Marsha site")

### src/backend/marsha/core/tests/models/test_video.py
"""Tests for the models in the ``core`` app of the Marsha project."""

from datetime import datetime, timedelta, timezone as baseTimezone
import random
from unittest import mock

from django.core.cache import cache
from django.db.utils import IntegrityError
from django.test import TestCase, override_settings
from django.utils import timezone

from marsha.core.defaults import (
    DELETED,
    ENDED,
    ERROR,
    HARVESTED,
    IDLE,
    LIVE_CHOICES,
    LIVE_TYPE_CHOICES,
    MAX_RESOLUTION_EXCEDEED,
    PENDING,
    PROCESSING,
    RAW,
    RUNNING,
    STATE_CHOICES,
    STOPPING,
)
from marsha.core.factories import VideoFactory
from marsha.core.utils.time_utils import to_timestamp


# pylint: disable=too-many-public-methods


class VideoModelsTestCase(TestCase):
    """Test our intentions about the Video model."""

    def setUp(self):
        """
        Reset the cache so that no cache key will be active
        """
        cache.clear()

    def test_models_video_str(self):
        """The str method should display the title of the video and its eventual soft deletion."""
        video = VideoFactory(title="j'espère")
        self.assertEqual(str(video), "j'espère")

        video.delete()
        self.assertEqual(str(video), "j'espère [deleted]")

    def test_models_video_live_state_set_without_live_type(self):
        """A video live_state should not be set without a live_type."""
        with self.assertRaises(IntegrityError):
            VideoFactory(
                live_state=random.choice([choice[0] for choice in LIVE_CHOICES])
            )

    def test_models_video_fields_lti_id_non_unique(self):
        """it should be possible to create 2 videos sharing the same playlists and lti_id."""
        video = VideoFactory()

        # A video with a different lti_id and the same playlist can still be created
        VideoFactory(playlist=video.playlist)

        # A video for a different playlist and the same lti_id can still be created
        VideoFactory(lti_id=video.lti_id)

        # A video with an already existing lti_id and playlist_id can still be created
        VideoFactory(lti_id=video.lti_id, playlist=video.playlist)

    def test_models_video_live_type_set_without_live_state(self):
        """A video live_type should not be set without a live_state."""
        with self.assertRaises(IntegrityError):
            VideoFactory(
                live_type=random.choice([choice[0] for choice in LIVE_TYPE_CHOICES])
            )

    def test_models_video_is_ready_to_show(self):
        """All combination where a video is ready or n

...[truncated]...