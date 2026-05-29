# README-derived retrieval query
tough dev school education backend ## README.md
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
* No l10n is allowed in python code, use [django translation](https://docs.djangoproject.com/en/dev/topics/i18n/translation/). .hadolint.yaml
.yamllint.yml
AGENTS.md
README.md
compose.yml
conftest.py
pyproject.toml
renovate.json
src/apps/__init__.py
src/apps/a12n/__init__.py
src/apps/a12n/admin.py
src/apps/a12n/api/forms.py
src/apps/a12n/api/serializers.py
src/apps/a12n/api/throttling.py
src/apps/a12n/api/views.py
src/apps/a12n/apps.py
src/apps/a12n/jwt.py
src/apps/a12n/models.py
src/apps/a12n/signals/handlers.py
src/apps/a12n/tests/__init__.py
src/apps/a12n/tests/api/tests_obtain_jwt_via_passwordless_token.py
src/apps/a12n/tests/api/tests_obtain_jwt_via_user_id.py
src/apps/a12n/tests/api/tests_obtain_token.py
src/apps/a12n/tests/api/tests_password_change.py
src/apps/a12n/tests/api/tests_password_reset_confirm.py
src/apps/a12n/tests/api/tests_refresh_token.py
src/apps/a12n/tests/api/tests_request_password_reset.py
src/apps/a12n/tests/api/tests_request_passwordless_token.py
src/apps/a12n/tests/tests_jwt_blacklisting.py
src/apps/a12n/tests/tests_passwordless_token_absolute_url.py
src/apps/a12n/urls.py
src/apps/a12n/utils.py
src/apps/amocrm/__init__.py
src/apps/amocrm/apps.py
src/apps/amocrm/client/__init__.py
src/apps/amocrm/client/client.py
src/apps/amocrm/client/http.py
src/apps/amocrm/dto/__init__.py
src/apps/amocrm/dto/catalogs.py
src/apps/amocrm/dto/customer.py
src/apps/amocrm/dto/groups.py
src/apps/amocrm/dto/lead.py
src/apps/amocrm/dto/lead_note.py
src/apps/amocrm/dto/lead_task.py
src/apps/amocrm/dto/pipelines.py
src/apps/amocrm/dto/product.py
src/apps/amocrm/dto/transaction.py
src/apps/amocrm/dto/user_operator.py
src/apps/amocrm/exceptions.py
src/apps/amocrm/ids.py
src/apps/amocrm/models/__init__.py
src/apps/amocrm/models/amocrm_course.py
src/apps/amocrm/models/amocrm_order_lead.py
src/apps/amocrm/models/amocrm_order_transaction.py
src/apps/amocrm/models/amocrm_product_group.py
src/apps/amocrm/models/amocrm_user.py
src/apps/amocrm/services/__init__.py
src/apps/amocrm/services/access_token_getter.py
src/apps/amocrm/services/course_pusher.py
src/apps/amocrm/services/group_pusher.py
src/apps/amocrm/services/orders/order_pusher.py
src/apps/amocrm/services/orders/order_returner.py
src/apps/amocrm/services/orders/order_task_creator.py
src/apps/amocrm/services/user_pusher.py
src/apps/amocrm/tasks.py
src/apps/amocrm/tests/__init__.py
src/apps/amocrm/tests/conftest.py
src/apps/amocrm/tests/dto/conftest.py
src/apps/amocrm/tests/dto/tests_catalogs.py
src/apps/amocrm/tests/dto/tests_customer.py
src/apps/amocrm/tests/dto/tests_groups.py
src/apps/amocrm/tests/dto/tests_lead.py
src/apps/amocrm/tests/dto/tests_lead_note.py
src/apps/amocrm/tests/dto/tests_lead_task.py
src/apps/amocrm/tests/dto/tests_pipelines.py
src/apps/amocrm/tests/dto/tests_product.py
src/apps/amocrm/tests/dto/tests_transaction.py
src/apps/amocrm/tests/dto/tests_user_operator.py
src/apps/amocrm/tests/http/__init__.py
src/apps/amocrm/tests/http/tests_http.py
src/apps/amocrm/tests/ids/tests_b2c_pipeline_id.py
src/apps/amocrm/tests/ids/tests_catalog_id.py
src/apps/amocrm/tests/ids/tests_contact_fields_ids.py
src/apps/amocrm/tests/ids/tests_product_fields_ids.py
src/apps/amocrm/tests/servic
...[truncated]...

# BM25 selected code snippets
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

### AGENTS.md
# Django Backend Development Guide

## Development cycle
- Ignore all typing errors if the code is a valid python
- Do not generate or run any tests until asked explicitly
- Prefer Django ORM features (managers, querysets) over raw SQL
- Keep models thin, use services for business logic
- Use factory pattern for object creation in tests
- Never check exceptions in the management commands


## Build/Test Commands
- Use uv for package management and running commands
- `make fmt` - Format the code using ruff
- `make lint` - Run all linters (ignore mypy errors)
- Run a single test: `cd src && uv run python -m pytest path/to/test_file.py::test_function -v`
- Run tests matching pattern: `cd src && uv run python -m pytest -k "pattern" -v`
- Run server: `make server`
- Run worker: `make worker`
- Run django manage command: `cd src && uv run python manage.py`


## Code Style
- Line length: 160 characters max
- Type checking: Use mypy annotations for all non-test code. Never use type annotations in tests
- Use absolute imports, no relative imports
- Class/variable naming: Follow Django conventions with snake_case
- Never create `__init__.py`
- Tests: Use pytest fixtures, keep tests atomic and isolated
- Tests: Use Model.update() for changing model properties in the test code. I.e. instead of `object.property = 'test' \n object.save()` use `object.update(property='test')`.

### compose.yml
services:
  postgres:
    image: postgres:15-alpine
    # contact us to gain access to the anonymized dump
    # image: ghcr.io/tough-dev-school/dev-db
    environment:
      - POSTGRES_PASSWORD=secret
    ports:
     - 5432:5432
    volumes:
      - dev-db-data:/var/lib/postgresql/data

  redis:
    image: redis:6-alpine
    ports:
      - 6379:6379

  s3:
    image: bitnamilegacy/minio
    environment:
      - MINIO_ROOT_USER=root
      - MINIO_ROOT_PASSWORD=ibcxJ8Du
      - MINIO_DEFAULT_BUCKETS=dev:public
    volumes:
      - s3-data:/data
    ports:
      - 9000:9000
      - 9001:9001

volumes:
  dev-db-data:
  s3-data:

### src/core/conf/http.py
from core.conf.environ import env

ABSOLUTE_HOST = env("ABSOLUTE_HOST", cast=str, default="https://app.tough-dev.school")
ALLOWED_HOSTS = ["*"]

CSRF_USE_SESSIONS = True
CORS_ALLOWED_ORIGINS = [
    "https://education.borshev.com",
    "https://tough-dev.school",
    "https://certificates.tough-dev.school",
    "https://lms.tough-dev.school",
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://.*\.lms-frontend-v2\.pages\.dev",
]

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

FRONTEND_URL = env("FRONTEND_URL", cast=str, default="https://lms.tough-dev.school/")
DIPLOMA_FRONTEND_URL = env("DIPLOMA_FRONTEND_URL", cast=str, default="https://cert.tough-dev.school/")

HTTP_CACHE_REDIS_URL = env("REDISCLOUD_URL", cast=str, default="")

### src/apps/amocrm/services/orders/order_task_creator.py
from dataclasses import dataclass
from datetime import timedelta
from typing import NamedTuple

from django.utils import timezone
from django.utils.functional import cached_property

from apps.amocrm import types
from apps.amocrm.dto import AmoCRMLeadNoteDTO, AmoCRMLeadTaskDTO, AmoCRMUserOperatorDTO
from apps.orders.models import Order
from core.services import BaseService


class AmoCRMOrderTaskCreatorException(Exception):
    """Raise when the AmoCRMOrderTaskCreator fails.

    The exception is inherited from the base 'Exception' because the service is intended for internal usage only.
    This implies that any exceptions are indicative of programming errors and must be captured by Sentry.
    """


class AmoCRMOrderTaskDataServiceNote(NamedTuple):
    service_name: str
    service_note: str


class AmoCRMOrderTaskData(NamedTuple):
    task_name: str
    task_type_id: types.TaskType
    task_responsible_user_email: str
    task_deadline_timedelta: timedelta = timedelta(days=3)
    service_note: AmoCRMOrderTaskDataServiceNote | None = None


@dataclass
class AmoCRMOrderTaskCreator(BaseService):
    """Create task in AmoCRM for the lead linked with the order.

    1. Locate the corresponding lead for the order.
    2. If 'service note' provided add it as 'service message' to the located lead.
    3. Look for existed not completed lead task with the same name and type. If not found — create new one.
    """

    order: Order
    task_data: AmoCRMOrderTaskData

    @cached_property
    def lead_id(self) -> int:
        if self.order.amocrm_lead:
            return self.order.amocrm_lead.amocrm_id

        return Order.objects.same_deal(self.order).filter(amocrm_lead__isnull=False).values_list("amocrm_lead__amocrm_id", flat=True)[0]

    @cached_property
    def responsible_user_id(self) -> int:
        for amo_user_operator in AmoCRMUserOperatorDTO().get():
            if amo_user_operator.email == self.task_data.task_responsible_user_email:
                return amo_user_operator.id

        raise AmoCRMOrderTaskCreatorException(f"There is no AmoCRM operators with email '{self.task_data.task_responsible_user_email}'")

    def act(self) -> None:
        self.validate_order()

        if self.task_data.service_note:
            AmoCRMLeadNoteDTO().create_service_message(
                lead_id=self.lead_id,
                service_name=self.task_data.service_note.service_name,
                note_text=self.task_data.service_note.service_note,
            )

        self.create_lead_task_if_needed()

    def validate_order(self) -> None:
        if self.
...[truncated]...

### src/apps/b2b/admin/deals/admin.py
from typing import TYPE_CHECKING

from django.http import HttpRequest
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy

from apps.b2b.admin.deals import actions
from apps.b2b.admin.deals.forms import DealChangeForm, DealCreateForm
from apps.b2b.admin.students import StudentInline
from apps.b2b.models import Deal
from core.admin import ModelAdmin, admin

if TYPE_CHECKING:
    from django_stubs_ext import StrPromise


@admin.register(Deal)
class DealAdmin(ModelAdmin):
    list_display = [
        "customer",
        "price_formatted",
        "currency",
        "orders",
        "status",
        "author",
    ]
    fields = [
        "author",
        "customer",
        "course",
        "price",
        "currency",
        "comment",
        "students",
        "orders",
    ]
    add_form = DealCreateForm
    form = DealChangeForm
    readonly_fields = [
        "author",
        "orders",
    ]
    inlines = [StudentInline]
    actions = [
        actions.complete,
        actions.ship_without_payment,
        actions.cancel,
    ]
    foreignkey_queryset_overrides = {
        "b2b.Deal.course": lambda apps: apps.get_model("products.Course").objects.for_admin(),
    }

    @mark_safe
    @admin.display(description=pgettext_lazy("deals", "Orders"))
    def orders(self, obj: Deal) -> str:
        url = reverse("admin:orders_order_changelist") + f"?deal__id__exact={obj.pk}"

        orders_count = obj.orders.count()

        if orders_count == 0:
            return "—"

        return f"<a target='_blank' href='{url}'>{orders_count}</a>"

    @admin.display(description=_("Status"))
    def status(self, obj: Deal) -> "StrPromise":
        return obj.get_status_representation()

    @admin.display(description=_("Price"), ordering="price")
    def price_formatted(self, obj: Deal) -> str:
        return self._price(obj.price)

    def get_readonly_fields(self, request: HttpRequest, obj: Deal | None = None) -> list[str]:
        """Block changes for complete and canceled deals"""
        if obj is None or (obj.canceled is None and obj.completed is None):
            return list(super().get_readonly_fields(request, obj))

        return [
            *super().get_readonly_fields(request, obj),
            "customer",
            "course",
            "price",
            "currency",
        ]

### src/apps/homework/services/question_crosscheck_dispatcher.py
from dataclasses import dataclass

from django.db.models import QuerySet

from apps.homework.models import Answer, AnswerCrossCheck, Question
from apps.homework.services.answer_crosscheck_dispatcher import AnswerCrossCheckDispatcher
from apps.lms.models import Lesson
from apps.mailing.tasks import send_mail
from apps.users.models import User
from core.services import BaseService


@dataclass
class QuestionCrossCheckDispatcher(BaseService):
    """Dispatches crosschecks for given question (and its neighbours).

    To improve readability, the user story is split in 2 services:
        - QuestionCrossCheckDispatcher (this one) finds the answers to mix between students
        - AnswerCrossCheckDispatcher mixes them between students
    """

    question: Question
    author: User
    answers_per_user: int = 3

    def act(self) -> int:
        self.crosschecks = self.dispatch_crosschecks()
        self.notify_users()

        return self.get_users_to_notify().count()

    def dispatch_crosschecks(self) -> list[AnswerCrossCheck]:
        dispatcher = AnswerCrossCheckDispatcher(
            answers=self.get_answers_to_check(),
            author=self.author,
            answers_per_user=self.answers_per_user,
        )
        return dispatcher()

    def notify_users(self) -> None:
        for user in self.get_users_to_notify():
            user_crosschecks_list = self.get_crosschecks_for_user(user)
            send_mail.delay(
                to=user.email,
                template_id="new-answers-to-check",
                ctx=self.get_notification_context(user_crosschecks_list),
                disable_antispam=True,
            )

    def get_users_to_notify(self) -> QuerySet[User]:
        return User.objects.filter(pk__in=[check.checker_id for check in self.crosschecks])

    def get_crosschecks_for_user(self, user: User) -> list[AnswerCrossCheck]:
        return [crosscheck for crosscheck in self.crosschecks if crosscheck.checker == user]

    def get_answers_to_check(self) -> QuerySet[Answer]:
        questions = self.get_questions_to_check()
        return (
            Answer.objects.filter(question__in=questions)
            .root_only()
            .exclude(
                do_not_crosscheck=True,
            )
        )

    def get_questions_to_check(self) -> QuerySet[Question]:
        """
        Questions with the same name that belong to the same product.group
        """
        current_lesson = Lesson.objects.filter(question=self.question).first()
        if current_lesson is None:
            return Question.objects.filter(pk=self.quest
...[truncated]...

### src/apps/b2b/admin/deals/forms.py
from typing import Any

from django import forms
from django.utils.translation import gettext_lazy as _

from apps.b2b.models import Deal
from apps.b2b.services import BulkStudentCreator, DealCreator, DealCurrencyChanger
from core.admin import ModelForm


class DealCreateForm(ModelForm):
    author = forms.CharField(required=False, widget=forms.HiddenInput)
    students = forms.CharField(
        label=_("Students"),
        required=False,
        widget=forms.Textarea,
    )

    class Meta:
        model = Deal
        fields = "__all__"

    def save(self, commit: bool = False) -> Deal:
        deal = DealCreator(
            customer=self.cleaned_data["customer"],
            course=self.cleaned_data["course"],
            price=self.cleaned_data["price"],
            currency=self.cleaned_data["currency"],
        )()

        student_list = self.cleaned_data["students"]
        if len(student_list) > 0:
            BulkStudentCreator(user_input=student_list, deal=deal)()

        return deal

    def save_m2m(self, *args: Any, **kwargs: dict[str, Any]) -> None: ...


class DealChangeForm(forms.ModelForm):
    students = forms.CharField(
        label=_("Bulk students add"),
        help_text=_("For complete deals new students will create new orders"),
        required=False,
        widget=forms.Textarea,
    )

    class Meta:
        model = Deal
        fields = "__all__"

    def save(self, commit: bool = False) -> Deal:
        self._change_currency(deal=self.instance)

        deal = super().save(commit=commit)

        self._create_students(deal)

        return deal

    def _change_currency(self, deal: Deal) -> None:
        currency = self.cleaned_data["currency"]
        if self.initial["currency"] != currency:
            DealCurrencyChanger(deal, new_currency_code=currency)()

    def _create_students(self, deal: Deal) -> None:
        student_list = self.cleaned_data["students"]
        if len(student_list) > 0:
            BulkStudentCreator(user_input=student_list, deal=deal)()

### src/apps/homework/tests/homework/cross_check/tests_question_crosscheck_dispatcher.py
import pytest

from apps.homework import tasks
from apps.homework.models import AnswerCrossCheck

pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture(autouse=True)
def common_group_for_both_courses(course, another_course, mixer):
    group = mixer.blend("products.Group")

    course.update(group=group)
    another_course.update(group=group)

    return group


def test_crosschecks_are_created(question_dispatcher):
    question_dispatcher()

    assert AnswerCrossCheck.objects.count() == 2


@pytest.mark.usefixtures("answers_to_another_question")
def test_answers_to_another_questions_are_ignored(question_dispatcher, question, another_question):
    first_question_course = question.lesson_set.first().module.course
    second_question_course = another_question.lesson_set.first().module.course
    assert first_question_course != second_question_course, "Questions are attached to the different courses"
    assert first_question_course.group == second_question_course.group, "Courses have the same group"

    question_dispatcher()

    assert AnswerCrossCheck.objects.count() == 2


@pytest.mark.usefixtures("answers_to_another_question")
def test_answers_to_another_questions_are_dispatched_if_product_and_name_match(question, another_question, question_dispatcher):
    question.update(name="Одинаковая домаЩка")  # also check case insensitiviy
    another_question.update(name="Одинаковая домащка")

    question_dispatcher()

    assert AnswerCrossCheck.objects.count() == 4


@pytest.mark.usefixtures("answers_to_another_question")
def test_anothers_to_another_questions_are_not_dispatched_if_name_matches_but_product_does_not(question, another_question, question_dispatcher, mixer):
    """Same as above, but changing product group of one of the courses"""
    question.update(name="Одинаковая домаЩка")
    another_question.update(name="Одинаковая домащка")

    question.lesson_set.first().module.course.update(group=mixer.blend("products.Group"))  # this removes 2 questions from the crosscheck

    question_dispatcher()

    assert AnswerCrossCheck.objects.count() == 2


def test_question_method_does_the_same(question, admin):
    question.dispatch_crosscheck(author=admin, answers_per_user=1)

    assert AnswerCrossCheck.objects.count() == 2


def test_task_does_the_same(question, admin):
    tasks.dispatch_crosscheck.delay(question_id=question.pk, author_id=admin.pk)

    assert AnswerCrossCheck.objects.count() == 2


def test_email_is_sent(question_dispatcher, send_mail, mocker, answers):
    question_dispatcher()

    assert send_mail.call_count == 2
    se
...[truncated]...

### src/core/conf/email.py
from core.conf.environ import env

EMAIL_ENABLED = env("EMAIL_ENABLED", cast=bool, default=False)

EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

DEFAULT_FROM_EMAIL = env("EMAIL_FROM", cast=str, default="")
DEFAULT_REPLY_TO = env("REPLY_TO", cast=str, default=DEFAULT_FROM_EMAIL)

ANYMAIL = {
    "POSTMARK_SERVER_TOKEN": env("POSTMARK_SERVER_TOKEN", cast=str, default=""),
    "DEBUG_API_REQUESTS": env("DEBUG"),
}

RECEIPTS_EMAIL = env("RECEIPTS_EMAIL", cast=str, default="receipts@tough-dev.school")
DANGEROUS_OPERATION_HAPPENED_EMAILS = env(
    "DANGEROUS_OPERATION_HAPPENED_EMAILS",
    cast=tuple,
    default=["fedor@borshev.com", "marianaonysko@gmail.com"],
)
PER_COURSE_EMAIL_CONFIGURATION = env("PER_COURSE_EMAIL_CONFIGURATION", cast=bool, default=False)

# Postmark template IDs
PASSWORDLESS_TOKEN_TEMPLATE_ID = env("PASSWORDLESS_TOKEN_TEMPLATE_ID", cast=str, default="passwordless-token")
PASSWORD_RESET_TEMPLATE_ID = env("PASSWORD_RESET_TEMPLATE_ID", cast=str, default="password-reset")

### src/apps/amocrm/tasks.py
from celery import Task
from django.apps import apps
from django.conf import settings
from httpx import TransportError

from apps.amocrm.client import AmoCRMClient
from apps.amocrm.client.http import AmoCRMClientException
from apps.amocrm.services.access_token_getter import AmoCRMTokenGetterException
from apps.amocrm.services.course_pusher import AmoCRMCoursePusher
from apps.amocrm.services.group_pusher import AmoCRMGroupsPusher
from apps.amocrm.services.orders.order_pusher import AmoCRMOrderPusher
from apps.amocrm.services.orders.order_returner import AmoCRMOrderReturner
from apps.amocrm.services.user_pusher import AmoCRMUserPusher
from core.celery import celery

__all__ = [
    "amocrm_enabled",
    "push_all_products_and_product_groups",
    "push_course",
    "push_order",
    "push_product_groups",
    "push_user",
    "return_order",
]


class AmoTask(Task):
    autoretry_for = [TransportError, AmoCRMTokenGetterException, AmoCRMClientException]
    retry_kwargs = {
        "max_retries": 10,
        "countdown": 1,
    }
    rate_limit = "3/s"
    acks_late = True


def amocrm_enabled() -> bool:
    return settings.AMOCRM_BASE_URL != ""


@celery.task(base=AmoTask)
def push_user(user_id: int) -> None:
    user = apps.get_model("users.User").objects.get(id=user_id)
    AmoCRMUserPusher(user=user)()


@celery.task(base=AmoTask)
def push_order(order_id: int) -> None:
    order = apps.get_model("orders.Order").objects.get(id=order_id)
    AmoCRMOrderPusher(order=order)()


@celery.task(base=AmoTask)
def return_order(order_id: int) -> None:
    order = apps.get_model("orders.Order").objects.get(id=order_id)
    AmoCRMOrderReturner(order=order)()


@celery.task(base=AmoTask)
def push_product_groups() -> None:
    AmoCRMGroupsPusher()()


@celery.task(base=AmoTask)
def push_course(course_id: int) -> None:
    course = apps.get_model("products.Course").objects.get(id=course_id)
    AmoCRMCoursePusher(course=course)()


@celery.task(base=AmoTask)
def push_all_products_and_product_groups() -> None:
    push_product_groups.apply_async(link=_push_all_courses.si())


@celery.task(base=AmoTask)
def enable_customers() -> None:
    client = AmoCRMClient()
    client.enable_customers()


@celery.task(base=AmoTask)
def _push_all_courses() -> None:
    courses = apps.get_model("products.Course").objects.all()
    for course in courses:
        push_course.delay(course_id=course.id)

### src/apps/b2b/services/deal_completer.py
from dataclasses import dataclass

from django.conf import settings
from django.contrib.admin.models import CHANGE
from django.utils import timezone

from apps.b2b.models import Deal
from apps.b2b.utils import assign_existing_orders, create_orders
from apps.banking import currency
from apps.orders.models import Order
from core.current_user import get_current_user
from core.pricing import format_price
from core.services import BaseService
from core.tasks import send_telegram_message, write_admin_log


@dataclass
class DealCompleter(BaseService):
    """Creates orders for the given deal"""

    deal: Deal
    ship_only: bool | None = False

    def act(self) -> None:
        if self.deal.completed is not None:
            return

        orders: list[Order] = []

        orders += create_orders(deal=self.deal, single_order_price=self.deal.get_single_order_price())
        orders += assign_existing_orders(deal=self.deal)

        if not self.ship_only:
            self.pay_and_ship(orders)  # this will pay and ship them
            self.send_happiness_message()
            self.mark_deal_as_complete()
            self.write_auditlog()
        else:
            self.ship_without_payment(orders)  # this will only ship
            self.mark_deal_as_shipped_without_payment()
            self.write_auditlog()

    def mark_deal_as_complete(self) -> None:
        self.deal.completed = timezone.now()
        self.deal.save()

    def mark_deal_as_shipped_without_payment(self) -> None:
        self.deal.shipped_without_payment = timezone.now()
        self.deal.save()

    @staticmethod
    def pay_and_ship(orders: list[Order]) -> None:
        for order in orders:
            order.set_paid(silent=True)

    @staticmethod
    def ship_without_payment(orders: list[Order]) -> None:
        for order in orders:
            order.ship_without_payment()

    def send_happiness_message(self) -> None:
        if not settings.HAPPINESS_MESSAGES_CHAT_ID:
            return

        send_telegram_message.delay(
            chat_id=settings.HAPPINESS_MESSAGES_CHAT_ID,
            text=f"💰+{format_price(self.deal.price)} {currency.get_symbol(self.deal.currency)}, {self.deal.customer}, {self.deal.course} продавец {self.deal.author}",
        )

    def write_auditlog(self) -> None:
        user = get_current_user()
        if user is None:
            raise RuntimeError("Cannot determine user")

        write_admin_log.delay(
            action_flag=CHANGE,
            change_message="Deal shipped without payment" if self.ship_only else "Deal completed",
            model="b2b
...[truncated]...

### src/apps/homework/tests/homework/api/answers/list/tests_answer_list_descendants.py
import pytest
from django.utils import timezone

pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture(autouse=True)
def answer(mixer, api, question):
    return mixer.blend("homework.Answer", author=api.user, question=question, parent=None)


@pytest.mark.usefixtures("comments", "crosschecks")
def test_no_comments_when_crosscheck_is_dispatched_but_user_did_not_perform_it(api, question):
    got = api.get(f"/api/v2/homework/answers/?question={question.slug}")["results"]

    assert got[0]["has_descendants"] is False


@pytest.mark.usefixtures("comments")
def test_users_without_crosschecks_see_all_descendandts(api, question, crosschecks, another_user):
    crosschecks["to_perform"].update(checker=another_user)

    got = api.get(f"/api/v2/homework/answers/?question={question.slug}")["results"]

    assert got[0]["has_descendants"] is True


@pytest.mark.xfail(strict=True, reason="WIP for @brachkow")
@pytest.mark.usefixtures("comments", "crosschecks")
def test_use_is_able_to_access_his_own_comments_even_when_they_did_not_perform_a_crosscheck(api, mixer, answer):
    mixer.blend("homework.Answer", parent=answer.parent, question=answer.question, author=api.user)

    got = api.get("/api/v2/homework/answers/")

    assert got[0]["has_descendants"] is True


@pytest.mark.usefixtures("comments")
def test_crosscheck_is_performed(api, crosschecks, question):
    crosschecks["to_perform"].update(checked=timezone.now())

    got = api.get(f"/api/v2/homework/answers/?question={question.slug}")["results"]

    assert got[0]["has_descendants"] is True


@pytest.mark.usefixtures("comments", "one_more_crosscheck_that_user_should_perform")
def test_only_one_crosscheck_is_performed(api, question, crosschecks):
    crosschecks["to_perform"].update(checked=timezone.now())  # check only one crosscheck, leaving the second one unchecked

    got = api.get(f"/api/v2/homework/answers/?question={question.slug}")["results"]

    assert got[0]["has_descendants"] is True


@pytest.mark.usefixtures("comments", "one_more_crosscheck_that_user_should_perform")
def test_endpoint_does_not_die_for_users_with_permissions(api, question, crosschecks):
    api.user.add_perm("homework.answer.see_all_answers")
    crosschecks["to_perform"].update(checked=timezone.now())  # check only one crosscheck, leaving the second one unchecked

    got = api.get(f"/api/v2/homework/answers/?question={question.slug}")["results"]

    assert got[0]["has_descendants"] is True


@pytest.mark.usefixtures("comments", "crosschecks")
def test_comments_from_users_with_always_display_comments_are_visible_in_li
...[truncated]...

### src/apps/b2b/tests/deal_completer/test_deal_completer_new_order_creation.py
from decimal import Decimal

import pytest

from apps.orders.models import Order

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures("usd"),
]


def test_orders_are_created(completer, factory):
    completer(deal=factory.deal(student_count=3))()

    assert Order.objects.count() == 3


def test_order_data_for_created_orders(completer, factory):
    deal = factory.deal(student_count=1)

    completer(deal=deal)()
    order = Order.objects.first()

    assert order.deal == deal, "Order should be linked to the deal"
    assert order.author == deal.author
    assert order.user == deal.students.first().user
    assert order.item == deal.course
    assert order.bank_id == "b2b"


def test_orders_are_paid_and_shipped(completer, factory):
    deal = factory.deal(student_count=1)

    completer(deal=deal)()
    order = Order.objects.first()

    assert order.paid is not None
    assert order.shipped is not None


def test_created_orders_are_paid(completer, factory):
    completer(deal=factory.deal(student_count=1))()
    order = Order.objects.first()

    assert order.paid is not None


@pytest.mark.parametrize(
    ("student_count", "single_order_price"),
    [
        (1, "100.50"),
        (3, "33.50"),
        (4, "25.13"),
        (5, "20.10"),
    ],
)
def test_price_calculation(completer, factory, student_count, single_order_price):
    deal = factory.deal(student_count=student_count, price=Decimal("100.50"))

    completer(deal=deal)()
    order = Order.objects.first()

    assert str(order.price) == single_order_price


@pytest.mark.usefixtures("usd")
@pytest.mark.parametrize(
    ("currency_code", "single_order_price"),
    [
        ("RUB", "50.00"),
        ("USD", "5000.00"),
        ("NNE", "50.00"),  # for nonexistant currencis the default rate is used
    ],
)
def test_currency_price_calculation(completer, factory, currency_code, single_order_price):
    deal = factory.deal(student_count=2, price=Decimal("100.00"), currency_code=currency_code)

    completer(deal=deal)()
    order = Order.objects.first()

    assert str(order.price) == single_order_price


def test_zero_price(factory):
    deal = factory.deal(student_count=0, price=Decimal(0))
    assert deal.get_single_order_price() == 0

### src/apps/dashamail/tasks.py
import httpx
from django.apps import apps

from apps.dashamail import exceptions
from apps.dashamail.directcrm import events as directcrm_events
from apps.dashamail.lists.dto import DashamailSubscriber
from apps.dashamail.services import DashamailDirectCRMSubscriber
from core.celery import celery


@celery.task(
    autoretry_for=[httpx.HTTPError, exceptions.DashamailException],
    retry_kwargs={
        "max_retries": 10,
        "countdown": 5,
    },
    rate_limit="1/s",
    name="dashamail.update_subscription",
)
def update_subscription(student_id: int) -> None:
    user = apps.get_model("users.User").objects.get(pk=student_id)

    DashamailSubscriber(user).subscribe()


@celery.task(
    autoretry_for=[httpx.HTTPError, exceptions.DashamailDirectCRMException],
    retry_kwargs={
        "max_retries": 10,
        "countdown": 5,
    },
    rate_limit="1/s",
    name="dashamail.directcrm.push_order_event",
)
def push_order_event(event_name: str, order_id: int) -> None:
    order = apps.get_model("orders.Order").objects.get(pk=order_id)
    Event = getattr(directcrm_events, event_name)
    Event(order).send()


@celery.task(
    autoretry_for=[httpx.HTTPError, exceptions.DashamailException],
    retry_kwargs={
        "max_retries": 10,
        "countdown": 5,
    },
    rate_limit="1/s",
    name="dashamail.directcrm.subscribe",
)
def directcrm_subscribe(order_id: int) -> None:
    order = apps.get_model("orders.Order").objects.get(pk=order_id)

    subscriber = DashamailDirectCRMSubscriber(
        user=order.user,
        product=order.course,
    )

    subscriber()

### src/apps/diplomas/services/diploma_regenerator.py
from dataclasses import dataclass
from typing import cast

from django.db.models import QuerySet

from apps.diplomas.models import Diploma, DiplomaTemplate
from apps.diplomas.services.diploma_generator import DiplomaGenerator
from apps.mailing.tasks import send_mail
from apps.studying.models import Study
from apps.users.models import User
from core.services import BaseService
from core.types import Language


@dataclass
class DiplomaRegenerator(BaseService):
    """Update and create student's diplomas.

    Tries to create diplomas on every possible language, to handle a case when student
    had a blank name for particular language, bot obtained it after the initial diploma
    generation. E.g. had only name in russian, and added an english name later.
    """

    student: User

    def act(self) -> None:
        generated_diplomas_count = 0

        for study in self.studies:
            generated_diplomas_count += self.generate_study_diplomas(study)

        if generated_diplomas_count > 0:
            self.notify()

    @property
    def studies(self) -> QuerySet[Study]:
        return Study.objects.filter(
            id__in=self.get_study_ids_for_diploma_regeneration(),
        ).select_related("course")

    def generate_study_diplomas(self, study: Study) -> int:
        count = 0
        for language in self.get_study_diploma_languages(study):
            self.regenerate(study, language)
            count += 1

        return count

    def get_study_ids_for_diploma_regeneration(self) -> list[int]:
        return list(
            Diploma.objects.filter(study__student=self.student)
            .filter_with_template()  # some diplomas have no template, can't regenerate them
            .order_by()
            .values_list("study__id", flat=True)
            .distinct("study__id"),
        )

    def get_study_diploma_languages(self, study: Study) -> list[Language]:
        study_diploma_languages = DiplomaTemplate.objects.filter(
            course=study.course,
            homework_accepted=study.homework_accepted,
            language__in=self.student.diploma_languages,
        ).values_list("language", flat=True)

        return [cast("Language", language) for language in study_diploma_languages]

    def notify(self) -> None:
        send_mail.delay(
            to=self.student.email,
            template_id="diplomas_regenerated",
            disable_antispam=True,
        )

    def regenerate(self, study: Study, language: Language) -> Diploma:
        return DiplomaGenerator(
            student=self.student,
            course=study.cours
...[truncated]...

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

        self.send_confirmation_message(or
...[truncated]...