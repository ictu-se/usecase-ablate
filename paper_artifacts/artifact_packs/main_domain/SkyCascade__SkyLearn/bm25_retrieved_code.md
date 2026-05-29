# README-derived retrieval query
SkyCascade SkyLearn ## README.md
![Group 23](https://github.com/user-attachments/assets/4e84251a-27b0-462b-bd5e-fb0bcadc4694)

### The world’s most high-end designed, lightweight, and feature-rich learning management system.

# SkyLearn: Open source learning management system

Learning management system using Django web framework. You might want to develop a learning management system (also known as a school/college management system) for a school/college organization, or simply for the purpose of learning the tech stack and enhancing your portfolio. In either case, this project would be a great way to get started. The aim is to create the world's most lightweight yet feature-rich learning management system. However, this is not possible without your support, so please give it a star ⭐️.

_Documentation is under development_

Let's enhance the project by contributing! 👩‍💻👩‍💻

<img width="1440" alt="screenshot" src="https://github.com/user-attachments/assets/08644f49-6ae0-4695-86cc-afe331c6f61a">

## Current features

- Dashboard: School demographics and analytics. Restricted to only admins
- News And Events: All users can access this page
- Admin manages students(Add, Update, Delete)
- Admin manages lecturers(Add, Update, Delete)
- Students can Add and Drop courses
- Lecturers submit students' scores: _Attendance, Mid exam, Final exam, assignment_
- The system calculates students' _Total, average, point, and grades automatically_
- Grade comment for each student with a **pass**, **fail**, or **pass with a warning**
- Assessment result page for students
- Grade result page for students
- Session/year and semester management
- Assessments and grades will be grouped by semester
- Upload video and documentation for each course
- PDF generator for students' registration slip and grade result
- Page access restriction
- Storing of quiz results under each user
- Question order randomization
- Previous quiz scores can be viewed on the category page
- Correct answers can be shown after each question or all at once at the end
- Logged-in users can return to an incomplete quiz to finish it and non-logged-in users can complete a quiz if their session persists
- The quiz can be limited to one attempt per user
- Questions can be given a category
- Success rate for each category can be monitored on a progress page
- Explanation for each question result can be given
- Pass marks can be set
- Multiple choice question type
- True/False question type
- Essay question type................._Coming soon_
- Custom message displayed for those that pass or fail a quiz
- Custom permission (view_sittings) added, allowing users with that permission to view quiz results from users
- A marking page which lists completed quizzes, can be filtered by quiz or user, and is used to mark essay questions

# Quick note for future contributors

If you would like to contribute, simply begin by implementing one from the list in the `TODO.md` file.

# Requirements:

> The following program(s) are required to run the project

- [Python3.8+](https://www.python.org/downloads/)

# Installation

- Clone the repo with

```bash
git clone https://github.com/SkyCascade/SkyLearn.git
```

- Create and activate a python virtual environment

```bash
pip install -r requirements.txt
```

- Create `.env` file inside the root directory

- Copy and paste everything in the `.env.example` file into the `.env` file. Don't forget to customize the variable values

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver
```

Last but not least, go to this address http://127.0.0.1:8000

#### _Check [this page](https://adilmohak.github.io/dj-lms-starter/) for more insight and support._

# References

- Quiz part: https://github.com/tomwalker/django_quiz

#### Show your support by ⭐️ this project! CODE_OF_CONDUCT.md
CONTRIBUTING.md
README.md
TODO.md
accounts/__init__.py
accounts/admin.py
accounts/apps.py
accounts/decorators.py
accounts/filters.py
accounts/forms.py
accounts/models.py
accounts/signals.py
accounts/tests/__init__.py
accounts/tests/test_decorators.py
accounts/tests/test_filters.py
accounts/translation.py
accounts/urls.py
accounts/utils.py
accounts/validators.py
accounts/views.py
config/__init__.py
config/asgi.py
config/settings.py
config/urls.py
config/wsgi.py
core/__init__.py
core/admin.py
core/apps.py
core/forms.py
core/models.py
core/tests.py
core/translation.py
core/urls.py
core/utils.py
core/views.py
course/__init__.py
course/admin.py
course/apps.py
course/decorators.py
course/filters.py
course/forms.py
course/models.py
course/tests.py
course/translation.py
course/urls.py
course/utils.py
course/views.py
manage.py
payments/__init__.py
payments/admin.py
payments/apps.py
payments/models.py
payments/tests.py
payments/urls.py
payments/views.py
quiz/__init__.py
quiz/admin.py
quiz/apps.py
quiz/forms.py
quiz/models.py
quiz/templatetags/__init__.py
quiz/templatetags/quiz_tags.py
quiz/tests.py
quiz/translation.py
quiz/urls.py
quiz/utils.py
quiz/views.py
requirements.txt
requirements/base.txt
requirements/local.txt
requirements/production.txt
result/__init__.py
result/admin.py
result/apps.py
result/models.py
result/tests.py
result/urls.py
result/views.py
scripts/__init__.py
scripts/generate_fake_accounts_data.py
scripts/generate_fake_core_data.py
scripts/generate_fake_data.py
search/__init__.py
search/admin.py
search/apps.py
search/models.py
search/templatetags/__init__.py
search/templatetags/class_name.py
search/tests.py
search/urls.py
search/views.py

# BM25 selected code snippets
### README.md
![Group 23](https://github.com/user-attachments/assets/4e84251a-27b0-462b-bd5e-fb0bcadc4694)

### The world’s most high-end designed, lightweight, and feature-rich learning management system.

# SkyLearn: Open source learning management system

Learning management system using Django web framework. You might want to develop a learning management system (also known as a school/college management system) for a school/college organization, or simply for the purpose of learning the tech stack and enhancing your portfolio. In either case, this project would be a great way to get started. The aim is to create the world's most lightweight yet feature-rich learning management system. However, this is not possible without your support, so please give it a star ⭐️.

_Documentation is under development_

Let's enhance the project by contributing! 👩‍💻👩‍💻

<img width="1440" alt="screenshot" src="https://github.com/user-attachments/assets/08644f49-6ae0-4695-86cc-afe331c6f61a">

## Current features

- Dashboard: School demographics and analytics. Restricted to only admins
- News And Events: All users can access this page
- Admin manages students(Add, Update, Delete)
- Admin manages lecturers(Add, Update, Delete)
- Students can Add and Drop courses
- Lecturers submit students' scores: _Attendance, Mid exam, Final exam, assignment_
- The system calculates students' _Total, average, point, and grades automatically_
- Grade comment for each student with a **pass**, **fail**, or **pass with a warning**
- Assessment result page for students
- Grade result page for students
- Session/year and semester management
- Assessments and grades will be grouped by semester
- Upload video and documentation for each course
- PDF generator for students' registration slip and grade result
- Page access restriction
- Storing of quiz results under each user
- Question order randomization
- Previous quiz scores can be viewed on the category page
- Correct answers can be shown after each question or all at once at the end
- Logged-in users can return to an incomplete quiz to finish it and non-logged-in users can complete a quiz if their session persists
- The quiz can be limited to one attempt per user
- Questions can be given a category
- Success rate for each category can be monitored on a progress page
- Explanation for each question result can be given
- Pass marks can be set
- Multiple choice question type
- True/False question type
- Essay question type................._Coming soon_
- Custom message displayed for those that pass or fail a quiz
- Custom permission (view_sittings) added, 
...[truncated]...

### TODO.md
# TODO

- **School calendar**
  - School calendar should be implemented displayed on the home page along with news and events
  - Managed by admin/superadmin
- **News and events**
  - News and events should be associated with the calendar
- **Add and Drop**:
  - Department head
  - The add and drop page should only include courses offered by the department head.
  - Add and drop date should be restricted by the school calendar.
- **Payment integration**:
  - Integrating PayPal and Stripe for students to pay their fees.
- **Integrate the dashboard with dynamic/live data**:
  - Overall attendance
  - School demographics
    - Lecturer qualification
    - Students' level
  - Students average grade per course:
    This helps to keep track of students' performance
  - Overall Course Resources
    - Total number of videos, courses, documentation
  - Event calendar:
    - A calendar that shows upcoming events
  - Enrollments per course
    - How many students enroll in each course
  - Website traffic over a specific user type (Admin, Student, Lecturer, etc.)
- **Apply data exporting for all tables**:
  - This can be done using jQuery libraries like `DataTables`
- **Using a template to PDF converter to generate reports**:
  - This can be done using the popular package `xhtml2pdf`

### config/settings.py
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY", default="o!ld8nrt4vc*h1zoey*wj48x*q0#ss12h=+zh)kk^6b3aygg=!"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["127.0.0.1", "adilmohak1.pythonanywhere.com"]

# change the default user models to our custom model
AUTH_USER_MODEL = "accounts.User"

# Application definition

DJANGO_APPS = [
    "modeltranslation",  # Translation
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Third party apps
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "django_filters",
]

# Custom apps
PROJECT_APPS = [
    "core.apps.CoreConfig",
    "accounts.apps.AccountsConfig",
    "course.apps.CourseConfig",
    "result.apps.ResultConfig",
    "search.apps.SearchConfig",
    "quiz.apps.QuizConfig",
    "payments.apps.PaymentsConfig",
]

# Combine all apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise to serve static files
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
    
...[truncated]...

### CONTRIBUTING.md
# Contributing to SkyLearn

Thank you for considering contributing to SkyLearn! We welcome your contributions to help improve and enhance the project.
Whether you're submitting code, documentation, or bug reports, your help is greatly appreciated.

Before you start contributing, please take a moment to review the following guidelines.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Style Guidelines](#style-guidelines)
- [License](#license)

## Code of Conduct

Please review and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a positive and respectful atmosphere within the community.

## Getting Started

Before contributing, make sure you have the project set up on your local machine. Refer to the README for installation and setup instructions.

## How Can I Contribute?

### Reporting Bugs

Found a bug? Please open an issue on the repository with a detailed description of the problem. Include steps to reproduce it, expected behavior, and any relevant information.

### Suggesting Enhancements

Have an idea for an improvement? We'd love to hear it! Open an issue and describe your enhancement suggestion, why you think it would be valuable, and any additional context.

### Pull Requests

We welcome pull requests! To contribute code:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and ensure that the code passes any existing tests.
4. Write clear and concise commit messages.
5. Push your branch to your fork.
6. Open a pull request to the `main` branch of this repository.

Please make sure your code adheres to our [style guidelines](#style-guidelines).

## Style Guidelines

Maintaining consistent coding style is important for the project's readability. Follow these guidelines when submitting code:

- Use consistent indentation (spaces).
- Keep lines under 80 characters for code, and under 120 characters for comments and documentation.
- Write clear and descriptive variable and function names.
- Document your code using comments or docstrings.
- Follow the coding conventions used in the existing codebase.

## License

By contributing to SkyLearn, you agree that your contributions will be licensed under the [SkyLearn's license](https://github.com/SkyCascade/SkyLearn/blob/main/LICENSE).

---

Thank you for contributing to SkyLearn!
Your support helps make this project better f
...[truncated]...

### quiz/models.py
import json
import re

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.validators import (
    MaxValueValidator,
    validate_comma_separated_integer_list,
)
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from model_utils.managers import InheritanceManager

from course.models import Course
from core.utils import unique_slug_generator

CHOICE_ORDER_OPTIONS = (
    ("content", _("Content")),
    ("random", _("Random")),
    ("none", _("None")),
)

CATEGORY_OPTIONS = (
    ("assignment", _("Assignment")),
    ("exam", _("Exam")),
    ("practice", _("Practice Quiz")),
)


class QuizManager(models.Manager):
    def search(self, query=None):
        queryset = self.get_queryset()
        if query:
            or_lookup = (
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(category__icontains=query)
                | Q(slug__icontains=query)
            )
            queryset = queryset.filter(or_lookup).distinct()
        return queryset


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Title"), max_length=60)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        help_text=_("A detailed description of the quiz"),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_OPTIONS, blank=True)
    random_order = models.BooleanField(
        default=False,
        verbose_name=_("Random Order"),
        help_text=_("Display the questions in a random order or as they are set?"),
    )
    answers_at_end = models.BooleanField(
        default=False,
        verbose_name=_("Answers at end"),
        help_text=_(
            "Correct answer is NOT shown after question. Answers displayed at the end."
        ),
    )
    exam_paper = models.BooleanField(
        default=False,
        verbose_name=_("Exam Paper"),
        help_text=_(
            "If yes, the result of each attempt by a user will be stored. Necessary for marking."
        ),
    )
    single_attempt = models.BooleanField(
        default=False,
        verbose_name=_("Single Attempt"),
        help_text=_("If yes, only one attempt by a user will be per
...[truncated]...

### requirements/base.txt
pytz==2022.7  # https://github.com/stub42/pytz
Pillow==9.3.0  # https://github.com/python-pillow/Pillow        
whitenoise==6.2.0  # https://github.com/evansd/whitenoise

# Django
# ------------------------------------------------------------------------------
django==4.0.8  # pyup: < 4.1  # https://www.djangoproject.com/
django-model-utils==4.3.1  # https://github.com/jazzband/django-model-utils
django-crispy-forms==1.14.0  # https://github.com/django-crispy-forms/django-crispy-forms
crispy-bootstrap5==0.7  # https://github.com/django-crispy-forms/crispy-bootstrap5
django-filter==23.5 # https://github.com/carltongibson/django-filter
django-modeltranslation==0.18.11 # https://github.com/Buren/django-modeltranslation

# PDF generator
reportlab==4.0.4
xhtml2pdf==0.2.15

# Customize django admin
django-jet-reboot==1.3.5

# Environment variable
python-decouple==3.8

# Payments
stripe==5.5.0
gopay==2.0.1

### quiz/forms.py
from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _
from django.forms.models import inlineformset_factory
from .models import Question, Quiz, MCQuestion, Choice


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_choices_list()]
        self.fields["answers"] = forms.ChoiceField(
            choices=choice_list, widget=RadioSelect
        )


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={"style": "width:100%"})
        )


class QuizAddForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(verbose_name=_("Questions"), is_stacked=False),
    )

    def __init__(self, *args, **kwargs):
        super(QuizAddForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["questions"].initial = (
                self.instance.question_set.all().select_subclasses()
            )

    def save(self, commit=True):
        quiz = super(QuizAddForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data["questions"])
        self.save_m2m()
        return quiz


class MCQuestionForm(forms.ModelForm):
    class Meta:
        model = MCQuestion
        exclude = ()


class MCQuestionFormSet(forms.BaseInlineFormSet):
    def clean(self):
        """
        Custom validation for the formset to ensure:
        1. At least two choices are provided and not marked for deletion.
        2. At least one of the choices is marked as correct.
        """
        super().clean()

        # Collect non-deleted forms
        valid_forms = [
            form for form in self.forms if not form.cleaned_data.get("DELETE", True)
        ]

        valid_choices = [
            "choice_text" in form.cleaned_data.keys() for form in valid_forms
        ]
        if not all(valid_choices):
            raise forms.ValidationError("You must add a valid choice name.")

        # If all forms are deleted, raise a validation error
        if len(valid
...[truncated]...

### quiz/admin.py
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from modeltranslation.forms import TranslationModelForm

from .models import (
    Quiz,
    Progress,
    Question,
    MCQuestion,
    Choice,
    EssayQuestion,
    Sitting,
)


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuizAdminForm(TranslationModelForm):
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(verbose_name=_("Questions"), is_stacked=False),
    )

    class Meta:
        model = Quiz
        fields = ["title_en"]

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["questions"].initial = (
                self.instance.question_set.all().select_subclasses()
            )

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data["questions"])
        self.save_m2m()
        return quiz


class QuizAdmin(TranslationAdmin):
    pass
    # form = QuizAdminForm
    # fields = (
    #     "title",
    #     "description",
    # )
    # list_display = ("title",)
    # # list_filter = ('category',)
    # search_fields = (
    #     "description",
    #     "category",
    # )


class MCQuestionAdmin(TranslationAdmin):
    list_display = ("content",)
    # list_filter = ('category',)
    fieldsets = [
        ("figure" "quiz" "choice_order", {"fields": ("content", "explanation")})
    ]

    search_fields = ("content", "explanation")
    filter_horizontal = ("quiz",)

    inlines = [ChoiceInline]


class ProgressAdmin(admin.ModelAdmin):
    search_fields = (
        "user",
        "score",
    )


class EssayQuestionAdmin(admin.ModelAdmin):
    list_display = ("content",)
    # list_filter = ('category',)
    fields = (
        "content",
        "quiz",
        "explanation",
    )
    search_fields = ("content", "explanation")
    filter_horizontal = ("quiz",)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(EssayQuestion, EssayQuestionAdmin)
admin.site.register(Sitting)

### accounts/tests/test_filters.py
from django.test import TestCase
from accounts.filters import LecturerFilter, StudentFilter
from accounts.models import User, Student
from course.models import Program


class LecturerFilterTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username="user1",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
        )
        User.objects.create(
            username="user2",
            first_name="Jane",
            last_name="Doe",
            email="jane@example.com",
        )
        User.objects.create(
            username="user3",
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
        )

    def test_username_filter(self):
        filter_set = LecturerFilter(data={"username": "user1"})
        self.assertEqual(len(filter_set.qs), 1)

    def test_name_filter(self):
        filter_set = LecturerFilter(data={"name": "John"})
        self.assertEqual(len(filter_set.qs), 1)

    def test_email_filter(self):
        filter_set = LecturerFilter(data={"email": "example.com"})
        self.assertEqual(
            len(filter_set.qs), 3
        )  # All users should be returned since all have email addresses with "example.com"

    def test_combined_filters(self):
        filter_set = LecturerFilter(data={"name": "Doe", "email": "example.com"})
        self.assertEqual(
            len(filter_set.qs), 2
        )  # Both John Doe and Jane Doe should be returned

        filter_set = LecturerFilter(data={"name": "Alice", "email": "example.com"})
        self.assertEqual(
            len(filter_set.qs), 1
        )  # 1 user matches Alice with "example.com" in the email

    def test_no_filters(self):
        filter_set = LecturerFilter(data={})
        self.assertEqual(
            len(filter_set.qs), 3
        )  # All users should be returned since no filters are applied


class StudentFilterTestCase(TestCase):
    def setUp(self):
        program1 = Program.objects.create(
            title="Computer Science", summary="Program for computer science students"
        )
        program2 = Program.objects.create(
            title="Mathematics", summary="Program for mathematics students"
        )
        program3 = Program.objects.create(
            title="Computer Engineering",
            summary="Program for computer engineering students",
        )

        Student.objects.create(
            student=User.objects.create(
                username="student1",
                first_name="John",
                last_name="D
...[truncated]...

### scripts/generate_fake_core_data.py
import os
import django
import random
from typing import List
from django.utils import timezone
from faker import Faker
from factory.django import DjangoModelFactory
from factory import SubFactory, LazyAttribute, Iterator, LazyFunction
from core.models import ActivityLog, NewsAndEvents, Session, Semester, SEMESTER, POST

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

fake = Faker()


class NewsAndEventsFactory(DjangoModelFactory):
    """
    Factory for creating NewsAndEvents instances.

    Attributes:
        title (str): The generated title for the news or event.
        summary (str): The generated summary.
        posted_as (str): The type of the post, either 'News' or 'Event'.
        updated_date (datetime): The generated date and time of update.
        upload_time (datetime): The generated date and time of upload.
    """

    class Meta:
        model = NewsAndEvents

    title: str = LazyAttribute(lambda x: fake.sentence(nb_words=4))
    summary: str = LazyAttribute(lambda x: fake.paragraph(nb_sentences=3))
    posted_as: str = LazyFunction(
        lambda: fake.random_element(elements=[choice[0] for choice in POST])
    )
    # updated_date: timezone.datetime = fake.date_time_this_year()
    # upload_time: timezone.datetime = fake.date_time_this_year()


class SessionFactory(DjangoModelFactory):
    """
    Factory for creating Session instances.

    Attributes:
        session (str): The generated session name.
        is_current_session (bool): Flag indicating if the session is current.
        next_session_begins (date): The date when the next session begins.
    """

    class Meta:
        model = Session

    session: str = LazyAttribute(lambda x: str(fake.random_int(min=2020, max=2030)))
    is_current_session: bool = fake.boolean(chance_of_getting_true=50)
    next_session_begins = LazyAttribute(lambda x: fake.future_datetime())


class SemesterFactory(DjangoModelFactory):
    """
    Factory for creating Semester instances.

    Attributes:
        semester (str): The generated semester name.
        is_current_semester (bool): Flag indicating if the semester is current.
        session (Session): The associated session.
        next_semester_begins (date): The date when the next semester begins.
    """

    class Meta:
        model = Semester

    semester: str = fake.random_element(elements=[choice[0] for choice in SEMESTER])
    is_current_semester: bool = fake.boolean(chance_of_getting_true=50)
    session: Session = SubFactory(SessionFactory)
    next_semester_b
...[truncated]...

### config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

admin.site.site_header = "SkyLearn Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("", include("core.urls")),
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path(
        "jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")
    ),  # Django JET dashboard URLS
    path("accounts/", include("accounts.urls")),
    path("programs/", include("course.urls")),
    path("result/", include("result.urls")),
    path("search/", include("search.urls")),
    path("quiz/", include("quiz.urls")),
    path("payments/", include("payments.urls")),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

### manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
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

### scripts/generate_fake_accounts_data.py
import os
import django
from typing import List, Tuple
from django.utils import timezone
from faker import Faker
from factory.django import DjangoModelFactory
from factory import SubFactory, LazyAttribute, Iterator
from django_extensions.management.commands import runscript

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from accounts.models import User, Student, Parent, DepartmentHead, LEVEL, RELATION_SHIP
from course.models import Program

fake = Faker()


class UserFactory(DjangoModelFactory):
    """
    Factory for creating User instances with optional flags.

    Attributes:
        username (str): The generated username.
        first_name (str): The generated first name.
        last_name (str): The generated last name.
        email (str): The generated email.
        date_joined (datetime): The current date and time.
        phone (str): The generated phone number.
        address (str): The generated address.
        is_student (bool): Flag indicating if the user is a student.
        is_lecturer (bool): Flag indicating if the user is a lecturer.
        is_parent (bool): Flag indicating if the user is a parent.
        is_dep_head (bool): Flag indicating if the user is a department head.
    """

    class Meta:
        model = User

    username: str = LazyAttribute(lambda x: fake.user_name())
    first_name: str = LazyAttribute(lambda x: fake.first_name())
    last_name: str = LazyAttribute(lambda x: fake.last_name())
    email: str = LazyAttribute(lambda x: fake.email())
    date_joined: timezone.datetime = timezone.now()
    phone: str = LazyAttribute(lambda x: fake.phone_number())
    address: str = LazyAttribute(lambda x: fake.address())
    is_student: bool = False
    is_lecturer: bool = False
    is_parent: bool = False
    is_dep_head: bool = False

    @classmethod
    def _create(cls, model_class: type, *args, **kwargs) -> User:
        """
        Create a User instance with optional flags.

        Args:
            model_class (type): The class of the model to create.

        Returns:
            User: The created User instance.
        """
        user: User = super()._create(model_class, *args, **kwargs)

        # Set the appropriate flags based on the user type
        if cls.is_student:
            user.is_student = True
        elif cls.is_parent:
            user.is_parent = True

        user.save()
        return user


class ProgramFactory(DjangoModelFactory):
    """
    Factory for creating Program instances.

    Attributes:
        title (str): The g
...[truncated]...

### result/urls.py
from django.urls import path
from .views import (
    add_score,
    add_score_for,
    grade_result,
    assessment_result,
    course_registration_form,
    result_sheet_pdf_view,
)


urlpatterns = [
    path("manage-score/", add_score, name="add_score"),
    path("manage-score/<int:id>/", add_score_for, name="add_score_for"),
    path("grade/", grade_result, name="grade_results"),
    path("assessment/", assessment_result, name="ass_results"),
    path("result/print/<int:id>/", result_sheet_pdf_view, name="result_sheet_pdf_view"),
    path(
        "registration/form/", course_registration_form, name="course_registration_form"
    ),
]

### accounts/views.py
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template, render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django_filters.views import FilterView
from xhtml2pdf import pisa

from accounts.decorators import admin_required
from accounts.filters import LecturerFilter, StudentFilter
from accounts.forms import (
    ParentAddForm,
    ProfileUpdateForm,
    ProgramUpdateForm,
    StaffAddForm,
    StudentAddForm,
)
from accounts.models import Parent, Student, User
from core.models import Semester, Session
from course.models import Course
from result.models import TakenCourse

# ########################################################
# Utility Functions
# ########################################################


def render_to_pdf(template_name, context):
    """Render a given template to PDF format."""
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="profile.pdf"'
    template = render_to_string(template_name, context)
    pdf = pisa.CreatePDF(template, dest=response)
    if pdf.err:
        return HttpResponse("We had some problems generating the PDF")
    return response


# ########################################################
# Authentication and Registration
# ########################################################


def validate_username(request):
    username = request.GET.get("username", None)
    data = {"is_taken": User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(data)


def register(request):
    if request.method == "POST":
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")
        messages.error(
            request, "Something is not correct, please fill all fields correctly."
        )
    else:
        form = StudentAddForm()
    return render(request, "registration/register.html", {"form": form})


# ########################################################
# Profile Views
# ########################################################


@login_required
def profile(request):
    """Show profile of the current user."""
    cur
...[truncated]...

### result/models.py
from decimal import Decimal
from django.conf import settings

from django.db import models
from django.urls import reverse

from accounts.models import Student
from core.models import Semester
from course.models import Course

A_PLUS = "A+"
A = "A"
A_MINUS = "A-"
B_PLUS = "B+"
B = "B"
B_MINUS = "B-"
C_PLUS = "C+"
C = "C"
C_MINUS = "C-"
D = "D"
F = "F"
NG = "NG"

GRADE_CHOICES = (
    (A_PLUS, "A+"),
    (A, "A"),
    (A_MINUS, "A-"),
    (B_PLUS, "B+"),
    (B, "B"),
    (B_MINUS, "B-"),
    (C_PLUS, "C+"),
    (C, "C"),
    (C_MINUS, "C-"),
    (D, "D"),
    (F, "F"),
    (NG, "NG"),
)

PASS = "PASS"
FAIL = "FAIL"

COMMENT_CHOICES = (
    (PASS, "PASS"),
    (FAIL, "FAIL"),
)

GRADE_BOUNDARIES = [
    (90, A_PLUS),
    (85, A),
    (80, A_MINUS),
    (75, B_PLUS),
    (70, B),
    (65, B_MINUS),
    (60, C_PLUS),
    (55, C),
    (50, C_MINUS),
    (45, D),
    (0, F),
]

GRADE_POINT_MAPPING = {
    A_PLUS: 4.0,
    A: 4.0,
    A_MINUS: 3.75,
    B_PLUS: 3.5,
    B: 3.0,
    B_MINUS: 2.75,
    C_PLUS: 2.5,
    C: 2.0,
    C_MINUS: 1.75,
    D: 1.0,
    F: 0.0,
    NG: 0.0,
}


class TakenCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="taken_courses"
    )
    assignment = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )
    mid_exam = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )
    quiz = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))
    attendance = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )
    final_exam = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )
    total = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00"), editable=False
    )
    grade = models.CharField(
        choices=GRADE_CHOICES, max_length=2, blank=True, editable=False
    )
    point = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00"), editable=False
    )
    comment = models.CharField(
        choices=COMMENT_CHOICES, max_length=200, blank=True, editable=False
    )

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.course.slug})

    def __str__(self):
        return f"{self.course.title} ({self.course.code})"

    def get_total(self):
        return sum(
            [
                Decimal(self.assignment),
                Decimal(s
...[truncated]...

### result/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT

# from reportlab.platypus.tables import Table
from reportlab.lib.units import inch
from reportlab.lib import colors

from core.models import Session, Semester
from course.models import Course
from accounts.models import Student
from accounts.decorators import lecturer_required, student_required
from .models import TakenCourse, Result


CM = 2.54


# ########################################################
# Score Add & Add for
# ########################################################
@login_required
@lecturer_required
def add_score(request):
    """
    Shows a page where a lecturer will select a course allocated
    to him for score entry. in a specific semester and session
    """
    current_session = Session.objects.filter(is_current_session=True).first()
    current_semester = Semester.objects.filter(
        is_current_semester=True, session=current_session
   
...[truncated]...