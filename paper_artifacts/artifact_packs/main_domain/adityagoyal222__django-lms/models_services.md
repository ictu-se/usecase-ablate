# Models/services
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