# README-derived retrieval query
mwinamijr django scms ## README.md
# Django School Management System
This an open source school management system API built with Django and Django-rest framework for managing school or college. It provides an API for administration, admission, attendance, schedule and results. It also provide users with different permissions to access various apps depending on their access level.

Techdometz is a tech startup helping schools and education centers to provide solutions to their tech problems. 
[Contact us](http://techdometz.com/contact-us/) for details.

# Quick Install
You should have at least basic django and django-rest framework experience to run django-scms. We test only in PostgreSQL database.

### Fork the repo
You first need to fork the repo from [Techdometz](https://github.com/TechDometz/django-scms).
### Clone the repo
Clone the forked repo

`git clone https://github.com/[username]/django-scms.git`  

### Create a virtual environment

There are several ways depending on the OS and package you choose. Here's my favorite  
`sudo apt-get install python3-pip`  
`pip3 install virtualenv`  
Then either  
`python3 -m venv venv`  
or  
`python -m venv venv`  
or  
`virtualenv venv` (you can call it venv or anything you like)

#### Activate the virtual environment  

in Mac or Linux
`source venv/bin/activate`  
in windows
`venv/Scripts/activate.bat`  


## 🚀 Key Features

- 🔐 **Authentication & Role-Based Access Control**:  
  Supports authentication and permission control for:
  - **Admins**
  - **Teachers**
  - **Accountants**
  - **Parents**

- 💸 **Finance Module** *(NEW)*:  
  - Manage **Receipts**
  - Track **Payments**
  - Generate **Financial Reports**

- 🧾 **School Information System (SIS)**:
  - Tracks student records and their associated parent/guardian contacts.
  - Manages class and academic year data.
  - Required module for all other apps.

- 📝 **Admissions**:
  - Manages student admission pipeline and levels.
  - Tracks marketing channels and open house participation.

---

## 🔧 Upcoming Features

- 📅 **Schedule Management**
- 🧠 **Examinations and Grading**
- 📚 **Digital Notes and Materials**
- 📊 **Attendance Tracking**

---

## Contributors

- [Mwinamijr](https://github.com/mwinamijr)

## License

The project is licensed under the MIT License README.md
academic/__init__.py
academic/admin.py
academic/apps.py
academic/management/commands/__init__.py
academic/management/commands/update_student_debt.py
academic/management/commands/update_unpaid_salaries.py
academic/models.py
academic/serializers.py
academic/tests.py
academic/validators.py
academic/views.py
administration/__init__.py
administration/admin.py
administration/apps.py
administration/common_objs.py
administration/models.py
administration/permissions.py
administration/serializers.py
administration/tests.py
administration/views.py
api/__init__.py
api/academic/urls.py
api/admin.py
api/administration/urls.py
api/apps.py
api/assignments/urls.py
api/attendance/urls.py
api/blog/urls.py
api/exceptions.py
api/finance/urls.py
api/journals/urls.py
api/middleware.py
api/notes/urls.py
api/schedule/urls.py
api/serializers.py
api/sis/urls.py
api/users/urls.py
api/views.py
attendance/__init__.py
attendance/admin.py
attendance/apps.py
attendance/models.py
attendance/serializers.py
attendance/tests.py
attendance/views.py
examination/__init__.py
examination/admin.py
examination/apps.py
examination/models.py
examination/serializers.py
examination/tests.py
examination/views.py
finance/__init__.py
finance/admin.py
finance/apps.py
finance/models.py
finance/serializers.py
finance/tests.py
finance/views.py
manage.py
notes/__init__.py
notes/admin.py
notes/apps.py
notes/models.py
notes/serializers.py
notes/tests.py
notes/views.py
requirements.txt
schedule/__init__.py
schedule/admin.py
schedule/apps.py
schedule/management/commands/generate_timetable.py
schedule/models.py
schedule/serializers.py
schedule/tests.py
schedule/views.py
school/__init__.py
school/asgi.py
school/settings.py
school/urls.py
school/wsgi.py
sis/__init__.py
sis/admin.py
sis/apps.py
sis/models.py
sis/serializers.py
sis/tests.py
sis/views.py
users/__init__.py
users/admin.py
users/apps.py
users/forms.py
users/managers.py
users/models.py
users/serializers.py
users/tests.py
users/views.py

# BM25 selected code snippets
### README.md
# Django School Management System
This an open source school management system API built with Django and Django-rest framework for managing school or college. It provides an API for administration, admission, attendance, schedule and results. It also provide users with different permissions to access various apps depending on their access level.

Techdometz is a tech startup helping schools and education centers to provide solutions to their tech problems. 
[Contact us](http://techdometz.com/contact-us/) for details.

# Quick Install
You should have at least basic django and django-rest framework experience to run django-scms. We test only in PostgreSQL database.

### Fork the repo
You first need to fork the repo from [Techdometz](https://github.com/TechDometz/django-scms).
### Clone the repo
Clone the forked repo

`git clone https://github.com/[username]/django-scms.git`  

### Create a virtual environment

There are several ways depending on the OS and package you choose. Here's my favorite  
`sudo apt-get install python3-pip`  
`pip3 install virtualenv`  
Then either  
`python3 -m venv venv`  
or  
`python -m venv venv`  
or  
`virtualenv venv` (you can call it venv or anything you like)

#### Activate the virtual environment  

in Mac or Linux
`source venv/bin/activate`  
in windows
`venv/Scripts/activate.bat`  


## 🚀 Key Features

- 🔐 **Authentication & Role-Based Access Control**:  
  Supports authentication and permission control for:
  - **Admins**
  - **Teachers**
  - **Accountants**
  - **Parents**

- 💸 **Finance Module** *(NEW)*:  
  - Manage **Receipts**
  - Track **Payments**
  - Generate **Financial Reports**

- 🧾 **School Information System (SIS)**:
  - Tracks student records and their associated parent/guardian contacts.
  - Manages class and academic year data.
  - Required module for all other apps.

- 📝 **Admissions**:
  - Manages student admission pipeline and levels.
  - Tracks marketing channels and open house participation.

---

## 🔧 Upcoming Features

- 📅 **Schedule Management**
- 🧠 **Examinations and Grading**
- 📚 **Digital Notes and Materials**
- 📊 **Attendance Tracking**

---

## Contributors

- [Mwinamijr](https://github.com/mwinamijr)

## License

The project is licensed under the MIT License

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

### school/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import JsonResponse


def custom_404_handler(request, exception):
    return JsonResponse(
        {
            "error": "Page Not Found",
            "detail": f"The requested URL {request.path} was not found on this server.",
        },
        status=404,
    )


def custom_500_handler(request):
    return JsonResponse(
        {
            "error": "Server Error",
            "detail": "An unexpected error occurred on the server. Please try again later.",
        },
        status=500,
    )


def custom_403_handler(request, exception):
    return JsonResponse(
        {
            "error": "Permission Denied",
            "detail": "You do not have permission to perform this action.",
        },
        status=403,
    )


def custom_400_handler(request, exception):
    return JsonResponse(
        {
            "error": "Bad Request",
            "detail": "The request could not be understood or was missing required parameters.",
        },
        status=400,
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/academic/", include("api.academic.urls")),
    path("api/administration/", include("api.administration.urls")),
    path("api/attendance/", include("api.attendance.urls")),
    path("api/assignments/", include("api.assignments.urls")),
    path("api/blog/", include("api.blog.urls")),
    path("api/finance/", include("api.finance.urls")),
    # path('api/journals/', include('api.journals.urls')),
    # path("api/notes/", include("api.notes.urls")),
    path("api/users/", include("api.users.urls")),
    path("api/timetable/", include("api.schedule.urls")),
    path("api/sis/", include("api.sis.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = custom_404_handler
handler500 = custom_500_handler
handler403 = custom_403_handler
handler400 = custom_400_handler

### manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

### academic/management/commands/update_unpaid_salaries.py
from django.core.management.base import BaseCommand
from users.models import Accountant
from academic.models import Teacher
from django.utils.timezone import now


class Command(BaseCommand):
    help = "Update unpaid salaries for all teachers and accountants."

    def handle(self, *args, **kwargs):
        # Get the current date
        today = now().date()

        # Check if it's the start of a new month
        if today.day == 1:
            # Update unpaid salary for all teachers and accountants
            teachers = Teacher.objects.all()
            accountants = Accountant.objects.all()

            for teacher in teachers:
                teacher.update_unpaid_salary()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated unpaid salary for {teacher.first_name} {teacher.last_name}."
                    )
                )

            for accountant in accountants:
                accountant.update_unpaid_salary()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated unpaid salary for {accountant.first_name} {accountant.last_name}."
                    )
                )

            self.stdout.write(
                self.style.SUCCESS("All unpaid salaries have been updated.")
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "It's not the start of the month, no updates were made."
                )
            )

### academic/management/commands/update_student_debt.py
from django.core.management.base import BaseCommand
from academic.models import Student
from administration.models import Term, AcademicYear
from django.utils.timezone import now


class Command(BaseCommand):
    help = "Update student debt at the start of each term and carry forward unpaid debt to the new academic year."

    def handle(self, *args, **kwargs):
        # Get the current date
        today = now().date()

        # Get the current academic year and term
        current_term = Term.objects.filter(
            start_date__lte=today, end_date__gte=today
        ).first()
        current_year = AcademicYear.objects.filter(current=True).first()

        if not current_term:
            self.stdout.write("No active term found for today.")
            return

        # Update debts for the current term
        students = Student.objects.all()
        for student in students:
            if current_term.academic_year == current_year:
                student.update_debt_for_term(current_term)
            else:
                student.carry_forward_debt_to_new_academic_year()

        self.stdout.write(f"Debts updated for term: {current_term.name}.")

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

### schedule/management/commands/generate_timetable.py
# timetable/management/commands/generate_timetable.py
from django.core.management.base import BaseCommand
from datetime import time, timedelta
from academic.models import AllocatedSubject
from schedule.models import Period
from administration.models import Term


class Command(BaseCommand):
    help = "Generate a timetable for the school learning days with a break after the fourth period."

    def handle(self, *args, **kwargs):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        period_duration = 40
        break_duration = 20
        periods_per_day = 8

        current_term = Term.objects.filter(is_current=True).first()
        if not current_term:
            self.stdout.write(self.style.ERROR("No current term set."))
            return

        allocated_subjects = AllocatedSubject.objects.filter(term=current_term)
        if not allocated_subjects.exists():
            self.stdout.write(
                self.style.WARNING("No AllocatedSubjects found for the current term.")
            )
            return

        for allocated_subject in allocated_subjects:
            weekly_limit = allocated_subject.weekly_periods
            max_daily_periods = allocated_subject.max_daily_periods
            classroom = allocated_subject.class_room
            subject = allocated_subject.subject
            teacher = allocated_subject.teacher

            day_periods = {day: 0 for day in days}

            for day in days:
                time_pointer = time(8, 0)
                consecutive_periods = 0

                for period_index in range(periods_per_day):
                    # Handle the break
                    if period_index == 4:
                        time_pointer = (
                            time_pointer.hour * 60
                            + time_pointer.minute
                            + break_duration
                        ) // 60, (time_pointer.minute + break_duration) % 60
                        time_pointer = time(*time_pointer)
                        continue

                    # Check weekly and daily limits
                    if (
                        day_periods[day] >= weekly_limit
                        or consecutive_periods >= max_daily_periods
                    ):
                        break

                    # Calculate end time
                    end_time_minutes = (
                        time_pointer.hour * 60 + time_pointer.minute + period_duration
                    )
                    end_time = time(end_time_minutes // 60, end_time_minutes % 60)

                    
...[truncated]...

### finance/serializers.py
from django.db import models
from rest_framework import serializers
from .models import (
    Receipt,
    Payment,
    ReceiptAllocation,
    PaymentAllocation,
    DebtRecord,
    PaymentRecord,
)
from academic.models import Student
from administration.models import Term
from users.models import CustomUser, Accountant
from administration.serializers import TermSerializer
from sis.serializers import StudentSerializer
from users.serializers import AccountantSerializer, UserSerializer


class ReceiptAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptAllocation
        fields = ["id", "name", "abbr"]


class PaymentAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAllocation
        fields = ["id", "name", "abbr"]


class ReceiptSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    paid_for = serializers.PrimaryKeyRelatedField(
        queryset=ReceiptAllocation.objects.all()
    )
    received_by = serializers.PrimaryKeyRelatedField(queryset=Accountant.objects.all())
    term = serializers.PrimaryKeyRelatedField(queryset=Term.objects.all())

    student_details = StudentSerializer(read_only=True, source="student")
    paid_for_details = ReceiptAllocationSerializer(read_only=True, source="paid_for")
    received_by_details = AccountantSerializer(read_only=True, source="received_by")
    term_details = TermSerializer(read_only=True, source="term")

    class Meta:
        model = Receipt
        fields = (
            "id",
            "receipt_number",
            "date",
            "payer",
            "paid_for",
            "paid_for_details",
            "student",
            "student_details",
            "amount",
            "term",
            "term_details",
            "paid_through",
            "payment_date",
            "status",
            "received_by",
            "received_by_details",
        )

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive value.")
        return value

    def create(self, validated_data):
        """
        Override create to apply payment to student's DebtRecords.
        """
        receipt = Receipt.objects.create(**validated_data)

        if (
            receipt.student
            and receipt.paid_for
            and receipt.paid_for.name.lower() == "school fees"
        ):
            self.apply_payment_to_debt(receipt.student, receipt.amount, receipt)

        return rec
...[truncated]...

### sis/serializers.py
from rest_framework import serializers

from academic.models import (
    StudentsMedicalHistory,
    Student,
    Parent,
    ReasonLeft,
    ClassLevel,
    ClassYear,
)
from academic.serializers import ClassLevelSerializer, ClassYearSerializer


class ReasonLeftSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReasonLeft
        fields = "__all__"


class StudentHealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsMedicalHistory
        fields = "__all__"


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class SiblingSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class_level = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "full_name",
            "admission_number",
            "gender",
            "class_level",
            "class_of_year",
        ]

    def get_full_name(self, obj):
        return obj.full_name

    def get_class_level(self, obj):
        return obj.class_level.name if obj.class_level else None


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class_level_display = serializers.SerializerMethodField()
    class_of_year_display = serializers.SerializerMethodField()
    parent_guardian_display = serializers.SerializerMethodField()
    siblings = SiblingSerializer(many=True, read_only=True)

    class_level = serializers.CharField(write_only=True, required=True)
    class_of_year = serializers.CharField(
        write_only=False, required=False, allow_null=True
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "admission_number",
            "parent_contact",
            "region",
            "city",
            "street",
            "gender",
            "religion",
            "date_of_birth",
            "std_vii_number",
            "prems_number",
            "full_name",
            "class_level_display",
            "class_of_year_display",
            "parent_guardian_display",
            "class_level",  # write-only
            "class_of_year",  # write-only
            "siblings",
        ]

    def get_full_name(self, obj):
        return obj.full_name

    def get_class_level_display(self, obj):
      
...[truncated]...

### finance/views.py
import openpyxl
from openpyxl.styles import Font
from django.db import transaction
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import (
    DjangoFilterBackend,
    FilterSet,
    DateFilter,
    CharFilter,
)
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from academic.models import Student
from administration.models import Term
from django.utils.timezone import now
from .models import (
    Receipt,
    Payment,
    ReceiptAllocation,
    PaymentAllocation,
    DebtRecord,
    PaymentRecord,
)
from .serializers import (
    ReceiptSerializer,
    PaymentSerializer,
    ReceiptAllocationSerializer,
    PaymentAllocationSerializer,
    DebtRecordSerializer,
    PaymentRecordSerializer,
    StudentDebtOverviewSerializer,
)


class PaymentAllocationListView(APIView):
    """
    Handles GET and POST requests for the list of insurances.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieve a list of all insurances.
        """
        insurances = PaymentAllocation.objects.all()
        serializer = PaymentAllocationSerializer(insurances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new insurance record.
        """
        serializer = PaymentAllocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentAllocationDetailView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single insurance.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(PaymentAllocation, pk=pk)

    def get(self, request, pk):
        """
        Retrieve details of a specific insurance.
        """
        print(request.data)
        insurance = self.get_object(pk)
        serializer = PaymentAllocationSerializer(insurance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an entire insurance record.
        """
        insurance = self.get_object(pk)
  
...[truncated]...

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

### attendance/models.py
from django.db import models
from django.conf import settings

from academic.models import Student
from users.models import CustomUser, Accountant
from academic.models import Teacher
import datetime


# Create your models here.
class AttendanceStatus(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text='"Present" will not be saved but may show as an option for teachers.',
    )
    code = models.CharField(
        max_length=10,
        unique=True,
        help_text="Short code used on attendance reports. Example: 'A' might be the code for 'Absent'.",
    )
    excused = models.BooleanField(default=False)
    absent = models.BooleanField(
        default=False, help_text="Used for different types of absent statuses."
    )
    late = models.BooleanField(
        default=False, help_text="Used for tracking late statuses."
    )
    half = models.BooleanField(
        default=False,
        help_text="Indicates half-day attendance. Do not check absent, otherwise it will double count.",
    )

    class Meta:
        verbose_name_plural = "Attendance Statuses"

    def __str__(self):
        return self.name


class TeachersAttendance(models.Model):
    date = models.DateField(blank=True, null=True, validators=settings.DATE_VALIDATORS)
    teacher = models.ForeignKey(Teacher, blank=True, on_delete=models.CASCADE)
    time_in = models.TimeField(blank=True, null=True)
    time_out = models.TimeField(blank=True, null=True)
    status = models.ForeignKey(
        AttendanceStatus, blank=True, null=True, on_delete=models.CASCADE
    )
    notes = models.CharField(max_length=500, blank=True)

    class Meta:
        unique_together = (("teacher", "date", "status"),)
        ordering = ("-date", "teacher")

    def __str__(self):
        return f"{self.teacher} - {self.date} {self.status}"

    @property
    def edit(self):
        return f"Edit {self.teacher} - {self.date}"

    def save(self, *args, **kwargs):
        """Update for those who are late"""
        present, created = AttendanceStatus.objects.get_or_create(name="Present")

        # Check if the teacher is marked as "Present" and if they are late
        if (
            self.status == present
            and self.time_in
            and self.time_in >= datetime.time(7, 0, 0)
        ):
            self.status.late = True  # Mark status as late
        elif self.status != present:
            self.status.late = False  # Reset late if not present

        super(TeachersAttendance, self).save(*args, **kwargs)


class StudentAttendance(models.Model)
...[truncated]...

### api/schedule/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from schedule.views import PeriodViewSet, run_generate_timetable

# Initialize the router
router = DefaultRouter()
router.register(r"periods", PeriodViewSet, basename="periods")

urlpatterns = [
    # Include ViewSet routes
    path("", include(router.urls)),
    # Generate timetable endpoint
    path("generate-timetable/", run_generate_timetable, name="generate_timetable"),
]

### api/middleware.py
from django.http import JsonResponse
from django.core.exceptions import (
    ValidationError,
    ObjectDoesNotExist,
    PermissionDenied,
)
from django.db import IntegrityError, DatabaseError
from rest_framework.exceptions import APIException
import logging
import traceback

logger = logging.getLogger(__name__)


class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)

        # Common Django errors
        except ValidationError as e:
            return JsonResponse(
                {
                    "error": "Validation Error",
                    "detail": (
                        e.message_dict if hasattr(e, "message_dict") else e.messages
                    ),
                },
                status=400,
            )

        except ObjectDoesNotExist as e:
            return JsonResponse(
                {"error": "Not Found", "detail": str(e)},
                status=404,
            )

        except PermissionDenied as e:
            return JsonResponse(
                {"error": "Permission Denied", "detail": str(e)},
                status=403,
            )

        except IntegrityError as e:
            return JsonResponse(
                {"error": "Integrity Error", "detail": str(e)},
                status=400,
            )

        except DatabaseError as e:
            return JsonResponse(
                {"error": "Database Error", "detail": str(e)},
                status=500,
            )

        # DRF exceptions (optional, for future use if you integrate DRF globally)
        except APIException as e:
            return JsonResponse(
                {"error": "API Error", "detail": str(e.detail)},
                status=e.status_code,
            )

        # Catch-all for other exceptions
        except Exception as e:
            logger.error("Unhandled exception: %s", traceback.format_exc())
            return JsonResponse(
                {"error": "Internal Server Error", "detail": str(e)},
                status=500,
            )

### users/serializers.py
from django.db import transaction
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from academic.models import Teacher, Subject, Parent
from .models import CustomUser, Accountant


class UserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isAccountant = serializers.SerializerMethodField(read_only=True)
    isTeacher = serializers.SerializerMethodField(read_only=True)
    isParent = serializers.SerializerMethodField(read_only=True)
    accountant_details = serializers.SerializerMethodField(read_only=True)
    teacher_details = serializers.SerializerMethodField(read_only=True)
    parent_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "middle_name",
            "last_name",
            "isAdmin",
            "isAccountant",
            "isTeacher",
            "isParent",
            "accountant_details",
            "teacher_details",
            "parent_details",
        ]

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_isAccountant(self, obj):
        return obj.is_accountant

    def get_isTeacher(self, obj):
        return obj.is_teacher

    def get_isParent(self, obj):
        return obj.is_parent

    def get_username(self, obj):
        if obj.first_name and obj.last_name:
            return f"{obj.first_name} {obj.last_name}"
        return obj.email or "Unknown User"

    def get_accountant_details(self, obj):
        """Return accountant details if the user is an accountant."""
        if obj.is_accountant and hasattr(obj, "accountant"):
            return AccountantSerializer(obj.accountant).data
        return None

    def get_teacher_details(self, obj):
        """Return teacher details if the user is a teacher."""
        if obj.is_teacher and hasattr(obj, "teacher"):
            return TeacherSerializer(obj.teacher).data
        return None

    def get_parent_details(self, obj):
        """Return parent details if the user is a parent."""
        if obj.is_parent and hasattr(obj, "parent"):
            return ParentSerializer(obj.parent).data
        return None


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fie
...[truncated]...

### sis/views.py
import openpyxl
from django.db import transaction
from django_filters.rest_framework import FilterSet, CharFilter, DjangoFilterBackend
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, generics
from django.http import Http404


from academic.models import Student, ClassLevel, Parent
from .serializers import StudentSerializer

# Students filter


class StudentFilter(FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    middle_name = CharFilter(field_name="middle_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")
    class_level = CharFilter(method="filter_by_class_level")

    class Meta:
        model = Student
        fields = ["first_name", "middle_name", "last_name", "class_level"]

    def filter_by_class_level(self, queryset, name, value):
        return queryset.filter(class_level__name__icontains=value)


class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response(
            self.get_serializer(student).data, status=status.HTTP_201_CREATED
        )


class StudentDetailView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Bu
...[truncated]...

### administration/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only admins can create/update/delete.
    Everyone else can read.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

### academic/validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core import validators
import re
from datetime import date


def class_room_validator(value):
    """Ensure the classroom name is unique."""
    from .models import ClassRoom

    if ClassRoom.objects.filter(name=value).exists():
        raise ValidationError(_('"{}" already exists.'.format(value)))


def subject_validator(value):
    """Ensure the subject name is unique."""
    from .models import Subject

    if Subject.objects.filter(name=value).exists():
        raise ValidationError(_('"{}" subject already exists.'.format(value)))


def stream_validator(value):
    """Ensure the stream name is unique."""
    from .models import Stream

    if Stream.objects.filter(name=value).exists():
        raise ValidationError(_('"{}" stream already exists.'.format(value)))


def students_date_of_birth_validator(value):
    """
    Validate the student's date of birth to ensure the age is at least 13 years.
    """
    required_age = 13
    least_year_of_birth = date.today().year - required_age

    if value.year > least_year_of_birth:
        raise ValidationErr
...[truncated]...