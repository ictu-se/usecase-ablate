# Deterministic random code snippets
### api/administration/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from administration.views import (
    AcademicYearListCreateView,
    AcademicYearDetailView,
    TermListCreateView,
    TermDetailView,
    SchoolEventViewSet,
    SchoolEventBulkUploadView,
    SchoolEventTemplateDownloadView,
)


router = DefaultRouter()
router.register(r"", SchoolEventViewSet, basename="school-events")


urlpatterns = [
    # AcademicYear URLs
    path(
        "academic-years/",
        AcademicYearListCreateView.as_view(),
        name="academic-year-list-create",
    ),
    path(
        "academic-years/<int:pk>/",
        AcademicYearDetailView.as_view(),
        name="academic-year-detail",
    ),
    # Term URLs
    path("terms/", TermListCreateView.as_view(), name="term-list-create"),
    path("terms/<int:pk>/", TermDetailView.as_view(), name="term-detail"),
    path("school-events/", include(router.urls)),
    path(
        "school-events/bulk-upload/",
        SchoolEventBulkUploadView.as_view(),
        name="school-events-bulk-upload",
    ),
    path(
        "school-events/template-download/",
        SchoolEventTemplateDownloadView.as_view(),
        name="school-events-template-download",
    ),
]

### school/wsgi.py
"""
WSGI config for school project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')

application = get_wsgi_application()

### api/serializers.py
from rest_framework import serializers
from administration.models import Article, CarouselImage

from users.serializers import UserSerializer

class ArticleSerializer(serializers.ModelSerializer):
	created_by = serializers.SerializerMethodField(read_only=True)
	#created_at = serializers.SerializerMethodField(read_only=True)
	short_content = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Article
		fields = ['id', 'title', 'content', 'short_content', 'picture', 'created_at', 'created_by']

	def get_created_by(self, obj):
		user = obj.created_by
		serializer = UserSerializer(user, many=False)
		if(serializer.data['first_name']):
			return serializer.data['first_name']
		return serializer.data['email']

	def get_short_content(self, obj):
		content = obj.content
		return content[:200]

class CarouselImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = CarouselImage
		fields = ['id', 'title', 'description', 'picture']

### notes/admin.py
from django.contrib import admin

from .models import *

admin.site.register(Assignment)
admin.site.register(GradedAssignment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(SpecificExplanations)
admin.site.register(Concept)
admin.site.register(Note)

### schedule/apps.py
from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    name = 'schedule'

### administration/serializers.py
from rest_framework import serializers
from .models import AcademicYear, Term, Article, CarouselImage, SchoolEvent


from users.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    # created_at = serializers.SerializerMethodField(read_only=True)
    short_content = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "content",
            "short_content",
            "picture",
            "created_at",
            "created_by",
        ]

    def get_created_by(self, obj):
        user = obj.created_by
        serializer = UserSerializer(user, many=False)
        if serializer.data["first_name"]:
            return serializer.data["first_name"]
        return serializer.data["email"]

    def get_short_content(self, obj):
        content = obj.content
        return content[:200]


class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ["id", "title", "description", "picture"]


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = "__all__"


class TermSerializer(serializers.ModelSerializer):
    academic_year = serializers.PrimaryKeyRelatedField(
        queryset=AcademicYear.objects.all(), write_only=True
    )
    academic_year_name = serializers.StringRelatedField(
        source="academic_year", read_only=True
    )

    class Meta:
        model = Term
        fields = [
            "id",
            "name",
            "academic_year",
            "academic_year_name",
            "start_date",
            "end_date",
        ]


class SchoolEventSerializer(serializers.ModelSerializer):
    term_name = serializers.CharField(source="term.name", read_only=True)
    academic_year = serializers.CharField(
        source="term.academic_year.name", read_only=True
    )

    class Meta:
        model = SchoolEvent
        fields = [
            "id",
            "name",
            "event_type",
            "term",
            "term_name",
            "academic_year",
            "start_date",
            "end_date",
            "description",
        ]

### school/settings.py
import os
import environ
from pathlib import Path
from datetime import timedelta, date
from django.core.validators import MinValueValidator  # Could use MaxValueValidator too

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "SECRET_KEY", default="2_5ub5rqi!%3v#xk$0e4z-jg22zg_$ejz&t3s0g$5lt*vvu!b@"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


DATE_VALIDATORS = [MinValueValidator(date(1970, 1, 1))]  # Unix epoch!


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "academic.apps.AcademicConfig",
    "administration.apps.AdministrationConfig",
    "attendance.apps.AttendanceConfig",
    "examination.apps.ExaminationConfig",
    "finance.apps.FinanceConfig",
    "notes.apps.NotesConfig",
    "schedule.apps.ScheduleConfig",
    "sis.apps.SisConfig",
    "users.apps.UsersConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "api.middleware.CustomExceptionMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "school.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "static/dist"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
...[truncated]...

### administration/tests.py
from django.test import TestCase

# Create your tests here.

### users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Group
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from administration.common_objs import *
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="first name"
    )
    middle_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="middle name"
    )
    last_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="last name"
    )
    phone_number = models.CharField(blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_accountant = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ["email"]

    def __str__(self):
        return self.email


class Accountant(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="accountant",
        null=True,
        blank=True,
    )
    username = models.CharField(unique=True, max_length=250, blank=True)
    first_name = models.CharField(max_length=300, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=300, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, blank=True)
    email = models.EmailField(blank=True, null=True)
    empId = models.CharField(max_length=8, null=True, blank=True, unique=True)
    tin_number = models.CharField(max_length=9, null=True, blank=True)
    nssf_number = models.CharField(max_length=9, null=True, blank=True)
    salary = models.IntegerField(blank=True, null=True)
    unpaid_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    national_id = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=150, blank=True)
    alt_email = 
...[truncated]...

### api/apps.py
from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

### schedule/views.py
from django.http import JsonResponse
from django.core.management import call_command
from io import StringIO
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Period
from .serializers import PeriodSerializer
from academic.models import AllocatedSubject


class PeriodCreateView(APIView):
    def post(self, request, *args, **kwargs):
        allocated_subject_id = request.data.get("allocated_subject")
        try:
            allocated_subject = AllocatedSubject.objects.get(id=allocated_subject_id)
        except AllocatedSubject.DoesNotExist:
            return Response(
                {"error": "AllocatedSubject not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(allocated_subject=allocated_subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


def run_generate_timetable(request):
    """
    View to trigger the timetable generation management command.
    """
    output = StringIO()
    try:
        call_command("generate_timetable", stdout=output)
        return JsonResponse({"status": "success", "message": output.getvalue()})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

### academic/apps.py
from django.apps import AppConfig


class AcademicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academic'

### schedule/tests.py
from django.test import TestCase

# Create your tests here.

### users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Accountant


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_accountant', 'is_teacher',)
    list_filter = ('email', 'is_staff', 'is_active', 'is_accountant', 'is_teacher',)
    fieldsets = (
        (None, {'fields': ('first_name', 'middle_name', 'last_name','email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_accountant', 'is_teacher',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_accountant', 'is_teacher',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Accountant)

### examination/serializers.py
from rest_framework import serializers

from .models import GradeScale, GradeScaleRule


class GradeScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeScale
        fields = "__all__"


class GradeScaleRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeScaleRule
        fields = "__all__"

### attendance/serializers.py
from rest_framework import serializers
from .models import (
    TeachersAttendance,
    AttendanceStatus,
    StudentAttendance,
    PeriodAttendance,
)


class AttendanceStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceStatus
        fields = "__all__"


class TeacherAttendanceSerializer(serializers.ModelSerializer):
    teacher = (
        serializers.StringRelatedField()
    )  # Display teacher's name instead of the ID
    status = serializers.StringRelatedField()  # Display status name instead of ID
    date = serializers.DateField(format="%Y-%m-%d")  # Date format in response

    class Meta:
        model = TeachersAttendance
        fields = ["id", "teacher", "date", "time_in", "time_out", "status", "notes"]


class StudentAttendanceSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()  # Display student name instead of ID
    status = serializers.StringRelatedField()  # Display status name instead of ID
    ClassRoom = serializers.StringRelatedField()  # Display classroom name instead of ID
    date = serializers.DateField(format="%Y-%m-%d")  # Date format in response

    class Meta:
        model = StudentAttendance
        fields = ["id", "student", "date", "ClassRoom", "status", "notes"]


class PeriodAttendanceSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()  # Display student name instead of ID
    status = serializers.StringRelatedField()  # Display status name instead of ID
    date = serializers.DateField(format="%Y-%m-%d")  # Date format in response

    class Meta:
        model = PeriodAttendance
        fields = [
            "id",
            "student",
            "date",
            "period",
            "status",
            "reason_for_absence",
            "notes",
        ]

### attendance/admin.py
from django.contrib import admin

from .models import *

admin.site.register(AttendanceStatus)
admin.site.register(TeachersAttendance)
admin.site.register(StudentAttendance)
admin.site.register(PeriodAttendance)

### finance/apps.py
from django.apps import AppConfig


class FinanceConfig(AppConfig):
    name = 'finance'

### examination/admin.py
from django.contrib import admin
from .models import *

admin.site.register(GradeScale)
admin.site.register(GradeScaleRule)
admin.site.register(Result)
admin.site.register(ExaminationListHandler)
admin.site.register(MarksManagement)

### notes/serializers.py
from rest_framework import serializers

from users.models import CustomUser as User
from .models import (
    Assignment,
    Question,
    Choice,
    GradedAssignment,
)


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "choices", "question", "order")


class AssignmentSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    teacher = StringSerializer(many=False)

    class Meta:
        model = Assignment
        fields = "__all__"

    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True).data
        return questions

    def create(self, request):
        data = request.data

        assignment = Assignment()
        teacher = User.objects.get(username=data["teacher"])
        assignment.teacher = teacher
        assignment.title = data["title"]
        assignment.save()

        order = 1
        for q in data["questions"]:
            newQ = Question()
            newQ.question = q["title"]
            newQ.order = order
            newQ.save()

            for c in q["choices"]:
                newC = Choice()
                newC.title = c
                newC.save()
                newQ.choices.add(newC)

            newQ.answer = Choice.objects.get(title=q["answer"])
            newQ.assignment = assignment
            newQ.save()
            order += 1
        return assignment


class GradedAssignmentSerializer(serializers.ModelSerializer):
    student = StringSerializer(many=False)

    class Meta:
        model = GradedAssignment
        fields = "__all__"

    def create(self, request):
        data = request.data
        print(data)

        assignment = Assignment.objects.get(id=data["asntId"])
        student = User.objects.get(username=data["username"])

        graded_asnt = GradedAssignment()
        graded_asnt.assignment = assignment
        graded_asnt.student = student

        questions = [q for q in assignment.questions.all()]
        answers = [data["answers"][a] for a in data["answers"]]

        answered_correct_count = 0
        for i in range(len(questions)):
            if questions[i].answer.title == answers[i]:
                answered_correct_count += 1
            i += 1

        grade = answered_correct_count / len(questions) * 100
        graded_asnt.grade = grade
        graded_asnt.save()
        
...[truncated]...

### school/asgi.py
"""
ASGI config for school project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')

application = get_asgi_application()