# README
## README.md
# Django LMS

Django LMS is a Learning Management System using the framework, you guessed it right, Django. The system gives teachers and students a simple platform to upload resources and assignments.

# Motivation
The project started as a challenge to improve and test my knowledge of Django. The initial version of this project was created within 5 days.

# Tech/Framework Used
* Python
* Django
* HTML
* CSS
* Bootstrap

# Features
This platform is fairly simple yet provides most of the necessary features required in a Learning Management System. It uses Django's MTV architecture.
* Signup
* Login
* Logout
* Course Creation
* Course Deletion
* Assignment Creation
* Assignment Submission
* Assignment Deletion
* Delete Submission
* Grade Submission
* Resource Creation
* Resource Deletion
* User Profile

# Code snippets
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

### courses/urls.py
from django.conf.urls import url
from courses import views

app_name = "courses"

urlpatterns = [
    url(r'^new/$', views.CreateCourse.as_view(), name="create"),
    url(r'^detail/(?P<pk>[-\w]+)/$', views.CourseDetail.as_view(), name='detail'),
    url(r'^all/', views.ListCourse.as_view(), name="list"),
    url(r'^enroll/(?P<pk>[-\w]+)/$', views.EnrollCourse.as_view(), name='enroll'),
    url(r'^unenroll/(?P<pk>[-\w]+)/$', views.UnenrollCourse.as_view(), name='unenroll'),
]

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

### resources/urls.py
from django.conf.urls import url
from resources import views

app_name = "resources"

urlpatterns = [
    url(r'^create/$', views.CreateResource.as_view(), name="create"),
    url(r'^delete/(?P<pk>[-\w]+)/$', views.delete_view, name='delete')
]

### django_lms/urls.py
"""django_lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from assignments import views
from django_lms import views as project_views
from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    url(r'^$', project_views.index, name="home"),
    path('admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^assignments/', include('assignments.urls', namespace='assignments')),
    url(r'^resources/', include('resources.urls', namespace="resources")),
    url(r'^user_profile/(?P<pk>[-\w]+)/$',
        project_views.UserProfile.as_view(), name="profile"),
    url('graphql/', FileUploadGraphQLView.as_view(graphiql=True))
]

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

### assignments/urls.py
from django.conf.urls import url
from assignments import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'assignments'
urlpatterns = [
    url(r'^create/$', views.CreateAssignment.as_view(), name="create"),
    url(r'^detail/(?P<pk>[-\w]+)/$', views.AssignmentDetail.as_view(), name='detail'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.UpdateAssignment.as_view(), name='update'),
    url(r'^delete/(?P<pk>[-\w]+)/$', views.DeleteAssignment.as_view(), name="delete"),
    url(r'^submit/$', views.SubmitAssignmentView.as_view(), name="submit"),
    url(r'^submission/detail/(?P<pk>[-\w]+)/$', views.SubmitAssignmentDetail.as_view(), name="submit_detail"),
    url(r'^submission/delete/(?P<pk>[-\w]+)/$', views.delete_view, name="submit_delete"),
    url(r'^grade/(?P<pk>[-\w]+)/$', views.grade_assignment, name='grade')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

### django_lms/views.py
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from django.shortcuts import render

class UserProfile(LoginRequiredMixin, generic.ListView):
    model = Course
    template_name = 'user_profile.html'

def index(request):
    return render(request, 'index.html')

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

### users/models.py
from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher')
    )

    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=1)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

### users/schema.py
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return User.objects.get(pk=id)

        return None

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    user_type = graphene.Int()

class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)
    
    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_instance = User(
            username=input.username,
            first_name=input.first_name,
            last_name=input.last_name,
            email=input.email,
            password=input.password,
            user_type=input.user_type
        )
        user_instance.save()
        return CreateUser(ok=ok, user=user_instance)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        user_instance = User.objects.get(pk=id)
        if user_instance:
            ok = True
            user_instance.username = input.username
            user_instance.first_name = input.first_name
            user_instance.last_name = input.last_name
            user_instance.email = input.email
            user_instance.password = input.password
            user_instance.user_type = input.user_type
            user_instance.save()
            return UpdateUser(ok=ok, user=user_instance)
        return UpdateUser(ok=ok, actor=None)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

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

### courses/schema.py
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from courses.models import Course
from users.models import User
from users import schema as user_schema

class CourseType(DjangoObjectType):
    class Meta:
        model = Course

class Query(ObjectType):
    course = graphene.Field(CourseType, id=graphene.Int())
    courses = graphene.List(CourseType)
    
    def resolve_course(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Course.objects.get(pk=id)
        
        return None
    
    def resolve_courses(self, info, **kwargs):
        return Course.objects.all()

class CourseInput(graphene.InputObjectType):
    id = graphene.ID()
    course_name = graphene.String()
    course_description = graphene.String()
    teacher = graphene.Field(user_schema.UserInput)
    students = graphene.List(user_schema.UserInput)

class CreateCourse(graphene.Mutation):
    class Arguments:
        input = CourseInput(required = True)

    ok = graphene.Boolean()
    course = graphene.Field(CourseType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        students = []
        teacher = User.objects.get(pk=input.teacher.id)
        for student_input in input.students:
            student = User.objects.get(pk=student_input.id)
            if student is None:
                return CreateCourse(ok=False, course=None)
            students.append(student)
        course_instance = Course(
            course_name = input.course_name,
            course_description = input.course_description,
            teacher = teacher
        )
        course_instance.save()
        course_instance.students.set(students)
        return CreateCourse(ok=ok, course=course_instance)
    
class UpdateCourse(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CourseInput(required=True)

    ok = graphene.Boolean()
    course = graphene.Field(CourseType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        course_instance = Course.objects.get(pk=id)
        teacher = User.objects.get(pk=input.teacher.id)
        if course_instance:
            ok = True
            students = []
            for student_input in input.students:
                student = User.objects.get(pk=student_input.id)
                if student is None:
                    return UpdateCourse(ok=False, course=None)
                students.append(student)
            course_instance.course_name = input.course_name
            course
...[truncated]...

### resources/forms.py
from django.forms import ModelForm, DateInput, TimeInput, Form
from django import forms
from django.shortcuts import get_object_or_404
from resources.models import Resource
from django.utils import timezone
from courses.models import Course
from users.models import User


class CreateResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = ('resource_name', 'resource_file', 'course')


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user_object = User.objects.filter(username=user.username)
        new_user_object = get_object_or_404(user_object)
        self.fields['course'].queryset = self.fields['course'].queryset.filter(teacher=new_user_object.id)

### resources/models.py
from django.db import models
from users.models import User
from courses.models import Course
from django.urls import reverse
from django.utils import timezone
import os
from django.conf import settings

# Create your models here.
class Resource(models.Model):
    resource_name = models.CharField(max_length=200, blank=False)
    resource_file = models.FileField(blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.resource_name

    def get_absolute_url(self):
        return reverse('courses:list')

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

### assignments/forms.py
from django.forms import ModelForm, DateInput, TimeInput, Form, DateTimeInput
from django import forms
from django.shortcuts import get_object_or_404
from assignments.models import SubmitAssignment, Assignment
from django.utils import timezone
from courses.models import Course
from users.models import User

class GradeAssignmentForm(ModelForm):
    
    class Meta:
        model = SubmitAssignment
        fields = ['grade']

class CreateAssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ('assignment_name', 'assignment_description',
                  'due_date', 'course')
        labels = {
            'due_date': 'Due Date (yyyy-mm-dd HH:MM)'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user_object = User.objects.filter(username=user.username)
        new_user_object = get_object_or_404(user_object)
        self.fields['course'].queryset = self.fields['course'].queryset.filter(teacher=new_user_object.id)

class SubmitAssignmentForm(ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = ('topic', 'description', 'assignment_file', 'assignment_ques', 'author')
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        assignment = kwargs.pop('assignment_id')
        super().__init__(*args, **kwargs)
        self.fields['assignment_ques'].queryset = self.fields['assignment_ques'].queryset.filter(pk=assignment)
        self.fields['author'].queryset = self.fields['author'].queryset.filter(username=user.username)

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

### assignments/models.py
from django.db import models
from users.models import User
from courses.models import Course
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import os
from django.conf import settings

# Create your models here.
class Assignment(models.Model):
    assignment_name = models.CharField(max_length=200, blank=False)
    assignment_description = models.TextField(blank=False)
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment_name

    def get_absolute_url(self):
        return reverse('assignments:detail', kwargs={'pk': self.pk})

class SubmitAssignment(models.Model):
    author = models.ForeignKey(User, related_name='assignment', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    assignment_file = models.FileField(blank=False, upload_to='assignments')
    submitted_date = models.DateTimeField(default=timezone.now)
    assignment_ques = models.ForeignKey(Assignment, related_name="question", on_delete=models.CASCADE, null=True)
    graded = models.BooleanField(default=False)
    grade = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.topic

    def grade_assignment(self, grade):
        self.grade = grade
        self.graded = True
        self.save()

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.assignment_file.name))
        super().delete(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('assignments:submit_detail', kwargs={'pk': self.pk})

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