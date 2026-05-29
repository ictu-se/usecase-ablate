# Deterministic random code snippets
### resources/admin.py
from django.contrib import admin
from resources.models import Resource
# Register your models here.
admin.site.register(Resource)

### assignments/views.py
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import os
from django.conf import settings

# from django.contrib import messages
from django.views import generic
from django.shortcuts import get_object_or_404
from users.models import User
from assignments.models import Assignment, SubmitAssignment
from assignments.forms import GradeAssignmentForm, CreateAssignmentForm, SubmitAssignmentForm
from courses.models import Course

# Create your views here.    
class CreateAssignment(LoginRequiredMixin, generic.CreateView):
    form_class = CreateAssignmentForm
    template_name = 'assignments/create_assignment_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class UpdateAssignment(LoginRequiredMixin, generic.UpdateView):
    model = Assignment
    form_class = CreateAssignmentForm
    template_name = 'assignments/create_assignment_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class DeleteAssignment(LoginRequiredMixin, generic.DeleteView):
    model = Assignment
    success_url = reverse_lazy('courses:list')

class SubmitAssignmentView(LoginRequiredMixin, generic.CreateView):
    form_class = SubmitAssignmentForm
    template_name = 'assignments/submitassignment_form.html'
    select_related = ('author', 'assignment_ques')
    # success_url = reverse('assignments:submit_detail')

    def get_context_data(self, **kwargs):
        assignments = Assignment.objects.filter(pk=self.request.session.get('assignment'))
        assignment_object = get_object_or_404(assignments)
        context = super(SubmitAssignmentView, self).get_context_data(**kwargs)
        context['duedate'] = assignment_object.due_date
        context['time'] = timezone.now()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['assignment_id'] = self.request.session.get('assignment')
        kwargs['user'] = self.request.user
        return kwargs

class SubmitAssignmentDetail(LoginRequiredMixin, generic.DetailView):
    model = SubmitAssignment
    template_nam
...[truncated]...

### courses/views.py
from django.shortcuts import render
import datetime
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.shortcuts import get_object_or_404
from users.models import User
from courses.models import Course, Enrollment
from assignments.models import Assignment
from resources.models import Resource

# Create your views here.
class CreateCourse(LoginRequiredMixin, generic.CreateView):
    fields = ('course_name', 'course_description')
    model = Course

    def get(self, request,*args, **kwargs):
        self.object = None
        context_dict = self.get_context_data()
        context_dict.update(user_type=self.request.user.user_type)
        return self.render_to_response(context_dict)
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(CreateCourse, self).form_valid(form)
    
class CourseDetail(generic.DetailView):
    model = Course

    def get_context_data(self,**kwargs):
        assignments = Assignment.objects.filter(course=self.kwargs['pk'])
        resources = Resource.objects.filter(course=self.kwargs['pk'])
        context = super(CourseDetail, self).get_context_data(**kwargs)
        context['assignments'] = assignments
        context['resources'] = resources
        return context

class ListCourse(generic.ListView):
    model = Course

class EnrollCourse(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('courses:detail', kwargs={'pk':self.kwargs.get('pk')})
    
    def get(self, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs.get('pk'))

        try:
            Enrollment.objects.create(student=self.request.user, course=course)
        except:
            messages.warning(self.request, 'You are already enrolled in the course.')
        else:
            messages.success(self.request, 'You are now enrolled in the course.')
        return super().get(self.request, *args, **kwargs)

class UnenrollCourse(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('courses:detail', kwargs={'pk':self.kwargs.get('pk')})

    def get(self, *args, **kwargs):

        try:
            enrollment = Enrollment.objects.filter(
                student=self.request.user,
                course__pk=self.kwargs.get('pk')
            ).get()
        except Enrollment.DoesNot
...[truncated]...

### users/urls.py
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from users import views

app_name = 'users'

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    url(r'logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'signup/$', views.SignUp.as_view(), name='signup')
]

### users/apps.py
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

### resources/tests.py
from django.test import TestCase

# Create your tests here.

### users/admin.py
from django.contrib import admin
from users.models import User

# Register your models here.
admin.site.register(User)

### courses/models.py
from django.db import models
from django.urls import reverse
from users.models import User

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_description = models.TextField()
    teacher = models.ForeignKey(User, related_name="course", on_delete=models.CASCADE)
    students = models.ManyToManyField(User, through='Enrollment', related_name="student_course")

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['course_name']

class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name="enrollments",on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="user_courses", on_delete=models.CASCADE)

    def __str__(self):
        self.student.username

    class Meta:
        unique_together = ('course', 'student')

### assignments/tests.py
from django.test import TestCase

# Create your tests here.

### django_lms/settings.py
"""
Django settings for django_lms project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x#d7_3ws7!%((d$pbm8l^=oghi%-^y&eo-9h@^^yx1#s826z0x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',
    'courses',
    'assignments',
    'bootstrap4',
    'resources',
    'graphene_django',
    'crispy_forms',
    'django_forms_bootstrap',
]

GRAPHENE = {
    'SCHEMA': 'django_lms.schema.schema'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_lms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "courses.context_processors.courses_processor"
            ],
        },
    },
]


WSGI_APPLICATION = 'django_lms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'EN
...[truncated]...

### assignments/schema.py
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from graphene_file_upload.scalars import Upload
from assignments.models import Assignment, SubmitAssignment
from courses.models import Course
from courses import schema as course_schema
from users import schema as user_schema


class AssignmentType(DjangoObjectType):
    class Meta:
        model = Assignment

class SubmissionType(DjangoObjectType):
    class Meta:
        model = SubmitAssignment

class Query(ObjectType):
    assignment = graphene.Field(AssignmentType, id=graphene.Int())
    submission = graphene.Field(SubmissionType, id=graphene.Int())
    assignments = graphene.List(AssignmentType)
    submissions = graphene.List(SubmissionType)

    def resolve_assignment(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Assignment.objects.get(pk=id)
        
        return None
    
    def resolve_submission(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return SubmitAssignment.objects.get(pk=id)
        
        return None
    
    def resolve_assignments(self, info, **kwargs):
        return Assignment.objects.all()
    
    def resolve_submissions(self, info, **kwargs):
        return SubmitAssignment.objects.all()

class AssignmentInput(graphene.InputObjectType):
    id = graphene.ID()
    assignment_name = graphene.String()
    assignment_description = graphene.String()
    start_date = graphene.DateTime()
    due_date = graphene.DateTime()
    course = graphene.Field(course_schema.CourseInput)

class SubmissionInput(graphene.InputObjectType):
    id = graphene.ID()
    author = graphene.Field(user_schema.UserInput)
    topic = graphene.String()
    description = graphene.String()
    assignment_file = Upload()
    submitted_date = graphene.DateTime()
    assignment_ques = graphene.Field(AssignmentInput)
    graded = graphene.Boolean()
    grade = graphene.Int()

class CreateAssignment(graphene.Mutation):
    class Arguments:
        input = AssignmentInput(required=True)
    
    ok = graphene.Boolean()
    assignment = graphene.Field(AssignmentType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        course = Course.objects.get(pk=input.course.id)
        assignment_instance = Assignment(
            assignment_name=input.assignment_name,
            assignment_description=input.assignment_description,
            start_date=input.start_date,
            due_date=input.due_date,
            course=course,
        )
        assignment_in
...[truncated]...

### manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_lms.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

### django_lms/asgi.py
"""
ASGI config for django_lms project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_lms.settings')

application = get_asgi_application()

### users/tests.py
from django.test import TestCase

# Create your tests here.

### django_lms/wsgi.py
"""
WSGI config for django_lms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_lms.settings')

application = get_wsgi_application()

### users/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

### django_lms/schema.py
import graphene
from courses import schema as course_schema
from resources import schema as resource_schema
from users import schema as user_schema
from assignments import schema as assignment_schema


class Query(assignment_schema.Query, course_schema.Query, resource_schema.Query, user_schema.Query, graphene.ObjectType):
    pass


class Mutation(assignment_schema.Mutation, course_schema.Mutation, resource_schema.Mutation, user_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

### resources/views.py
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from resources.forms import CreateResourceForm
from resources.models import Resource

# Create your views here.


class CreateResource(LoginRequiredMixin, generic.CreateView):
    form_class = CreateResourceForm
    template_name = 'resources/create_resource_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@login_required
def delete_view(request, pk):
    obj = get_object_or_404(Resource, pk=pk)
    context = {'resource': obj}
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse("courses:list"))
    return render(request, "resources/resource_confirm_delete.html", context)

### users/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_type')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = "Email Address"
        self.fields['user_type'].label = "Register as:"

### resources/schema.py
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from graphene_file_upload.scalars import Upload
from resources.models import Resource
from courses.models import Course
from courses import schema as course_schema


class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource


class Query(ObjectType):
    resource = graphene.Field(ResourceType, id=graphene.Int())
    resources = graphene.List(ResourceType)

    def resolve_resource(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Resource.objects.get(pk=id)

        return None

    def resolve_resources(self, info, **kwargs):
        return Resource.objects.all()


class ResourceInput(graphene.InputObjectType):
    id = graphene.ID()
    resource_name = graphene.String()
    resource_file = Upload()
    course = graphene.Field(course_schema.CourseInput)


class CreateResource(graphene.Mutation):
    class Arguments:
        input = ResourceInput(required=True)

    ok = graphene.Boolean()
    resource = graphene.Field(ResourceType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        course = Course.objects.get(pk=input.course.id)
        resource_instance = Resource(
            resource_name=input.resource_name,
            resource_file=input.resource_file,
            course=course,
        )
        resource_instance.save()
        return CreateResource(ok=ok, resource=resource_instance)


class UpdateResource(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ResourceInput(required=True)

    ok = graphene.Boolean()
    resource = graphene.Field(ResourceType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        course = Course.objects.get(pk=input.course.id)
        resource_instance = Resource.objects.get(pk=id)
        if resource_instance:
            ok = True
            resource_instance.resource_name = input.resource_name
            resource_instance.resource_file = input.resource_file
            resource_instance.course = course
            resource_instance.save()
            return UpdateResource(ok=ok, resource=resource_instance)
        return UpdateResource(ok=ok, resource=None)


class Mutation(graphene.ObjectType):
    create_resource = CreateResource.Field()
    update_resource = UpdateResource.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

### assignments/admin.py
from django.contrib import admin
from assignments.models import Assignment, SubmitAssignment

# Register your models here.
admin.site.register(Assignment)
admin.site.register(SubmitAssignment)