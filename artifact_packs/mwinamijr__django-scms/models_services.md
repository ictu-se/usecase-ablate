# Models/services
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

### users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

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

### administration/models.py
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import date, datetime
from user_agents import parse

from .common_objs import *
from users.models import CustomUser


class Article(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="articles", blank=True, null=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CarouselImage(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="carousel")

    def __str__(self):
        return self.title


class AccessLog(models.Model):
    login = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    ua = models.CharField(
        max_length=2000,
        help_text="User agent. We can use this to determine operating system and browser in use.",
    )
    date = models.DateTimeField(
        auto_now_add=True
    )  # Set this to add the timestamp on creation only
    ip = models.GenericIPAddressField()
    usage = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.login} - {self.usage} on {self.date}"

    def os(self):
        """
        Extract the operating system from the user agent string.
        Returns 'Unknown' if it cannot be detected.
        """
        try:
            user_agent = parse(self.ua)
            return user_agent.os.family
        except Exception as e:
            print(f"Error extracting OS from UA: {e}")
            return "Unknown"

    def browser(self):
        """
        Extract the browser from the user agent string.
        Returns 'Unknown' if it cannot be detected.
        """
        try:
            user_agent = parse(self.ua)
            return user_agent.browser.family
        except Exception as e:
            print(f"Error extracting Browser from UA: {e}")
            return "Unknown"

    class Meta:
        indexes = [
            models.Index(fields=["login"]),  # Add index for faster querying by login
            models.Index(fields=["date"]),  # Add index for faster querying by date
        ]


class School(models.Model):
    active = models.BooleanField(
        default=False,
        help_text="DANGER..!!!! If marked, 
...[truncated]...

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

### sis/models.py
from django.db import models


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="api/sis/students/bulkupload")

### notes/models.py
from django.db import models

from academic.models import Student, SubTopic
from users.models import CustomUser as User


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class GradedAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.SET_NULL, blank=True, null=True
    )
    grade = models.FloatField()

    def __str__(self):
        return self.student.username


class Choice(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name="answer", blank=True, null=True
    )
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name="questions",
        blank=True,
        null=True,
    )
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question


class SpecificExplanations(models.Model):
    sub_topic = models.ForeignKey(
        SubTopic, on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    examples = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return f"{self.name} {self.sub_topic}"


class Concept(models.Model):
    sub_topic = models.ForeignKey(
        SubTopic, on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    image = models.ImageField(
        verbose_name=None, upload_to="concept images", blank=True, null=True
    )
    list_of_explanations = models.ManyToManyField(SpecificExplanations, blank=True)

    def __str__(self):
        return f"{self.name} {self.sub_topic}"


class Note(models.Model):
    sub_topic = models.ForeignKey(
        SubTopic, on_delete=models.CASCADE, blank=True, null=True
    )
    notes = models.ManyToManyField(Concept, blank=True)

    def __str__(self):
        return f"{self.sub_topic}"

### finance/models.py
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal
from administration.models import Term
from users.models import Accountant, CustomUser as User
from academic.models import Teacher, Student


class PaymentStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    COMPLETED = "Completed", "Completed"
    CANCELLED = "Cancelled", "Cancelled"


class PaymentThrough(models.TextChoices):
    CRDB = "CRDB", "CRDB"
    NMB = "NMB", "NMB"
    NBC = "NBC", "NBC"
    HATI_MALIPO = "HATI MALIPO", "HATI MALIPO"
    CASH = "CASH", "CASH"
    UNKNOWN = "Unknown", "Unknown"


class DebtRecord(models.Model):
    student = models.ForeignKey(
        Student, related_name="debt_records", on_delete=models.CASCADE
    )
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    amount_added = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )
    amount_paid = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )
    note = models.TextField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_reversed = models.BooleanField(default=False)
    reversed_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("student", "term")
        ordering = ["-date_updated"]

    def __str__(self):
        return f"{self.student.full_name} - {self.term.name} - {self.amount_added}"

    @property
    def balance(self):
        return max(Decimal("0.00"), self.amount_added - self.amount_paid)

    def apply_payment(self, amount):
        """
        Applies a payment to this debt record and prevents overpayment.
        """
        amount = Decimal(amount)
        if amount <= 0:
            raise ValueError("Payment must be positive.")
        if self.balance < amount:
            raise ValueError("Cannot pay more than the remaining balance.")
        self.amount_paid += amount
        self.save()

    def reverse(self):
        self.is_reversed = True
        self.reversed_on = timezone.now()
        self.save()


class ReceiptAllocation(models.Model):
    name = models.CharField(max_length=255, null=True)
    abbr = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class PaymentAllocation(models.Model):
    name = models.CharField(max_length=255, null=True)
    abbr = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.n
...[truncated]...

### academic/models.py
from django.db import models, transaction
from django.db.models import F
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from django.utils import timezone
from users.models import CustomUser
from administration.models import AcademicYear, Term

from .validators import *
from administration.common_objs import *


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order_rank = models.IntegerField(
        blank=True, null=True, help_text="Rank for subject reports"
    )

    class Meta:
        ordering = ("order_rank", "name")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()

        super().save(*args, **kwargs)


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subject_code = models.CharField(max_length=10, blank=True, null=True, unique=True)
    is_selectable = models.BooleanField(
        default=False, help_text="Select if subject is optional"
    )
    graded = models.BooleanField(default=True, help_text="Teachers can submit grades")
    description = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["subject_code"]
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def save(self, *args, **kwargs):
        # Generate description
        self.name = self.name.lower()
        self.description = f"{self.name.lower()} - {self.subject_code}"

        super().save(*args, **kwargs)


class Teacher(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="teacher",
        null=True,
        blank=True,
    )
    username = models.CharField(unique=True, max_length=250, blank=True)
    first_name = models.CharField(max_length=300, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=300, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, blank=True)
    email = models.EmailField(blank=True, null=True)
    empId = models.CharField(max_length=8, unique=True, null=True, blank=True)
    tin_number =
...[truncated]...

### schedule/models.py
from django.db import models

from academic.models import ClassRoom, Teacher, AllocatedSubject


class Period(models.Model):
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
        ],
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    subject = models.ForeignKey(AllocatedSubject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("day_of_week", "start_time", "classroom")

    def __str__(self):
        return f"{self.classroom} - {self.subject} ({self.day_of_week} {self.start_time}-{self.end_time})"

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

### examination/models.py
import datetime
from django.db import models
from django.core.exceptions import ValidationError
from academic.models import Student, Teacher, ClassRoom, StudentClassEnrollment, Subject
from administration.models import AcademicYear, Term


class GradeScale(models.Model):
    """Translate a numeric grade to some other scale.
    Example: Letter grade or 4.0 scale."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_rule(self, grade):
        if grade is None:
            return None
        rule = self.gradescalerule_set.filter(
            min_grade__lte=grade, max_grade__gte=grade
        ).first()
        if not rule:
            # Optionally log or raise a warning
            print(f"No rule found for grade: {grade}")
        return rule

    def to_letter(self, grade):
        rule = self.get_rule(grade)
        if rule:
            return rule.letter_grade
        return None  # Return None if no rule found

    def to_numeric(self, grade):
        rule = self.get_rule(grade)
        if rule:
            return rule.numeric_scale
        return None  # Return None if no rule found


class GradeScaleRule(models.Model):
    """One rule for a grade scale."""

    min_grade = models.DecimalField(max_digits=5, decimal_places=2)
    max_grade = models.DecimalField(max_digits=5, decimal_places=2)
    letter_grade = models.CharField(max_length=50, blank=True, null=True)
   
...[truncated]...