# Deterministic random code snippets
### src/core/fixtures/timezone.py
from zoneinfo import ZoneInfo

import pytest


@pytest.fixture
def kamchatka_timezone(settings) -> ZoneInfo:
    timezone_str = "Asia/Kamchatka"
    settings.TIME_ZONE = timezone_str
    return ZoneInfo(timezone_str)

### src/apps/notion/tests/notion/legacy_api/conftest.py
import pytest

from apps.notion.page import NotionPage

pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture
def api(api):
    """We test it as normal student, not superuser to check permissions"""
    api.user.update(is_superuser=False)

    return api


@pytest.fixture(autouse=True)
def order(factory, course, api):
    return factory.order(
        user=api.user,
        item=course,
        is_paid=True,
    )


@pytest.fixture
def unpaid_order(order, refund):
    refund(order)

    return order


@pytest.fixture(autouse=True)
def material(mixer, course):
    return mixer.blend(
        "notion.Material",
        course=course,
        page_id="0e5693d2173a4f77ae8106813b6e5329",
        slug="4d5726e8ee524448b8f97be4c7f8e632",
    )


@pytest.fixture
def mock_notion_response(mocker, page: NotionPage):
    return mocker.patch("apps.notion.client.NotionClient.fetch_page", return_value=page)

### src/apps/orders/tests/orders/promocode/tests_promocode_apply.py
from decimal import Decimal

import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def course(course):
    return course.update(price=100_500)


@pytest.mark.parametrize(
    ("discount_percent", "expected"),
    [
        ("50", 50_250),
        ("25", 75_375),
        ("0", 100_500),
        ("100", 0),
    ],
)
def test_discount_percent(discount_percent, expected, course, mixer):
    promocode = mixer.blend("orders.PromoCode", discount_percent=discount_percent)

    assert promocode.apply(course) == Decimal(expected)


@pytest.mark.parametrize(
    ("discount_value", "expected"),
    [
        ("50", 100_450),
        ("1", 100_499),
        (0, 100_500),
        (100_600, 100_500),  # greater then the course price
    ],
)
def test_discount_value(discount_value, expected, course, mixer):
    promocode = mixer.blend("orders.PromoCode", discount_percent=None, discount_value=discount_value)

    assert promocode.apply(course) == Decimal(expected)

### src/apps/users/tests/users/email_changer/test_changing_user_email_to_the_new_one.py
import pytest
from django.core.exceptions import ValidationError

pytestmark = [pytest.mark.django_db]


def test_fields_are_changed(user, service):
    service(new_email="new@email.com")()

    user.refresh_from_db()

    assert user.email == "new@email.com"
    assert user.username == "new@email.com"


def test_duplicate_username_protection(service, mixer):
    mixer.blend("users.User", email="some.other@email.com", username="new@email.com")

    with pytest.raises(ValidationError):
        service(new_email="new@email.com")()


@pytest.mark.dashamail
def test_user_is_subscribed_to_dashamail(service, subscribe):
    service(new_email="new@email.com")()

    assert subscribe.call_count == 1


def test_user_is_not_subscribed_if_dashamail_is_disabled(service, subscribe):
    """Same as above, but without enabling dashamail"""
    service(new_email="new@email.com")()

    assert subscribe.call_count == 0

### src/apps/banking/zero_price_bank.py
from decimal import Decimal
from typing import TYPE_CHECKING

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.banking.base import Bank

if TYPE_CHECKING:
    from apps.orders.models import Order


class ZeroPriceBank(Bank):
    """Bank used for zero-priced orders, redirects user to URL provided by frontend"""

    currency = "KIS"
    currency_symbol = "💋"
    default_acquiring_percent = Decimal(0)
    name = _("Zero Price")

    def __init__(
        self,
        order: "Order",
        success_url: str | None = None,
        fail_url: str | None = None,
        idempotency_key: str | None = None,
        redirect_url: str | None = None,
    ) -> None:
        super().__init__(
            order=order,
            success_url=success_url,
            fail_url=fail_url,
            idempotency_key=idempotency_key,
        )
        self.redirect_url = redirect_url

    def validate_order(self, order: "Order") -> None:
        if order.price != 0:
            raise ValidationError("ZeroPriceBank may be used only with zero-priced orders")

    def get_initial_payment_url(self) -> str:
        if self.redirect_url is None:
            raise ValidationError("Please provide redirect_url when using ZeroPriceBank")

        return self.redirect_url

### src/core/fixtures/pause_slow_background_jobs.py
import pytest


@pytest.fixture(autouse=True)
def _pause_auditlog(mocker, request):
    if request.node.get_closest_marker("auditlog") is None:
        mocker.patch("core.tasks.write_admin_log.write_admin_log.delay")

        mocker.patch("apps.orders.services.order_paid_setter.OrderPaidSetter.write_auditlog")
        mocker.patch("apps.orders.services.order_shipper.OrderShipper.write_auditlog")
        mocker.patch("apps.orders.services.order_refunder.OrderRefunder.write_auditlog")
        mocker.patch("apps.b2b.services.deal_completer.DealCompleter.write_auditlog")
        mocker.patch("apps.b2b.services.bulk_student_creator.BulkStudentCreator.write_auditlog_for_student_creation")


@pytest.fixture(autouse=True)
def _pause_dashamail(mocker, request):
    """Pause dashamail background jobs"""
    if request.node.get_closest_marker("dashamail") is None:
        mocker.patch("apps.dashamail.tasks.update_subscription.delay")
        mocker.patch("apps.dashamail.tasks.update_subscription.apply_async")

        mocker.patch("apps.dashamail.tasks.push_order_event.delay")
        mocker.patch("apps.dashamail.tasks.push_order_event.si")
        mocker.patch("apps.dashamail.tasks.push_order_event.apply_async")

        mocker.patch("apps.dashamail.tasks.directcrm_subscribe.delay")
        mocker.patch("apps.dashamail.tasks.directcrm_subscribe.si")
        mocker.patch("apps.dashamail.tasks.directcrm_subscribe.apply_async")


@pytest.fixture(autouse=True)
def _pause_tags(mocker, request):
    """Pause background flags rebuilding"""
    if request.node.get_closest_marker("user_tags_rebuild") is None:
        mocker.patch("apps.users.tasks.rebuild_tags.delay")
        mocker.patch("apps.users.tasks.rebuild_tags.apply_async")
        mocker.patch("apps.users.tasks.generate_tags")

### src/core/fixtures/send_mail.py
import pytest


@pytest.fixture
def send_mail(mocker):
    return mocker.patch("apps.mailing.tasks.send_mail.delay")

### src/apps/a12n/tests/api/tests_refresh_token.py
import pytest
from freezegun import freeze_time

from apps.a12n.utils import get_jwt

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.freeze_time("2049-01-05"),
    pytest.mark.skip(reason="We dropped refreshing functionality, but may restore it in the future, so this will save the API"),
]


@pytest.fixture
def refresh_token(api):
    def _refresh_token(token, expected_status_code=201):
        return api.post(
            "/api/v2/auth/token/refresh/",
            {
                "token": token,
            },
            format="json",
            expected_status_code=expected_status_code,
        )

    return _refresh_token


@pytest.fixture
def initial_token(api):
    with freeze_time("2049-01-03"):
        return get_jwt(api.user)


def test_refresh_token_ok(initial_token, refresh_token):
    got = refresh_token(initial_token)

    assert "token" in got


def test_refreshed_token_is_a_token(initial_token, refresh_token):
    got = refresh_token(initial_token)

    assert len(got["token"]) > 32


def test_refreshed_token_is_new_one(initial_token, refresh_token):
    got = refresh_token(initial_token)

    assert got["token"] != initial_token


def test_refresh_token_fails_with_incorrect_previous_token(refresh_token):
    got = refresh_token("some-invalid-previous-token", expected_status_code=400)

    assert "non_field_errors" in got


def test_token_is_not_allowed_to_refresh_if_expired(initial_token, refresh_token):
    with freeze_time("2099-02-05"):
        got = refresh_token(initial_token, expected_status_code=400)

    assert "expired" in got["non_field_errors"][0]


def test_received_token_works(anon, refresh_token, initial_token):
    token = refresh_token(initial_token)["token"]

    anon.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    got = anon.get("/api/v2/users/me/")

    assert got is not None

### src/apps/amocrm/tests/ids/tests_product_fields_ids.py
import pytest

from apps.amocrm import types
from apps.amocrm.exceptions import AmoCRMCacheException
from apps.amocrm.ids import product_field_id


@pytest.fixture(autouse=True)
def mock_get_catalog_id(mocker):
    return mocker.patch("apps.amocrm.ids.products_catalog_id", return_value=123)


@pytest.fixture
def group_field():
    return types.CatalogField(id=333, code="GROUP")


@pytest.fixture
def fields(group_field):
    return [
        group_field,
        types.CatalogField(id=123, code="EXTERNAL_ID"),
    ]


@pytest.fixture(autouse=True)
def mock_get_catalog_fields(mocker, fields):
    return mocker.patch("apps.amocrm.dto.catalogs.AmoCRMCatalogsDTO.get_fields", return_value=fields)


def test_return_id_if_in_cache(group_field):
    got = product_field_id("GROUP")

    assert got == group_field.id


def test_fail_if_not_in_cache_and_not_in_response(mock_get_catalog_fields):
    mock_get_catalog_fields.return_value = [types.CatalogField(id=123, code="EXTERNAL_ID")]

    with pytest.raises(AmoCRMCacheException):
        product_field_id("GROUP")

### src/apps/b2b/apps.py
from django.apps import AppConfig


class B2BConfig(AppConfig):
    name = "apps.b2b"

### src/core/tasks/tg.py
from core.celery import celery
from core.integrations import tg


@celery.task
def send_telegram_message(chat_id: str, text: str) -> None:
    tg.send_message(chat_id=chat_id, text=text)

### src/apps/a12n/tests/api/tests_obtain_token.py
import pytest

from apps.a12n.jwt import decode_jwt_without_validation
from apps.users.services import UserCreator

pytestmark = pytest.mark.django_db


@pytest.fixture
def get_token(api):
    def _get_token(username, password, expected_status_code=201):
        return api.post(
            "/api/v2/auth/token/",
            {
                "username": username,
                "password": password,
            },
            format="json",
            expected_status_code=expected_status_code,
        )

    return _get_token


def test_getting_token_ok(api, get_token):
    got = get_token(api.user.username, api.password)

    assert "token" in got


def test_getting_token_by_email(user, get_token):
    user = UserCreator(name="lol bar", email="lolbar@example.com")()
    user.set_password("123456")
    user.save()

    got = get_token("lolbar@example.com", "123456")

    assert "token" in got


def test_getting_token_case_sensitive_email(get_token):
    user = UserCreator(name="lol bar", email="lolbar@example.com")()
    user.set_password("123456")
    user.save()

    got2 = get_token("LOLBAR@EXAMPLE.Com", "123456", expected_status_code=400)

    assert "non_field_errors" in got2


def test_getting_token_case_sensitive_username(get_token, mixer):
    user = mixer.blend("users.User", username="Jimbo", email="jimbo@example.com")
    user.set_password("123456")
    user.save()

    got2 = get_token("jimbo", "123456", expected_status_code=400)
    assert "non_field_errors" in got2


def test_getting_token_is_a_token(api, get_token):
    got = get_token(api.user.username, api.password)

    payload = decode_jwt_without_validation(got["token"])

    assert payload["iss"] == "education-backend"
    assert payload["user_public_id"] == str(api.user.uuid)


def test_getting_token_with_incorrect_password(api, get_token):
    got = get_token(api.user.username, "z3r0c00l", expected_status_code=400)

    assert "non_field_errors" in got


def test_getting_token_when_banned_by_axes(api, get_token, settings):
    settings.AXES_FAILURE_LIMIT = 0

    got = get_token(api.user.username, api.password, expected_status_code=403)

    assert got == {"detail": "Too many failed login attempts"}


@pytest.mark.parametrize(
    ("extract_token", "status_code"),
    [
        (lambda response: response["token"], 200),
        (
            lambda *args: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRpbW90aHk5NSIsImlhdCI6MjQ5MzI0NDgwMCwiZXhwIjoyNDkzMjQ1MTAwLCJqdGkiOiI2MWQ2MTE3YS1iZWNlLTQ5YWEtYWViYi1mOGI4MzBhZDBlNzgiLCJ1c2VyX2lkIjoxLCJvcmlnX2lhdCI6MjQ5MzI0NDgwMH0.YQnk0v
...[truncated]...

### src/apps/a12n/tests/tests_passwordless_token_absolute_url.py
import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture(autouse=True)
def _freeze_absolute_url(settings):
    settings.FRONTEND_URL = "https://frontend/lms/"


def test(mixer):
    token = mixer.blend("a12n.PasswordlessAuthToken", token="3149798e-c219-47f5-921f-8ae9a75b709b")

    assert token.get_absolute_url() == "https://frontend/lms/auth/passwordless/3149798e-c219-47f5-921f-8ae9a75b709b/"

### src/apps/banking/price_calculator.py
from decimal import Decimal
from typing import Type

from apps.banking.base import Bank


def to_bank(bank: Type[Bank], price: Decimal) -> Decimal:
    """Get sum in bank currency"""
    exchanged_price = Decimal(price) / Decimal(bank.get_currency_rate())

    if not price % 1:  # initial price contains decimal part, e.g. kopecks
        exchanged_price = Decimal(round(exchanged_price))

    return round(exchanged_price, 2)

### src/core/conf/markdown.py
from bleach.sanitizer import ALLOWED_ATTRIBUTES as _ALLOWED_ATTRIBUTES
from bleach.sanitizer import ALLOWED_TAGS as _ALLOWED_TAGS

BLEACH_ALLOWED_TAGS = [
    *_ALLOWED_TAGS,
    "p",
    "img",
    "br",
    "hr",
    "pre",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h3",
]

BLEACH_ALLOWED_ATTRIBUTES = {
    **_ALLOWED_ATTRIBUTES,
    "img": {
        "src",
        "alt",
    },
}

### src/apps/orders/tests/orders/order_shipping/tests_marketing_integrations.py
import pytest

pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture
def _enable_amocrm(settings):
    settings.AMOCRM_BASE_URL = "https://test.amocrm.ru"
    settings.AMOCRM_REDIRECT_URL = "https://test-education.ru"
    settings.AMOCRM_INTEGRATION_ID = "4815162342"
    settings.AMOCRM_CLIENT_SECRET = "top-secret-007"
    settings.AMOCRM_AUTHORIZATION_CODE = "1337yep"


@pytest.fixture
def update_amocrm_order(mocker):
    return mocker.patch("apps.amocrm.tasks.AmoCRMOrderPusher.act")


@pytest.fixture
def update_amocrm_user(mocker):
    return mocker.patch("apps.amocrm.tasks.AmoCRMUserPusher.act")


@pytest.fixture(autouse=True)
def update_dashamail(mocker):
    return mocker.patch("apps.dashamail.tasks.DashamailSubscriber.subscribe")


@pytest.fixture(autouse=True)
def update_dashamail_directcrm(mocker):
    return mocker.patch("apps.dashamail.tasks.directcrm_events.OrderPaid.send")


@pytest.mark.usefixtures("_enable_amocrm")
def test_amocrm_is_updated(order, update_amocrm_order, update_amocrm_user):
    order.set_paid()

    update_amocrm_order.assert_called_once()
    update_amocrm_user.assert_called_once()


@pytest.mark.user_tags_rebuild
def test_tags_are_rebuilt(order):
    assert "any-purchase" not in order.user.tags

    order.set_paid()
    order.user.refresh_from_db()

    assert "any-purchase" in order.user.tags


@pytest.mark.dashamail
def test_dashamail_is_updated(order, update_dashamail):
    order.set_paid()

    update_dashamail.assert_called_once()


def test_dashamail_is_not_updated_if_disabled(order, update_dashamail):
    order.set_paid()

    update_dashamail.assert_not_called()


@pytest.mark.dashamail
def test_dashamail_directm_is_updated(order, update_dashamail_directcrm):
    order.set_paid()

    update_dashamail_directcrm.assert_called_once()


def test_dashamail_directcrm_is_not_updated_if_disabled(order, update_dashamail_directcrm):
    order.set_paid()

    update_dashamail_directcrm.assert_not_called()

### src/apps/products/models/group.py
from django.utils.translation import gettext_lazy as _

from core.models import TimestampedModel, models


class Group(TimestampedModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    dashamail_list_id = models.IntegerField(null=True)

    evergreen = models.BooleanField(_("Evergreen"), default=False)

    class Meta:
        verbose_name = _("Product group")
        verbose_name_plural = _("Product groups")

### src/apps/tinkoff/apps.py
from django.apps import AppConfig


class TinkoffConfig(AppConfig):
    name = "apps.tinkoff"

### src/apps/orders/services/order_diploma_generator.py
from dataclasses import dataclass

from django.utils.functional import cached_property

from apps.diplomas.models import DiplomaTemplate
from apps.diplomas.tasks import generate_diploma
from apps.orders.models import Order
from apps.products.models import Course
from apps.studying.models import Study
from apps.users.models import User
from core.services import BaseService


@dataclass
class OrderDiplomaGenerator(BaseService):
    order: Order

    def act(self) -> None:
        for language in self.get_available_languages():
            generate_diploma.delay(
                student_id=self.student.id,
                course_id=self.course.id,
                language=language,
            )

    @cached_property
    def study(self) -> Study:
        return self.order.study

    @cached_property
    def student(self) -> User:
        return self.study.student

    @cached_property
    def course(self) -> Course:
        return self.study.course

    def get_available_languages(self) -> list[str]:
        return [
            template.language
            for template in DiplomaTemplate.objects.filter(
                course=self.course,
                homework_accepted=self.study.homework_accepted,
                language__in=self.student.diploma_languages,
            )
        ]

### src/apps/amocrm/types.py
"""typing for amocrm dto responses"""

from enum import IntEnum
from typing import NamedTuple


class CatalogField(NamedTuple):
    """Represents amocrm's custom catalog field that could be used with various entities

    https://www.amocrm.ru/developers/content/crm_platform/custom-fields
    """

    id: int
    code: str


class Catalog(NamedTuple):
    """Represents amocrm's catalog aka 'список'

    https://www.amocrm.ru/developers/content/crm_platform/catalogs-api#lists-list
    """

    id: int
    name: str
    type: str


class TaskType(IntEnum):
    """Represents type of amocrm's task.

    Look for `task_type` at https://www.amocrm.ru/developers/content/crm_platform/tasks-api#common-info
    """

    CONTACT = 1
    MEETING = 2


class Task(NamedTuple):
    """Represents amocrm's Taks

    Only fields that are used in the app are listed.
    https://www.amocrm.ru/developers/content/crm_platform/tasks-api#tasks-list
    """

    id: int
    task_type_id: TaskType
    is_completed: bool
    text: str


class PipelineStatus(NamedTuple):
    """Represents status of amocrm's Pipeline. The statuses may be system of user-defined.

    https://www.amocrm.ru/developers/content/crm_platform/leads_pipelines#Общая-информация
    """

    id: int
    name: str


class Pipeline(NamedTuple):
    """Represents amocrm's Pipeline

    https://www.amocrm.ru/developers/content/crm_platform/leads_pipelines
    """

    id: int
    name: str
    statuses: list[PipelineStatus]


class UserOperator(NamedTuple):
    """Represents amocrm's User.

    The 'UserOperator' is used to distinguish from the 'AmoCRMUser' model that link amocrm's customers.

    Only fields that are used in the app are listed.
    All the available fields are listed in docs:
    https://www.amocrm.ru/developers/content/crm_platform/users-api#users-list
    """

    id: int
    name: str
    email: str

### src/core/models.py
import operator
from collections.abc import Iterable
from functools import reduce
from typing import Any

from django.db import models
from django.db.models.base import ModelBase
from django.utils import timezone

__all__ = [
    "DefaultModel",
    "TimestampedModel",
    "models",
]


class TestUtilsMixin:
    def update(self: "models.Model", **kwargs: "Any") -> "models.Model":  # type: ignore[misc]
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.save(update_fields=kwargs.keys())

        return self


class DefaultModel(TestUtilsMixin, models.Model):
    class Meta:
        abstract = True

    def __str__(self) -> str:
        name = getattr(self, "name", None)
        if name is not None:
            return str(name)

        return super().__str__()


class TimestampedModel(DefaultModel):
    """
    Default app model that has `created` and `updated` attributes.
    """

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True

    def save(
        self,
        *,
        force_insert: bool | tuple[ModelBase, ...] = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ) -> None:
        if self.pk:
            self.modified = timezone.now()
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class SubqueryCount(models.Subquery):
    template = "(SELECT count(id) FROM (%(subquery)s) _count)"
    output_field = models.IntegerField()


class SubquerySum(models.Subquery):
    template = '(SELECT SUM(_agg."%(column)s") FROM (%(subquery)s) _agg)'

    def __init__(self, queryset: models.QuerySet, column: str, **kwargs: dict) -> None:
        super().__init__(queryset=queryset, output_field=models.IntegerField(), column=column, **kwargs)


def only_one_or_zero_is_set(*fields: str) -> models.Q:
    """Generate a query for CheckConstraint that allows to set only one (or none of) given fields"""
    constraints = []
    for field in fields:
        constraint = models.Q(
            **{
                f"{field}__isnull": False,
                **{f"{empty_field}__isnull": True for empty_field in fields if empty_field != field},
            },
        )
        constraints.append(constraint)

    all_fields_can_empty_constraint = models.Q(
        **{f"{field}__isnull": True for field
...[truncated]...