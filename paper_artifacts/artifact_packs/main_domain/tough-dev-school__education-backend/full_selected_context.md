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

# Selected code and test snippets
### src/apps/users/api/serializers.py
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "username",
            "first_name",
            "last_name",
            "first_name_en",
            "last_name_en",
            "random_name",
            "email",
            "gender",
            "github_username",
            "linkedin_username",
            "telegram_username",
            "avatar",
        ]


class UserSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "username",
            "first_name",
            "last_name",
            "first_name_en",
            "last_name_en",
            "random_name",
            "email",
            "gender",
            "github_username",
            "linkedin_username",
            "telegram_username",
            "avatar",
            "is_staff",
            "rank",
            "rank_label_color",
        ]


class UserSelfUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "first_name_en",
            "last_name_en",
            "gender",
            "github_username",
            "linkedin_username",
            "telegram_username",
            "avatar",
        ]


class UserSafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "first_name_en",
            "last_name_en",
            "random_name",
            "avatar",
            "rank",
            "rank_label_color",
        ]

### src/apps/lms/api/serializers/lesson.py
from typing import Literal

from drf_spectacular.utils import extend_schema_field, inline_serializer
from rest_framework import serializers

from apps.homework.api.serializers import HomeworkStatsSerializer, QuestionSerializer
from apps.homework.models import Question
from apps.lms.models import Call, Lesson
from apps.notion.models import Material as NotionMaterial


class NotionMaterialSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="get_short_slug")

    class Meta:
        model = NotionMaterial
        fields = [
            "id",
            "title",
        ]


class CallSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()
    recommended_video_provider = serializers.SerializerMethodField()

    class Meta:
        model = Call
        fields = [
            "name",
            "description",
            "url",
            "video",
            "datetime",
            "recommended_video_provider",
        ]

    @extend_schema_field(
        field=inline_serializer(
            name="VideoProviderSerializer",
            fields={
                "provider": serializers.CharField(),
                "embed": serializers.URLField(),
                "src": serializers.URLField(),
            },
            many=True,
        ),
    )
    def get_video(self, call: Call) -> list[dict]:
        videos = []

        if call.youtube_id:
            videos.append(
                {
                    "provider": "youtube",
                    "embed": call.get_youtube_embed_src(),
                    "src": call.get_youtube_url(),
                }
            )

        if call.rutube_id:
            videos.append(
                {
                    "provider": "rutube",
                    "embed": call.get_rutube_embed_src(),
                    "src": call.get_rutube_url(),
                }
            )

        return videos

    def get_recommended_video_provider(self, call: Call) -> Literal["youtube", "rutube"] | None:
        request = self.context["request"]
        if request is not None and request.country_code == "RU" and call.rutube_id is not None:
            return "rutube"

        if call.youtube_id is None and call.rutube_id is not None:
            return "rutube"

        if call.youtube_id is not None:
            return "youtube"

        return None


class LessonSerializer(serializers.ModelSerializer):
    """Serialize lesson for the user, lesson should be annotated with crosschecks stats"""

    material = NotionMaterialSerializer(required=False)
    call = CallS
...[truncated]...

### src/apps/a12n/api/forms.py
from typing import Any
from urllib.parse import urljoin

from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm as DjangoPasswordResetForm

from apps.mailing.tasks import send_mail


class EspTemplatePasswordResetForm(DjangoPasswordResetForm):
    """Same as Django's password reset form but use ESP template for email."""

    def get_reset_url(self, context: dict[str, Any]) -> str:
        # reset url is similar to django's `registration/password_reset_email.html` template
        return urljoin(
            settings.FRONTEND_URL,
            "/".join(["auth", "password", "reset", context["uid"], context["token"], ""]),
        )

    def send_mail(
        self,
        subject_template_name: str,
        email_template_name: str,
        context: dict[str, Any],
        from_email: str | None,
        to_email: str,
        html_email_template_name: str | None = None,
    ) -> None:
        send_mail.delay(
            to=to_email,
            template_id=settings.PASSWORD_RESET_TEMPLATE_ID,
            ctx={
                "name": context["user"].get_full_name(),
                "email": to_email,
                "action_url": self.get_reset_url(context),
            },
            disable_antispam=True,
        )

### src/apps/a12n/api/serializers.py
from dj_rest_auth.serializers import PasswordResetSerializer as DjRestAuthPasswordResetSerializer
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework.fields import BooleanField, CharField
from rest_framework.serializers import Serializer
from rest_framework_jwt.utils import jwt_encode_payload

from apps.a12n.api.forms import EspTemplatePasswordResetForm

EXAMPLE_TOKEN = jwt_encode_payload({"sub": "1234567890", "name": "John Doe", "iat": 1516239022})


class PasswordResetSerializer(DjRestAuthPasswordResetSerializer):
    password_reset_form_class = EspTemplatePasswordResetForm


class OkSerializer(Serializer):
    ok = BooleanField(initial=True, read_only=True)


@extend_schema_serializer(examples=[OpenApiExample(name="default", value={"token": EXAMPLE_TOKEN}, response_only=True)])
class TokenSerializer(Serializer):
    token = CharField(read_only=True)

### src/apps/notion/api/serializers.py
from rest_framework import serializers

from apps.notion.models import NotionCacheEntryStatus
from apps.notion.page import NotionPage


class NotionPageSerializer(serializers.Serializer):
    def to_representation(self, page: NotionPage) -> dict:
        return {block.id: block.get_data() for block in page.blocks.ordered()}


class NotionCacheEntryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotionCacheEntryStatus
        fields = [
            "fetch_started",
            "fetch_complete",
        ]

### src/apps/orders/api/serializers.py
from rest_framework import serializers

from apps.banking.selector import BANK_CHOICES
from apps.products.models import Course


class OrderDraftRequestSerializer(serializers.Serializer):
    course = serializers.SlugRelatedField(queryset=Course.objects.all(), slug_field="slug")
    promocode = serializers.CharField(required=False)
    desired_bank = serializers.ChoiceField(choices=BANK_CHOICES, required=False)

### src/apps/banking/api/serializers.py
from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Type

from rest_framework import serializers

from apps.banking.base import Bank
from core.pricing import format_price


@dataclass
class Price:
    price: Decimal
    bank: Type[Bank]


class PriceSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    formatted_price = serializers.CharField()
    currency = serializers.CharField(max_length=4)
    currency_symbol = serializers.CharField(max_length=1)

    def to_representation(self, instance: Price) -> dict[str, Any]:
        return {
            "price": str(instance.price).replace(".00", ""),
            "formatted_price": format_price(instance.price),
            "currency": instance.bank.currency,
            "currency_symbol": instance.bank.currency_symbol,
        }


__all__ = [
    "Price",
    "PriceSerializer",
]

### src/apps/tinkoff/api/serializers.py
from _decimal import Decimal

from rest_framework import serializers

from apps.tinkoff.models import DolyameNotification, PaymentNotification


class PaymentNotificationSerializer(serializers.ModelSerializer):
    TerminalKey = serializers.CharField(source="terminal_key")
    OrderId = serializers.IntegerField(source="order_id")
    Success = serializers.BooleanField(source="success")
    Status = serializers.CharField(source="status")
    PaymentId = serializers.IntegerField(source="payment_id")
    ErrorCode = serializers.CharField(source="error_code", required=False, allow_null=True)
    Amount = serializers.IntegerField(source="amount")
    RebillId = serializers.IntegerField(source="rebill_id", required=False, allow_null=True)
    CardId = serializers.CharField(source="card_id", required=False, allow_null=True, allow_blank=True)
    Pan = serializers.CharField(source="pan", required=False, allow_null=True)
    DATA = serializers.CharField(source="data", required=False, allow_null=True)
    Token = serializers.CharField(source="token")
    ExpDate = serializers.CharField(source="exp_date", required=False, allow_null=True)

    class Meta:
        model = PaymentNotification
        fields = [
            "TerminalKey",
            "OrderId",
            "Success",
            "Status",
            "PaymentId",
            "ErrorCode",
            "Amount",
            "RebillId",
            "CardId",
            "Pan",
            "DATA",
            "Token",
            "ExpDate",
        ]

    def validate_Amount(self, validated_data: int) -> Decimal:
        return Decimal(validated_data / 100)


class DolyameNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DolyameNotification
        fields = [
            "order",
            "status",
            "amount",
            "demo",
            "residual_amount",
            "client_info",
            "payment_schedule",
        ]

### src/apps/diplomas/api/serializers.py
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.diplomas.models import Diploma
from apps.products.api.serializers import CourseSimpleSerializer
from apps.studying.models import Study
from apps.users.api.serializers import UserSafeSerializer


class DiplomaSerializer(serializers.ModelSerializer):
    student = UserSafeSerializer(source="study.student")
    course = CourseSimpleSerializer(source="study.course")
    url = serializers.URLField(source="get_absolute_url")

    class Meta:
        model = Diploma
        fields = [
            "course",
            "slug",
            "language",
            "image",
            "student",
            "url",
        ]


class DiplomaRetrieveSerializer(serializers.ModelSerializer):
    student = UserSafeSerializer(source="study.student")
    course = CourseSimpleSerializer(source="study.course")
    other_languages = serializers.SerializerMethodField()

    class Meta:
        model = Diploma
        fields = [
            "course",
            "slug",
            "language",
            "image",
            "student",
            "other_languages",
        ]

    def get_other_languages(self, diploma: Diploma) -> dict:
        return DiplomaSerializer(diploma.get_other_languages(), many=True).data


class DiplomaCreateSerializer(serializers.ModelSerializer):
    student = serializers.IntegerField(source="study.student_id")
    course = serializers.IntegerField(source="study.course_id")

    class Meta:
        model = Diploma
        fields = [
            "student",
            "course",
            "language",
            "image",
        ]

    def create(self, validated_data: dict) -> Diploma:
        validated_study_data = validated_data.pop("study")

        validated_data["study"] = self.get_study(
            student_id=validated_study_data["student_id"],
            course_id=validated_study_data["course_id"],
        )

        return super().create(validated_data)

    @staticmethod
    def get_study(student_id: str, course_id: str) -> Study | None:
        try:
            return Study.objects.get(student__id=student_id, course_id=course_id)
        except Study.DoesNotExist:
            raise ValidationError("Cant find student, course, or student purchased that course")

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

### src/apps/studying/api/serializers.py
from rest_framework import serializers

from apps.lms.models import CourseLink
from apps.products.models import Course


class CourseLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLink
        fields = ["name", "url"]


class CourseSerializer(serializers.ModelSerializer):
    home_page_slug = serializers.CharField()
    links = CourseLinkSerializer(many=True, read_only=True, source="courselink_set")
    tariff_name = serializers.CharField(required=True, allow_null=True)
    cover = serializers.ImageField(required=True, allow_null=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "slug",
            "name",
            "product_name",
            "tariff_name",
            "home_page_slug",
            "cover",
            "chat",
            "calendar_ios",
            "calendar_google",
            "links",
        ]

### src/apps/lms/api/serializers/module.py
from django.utils import timezone
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from apps.lms.models import Module
from core.serializers import MarkdownField


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Markdown in descrpition",
            value={
                "id": 100500,
                "name": "Первая неделя",
                "has_started": True,
                "start_date": "2023-12-01 15:30:00+03:00",
                "description": "Cамая важная неделя",
                "text": "<p><strong>Первая</strong> неделя — <em>самая важная неделя</em></p>",
            },
        ),
    ]
)
class ModuleSerializer(serializers.ModelSerializer):
    text = MarkdownField()
    has_started = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = [
            "id",
            "name",
            "start_date",
            "has_started",
            "description",
            "text",
        ]

    def get_has_started(self, module: Module) -> bool:
        if module.start_date is None:
            return True

        return module.start_date <= timezone.now()


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Default",
            value={
                "id": 100500,
                "name": "Первая неделя",
                "has_started": True,
                "start_date": "2023-12-01 15:30:00+03:00",
                "description": "Cамая важная неделя",
                "lesson_count": 1,
                "single_lesson_id": 57,
                "text": "<p><strong>Первая</strong> неделя — <em>самая важная неделя</em></p>",
            },
        ),
        OpenApiExample(
            name="Multiple lessons",
            value={
                "id": 100500,
                "name": "Вторая неделя",
                "has_started": True,
                "start_date": "2023-12-01 15:30:00+03:00",
                "description": "Тоже важная неделя",
                "lesson_count": 2,
                "single_lesson_id": None,
                "text": "<p><strong>Первая</strong> неделя — <em>самая важная неделя</em></p>",
            },
        ),
    ]
)
class ModuleDetailSerializer(ModuleSerializer):
    lesson_count = serializers.IntegerField()  # has to be annotated by .for_viewset()
    single_lesson_id = serializers.IntegerField()

    class Meta(ModuleSerializer.Meta):
        model = Module
        fields = ModuleSerializer.Meta.fields + [
            "lesson_count",
           
...[truncated]...

### src/apps/lms/api/serializers/__init__.py
from apps.lms.api.serializers.breadcrums import BreadcrumbsSerializer
from apps.lms.api.serializers.lesson import LessonSerializer
from apps.lms.api.serializers.module import ModuleDetailSerializer, ModuleSerializer

__all__ = [
    "BreadcrumbsSerializer",
    "LessonSerializer",
    "ModuleDetailSerializer",
    "ModuleSerializer",
]

### src/apps/homework/api/serializers/image.py
from rest_framework import serializers

from apps.homework.models import AnswerImage


class AnswerImageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = serializers.FileField()

    class Meta:
        model = AnswerImage
        fields = [
            "author",
            "image",
        ]

### src/apps/homework/api/serializers/stats.py
from rest_framework import serializers

from apps.homework.models import Question, StatsAnnotatedQuestion


class CrossCheckStatsSerializer(serializers.Serializer):
    total = serializers.IntegerField(source="crosschecks_total")
    checked = serializers.IntegerField(source="crosschecks_checked")


class CommentStatsSerializer(serializers.Serializer):
    comments = serializers.IntegerField(source="comment_count")
    hidden_before_crosscheck_completed = serializers.SerializerMethodField()

    def get_hidden_before_crosscheck_completed(self, instance: StatsAnnotatedQuestion) -> int | None:
        request = self.context["request"]
        return instance.comment_count - instance.get_allowed_comment_count(request.user)  # type: ignore[attr-defined]

    def to_representation(self, instance: StatsAnnotatedQuestion) -> dict:
        if not instance.is_sent:  # type: ignore[attr-defined]
            return {}

        return super().to_representation(instance)


class TemporarySoonToBeDepricatedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "slug",
            "name",
            "deadline",
        ]


class HomeworkStatsSerializer(serializers.Serializer):
    """Requires *any* model annotaded with statistics. For annotation examples check homework.QuestionQuerySet"""

    is_sent = serializers.BooleanField()
    crosschecks = CrossCheckStatsSerializer(required=False, source="*")
    comments = CommentStatsSerializer(required=False, source="*")
    question = TemporarySoonToBeDepricatedQuestionSerializer(source="*")

### src/apps/lms/api/serializers/breadcrums.py
from drf_spectacular.utils import extend_schema_field, inline_serializer
from rest_framework import serializers

from apps.lms.api.serializers.module import ModuleSerializer
from apps.lms.models import Course, Lesson
from core.serializers import MarkdownField


class LMSCourseSerializer(serializers.ModelSerializer):
    homework_check_recommendations = MarkdownField()

    class Meta:
        model = Course
        fields = [
            "id",
            "slug",
            "name",
            "cover",
            "chat",
            "calendar_ios",
            "calendar_google",
            "homework_check_recommendations",
        ]


class BreadcrumbsSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()
    course = LMSCourseSerializer(source="module.course")
    lesson = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = [
            "module",
            "course",
            "lesson",
        ]

    @extend_schema_field(
        field=inline_serializer(
            name="LessonPlainSerializer",
            fields={
                "id": serializers.IntegerField(),
            },
        )
    )
    def get_lesson(self, lesson: Lesson) -> dict:
        return {
            "id": lesson.id,
        }

### src/apps/homework/api/serializers/answer.py
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.homework.api.serializers.attachment import AnswerAttachmentSerializer
from apps.homework.api.serializers.question import QuestionSerializer
from apps.homework.api.serializers.reaction import ReactionDetailedSerializer
from apps.homework.models import Answer, Question, TreeAnnotatedAnswer
from apps.homework.models.answer import AnswerQuerySet
from apps.users.api.serializers import UserSafeSerializer
from core.serializers import MarkdownField, SoftField


class AnswerSerializer(serializers.ModelSerializer):
    author = UserSafeSerializer()
    legacy_text = MarkdownField()
    parent = SoftField(source="parent.slug")  # type: ignore
    question = serializers.CharField(source="question.slug")
    has_descendants = serializers.SerializerMethodField()
    reactions = ReactionDetailedSerializer(many=True)
    attachments = AnswerAttachmentSerializer(many=True, read_only=True)
    is_editable = serializers.SerializerMethodField()
    content = serializers.DictField(required=True)

    class Meta:
        model = Answer
        fields = [
            "created",
            "modified",
            "slug",
            "question",
            "author",
            "parent",
            "legacy_text",
            "content",
            "has_descendants",
            "is_editable",
            "reactions",
            "attachments",
        ]

    def get_is_editable(self, answer: Answer) -> bool:
        return answer.is_editable and self.context["request"].user == answer.author

    def get_descendants_queryset(self, answer: Answer) -> AnswerQuerySet:
        user = self.context["request"].user
        if user.has_perm("homework.see_all_answers"):
            return answer.get_comments()

        return answer.get_limited_comments_for_user_by_crosschecks(user)

    def get_has_descendants(self, answer: TreeAnnotatedAnswer) -> bool:
        if answer.author_id == self.context["request"].user.id:
            return self.get_descendants_queryset(answer).exists()

        return answer.children_count > 0  # type: ignore[attr-defined]


class AnswerTreeSerializer(AnswerSerializer):
    descendants = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = AnswerSerializer.Meta.fields + [
            "descendants",
        ]

    @extend_schema_field(AnswerSerializer(many=True))
    def get_descendants(self, answer: Answer) -> list[dict]:
        cached = self._get_cached_descendands(answer)
        if cached is not None:
         
...[truncated]...

### src/apps/homework/api/serializers/__init__.py
from apps.homework.api.serializers.answer import (
    AnswerCommentTreeSerializer,
    AnswerCreateSerializer,
    AnswerSerializer,
    AnswerSimpleSerializer,
    AnswerTreeSerializer,
    AnswerUpdateSerializer,
)
from apps.homework.api.serializers.attachment import AnswerAttachmentSerializer, AnswerAttachmentUploadSerializer
from apps.homework.api.serializers.crosscheck import CrossCheckSerializer
from apps.homework.api.serializers.image import AnswerImageSerializer
from apps.homework.api.serializers.question import QuestionDetailSerializer, QuestionSerializer
from apps.homework.api.serializers.reaction import ReactionCreateSerializer, ReactionDetailedSerializer
from apps.homework.api.serializers.stats import HomeworkStatsSerializer

__all__ = [
    "AnswerAttachmentSerializer",
    "AnswerAttachmentUploadSerializer",
    "AnswerCommentTreeSerializer",
    "AnswerCreateSerializer",
    "AnswerImageSerializer",
    "AnswerSerializer",
    "AnswerSimpleSerializer",
    "AnswerTreeSerializer",
    "AnswerUpdateSerializer",
    "CrossCheckSerializer",
    "HomeworkStatsSerializer",
    "QuestionDetailSerializer",
    "QuestionSerializer",
    "ReactionCreateSerializer",
    "ReactionDetailedSerializer",
]

### src/apps/homework/api/serializers/question.py
from drf_spectacular.helpers import lazy_serializer
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.homework.api.serializers.stats import HomeworkStatsSerializer
from apps.homework.models import Question
from apps.products.models import Course
from core.serializers import MarkdownField


class QuestionCourseSerializer(serializers.ModelSerializer):
    homework_check_recommendations = MarkdownField()

    class Meta:
        model = Course
        fields = [
            "id",
            "slug",
            "name",
            "cover",
            "chat",
            "calendar_ios",
            "calendar_google",
            "homework_check_recommendations",
        ]


class QuestionSerializer(serializers.ModelSerializer):
    markdown_text = serializers.CharField(source="text")

    class Meta:
        model = Question
        fields = [
            "slug",
            "name",
            "markdown_text",
            "deadline",
        ]


class QuestionDetailSerializer(serializers.ModelSerializer):
    markdown_text = serializers.CharField(source="text")
    breadcrumbs = serializers.SerializerMethodField()
    homework = HomeworkStatsSerializer(source="*")
    course = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            "breadcrumbs",
            "slug",
            "name",
            "markdown_text",
            "deadline",
            "homework",
            "course",
        ]

    @extend_schema_field(QuestionCourseSerializer)
    def get_course(self, question: Question) -> dict:
        course = question.get_course(user=self.context["request"].user)

        if course is None:
            course = question.get_legacy_course()

        return QuestionCourseSerializer(course).data

    @extend_schema_field(lazy_serializer("apps.lms.api.serializers.BreadcrumbsSerializer")())
    def get_breadcrumbs(self, question: Question) -> dict | None:
        from apps.lms.api.serializers import BreadcrumbsSerializer

        lesson = question.get_lesson(user=self.context["request"].user)

        return BreadcrumbsSerializer(lesson).data if lesson is not None else None

### src/apps/homework/api/serializers/reaction.py
from rest_framework import serializers

from apps.homework.models import Reaction
from apps.users.api.serializers import UserSafeSerializer


class ReactionDetailedSerializer(serializers.ModelSerializer):
    author = UserSafeSerializer()
    answer = serializers.CharField(source="answer.slug")

    class Meta:
        model = Reaction
        fields = [
            "slug",
            "emoji",
            "author",
            "answer",
        ]


class ReactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = [
            "emoji",
            "slug",
        ]

### src/apps/homework/api/serializers/attachment.py
from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from apps.homework.models import AnswerAttachment


class AnswerAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAttachment
        fields = [
            "id",
            "file",
            "created",
        ]


class AnswerAttachmentUploadSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    file = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    class Meta:
        model = AnswerAttachment
        fields = [
            "author",
            "file",
        ]

### src/apps/homework/api/serializers/crosscheck.py
from rest_framework import serializers

from apps.homework.api.serializers.answer import AnswerSimpleSerializer
from apps.homework.models import AnswerCrossCheck


class CrossCheckSerializer(serializers.ModelSerializer):
    answer = AnswerSimpleSerializer()
    is_checked = serializers.SerializerMethodField()

    class Meta:
        model = AnswerCrossCheck
        fields = (
            "id",
            "answer",
            "is_checked",
        )

    def get_is_checked(self, obj: "AnswerCrossCheck") -> bool:
        return obj.checked is not None

### src/apps/lms/tests/api/test_lesson_list.py
import pytest

pytestmark = [pytest.mark.django_db]


def test_ok(api, module, lesson):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert len(got["results"]) == 1
    assert got["results"][0]["id"] == lesson.id


@pytest.mark.usefixtures("_no_purchase")
def test_zero_lessons_if_no_purchase(api, module):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert len(got["results"]) == 0


def test_401_for_anon_users(anon, module):
    anon.get(f"/api/v2/lms/lessons/?module={module.pk}", expected_status_code=401)


def test_no_results_for_non_existent_modules(api):
    api.get("/api/v2/lms/lessons/?module=10005000", expected_status_code=400)


@pytest.mark.freeze_time("2032-12-09 15:30:30+03:00")
def test_no_results_if_module_is_not_started_yet(api, module):
    module.update(start_date="2032-12-15 15:30:30+03:00")

    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert len(got["results"]) == 0


def test_ok_for_module_without_start_date(api, module):
    module.update(start_date=None)

    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert len(got["results"]) == 1


def test_filter_works(api, another_module):
    got = api.get(f"/api/v2/lms/lessons/?module={another_module.pk}")

    assert len(got["results"]) == 0


def test_hidden_lessons_are_not_shown(api, module, lesson):
    lesson.update(hidden=True)

    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert len(got["results"]) == 0


@pytest.mark.parametrize(
    "disable_pagination_value",
    [
        "True",
        "true",
        "1",
    ],
)
def test_pagination_could_be_disable_with_query_param(api, module, lesson, disable_pagination_value):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}&disable_pagination={disable_pagination_value}")

    assert got[0]["id"] == lesson.id

### src/apps/lms/tests/api/test_call_in_lesson.py
import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def call(mixer):
    return mixer.blend(
        "lms.Call",
        name="Обязательный созвон",
        description="Не пропустите",
        url="https://skype.icq",
        datetime="2032-12-01 15:30:44 +03:00",
    )


@pytest.fixture
def _youtube_video(call):
    call.update(
        youtube_id="B3EE",
    )


@pytest.fixture
def _rutube_video(call):
    call.update(
        rutube_id="D4FF",
        rutube_access_key="KFF",
    )


@pytest.fixture(autouse=True)
def lesson(lesson, call):
    lesson.update(call=call)

    return lesson


def test_no_call(api, module, lesson):
    lesson.update(call=None)
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert got["results"][0]["id"] == lesson.id
    assert got["results"][0]["call"] is None


def test_fields(api, module, lesson):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert got["results"][0]["id"] == lesson.id
    assert got["results"][0]["call"]["name"] == "Обязательный созвон"
    assert got["results"][0]["call"]["description"] == "Не пропустите"
    assert got["results"][0]["call"]["url"] == "https://skype.icq"
    assert got["results"][0]["call"]["datetime"] == "2032-12-01T15:30:44+03:00"


@pytest.mark.usefixtures("kamchatka_timezone")
def test_timezone(api, module):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert got["results"][0]["call"]["datetime"] == "2032-12-02T00:30:44+12:00"


def test_empty_video(api, module):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert got["results"][0]["call"]["video"] == []


@pytest.mark.usefixtures("_youtube_video", "_rutube_video")
def test_both_videos(api, module):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")["results"][0]["call"]["video"]

    assert got[0]["provider"] == "youtube"
    assert got[1]["provider"] == "rutube"

    assert "B3EE" in got[0]["src"], "youtube src"
    assert "B3EE" in got[0]["embed"], "youtube embed"

    assert "D4FF" in got[1]["src"], "rutube src"
    assert "D4FF" in got[1]["embed"], "rutube embed"

    assert "KFF" in got[1]["src"], "rutube access key"
    assert "KFF" in got[1]["embed"], "rutube access key"


@pytest.mark.usefixtures("_youtube_video")
def test_youtube_video(api, module):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")["results"][0]["call"]["video"]

    assert len(got) == 1
    assert got[0]["provider"] == "youtube"
    assert "B3EE" in got[0]["src"], "youtube src"
    assert "B3EE" in got[0]["embed"], "youtube embed"
...[truncated]...

### src/apps/lms/tests/api/test_lesson_retrieve.py
import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def call(mixer):
    return mixer.blend(
        "lms.Call",
        name="Обязательный созвон",
        description="Не пропустите",
        url="https://skype.icq",
        datetime="2032-12-01 15:30:44 +03:00",
    )


@pytest.fixture
def material(mixer):
    return mixer.blend("notion.Material", title="Урок 3")


@pytest.fixture
def question(mixer):
    return mixer.blend(
        "homework.Question",
        text="Составьте *математическую модель* каждого атома в атмосфере Земли на год вперед, учитывая все возможные взаимодействия и условия.",
    )


def test_ok(api, lesson):
    got = api.get(f"/api/v2/lms/lessons/{lesson.pk}/")

    assert got["id"] == lesson.id
    assert got["material"] is None
    assert got["call"] is None


@pytest.mark.usefixtures("_no_purchase")
def test_404_if_no_purchase(api, lesson):
    api.get(f"/api/v2/lms/lessons/{lesson.pk}/", expected_status_code=404)


def test_404_if_hidden(api, lesson):
    lesson.update(hidden=True)

    api.get(f"/api/v2/lms/lessons/{lesson.pk}/", expected_status_code=404)


@pytest.mark.freeze_time("2032-12-09 15:30:30+03:00")
def test_404_if_module_is_not_started_yet(api, lesson):
    lesson.module.update(start_date="2032-12-15 15:30:30+03:00")

    api.get(f"/api/v2/lms/lessons/{lesson.pk}/", expected_status_code=404)


def test_ok_for_module_without_start_date(api, lesson):
    lesson.module.update(start_date=None)

    api.get(f"/api/v2/lms/lessons/{lesson.pk}/", expected_status_code=200)


def test_no_anon(anon, lesson):
    anon.get(f"/api/v2/lms/lessons/{lesson.pk}/", expected_status_code=401)


def test_call(api, lesson, call):
    lesson.update(call=call)

    got = api.get(f"/api/v2/lms/lessons/{lesson.pk}/")

    assert got["id"] == lesson.id
    assert got["call"]["name"] == "Обязательный созвон"
    assert got["call"]["description"] == "Не пропустите"
    assert got["call"]["url"] == "https://skype.icq"
    assert got["call"]["datetime"] == "2032-12-01T15:30:44+03:00"


def test_material(api, lesson, material):
    lesson.update(material=material)

    got = api.get(f"/api/v2/lms/lessons/{lesson.pk}/")

    assert got["id"] == lesson.id
    assert got["material"]["id"] == str(material.slug).replace("-", "")
    assert got["material"]["title"] == "Урок 3"


def test_question(api, lesson, question):
    lesson.update(question=question)

    got = api.get(f"/api/v2/lms/lessons/{lesson.pk}/")

    assert got["homework"]["question"]["name"] == question.name

### src/apps/lms/tests/api/test_material_in_lesson.py
import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def material(mixer):
    return mixer.blend("notion.Material", title="Урок 3")


def test_no_material(api, module, lesson):
    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert got["results"][0]["id"] == lesson.id
    assert got["results"][0]["material"] is None


def test_attached_material(api, module, lesson, material):
    lesson.update(material=material)

    got = api.get(f"/api/v2/lms/lessons/?module={module.pk}")

    assert got["results"][0]["id"] == lesson.id
    assert got["results"][0]["material"]["id"] == str(material.slug).replace("-", "")
    assert got["results"][0]["material"]["title"] == "Урок 3"