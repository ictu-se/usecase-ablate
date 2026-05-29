# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

# README
## README.md
# Backend for [tough-dev.school](https://tough-dev.school/)

![CI](https://github.com/tough-dev-school/education-backend/actions/workflows/ci.yml/badge.svg) [![Crossplatform](https://github.com/tough-dev-school/education-backend/actions/workflows/crossplatform.yml/badge.svg)](https://github.com/tough-dev-school/education-backend/actions/workflows/crossplatform.yml)

Django-based production project, integrated with Tinkoff, Dashamail, Postmark, S3 and telegram. Frontend is built on vue.js in the [separate repo](https://github.com/tough-dev-school/lms-frontend-v2).

## Configuration

Configuration is stored in `src/core/.env`, for examples see `src/core/.env.ci`

## Installing on a local machine

This project requires python 3.14. Deps are managed by [uv](https://docs.astral.sh/uv/).

Install requirements:

```bash
uv sync
```

Configure postgres and redis. It's convenient to use docker and docker-compose:

```bash
docker compose up -d
```

If you don't have access to de-anonymized db image use `postgres:13.6-alpine` in `docker-compose.yml` instead:

```yaml
postgres:
    image: postgres:13.6-alpine
    ...
```

Run the server:

```bash
cp src/core/.env.ci src/core/.env

uv run python src/manage.py migrate
uv run python src/manage.py createsuperuser

make server
```

Testing:

```bash
# run lint
make lint

# run unit tests
make test
```

## Backend Code requirements

### Style

* Obey [django's style guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style).
* Configure your IDE to use `ruff` for checking your python code. For running linters manualy, do `make lint`
* Prefer English over your native language in comments and commit messages.
* Commit messages should contain the unique id of issue they are linked to (refs #100500)
* Every model and a model method should have a docstring.

### Code organisation

* KISS and DRY.
* Obey [django best practices](http://django-best-practices.readthedocs.io/en/latest/index.html)
* If you want to implement some business logic — make a service for that. Service examples: [UserCreator](https://github.com/tough-dev-school/education-backend/blob/master/src/apps/users/services/user_creator.py), [OrderCreator](https://github.com/tough-dev-school/education-backend/blob/master/src/apps/orders/services/order_creator.py)
* **No logic is allowed within the views or templates**. Only services and models.
* Use PEP-484 [type hints](https://www.python.org/dev/peps/pep-0484/) when possible.
* Prefer [Manager](https://docs.djangoproject.com/en/dev/topics/db/managers/) methods over static methods.
* Do not use [signals](https://docs.djangoproject.com/en/dev/topics/signals/) for business logic. Signals are good only for notification purposes.
* No l10n is allowed in python code, use [django translation](https://docs.djangoproject.com/en/dev/topics/i18n/translation/).

# File tree
.hadolint.yaml
.yamllint.yml
AGENTS.md
README.md
compose.yml
conftest.py
pyproject.toml
renovate.json
src
  apps
    __init__.py
    a12n
      __init__.py
      admin.py
      api
        forms.py
        serializers.py
        throttling.py
        views.py
      apps.py
      jwt.py
      models.py
      signals
        handlers.py
      tests
        __init__.py
        api
          tests_obtain_jwt_via_passwordless_token.py
          tests_obtain_jwt_via_user_id.py
          tests_obtain_token.py
          tests_password_change.py
          tests_password_reset_confirm.py
          tests_refresh_token.py
          tests_request_password_reset.py
          tests_request_passwordless_token.py
        tests_jwt_blacklisting.py
        tests_passwordless_token_absolute_url.py
      urls.py
      utils.py
    amocrm
      __init__.py
      apps.py
      client
        __init__.py
        client.py
        http.py
      dto
        __init__.py
        catalogs.py
        customer.py
        groups.py
        lead.py
        lead_note.py
        lead_task.py
        pipelines.py
        product.py
        transaction.py
        user_operator.py
      exceptions.py
      ids.py
      models
        __init__.py
        amocrm_course.py
        amocrm_order_lead.py
        amocrm_order_transaction.py
        amocrm_product_group.py
        amocrm_user.py
      services
        __init__.py
        access_token_getter.py
        course_pusher.py
        group_pusher.py
        orders
          order_pusher.py
          order_returner.py
          order_task_creator.py
        user_pusher.py
      tasks.py
      tests
        __init__.py
        conftest.py
        dto
          conftest.py
          tests_catalogs.py
          tests_customer.py
          tests_groups.py
          tests_lead.py
          tests_lead_note.py
          tests_lead_task.py
          tests_pipelines.py
          tests_product.py
          tests_transaction.py
          tests_user_operator.py
        http
          __init__.py
          tests_http.py
        ids
          tests_b2c_pipeline_id.py
          tests_catalog_id.py
          tests_contact_fields_ids.py
          tests_product_fields_ids.py
        services
          order
          tests_course_pusher.py
          tests_group_pusher.py
          tests_user_pusher.py
        tests_access_token_getter.py
      types.py
    b2b
      __init__.py
      admin
        __init__.py
        customers.py
        deals
          __init__.py
          actions.py
          admin.py
          forms.py
        students.py
      apps.py
      factory.py
      models
        __init__.py
        customer.py
        deal.py
        student.py
      services
        __init__.py
        bulk_student_creator.py
        deal_completer.py
        deal_creator.py
        deal_currency_changer.py
      tests
        conftest.py
        deal_completer
          conftest.py
          test_deal_completer.py
          test_deal_completer_existing_order_assignment.py
          test_deal_completer_happiness_message.py
          test_deal_completer_new_order_creation.py
          test_deal_completer_shipping_without_payment.py
        test_bulk_student_creator.py
        test_deal_creator_service.py
        test_deal_currency_changer.py
        test_deal_status_str.py
      utils.py
    banking
      __init__.py
      admin
        __init__.py
        acquiring_percent.py
        currency_rate.py
      api
        serializers.py
      apps.py
      b2b.py
      base.py
      currency.py
      exceptions.py
      factory.py
      fixtures.py
      models.py
      price_calculator.py
      selector.py
      tests
        __init__.py
        tests_get_bank.py
        tests_get_bank_or_default.py
        tests_get_currency_rate.py
        tests_get_id.py
        tests_price_calculator.py
      urls.py
      zero_price_bank.py
    chains
      __init__.py
      admin
        __init__.py
        chain.py
        forms.py
        message.py
      apps.py
      models
        __init__.py
        chain.py
        message.py
        progress.py
      services
        __init__.py
        chain_sender.py
        message_sender.py
      tasks.py
      tests
        __init__.py
        chain_sender
          conftest.py
          test_chain_sender_integrational.py
          test_chain_tasks.py
          test_sending_next_messages.py
          test_sending_root_messages.py
        conftest.py
        message_sender
          conftest.py
          test_sending_message.py
        test_message_time_to_send.py
        unit
          test_chain_queryset_active.py
          test_chain_queryset_editable.py
          test_progress_get_last.py
    dashamail
      __init__.py
      apps.py
      directcrm
        events
          __init__.py
          base.py
          order_created.py
          order_paid.py
      enabled.py
      exceptions.py
      fixtures.py
      lists
      services
      tasks.py
      tests
    diplomas
    homework
    lms
    mailing
    notion
    orders
    products
    stripebank
    studying
    tinkoff
    users
  core
  manage.py

# Oracle-selected code and test snippets
### README.md
# Backend for [tough-dev.school](https://tough-dev.school/)

![CI](https://github.com/tough-dev-school/education-backend/actions/workflows/ci.yml/badge.svg) [![Crossplatform](https://github.com/tough-dev-school/education-backend/actions/workflows/crossplatform.yml/badge.svg)](https://github.com/tough-dev-school/education-backend/actions/workflows/crossplatform.yml)

Django-based production project, integrated with Tinkoff, Dashamail, Postmark, S3 and telegram. Frontend is built on vue.js in the [separate repo](https://github.com/tough-dev-school/lms-frontend-v2).

## Configuration

Configuration is stored in `src/core/.env`, for examples see `src/core/.env.ci`

## Installing on a local machine

This project requires python 3.14. Deps are managed by [uv](https://docs.astral.sh/uv/).

Install requirements:

```bash
uv sync
```

Configure postgres and redis. It's convenient to use docker and docker-compose:

```bash
docker compose up -d
```

If you don't have access to de-anonymized db image use `postgres:13.6-alpine` in `docker-compose.yml` instead:

```yaml
postgres:
    image: postgres:13.6-alpine
    ...
```

Run the server:

```bash
cp src/core/.env.ci src/core/.env

uv run python src/manage.py migrate
uv run python src/manage.py createsuperuser

make server
```

Testing:

```bash
# run lint
make lint

# run unit tests
make test
```

## Backend Code requirements

### Style

* Obey [django's style guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style).
* Configure your IDE to use `ruff` for checking your python code. For running linters manualy, do `make lint`
* Prefer English over your native language in comments and commit messages.
* Commit messages should contain the unique id of issue they are linked to (refs #100500)
* Every model and a model method should have a docstring.

### Code organisation

* KISS and DRY.
* Obey [django best practices](http://django-best-practices.readthedocs.io/en/latest/index.html)
* If you want to implement some business logic — make a service for that. Service examples: [UserCreator](https://github.com/tough-dev-school/education-backend/blob/master/src/apps/users/services/user_creator.py), [OrderCreator](https://github.com/tough-dev-school/education-backend/blob/master/src/apps/orders/services/order_creator.py)
* **No logic is allowed within the views or templates**. Only services and models.
* Use PEP-484 [type hints](https://www.python.org/dev/peps/pep-0484/) when possible.
* Prefer [Manager](https://docs.djangoproject.com/en/dev/topics/db/managers/) methods over static methods
...[truncated]...

### src/apps/products/urls.py
from django.urls import path

from apps.products.api import views

urlpatterns = [
    path("courses/<str:slug>/promocode/", views.PromocodeView.as_view()),
    path("courses/<str:slug>/purchase/", views.PurchaseView.as_view()),
    path("course-groups/<str:slug>/courses/", views.ProductGroupView.as_view()),
]

### src/apps/products/api/views.py
from typing import TYPE_CHECKING, Any

from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.banking import price_calculator
from apps.banking.api.serializers import Price, PriceSerializer
from apps.banking.selector import BANK_KEYS, get_bank_or_default
from apps.orders.api.throttling import OrderDraftThrottle, PurchaseThrottle
from apps.orders.models import PromoCode
from apps.orders.services import OrderCreator
from apps.products.api.serializers import CourseWithPriceSerializer, PurchaseSerializer
from apps.products.models import Course
from apps.products.models import Group as ProductGroup
from apps.users.services import UserCreator
from core.throttling import PublicIDThrottle

if TYPE_CHECKING:
    from rest_framework.request import Request

    from apps.orders.models import Order
    from apps.users.models import User


class PromocodeView(APIView):
    throttle_classes = [OrderDraftThrottle]
    permission_classes = [AllowAny]

    @extend_schema(
        responses=PriceSerializer,
        parameters=[
            OpenApiParameter(name="promocode", type=str),
            OpenApiParameter(name="desired_bank", type=str, many=False, enum=BANK_KEYS),
        ],
    )
    def get(self, request: "Request", slug: str | None = None, **kwargs: dict[str, Any]) -> Response:
        item = get_object_or_404(Course, slug=slug)
        promocode = self._get_promocode(request)

        price = promocode.apply(item) if promocode is not None else item.price
        Bank = get_bank_or_default(desired=request.GET.get("desired_bank"))
        price = price_calculator.to_bank(Bank, price)

        serializer = PriceSerializer(instance=Price(price, Bank))

        return Response(serializer.data)

    def _get_promocode(self, request: "Request") -> PromoCode | None:
        try:
            promocode_name = request.GET["promocode"]
        except KeyError:
            return None

        return PromoCode.objects.get_or_nothing(name=promocode_name)


class PurchaseView(APIView):
    throttle_classes = [PurchaseThrottle]
    permission_classes = [AllowAny]

    @extend_schema(request=PurchaseSerializer, responses={302: None})
    def post(self, request: "Request", slug: str | None = None, **kwargs: dict[str, Any]) -> HttpResponseRedirect:
        item =
...[truncated]...

### src/apps/products/api/serializers.py
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.banking import price_calculator
from apps.banking.api.serializers import Price, PriceSerializer
from apps.banking.selector import BANK_CHOICES
from apps.products.models import Course


class CourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "name",
            "name_international",
            "product_name",
            "tariff_name",
        ]


class CourseWithPriceSerializer(serializers.ModelSerializer):
    """Course with commercial data. Requires bank context"""

    price = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "slug",
            "name",
            "name_international",
            "product_name",
            "tariff_name",
            "price",
        ]

    @extend_schema_field(PriceSerializer)
    def get_price(self, course: Course) -> dict:
        Bank = self.context["Bank"]  # needs to know a bank name to calculate the price
        price = price_calculator.to_bank(Bank, course.price)

        return PriceSerializer(instance=Price(price, Bank)).data


class PurchaseSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    desired_bank = serializers.ChoiceField(choices=BANK_CHOICES, required=False)
    promocode = serializers.CharField(max_length=100, required=False)
    success_url = serializers.CharField(max_length=256, required=False)
    redirect_url = serializers.CharField(max_length=256, required=False)
    subscribe = serializers.CharField(max_length=5, default="")
    analytics = serializers.CharField(required=False)

    def validate_subscribe(self, value: str | None) -> bool:
        if value:
            return value.lower() in ["true", "1", "yes"]
        return False

### src/apps/products/tests/products/test_courses_by_group.py
from decimal import Decimal

import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def course(factory):
    return factory.course(price=90450)


@pytest.fixture(autouse=True)
def group(mixer, course):
    group = mixer.blend("products.Group", slug="rolling-in-it")

    course.update(group=group)


@pytest.fixture(autouse=True)
def _freeze_currency_rates(mocker):
    mocker.patch("apps.stripebank.bank.StripeBankUSD.get_currency_rate", return_value=Decimal(70))
    mocker.patch("apps.stripebank.bank.StripeBankKZT.get_currency_rate", return_value=Decimal("0.18"))


def test_list(anon, course):
    got = anon.get("/api/v2/course-groups/rolling-in-it/courses/")

    assert got[0]["slug"] == course.slug
    assert got[0]["name"] == course.name
    assert got[0]["price"]["price"] == "90450"
    assert got[0]["price"]["formatted_price"] == "90\xa0450"


def test_404_for_nonexistant_slug(anon):
    anon.get("/api/v2/course-groups/nonexistant/courses/", expected_status_code=404)


def test_another_groups_are_excluded(anon, course, mixer):
    course.update(group=mixer.blend("products.Group"))

    got = anon.get("/api/v2/course-groups/rolling-in-it/courses/")

    assert len(got) == 0


@pytest.mark.parametrize(
    ("bank", "expected_price", "expected_formatted_price", "expected_currency", "expected_currency_symbol"),
    [
        ("tinkoff_bank", "90450", "90\xa0450", "RUB", "₽"),
        ("stripe", "1292", "1\xa0292", "USD", "$"),
        ("stripe_kz", "502500", "502\xa0500", "KZT", "₸"),
    ],
)
def test_price_by_bank(anon, bank, expected_price, expected_formatted_price, expected_currency, expected_currency_symbol):
    got = anon.get(f"/api/v2/course-groups/rolling-in-it/courses/?desired_bank={bank}")

    assert got[0]["price"]["price"] == expected_price
    assert got[0]["price"]["formatted_price"] == expected_formatted_price
    assert got[0]["price"]["currency"] == expected_currency
    assert got[0]["price"]["currency_symbol"] == expected_currency_symbol

### src/apps/products/tests/products/courses/tests_course_for_admin.py
import pytest

from apps.products.models import Course

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.freeze_time("2032-12-04 15:30:55"),
]


@pytest.fixture
def course(factory):
    course = factory.course()

    course.group.update(created="2032-12-01 15:30:55+03:00", evergreen=False)

    return course


def queryset():
    return Course.objects.for_admin()


def test_on_by_default(course):
    assert course in queryset()


def test_off_after_2_years(course):
    course.group.update(created="2030-12-01 15:30:55+03:00")

    assert course not in queryset()


def test_on_after_2_years_if_evergreen(course):
    course.group.update(
        created="2030-12-01 15:30:55+03:00",
        evergreen=True,
    )

### src/apps/products/tests/products/courses/tests_course_str.py
import pytest

pytestmark = [pytest.mark.django_db]


def test_course_with_group(factory):
    group = factory.group(name="Милые котики")
    course_with_group = factory.course(name="Курс как стать милым котиком", group=group)
    assert str(course_with_group) == "Курс как стать милым котиком - Милые котики"

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

### src/apps/orders/models/promocode.py
import contextlib
from decimal import Decimal
from typing import Optional

from django.core.exceptions import ValidationError
from django.db.models import Case, CheckConstraint, Count, Q, QuerySet, When
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.products.models import Course
from core.models import TimestampedModel, models


class PromoCodeQuerySet(QuerySet):
    def active(self) -> QuerySet["PromoCode"]:
        return self.filter(
            active=True,
        ).filter(
            Q(expires__isnull=True) | Q(expires__gte=timezone.now()),
        )

    def with_order_count(self) -> QuerySet["PromoCode"]:
        return self.annotate(
            order_count=Count(
                Case(
                    When(order__paid__isnull=False, then=1),
                    output_field=models.IntegerField(),
                )
            )
        )

    def get_or_nothing(self, name: str | None) -> Optional["PromoCode"]:
        if name is not None:
            with contextlib.suppress(PromoCode.DoesNotExist):
                return self.active().get(name__iexact=name.strip())


PromoCodeManager = models.Manager.from_queryset(PromoCodeQuerySet)


class PromoCode(TimestampedModel):
    objects = PromoCodeManager()

    name = models.CharField(_("Promo Code"), max_length=32, unique=True, db_index=True)
    discount_percent = models.IntegerField(_("Discount percent"), null=True, blank=True)
    discount_value = models.IntegerField(_("Discount amount"), null=True, blank=True, help_text=_("Takes precedence over percent"))
    expires = models.DateTimeField(_("Expiration date"), null=True, blank=True)
    active = models.BooleanField(_("Active"), default=True)
    destination = models.TextField(_("Destination"))

    courses = models.ManyToManyField("products.Course", help_text=_("Can not be used for courses not checked here"), blank=True)

    class Meta:
        verbose_name = _("Promo Code")
        verbose_name_plural = _("Promo Codes")
        constraints = [
            CheckConstraint(condition=Q(discount_percent__isnull=False) | Q(discount_value__isnull=False), name="percent or value must be set"),
        ]

    def clean(self) -> None:
        if self.discount_percent is None and self.discount_value is None:
            raise ValidationError(_("Percent or value must be set"))

    def compatible_with(self, course: Course) -> bool:
        return self.courses.count() == 0 or course in self.courses.all()

    def apply(self, course: Course) -> Decimal:
        if not self.compatible_with(course):

...[truncated]...

### src/apps/orders/tests/orders/promocode/tests_price_with_promocode.py
from decimal import Decimal

import pytest

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures("ten_percent_promocode"),
]


@pytest.fixture(autouse=True)
def _freeze_stripe_course(mocker):
    mocker.patch("apps.stripebank.bank.StripeBankUSD.get_currency_rate", return_value=Decimal(70))  # let it be forever :'(


@pytest.fixture(autouse=True)
def _freeze_stripe_kz_course(mocker):
    mocker.patch("apps.stripebank.bank.StripeBankKZT.get_currency_rate", return_value=Decimal("0.18"))


@pytest.mark.parametrize(
    "code",
    [
        "TESTCODE",
        "testcode",
        "testcode ",
        " testcode",
    ],
)
def test(api, course, code):
    got = api.get(f"/api/v2/courses/{course.slug}/promocode/?promocode={code}")

    assert got["price"] == "90450"
    assert got["formatted_price"] == "90 450"
    assert got["currency"] == "RUB"
    assert got["currency_symbol"] == "₽"


@pytest.mark.parametrize(
    ("bank", "expected_price", "expected_formatted_price", "expected_currency", "expected_currency_symbol"),
    [
        ("tinkoff_bank", "90450", "90 450", "RUB", "₽"),
        ("tinkoff_credit", "90450", "90 450", "RUB", "₽"),
        ("stripe", "1292", "1 292", "USD", "$"),
        ("stripe_kz", "502500", "502 500", "KZT", "₸"),
    ],
)
def test_promocode_with_bank(api, course, bank, expected_price, expected_formatted_price, expected_currency, expected_currency_symbol):
    got = api.get(f"/api/v2/courses/{course.slug}/promocode/?promocode=TESTCODE&desired_bank={bank}")

    assert got["price"] == expected_price
    assert got["formatted_price"] == expected_formatted_price
    assert got["currency"] == expected_currency
    assert got["currency_symbol"] == expected_currency_symbol


@pytest.mark.parametrize(
    "code",
    [
        "EV1L",
        "",
    ],
)
def test_bad_promocode(api, course, code):
    got = api.get(f"/api/v2/courses/{course.slug}/promocode/?promocode={code}")

    assert got["price"] == "100500"


def test_incompatible_promocode(api, course, another_course, ten_percent_promocode):
    ten_percent_promocode.courses.add(course)

    got = api.get(f"/api/v2/courses/{another_course.slug}/promocode/?promocode=TESTCODE")

    assert got["price"] == "100500"


def test_compatible_promocode(api, course, ten_percent_promocode):
    ten_percent_promocode.courses.add(course)

    got = api.get(f"/api/v2/courses/{course.slug}/promocode/?promocode=TESTCODE")

    assert got["price"] == "90450"


def test_wihtout_promocode(api, course):
    got = api.get(
        f"/api/v2/courses/{course.slug}/promocode/",
    )

   
...[truncated]...

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

### src/apps/orders/tests/orders/promocode/tests_promocode_compatible_with.py
import pytest

pytestmark = [pytest.mark.django_db]


def test_true_if_no_courses_are_attached(ten_percent_promocode, course):
    assert ten_percent_promocode.compatible_with(course) is True


def test_false_if_some_courses_are_attached_but_given_is_not_attached(ten_percent_promocode, course, another_course):
    ten_percent_promocode.courses.add(course)

    assert ten_percent_promocode.compatible_with(another_course) is False


def test_true_if_course_is_attached(ten_percent_promocode, course):
    ten_percent_promocode.courses.add(course)

    assert ten_percent_promocode.compatible_with(course) is True

### src/apps/orders/tests/orders/promocode/tests_promocode_get_or_nothing.py
import pytest

from apps.orders.models import PromoCode

pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    "name",
    [
        "TESTCODE",
        "testcode",
        "tEStCOde",
        "  TESTCODE",
        "TESTCODE  ",
    ],
)
def test_found(ten_percent_promocode, name):
    assert PromoCode.objects.get_or_nothing(name=name) == ten_percent_promocode


@pytest.mark.usefixtures("ten_percent_promocode")
def test_not_found():
    assert PromoCode.objects.get_or_nothing(name="NONEXISTANT") is None


def test_not_found_when_promo_code_is_disabled(ten_percent_promocode):
    ten_percent_promocode.update(active=False)

    assert PromoCode.objects.get_or_nothing(name="TESTCODE") is None


@pytest.mark.freeze_time("2032-12-01 15:30:00+04:00")
@pytest.mark.parametrize(
    ("expires", "is_found"),
    [
        ("2032-12-01 15:30:00+04:00", True),
        ("2032-11-10 15:30:00+04:00", False),
        ("2032-12-05 15:30:00+04:00", True),
    ],
)
def test_not_found_when_promo_code_has_expired(ten_percent_promocode, expires, is_found):
    ten_percent_promocode.update(expires=expires)

    assert (PromoCode.objects.get_or_nothing(name="TESTCODE") is not None) is is_found


@pytest.mark.usefixtures("ten_percent_promocode")
def test_empty_name():
    assert PromoCode.objects.get_or_nothing(name=None) is None

### src/apps/orders/urls.py
from django.urls import path

from apps.orders.api import views

urlpatterns = [
    path("<str:slug>/confirm/", views.OrderConfirmationView.as_view(), name="confirm-order"),
    path("draft/", views.OrderDraftView.as_view()),
]

### src/apps/orders/api/views.py
from typing import Any, Type

from django.http import HttpResponseRedirect
from drf_spectacular.utils import OpenApiExample, extend_schema, inline_serializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from apps.banking import price_calculator
from apps.banking.api.serializers import Price, PriceSerializer
from apps.banking.base import Bank
from apps.banking.selector import get_bank_or_default
from apps.orders.api.serializers import OrderDraftRequestSerializer
from apps.orders.api.throttling import OrderDraftThrottle
from apps.orders.models import Order, PromoCode
from apps.products.api.serializers import CourseSimpleSerializer
from apps.products.models import Course
from core.throttling import PublicIDThrottle
from core.views import AnonymousAPIView


@extend_schema(
    responses={
        301: None,
    }
)
class OrderConfirmationView(RetrieveAPIView):
    """Redirects user to the confirmation URL"""

    queryset = Order.objects.available_to_confirm()
    lookup_field = "slug"
    permission_classes = [AllowAny]
    throttle_classes = [PublicIDThrottle]

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> HttpResponseRedirect:  # type: ignore
        order = self.get_object()

        order.set_paid()  # will be shipped on first confirmation

        return HttpResponseRedirect(redirect_to=order.item.confirmation_success_url)


class OrderDraftView(AnonymousAPIView):
    throttle_classes = [OrderDraftThrottle]

    @extend_schema(
        request=OrderDraftRequestSerializer,
        description="Create an order draft with given bank and promocode",
        responses={
            200: inline_serializer(
                name="OrderDraftSerializer",
                fields={
                    "course": CourseSimpleSerializer(),
                    "price": PriceSerializer(),
                },
            ),
        },
        examples=[
            OpenApiExample(
                name="Product slug",
                request_only=True,
                value={
                    "course": "popug-3-self",
                },
            ),
            OpenApiExample(
                name="Promocode",
                request_only=True,
                value={
                    "course": "popug-3-self",
                    "promocode": "MYSECRETCODE",
                },
            ),
            OpenApiExample(
                name="Particular bank",
                request_only=True,
      
...[truncated]...

### src/apps/orders/api/serializers.py
from rest_framework import serializers

from apps.banking.selector import BANK_CHOICES
from apps.products.models import Course


class OrderDraftRequestSerializer(serializers.Serializer):
    course = serializers.SlugRelatedField(queryset=Course.objects.all(), slug_field="slug")
    promocode = serializers.CharField(required=False)
    desired_bank = serializers.ChoiceField(choices=BANK_CHOICES, required=False)

### src/apps/orders/tests/orders/order_creator/tests_order_creator.py
import pytest

from apps.orders.models import Order

pytestmark = [pytest.mark.django_db]


def get_order():
    return Order.objects.last()


def test_user(create, user, course):
    order = create(user=user, item=course)

    order.refresh_from_db()

    assert order.user == user


def test_course(create, user, course):
    order = create(user=user, item=course)

    order.refresh_from_db()

    assert order.price == 100500
    assert order.item == course


def test_free_course(create, user, course):
    course.update(price=0)

    order = create(user=user, item=course)

    order.refresh_from_db()

    assert order.price == 0
    assert order.item == course
    assert order.paid is None


def test_course_manual(create, user, course):
    order = create(user=user, item=course)

    order.refresh_from_db()

    assert order.price == 100500
    assert order.item == course


@pytest.mark.parametrize("price", [0, 200500])
def test_forced_price(create, user, course, price):
    order = create(user=user, item=course, price=price)

    order.refresh_from_db()

    assert order.price == price

### src/apps/orders/tests/orders/order_creator/tests_order_creator_promocodes.py
import pytest

from apps.orders.models import Order

pytestmark = [pytest.mark.django_db]


def get_order():
    return Order.objects.last()


@pytest.fixture(autouse=True)
def testcode(mixer):
    return mixer.blend("orders.Promocode", name="TESTCODE", discount_percent=10)


@pytest.mark.parametrize(
    ("promocode", "expected"),
    [
        ("TESTCODE", 90450),
        ("", 100500),
        ("3V1l", 100500),
    ],
)
def test(promocode, expected, user, course, create):
    order = create(user=user, item=course, promocode=promocode)

    order.refresh_from_db()

    assert order.price == expected

### src/apps/orders/tests/orders/order_creator/tests_order_author.py
import pytest

pytestmark = [pytest.mark.django_db]


def test_default_author_is_the_order_user(create, user, course):
    order = create(user=user, item=course)

    order.refresh_from_db()

    assert order.author == user


@pytest.mark.usefixtures("_set_current_user")
def test_current_user_if_specified(create, user, another_user, course):
    order = create(user=another_user, item=course)

    order.refresh_from_db()

    assert order.author == user, "User is set from the current user"


def test_manualy_specified_author(create, user, another_user, course):
    order = create(user=user, item=course, author=another_user)

    order.refresh_from_db()

    assert order.author == another_user, "Manuly specified author"

### src/apps/orders/tests/orders/order_creator/tests_order_creator_confirmation_message.py
import pytest

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures("send_mail"),
]


@pytest.fixture(autouse=True)
def _freeze_frontend_host(settings):
    settings.FRONTEND_URL = "https://school.host"


def test_message_is_not_sent_by_default(create, user, course, send_mail):
    create(user=user, item=course)

    send_mail.assert_not_called()


def test_message_is_not_sent_on_non_free_courses(course, send_mail):
    course.update(
        confirmation_template_id="test-confirmation-template-id",
        price=100500,
    )

    send_mail.assert_not_called()


def test_message_is_sent_when_course_has_confirmation_template_id(create, user, course, send_mail):
    course.update(
        confirmation_template_id="test-confirmation-template-id",
        price=0,
    )

    order = create(user=user, item=course)

    send_mail.assert_called_once_with(
        to=user.email,
        template_id="test-confirmation-template-id",
        ctx=dict(
            item="Курс кройки и шитья",
            item_lower="курс кройки и шитья",
            firstname="Авраам Соломонович",
            confirmation_url=f"https://school.host/api/v2/orders/{order.slug}/confirm/",
        ),
    )

### src/apps/users/services/user_creator.py
import uuid
from dataclasses import dataclass

from django.utils.functional import cached_property
from rest_framework import serializers

from apps.dashamail import tasks as dashamail
from apps.dashamail.enabled import dashamail_enabled
from apps.users.models import User
from apps.users.random_name import random_name
from core.services import BaseService


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]


@dataclass
class UserCreator(BaseService):
    email: str
    name: str | None = ""
    force_subscribe: bool | None = False

    @cached_property
    def username(self) -> str:
        return self.email.lower() or str(uuid.uuid4())

    def act(self) -> User:
        existing_user = self.get()
        if existing_user is not None:
            return existing_user

        created_user = self.create()

        if self.force_subscribe and dashamail_enabled():
            self.push_to_dashamail(created_user)

        return created_user

    def get(self) -> User | None:
        if self.email:
            return User.objects.filter(is_active=True).filter(email__iexact=self.email).order_by("date_joined").first()

    def create(self) -> User:
        user = User.objects.create(
            email=self.email.lower(),
            username=self.username,
            random_name=random_name(),
            **User.parse_name(self.name or ""),
        )
        return user

    @staticmethod
    def push_to_dashamail(user: User) -> None:
        dashamail.update_subscription.apply_async(
            kwargs={"student_id": user.id},
            countdown=5,  # voodoo sleep to make sure the new row became available in all other transactions
        )

### src/apps/orders/services/order_creator.py
import json
from dataclasses import dataclass
from decimal import Decimal
from typing import Type
from urllib.parse import urljoin

from celery import chain
from django.conf import settings
from django.urls import reverse
from django.utils.functional import cached_property

from apps.amocrm.tasks import amocrm_enabled, push_order, push_user
from apps.b2b.models import Deal
from apps.banking.base import Bank
from apps.banking.selector import get_bank_or_default
from apps.dashamail import tasks as dashamail
from apps.dashamail.enabled import dashamail_enabled
from apps.mailing.tasks import send_mail
from apps.orders.models import Order, PromoCode
from apps.products.models import Course
from apps.users.models import User
from apps.users.tasks import rebuild_tags
from core.current_user import get_current_user
from core.exceptions import AppServiceException
from core.helpers import lower_first
from core.services import BaseService


class OrderCreatorException(AppServiceException):
    pass


@dataclass
class OrderCreator(BaseService):
    user: User
    item: Course
    subscribe: bool | None = False
    price: Decimal | None = None
    author: User | None = None
    promocode: str | PromoCode | None = None
    desired_bank: str | None = None
    analytics: str | None = None
    deal: Deal | None = None
    raw: dict | None = None

    def __post_init__(self) -> None:
        self.price = self.price if self.price is not None else self.item.price
        if isinstance(self.promocode, str):
            self.promocode = self._get_promocode(self.promocode)
        if self.promocode is not None:
            self.price = self.promocode.apply(self.item)

        self.desired_bank = self.desired_bank if self.desired_bank is not None else ""

    def get_author(self) -> User:
        """Author (seller) of the order.
        1. Particular author, e.g. when creating order from the b2b deal
        2. Current user, e.g. when creating order from the admin interface
        3. Student himself, self-ordering from the website
        """

        return next(author for author in [self.author, get_current_user(), self.user] if author is not None)

    def act(self) -> Order:
        order = self.create()

        order.set_item(self.item)
        order.save()

        self.save_acquring_details(order)

        self.send_confirmation_message(order)
        self.update_user_tags(order)

        if amocrm_enabled():
            self.push_to_amocrm(order)

        if self.subscribe and dashamail_enabled():
            self.push_to_dashamail(order)
            self.push_to_dasham
...[truncated]...

### src/apps/products/tests/products/course_api/tests_purchasing_course.py
import json
from decimal import Decimal

import pytest

from apps.orders.models import Order

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def rebuild_tags(mocker):
    return mocker.patch("apps.users.tasks.rebuild_tags.delay")


@pytest.fixture
def push_customer_to_amocrm(mocker):
    return mocker.patch("apps.amocrm.tasks.push_user.si")


@pytest.fixture
def push_to_dashamail(mocker):
    return mocker.patch("apps.orders.services.order_creator.OrderCreator.push_to_dashamail")


@pytest.fixture
def push_to_dashamail_directcrm(mocker):
    return mocker.patch("apps.orders.services.order_creator.OrderCreator.push_to_dashamail_directcrm")


@pytest.fixture
def push_order_to_amocrm(mocker):
    return mocker.patch("apps.amocrm.tasks.push_order.si")


def get_order():
    return Order.objects.last()


def test_order(call_purchase, course):
    call_purchase()

    placed = get_order()

    assert placed.item == course
    assert placed.price == Decimal("1900.00")
    assert not hasattr(placed, "study")  # Study record is not created yet, because order is not paid


def test_user(call_purchase):
    call_purchase()

    placed = get_order()

    assert placed.user.first_name == "Забой"
    assert placed.user.last_name == "Шахтёров"
    assert placed.user.email == "zaboy@gmail.com"


def test_analytics_metadata(call_purchase):
    call_purchase(
        analytics=json.dumps(
            {
                "test_param": "test_value",
                "empty": None,
            }
        )
    )
    placed = get_order()

    assert placed.analytics["test_param"] == "test_value"
    assert placed.analytics["empty"] is None


@pytest.mark.parametrize(
    "weird",
    [
        "None",
        "'test':'case",
        "test':case",
        "test:",
        "test:'",
        "test:''",
    ],
)
def test_weird_analytics_params_do_not_break_order_creation(call_purchase, weird):
    call_purchase(analytics=weird)

    placed = get_order()

    assert placed is not None
    assert "name" in placed.raw


def test_order_creation_does_not_fail_with_nonexistant_params(call_purchase):
    """Need this test cuz we may alter frontend request without corresponding changes on backend"""
    call_purchase(
        **{  # NOQA: PIE804
            "nonexistant": "None",
            "Петрович": "Львович",
        }
    )

    placed = get_order()

    assert placed is not None
    assert "Петрович" in placed.raw


@pytest.mark.dashamail
@pytest.mark.parametrize(
    ("subscribe", "should_be_subscribed"),
    [
        (True, True),
        (False, False),
        ("tRue", Tr
...[truncated]...

### src/apps/products/tests/products/course_api/tests_purchasing_course_with_promocode.py
from decimal import Decimal

import pytest

from apps.orders.models import Order

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures("testcode"),
]


def get_order():
    return Order.objects.last()


@pytest.fixture
def another_course(factory):
    return factory.course(slug="kamazing-navoza", price=100500)


@pytest.mark.parametrize(
    ("promocode", "expected"),
    [
        ("TESTCODE", 1710),
        ("", 1900),
        ("3V1L_H4XX0R", 1900),
    ],
)
def test_purchasing_with_promocode(call_purchase, course, promocode, expected):
    call_purchase(promocode=promocode)

    placed = get_order()

    assert placed.item == course
    assert placed.price == Decimal(expected)


def test_incompatible_promocode(call_purchase, another_course, testcode):
    testcode.courses.add(another_course)

    call_purchase(promocode="TESTCODE")
    placed = get_order()

    assert placed.price == Decimal(1900), "promocode should not be accepteed"


@pytest.mark.freeze_time("2032-12-01 23:59")
def test_expired_promocode(call_purchase, testcode):
    testcode.update(expires="2032-11-01 15:30:00+02:00")

    call_purchase(promocode="TESTCODE")
    placed = get_order()

    assert placed.price == Decimal(1900), "promocode should not be accepteed"


def test_promocode_is_stored(call_purchase, testcode):
    call_purchase(promocode="TESTCODE")

    placed = get_order()

    assert placed.promocode == testcode


def test_promocode_is_empty_when_no_promocode_supplied(call_purchase):
    call_purchase()

    placed = get_order()

    assert placed.promocode is None

### src/apps/products/tests/products/course_api/tests_purchasing_zero_priced_course.py
from decimal import Decimal

import pytest

from apps.orders.models import Order

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def course(course):
    return course.update(price=0)


def get_order() -> Order | None:
    return Order.objects.last()


def test_order_is_created(call_purchase, course):
    call_purchase(desired_bank="zero_price", redirect_url="https://thank.you")

    placed = get_order()

    assert placed.item == course
    assert placed.price == Decimal(0)
    assert placed.paid is None
    assert placed.bank_id == "zero_price"
    assert placed.acquiring_percent == 0
    assert placed.ue_rate == 1


def test_redirect(call_purchase):
    response = call_purchase(as_response=True)

    assert response.status_code == 302
    assert response["Location"] == "https://bank.test/pay/"

### src/apps/orders/tests/orders/test_purchasing_order_with_non_trimmed_email.py
import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture(autouse=True)
def course(factory):
    return factory.course(slug="ruloning-oboev", price=1900)


@pytest.fixture(autouse=True)
def user_with_the_same_username_but_without_a_space_in_the_end(mixer):
    user = mixer.blend("users.User", email="zaboy@gmail.com")

    return user.update(username="zaboy@gmail.com")  # workaround for make_username_truly_random(), we need particular username here


@pytest.fixture(autouse=True)
def bank(mocker):
    return mocker.patch("apps.tinkoff.bank.TinkoffBank.get_initial_payment_url", return_value="https://mocked")


@pytest.fixture
def call_purchase(api):
    return lambda **kwargs: api.post(
        "/api/v2/courses/ruloning-oboev/purchase/",
        data=kwargs,
        format="multipart",
        expected_status_code=302,
    )


@pytest.mark.parametrize(
    "email",
    [
        "zaboy@gmail.com ",
        " zaboy@gmail.com",
    ],
)
def test(call_purchase, bank, email):
    call_purchase(name="Забой Шахтёров", email=email)

    bank.assert_called_once()