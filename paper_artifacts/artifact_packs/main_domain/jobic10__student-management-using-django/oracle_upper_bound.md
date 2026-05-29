# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

# README
## README.md
# Student Management System Created Using Django
This is a Simple Student Management System Developed While Learning Django.
Feel free to make changes based on your requirements.

[Front-end Template](http://adminlte.io "Admin LTE.io")


[Project Demo on YouTube](https://www.youtube.com/watch?v=kArCR96m7uo "Django Student Management System Demo")

And if you like this project, then ADD a STAR ⭐️  to this project 👆
## Deployed to
https://smswithdjango.herokuapp.com/


## Features of this Project

### A. Admin Users Can
1. See Overall Summary Charts of Students Performances, Staff Performances, Courses, Subjects, Leave, etc.
2. Manage Staff (Add, Update and Delete)
3. Manage Students (Add, Update and Delete)
4. Manage Course (Add, Update and Delete)
5. Manage Subjects (Add, Update and Delete)
6. Manage Sessions (Add, Update and Delete)
7. View Student Attendance
8. Review and Reply Student/Staff Feedback
9. Review (Approve/Reject) Student/Staff Leave

### B. Staff/Teachers Can
1. See the Overall Summary Charts related to their students, their subjects, leave status, etc.
2. Take/Update Students Attendance
3. Add/Update Result
4. Apply for Leave
5. Send Feedback to HOD

### C. Students Can
1. See the Overall Summary Charts related to their attendance, their subjects, leave status, etc.
2. View Attendance
3. View Result
4. Apply for Leave
5. Send Feedback to HOD


## 📸 ScreenShots

<img src="ss/1.png"/>
<img src="ss/2.png"/>
<img src="ss/3.png"/>
<img src="ss/4.png"/>
<img src="ss/5.png"/>

| Admin| Staff| Student |
|------|-------|---------|
|<img src="ss/admin5.png" width="400">|<img src="ss/staff1.png" width="400">|<img src="ss/student1.png" width="400">|
|<img src="ss/admin2.png" width="400">|<img src="ss/staff2.png" width="400">|<img src="ss/student2.png" width="400">|
|<img src="ss/admin3.png" width="400">|<img src="ss/staff3.png" width="400">|<img src="ss/student3.png" width="400">|
|<img src="ss/admin4.png" width="400">|<img src="ss/staff4.png" width="400">|<img src="ss/student4.png" width="400">|
|<img src="ss/admin1.png" width="400">|<img src="ss/staff5.png" width="400">|<img src="ss/student5.png" width="400">|
|<img src="ss/admin6.png" width="400">|<img src="ss/staff6.png" width="400">|<img src="ss/student6.png" width="400">|



## Support Developer
1. Add a Star 🌟  to this 👆 Repository
2. Follow on Twitter/Github


## Passport/Images
Images are from [Unsplash](https://unsplash.com)


## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/jobic10/student-management-using-django.git
```

Then, Enter the project
```
$  cd student-management-using-django
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Use **[]** as your host. 
```python
ALLOWED_HOSTS = []
```
*Do not use the fault allowed settings in this repo. It has security risk!*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```



Then Add Email and Password

**or Use Default Credentials**

*For HOD /SuperAdmin*
Email: admin@admin.com
Password: admin

*For Staff*
Email: staff@staff.com
Password: staff

*For Student*
Email: student@student.com
Password: student



## For Sponsor or Projects Enquiry
1. Email - jobowonubi@gmail.com
2. LinkedIn - [jobic10](https://www.linkedin.com/in/jobic10 "Owonubi Job Sunday on LinkedIn")
2. Twitter - [jobic10](https://www.twitter.com/jobic10 "Owonubi Job Sunday on Twitter")



## Project's Journey
- [x] Admin/Staff/Student Login
- [x] Add and Edit Course
- [x] Add and Edit Staff
- [x] Add and Edit Student
- [x] Add and Edit Subject
- [x] Upload Staff's Picture
- [x] Upload Student's Picture
- [x] Sidebar Active Status
- [x] Named URLs
- [x] Model Forms for adding  student
- [x] Model Forms for all
- [x] Views Permission (MiddleWareMixin)
- [x] Attendance and Update Attendance
- [x] Password Reset Via Email
- [x] Apply For Leave
- [x] Students Can Check Attendance
- [x] Check Email Availability
- [x] Reply to Leave Applications
- [x] Reply to Feedback
- [x] Admin View Attendance
- [x] Password Change for Admin, Staff and Students using *set_password()*
- [x] Admin Profile Edit
- [x] Staff Profile Edit
- [x] Student Profile Edit
- [x] Student Dashboard Fixed
- [x] Passing Page Title From View  - Improved
- [x] Staff Dashboard Fixed
- [x] Admin Dashboard Fixed
- [x] Firebase Web Push Notifications
- [x] Staff Add Student's Result
- [x] Staff Edit Result Using CBVs (Class Based Views)
- [x] Google CAPTCHA
- [x] Student View Result
- [x] Change all links to be dynamic
- [x] Code Restructure - Very Important


## Questions I asked While Developing This
- https://stackoverflow.com/questions/63829896/is-there-a-specific-way-of-adding-apps-in-django/


## Helpful Links
- https://stackoverflow.com/questions/55969952/how-can-i-avoid-a-user-from-registering-an-already-used-email-in-django
- https://stackoverflow.com/questions/7562573/how-do-i-get-django-forms-to-show-the-html-required-attribute
- https://stackoverflow.com/questions/40910149/django-exists-versus-doesnotexist
- https://www.edureka.co/community/80982/how-can-i-have-multiple-models-in-a-single-django-modelform
- https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for
- https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
- https://stackoverflow.com/questions/32576348/how-can-i-create-django-modelform-for-an-abstract-model
- https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
- https://stackoverflow.com/questions/64145745/create-user-missing-1-required-positional-argument-username?noredirect=1#64145844
- https://stackoverflow.com/questions/36059194/what-is-the-difference-between-json-dump-and-json-dumps-in-python
- https://stackoverflow.com/questions/64188313/django-can-i-delete-apps-static-files-after-running-collectstatic/64189244#64189244
- https://stackoverflow.com/questions/29416478/change-form-field-value-before-saving
- https://support.google.com/mail/thread/38519529?hl=en
- https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript
- https://stackoverflow.com/questions/3429084/why-do-i-get-an-object-is-not-iterable-error

# File tree
README.md
main_app
  EditResultView.py
  EmailBackend.py
  __init__.py
  admin.py
  apps.py
  forms.py
  hod_views.py
  middleware.py
  models.py
  staff_views.py
  student_views.py
  tests.py
  urls.py
  views.py
manage.py
requirements.txt
student_management_system
  __init__.py
  asgi.py
  settings.py
  urls.py
  wsgi.py

# Oracle-selected code and test snippets
### main_app/urls.py
"""student_management_system URL Configuration

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
from django.urls import path

from main_app.EditResultView import EditResultView

from . import hod_views, staff_views, student_views, views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("get_attendance", views.get_attendance, name='get_attendance'),
    path("firebase-messaging-sw.js", views.showFirebaseJS, name='showFirebaseJS'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("admin/home/", hod_views.admin_home, name='admin_home'),
    path("staff/add", hod_views.add_staff, name='add_staff'),
    path("course/add", hod_views.add_course, name='add_course'),
    path("send_student_notification/", hod_views.send_student_notification,
         name='send_student_notification'),
    path("send_staff_notification/", hod_views.send_staff_notification,
         name='send_staff_notification'),
    path("add_session/", hod_views.add_session, name='add_session'),
    path("admin_notify_student", hod_views.admin_notify_student,
         name='admin_notify_student'),
    path("admin_notify_staff", hod_views.admin_notify_staff,
         name='admin_notify_staff'),
    path("admin_view_profile", hod_views.admin_view_profile,
         name='admin_view_profile'),
    path("check_email_availability", hod_views.check_email_availability,
         name="check_email_availability"),
    path("session/manage/", hod_views.manage_session, name='manage_session'),
    path("session/edit/<int:session_id>",
         hod_views.edit_session, name='edit_session'),
    path("student/view/feedback/", hod_views.student_feedback_message,
         name="student_feedback_message",),
    path("staff/view/feedback/", hod_views.staff_feedback_message,
         name="staff_feedback_message",),
    path("student/view/leave/", hod_views.view_student_leave,
         name="view_student_leave",),
    path("staff/view/leave/", hod_views.view_staff_lea
...[truncated]...

### main_app/hod_views.py
import json
import requests
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from .forms import *
from .models import *


def admin_home(request):
    total_staff = Staff.objects.all().count()
    total_students = Student.objects.all().count()
    subjects = Subject.objects.all()
    total_subject = subjects.count()
    total_course = Course.objects.all().count()
    attendance_list = Attendance.objects.filter(subject__in=subjects)
    total_attendance = attendance_list.count()
    attendance_list = []
    subject_list = []
    for subject in subjects:
        attendance_count = Attendance.objects.filter(subject=subject).count()
        subject_list.append(subject.name[:7])
        attendance_list.append(attendance_count)
    context = {
        'page_title': "Administrative Dashboard",
        'total_students': total_students,
        'total_staff': total_staff,
        'total_course': total_course,
        'total_subject': total_subject,
        'subject_list': subject_list,
        'attendance_list': attendance_list

    }
    return render(request, 'hod_template/home_content.html', context)


def add_staff(request):
    form = StaffForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Staff'}
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            password = form.cleaned_data.get('password')
            course = form.cleaned_data.get('course')
            passport = request.FILES.get('profile_pic')
            fs = FileSystemStorage()
            filename = fs.save(passport.name, passport)
            passport_url = fs.url(filename)
            try:
                user = CustomUser.objects.create_user(
                    email=email, password=password, user_type=2, first_name=first_name, last_name=last_name, profile_pic=passport_url)
                user.gender = gender
                user.address = address
           
...[truncated]...

### main_app/forms.py
from django import forms
from django.forms.widgets import DateInput, TextInput

from .models import *


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomUserForm(FormSettings):
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    widget = {
        'password': forms.PasswordInput(),
    }
    profile_pic = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        if kwargs.get('instance'):
            instance = kwargs.get('instance').admin.__dict__
            self.fields['password'].required = False
            for field in CustomUserForm.Meta.fields:
                self.fields[field].initial = instance.get(field)
            if self.instance.pk is not None:
                self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"

    def clean_email(self, *args, **kwargs):
        formEmail = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if CustomUser.objects.filter(email=formEmail).exists():
                raise forms.ValidationError(
                    "The given email is already registered")
        else:  # Update
            dbEmail = self.Meta.model.objects.get(
                id=self.instance.pk).admin.email.lower()
            if dbEmail != formEmail:  # There has been changes
                if CustomUser.objects.filter(email=formEmail).exists():
                    raise forms.ValidationError("The given email is already registered")

        return formEmail

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender',  'password','profile_pic', 'address' ]


class StudentForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields + \
            ['course', 'session']


class AdminForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
    
...[truncated]...

### main_app/models.py
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class Session(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return "From " + str(self.start_year) + " to " + str(self.end_year)


class CustomUser(AbstractUser):
    USER_TYPE = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    GENDER = [("M", "Male"), ("F", "Female")]
    
    
    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)
    profile_pic = models.ImageField()
    address = models.TextField()
    fcm_token = models.TextField(default="")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.last_name + ", " + self.first_name


class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)



class Course(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    course =
...[truncated]...

### main_app/staff_views.py
import json

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,redirect, render)
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


def staff_home(request):
    staff = get_object_or_404(Staff, admin=request.user)
    total_students = Student.objects.filter(course=staff.course).count()
    total_leave = LeaveReportStaff.objects.filter(staff=staff).count()
    subjects = Subject.objects.filter(staff=staff)
    total_subject = subjects.count()
    attendance_list = Attendance.objects.filter(subject__in=subjects)
    total_attendance = attendance_list.count()
    attendance_list = []
    subject_list = []
    for subject in subjects:
        attendance_count = Attendance.objects.filter(subject=subject).count()
        subject_list.append(subject.name)
        attendance_list.append(attendance_count)
    context = {
        'page_title': 'Staff Panel - ' + str(staff.admin.last_name) + ' (' + str(staff.course) + ')',
        'total_students': total_students,
        'total_attendance': total_attendance,
        'total_leave': total_leave,
        'total_subject': total_subject,
        'subject_list': subject_list,
        'attendance_list': attendance_list
    }
    return render(request, 'staff_template/home_content.html', context)


def staff_take_attendance(request):
    staff = get_object_or_404(Staff, admin=request.user)
    subjects = Subject.objects.filter(staff_id=staff)
    sessions = Session.objects.all()
    context = {
        'subjects': subjects,
        'sessions': sessions,
        'page_title': 'Take Attendance'
    }

    return render(request, 'staff_template/staff_take_attendance.html', context)


@csrf_exempt
def get_students(request):
    subject_id = request.POST.get('subject')
    session_id = request.POST.get('session')
    try:
        subject = get_object_or_404(Subject, id=subject_id)
        session = get_object_or_404(Session, id=session_id)
        students = Student.objects.filter(
            course_id=subject.course.id, session=session)
        student_data = []
        for student in students:
            data = {
                    "id": student.id,
                    "name": student.admin.last_name + " " + student.admin.first_name
                    }
            student_data.append(data)
        return JsonResponse(json.dumps(student_data), content_type='application/json', safe=F
...[truncated]...

### main_app/templates/staff_template/staff_take_attendance.html
{% extends 'main_app/base.html' %}
{% load static %}
{% block page_title %}{{page_title}}{% endblock page_title %}
{% block content %}

<section class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <!-- general form elements -->
                <div class="card card-primary">
                    <div class="card-header">
                        <h3 class="card-title">{{page_title}}</h3>
                    </div>

                    <!-- /.card-header -->
                    <!-- form start -->
                    <div class="card-body">



                        <div class="form-group">
                            <label>Subject</label>
                            <select name="subject" class="form-control" id='subject'>
                                <option value="">----</option>
                                {% for subject in subjects  %}
                                <option value="{{subject.id}}">{{subject.name}}</option>
                                {% endfor %}
                            </select>
                        </div>


                        <div class="form-group">
                            <label>Session Year</label>
                            <select name="session" id='session' class="form-control">
                                <option value="">----</option>
                                {% for session in sessions  %}
                                <option value="{{session.id}}">{{session}} </option>
                                {% endfor %}
                            </select>
                        </div>
                        {% comment %}

                        <div>
                            <label>Attendance Date</label>
                            <input type="date" class='form-control' name="attendance_date" id='attendance_date' id="">
                        </div>
                        {% endcomment %}

                    </div>
                    <!-- /.card-body -->

                    <div class="card-footer">
                        <button type="button" id='fetch_student' class="btn btn-primary btn-block">Fetch
                            Students</button>
                        <div class="form-group" id="student_data">

                        </div>
                    </div>
                </div>
                <!-- /.card -->

            </div>
        </div>
    </div>
</section>
{% endblock content %}


{% block custom_js %}
<script>
    $(document).ready(function () {

       
        $("#fetch_
...[truncated]...

### main_app/templates/staff_template/staff_update_attendance.html
{% extends 'main_app/base.html' %}
{% load static %}
{% block page_title %}{{page_title}}{% endblock page_title %}
{% block content %}

<section class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <!-- general form elements -->
                <div class="card card-primary">
                    <div class="card-header">
                        <h3 class="card-title">{{page_title}}</h3>
                    </div>

                    <!-- /.card-header -->
                    <!-- form start -->
                    <div class="card-body">



                        <div class="form-group">
                            <label>Subject</label>
                            <select name="subject" class="form-control" id='subject'>
                                <option value="">----</option>
                                {% for subject in subjects  %}
                                <option value="{{subject.id}}">{{subject.name}}</option>
                                {% endfor %}
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Session</label>
                            <select name="session" class="form-control" id='session'>
                                <option value="">----</option>
                                {% for session in sessions  %}
                                <option value="{{session.id}}">{{session}}</option>
                                {% endfor %}
                            </select>
                        </div>
                        <div class="form-group"><div  style="display: none;" class="alert alert-danger" id='error_attendance'></div>
                                <div class="alert alert-success" id='success_attendance' style="display: none;"></div>
                             <button type="button" id='fetch_attendance' class="btn btn-primary btn-block">Fetch
                                    Attendance</button>
                        </div>
                    <!-- /.card-body -->
                    
                        
                               
                            <div class="form-group" style="display: none;" id="attendance_block">
                            <div class="form-group">
                                <label>Attendance Date</label>
                                <select name="attendance_date" id='attendance_date' class="form-control">
                               
                            
...[truncated]...

### main_app/EditResultView.py
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import messages
from .models import Subject, Staff, Student, StudentResult
from .forms import EditResultForm
from django.urls import reverse


class EditResultView(View):
    def get(self, request, *args, **kwargs):
        resultForm = EditResultForm()
        staff = get_object_or_404(Staff, admin=request.user)
        resultForm.fields['subject'].queryset = Subject.objects.filter(staff=staff)
        context = {
            'form': resultForm,
            'page_title': "Edit Student's Result"
        }
        return render(request, "staff_template/edit_student_result.html", context)

    def post(self, request, *args, **kwargs):
        form = EditResultForm(request.POST)
        context = {'form': form, 'page_title': "Edit Student's Result"}
        if form.is_valid():
            try:
                student = form.cleaned_data.get('student')
                subject = form.cleaned_data.get('subject')
                test = form.cleaned_data.get('test')
                exam = form.cleaned_data.get('exam')
                # Validating
                result = StudentResult.objects.get(student=student, subject=subject)
                result.exam = exam
                result.test = test
                result.save()
                messages.success(request, "Result Updated")
                return redirect(reverse('edit_student_result'))
            except Exception as e:
                messages.warning(request, "Result Could Not Be Updated")
        else:
            messages.warning(request, "Result Could Not Be Updated")
        return render(request, "staff_template/edit_student_result.html", context)

### main_app/student_views.py
import json
import math
from datetime import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


def student_home(request):
    student = get_object_or_404(Student, admin=request.user)
    total_subject = Subject.objects.filter(course=student.course).count()
    total_attendance = AttendanceReport.objects.filter(student=student).count()
    total_present = AttendanceReport.objects.filter(student=student, status=True).count()
    if total_attendance == 0:  # Don't divide. DivisionByZero
        percent_absent = percent_present = 0
    else:
        percent_present = math.floor((total_present/total_attendance) * 100)
        percent_absent = math.ceil(100 - percent_present)
    subject_name = []
    data_present = []
    data_absent = []
    subjects = Subject.objects.filter(course=student.course)
    for subject in subjects:
        attendance = Attendance.objects.filter(subject=subject)
        present_count = AttendanceReport.objects.filter(
            attendance__in=attendance, status=True, student=student).count()
        absent_count = AttendanceReport.objects.filter(
            attendance__in=attendance, status=False, student=student).count()
        subject_name.append(subject.name)
        data_present.append(present_count)
        data_absent.append(absent_count)
    context = {
        'total_attendance': total_attendance,
        'percent_present': percent_present,
        'percent_absent': percent_absent,
        'total_subject': total_subject,
        'subjects': subjects,
        'data_present': data_present,
        'data_absent': data_absent,
        'data_name': subject_name,
        'page_title': 'Student Homepage'

    }
    return render(request, 'student_template/home_content.html', context)


@ csrf_exempt
def student_view_attendance(request):
    student = get_object_or_404(Student, admin=request.user)
    if request.method != 'POST':
        course = get_object_or_404(Course, id=student.course.id)
        context = {
            'subjects': Subject.objects.filter(course=course),
            'page_title': 'View Attendance'
        }
        return render(request, 'student_template/student_view_attendance.html', context)
    else:
        subject_id = request.POST.get('subject')
        
...[truncated]...

### main_app/templates/student_template/student_view_attendance.html
{% extends 'main_app/base.html' %}
{% load static %}
{% block page_title %}{{page_title}}{% endblock page_title %}
{% block custom_css %}
<style>
.attendance_div_red{
    padding: 10px;
    background: #f44336;
    border: 3px solid white;
    text-align: center;
    color: #fff;
    border-radius: 30px;
    box-shadow: 1px 1px 1px grey;
    margin: 5px;
}
.attendance_div_green{
    padding: 10px;
    background: #4CAF50;
    border: 3px solid white;
    text-align: center;
    color: #fff;
    border-radius: 30px;
    box-shadow: 1px 1px 1px grey;
    margin: 5px;
}
</style>
{% endblock custom_css %}

{% block content %}

<section class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <!-- general form elements -->
                <div class="card card-primary">
                    <div class="card-header">
                        <h3 class="card-title">{{page_title}}</h3>
                    </div>
                    <!-- /.card-header -->
                    <!-- form start -->
                    <div class="card-body">



                        <div class="form-group">
                            <label>Select Subject</label>
                            <select  id="subject" class="form-control">
                                <option value="">----</option>
                                {% for subject in subjects  %}
                                <option value="{{subject.id}}">{{subject.name}} </option>
                                {% endfor %}
                            </select>
                        </div>
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label>Start Date</label>
                                    <input type="date" class="form-control" placeholder="Start Date" name="start_date" required id="start_date">
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label>End Date</label>
                                    <input type="date" class="form-control" placeholder="End Date" name="end_date"  id="end_date">
                                </div>
                            </div>
                            <button type="button" id="fetch_attendance" class="btn btn-primary btn-block">Fetch
                                Attendance Data</button>

...[truncated]...

### main_app/templates/student_template/student_view_result.html
{% extends 'main_app/base.html' %}
{% load static %}
{% block page_title %}{{page_title}}{% endblock page_title %}

{% block content %}

<section class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <!-- general form elements -->
       
                <!-- /.card -->
<div class="card card-primary">
    <div class="card-header"><h3 class="card-title">{{page_title}}</h3>
    </div>
   <div class="table p-2">

       <table class="table table-bordered">
           <tr>
               <th>ID</th>
               <th>Subject</th>
               <th>Test</th>
               <th>Exam</th>
               <th>Total</th>
        </tr>
        {% for result in results %}
        <tr>
            <td>{{forloop.counter}}</td>
            <td>{{ result.subject }}</td>
            <td>{{ result.test }}</td>
            <td>{{ result.exam }}</td>
            <td>{{ result.test|add:result.exam }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
    </div>
            </div>
        </div>
    </div>
</section>
{% endblock content %}

### main_app/views.py
import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from .EmailBackend import EmailBackend
from .models import Attendance, Session, Subject

# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("admin_home"))
        elif request.user.user_type == '2':
            return redirect(reverse("staff_home"))
        else:
            return redirect(reverse("student_home"))
    return render(request, 'main_app/login.html')


def doLogin(request, **kwargs):
    if request.method != 'POST':
        return HttpResponse("<h4>Denied</h4>")
    else:
        #Google recaptcha
        captcha_token = request.POST.get('g-recaptcha-response')
        captcha_url = "https://www.google.com/recaptcha/api/siteverify"
        captcha_key = "6LfswtgZAAAAABX9gbLqe-d97qE2g1JP8oUYritJ"
        data = {
            'secret': captcha_key,
            'response': captcha_token
        }
        # Make request
        try:
            captcha_server = requests.post(url=captcha_url, data=data)
            response = json.loads(captcha_server.text)
            if response['success'] == False:
                messages.error(request, 'Invalid Captcha. Try Again')
                return redirect('/')
        except:
            messages.error(request, 'Captcha could not be verified. Try Again')
            return redirect('/')
        
        #Authenticate
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("admin_home"))
            elif user.user_type == '2':
                return redirect(reverse("staff_home"))
            else:
                return redirect(reverse("student_home"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")



def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/")


@csrf_exempt
def get_attendance(request):
    subject_id = request.POST.get('subject')
    session_id = request.POST.get('session')
    try:
        subject = get_object_or_404(Subject, id=subject_id)
        session = get_object
...[truncated]...

### student_management_system/urls.py
"""student_management_system URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("", include('main_app.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)