# Routes/controllers
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

### api/admin.py
from django.contrib import admin

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

### users/views.py
import openpyxl
from django.db.models import Q
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import FilterSet, CharFilter, DjangoFilterBackend
from rest_framework import viewsets, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from academic.models import Teacher, Subject, Parent
from .models import CustomUser as User, Accountant
from .serializers import (
    UserSerializer,
    UserSerializerWithToken,
    AccountantSerializer,
    TeacherSerializer,
    ParentSerializer,
)


# Custom Token View
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_data = UserSerializerWithToken(self.user).data
        data.update(user_data)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


class UserFilter(FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    middle_name = CharFilter(field_name="middle_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")

    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
        ]


class TeacherFilter(FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    middle_name = CharFilter(field_name="middle_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")

    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "middle_name",
            "last_name",
        ]


class ParentFilter(FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    middle_name = CharFilter(field_name="middle_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="la
...[truncated]...

### administration/views.py
import openpyxl
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from rest_framework import generics, viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AcademicYear, Term, Article, CarouselImage, SchoolEvent
from .serializers import (
    AcademicYearSerializer,
    TermSerializer,
    ArticleSerializer,
    CarouselImageSerializer,
    SchoolEventSerializer,
)
from .permissions import IsAdminOrReadOnly


# Article Views
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


# CarouselImage Views
class CarouselImageListCreateView(generics.ListCreateAPIView):
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselImageSerializer
    permission_classes = [IsAuthenticated]


class CarouselImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselImageSerializer
    permission_classes = [IsAuthenticated]


# AcademicYear Views
class AcademicYearListCreateView(generics.ListCreateAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class AcademicYearDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated]


# Term Views
class TermListCreateView(generics.ListCreateAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class TermDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated]


class SchoolEventViewSet(viewsets.ModelViewSet):
    queryset = SchoolEvent.objects.select_related("term", "term__academic_year").all()
    serializer_class = Sch
...[truncated]...

### api/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import (
    MyTokenObtainPairView,
    getUserProfile,
    UserListView,
    UserDetailView,
    ParentListView,
    ParentDetailView,
    AccountantListView,
    AccountantDetailView,
    TeacherListView,
    TeacherDetailView,
    BulkUploadTeachersView,
)


urlpatterns = [
    # JWT Token endpoint
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profile/", getUserProfile, name="users-profile"),
    path("users/", UserListView.as_view(), name="users-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    # teacher URLs
    path("teachers/", TeacherListView.as_view(), name="teacher-list-create"),
    path(
        "teachers/bulk-upload/",
        BulkUploadTeachersView.as_view(),
        name="teacher-bulk-upload",
    ),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="accountant-detail"),
    # Accountant URLs
    path("accountants/", AccountantListView.as_view(), name="accountant-list-create"),
    path(
        "accountants/<int:pk>/",
        AccountantDetailView.as_view(),
        name="accountant-detail",
    ),
    # Parent URLs
    path("parents/", ParentListView.as_view(), name="parent-list-create"),
    path("parents/<int:pk>/", ParentDetailView.as_view(), name="parent-detail"),
]

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

### api/apps.py
from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

### api/views.py
from rest_framework import viewsets, status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.http import Http404

from administration.models import Article, CarouselImage
from .serializers import (
	ArticleSerializer, CarouselImageSerializer)

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class CarouselImageViewSet(viewsets.ModelViewSet):
	queryset = CarouselImage.objects.all()
	serializer_class = CarouselImageSerializer


class ArticleListView(views.APIView):
	"""
    List all articles, or create a new article.
    """
	def get(self, request, format=None):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(views.APIView):
	def get_object(self, pk):
		try:
			return Article.objects.get(pk=pk)
		except Article.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
		article = self.get_object(pk)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		article = self.get_object(pk)
		serializer = ArticleSerializer(article, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		article = self.get_object(pk)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

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

### notes/views.py
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import *
from .serializers import *


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def create(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class GradedAssignmentListView(ListAPIView):
    serializer_class = GradedAssignmentSerializer

    def get_queryset(self):
        queryset = GradedAssignment.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(student__username=username)
        return queryset


class GradedAssignmentCreateView(CreateAPIView):
    serializer_class = GradedAssignmentSerializer
    queryset = GradedAssignment.objects.all()

    def post(self, request):
        print(request.data)
        serializer = GradedAssignmentSerializer(data=request.data)
        serializer.is_valid()
        graded_assignment = serializer.create(request)
        if graded_assignment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)

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

### academic/views.py
import openpyxl
from django.db.models import F
from django.core.exceptions import ValidationError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from administration.models import AcademicYear
from .models import (
    Subject,
    Department,
    ClassRoom,
    ClassLevel,
    Stream,
    Teacher,
    GradeLevel,
    ClassYear,
    ReasonLeft,
    StudentClassEnrollment as StudentClass,
    Student,
)
from .serializers import (
    DepartmentSerializer,
    ClassLevelSerializer,
    GradeLevelSerializer,
    ClassYearSerializer,
    ReasonLeftSerializer,
    StreamSerializer,
    SubjectSerializer,
    ClassRoomSerializer,
    StudentClassEnrollmentSerializer,
)


# Department Views
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


# ClassLevel Views
class ClassLevelListCreateView(generics.ListCreateAPIView):
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class ClassLevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializer
    permission_classes = [IsAuthenticated]


# GradeLevel Views
class GradeLevelListCreateView(generics.ListCreateAPIView):
    queryset = GradeLevel.objects.all()
    serializer_class = GradeLevelSerializer
    permission_classes = [IsAuthenticated]


class GradeLevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GradeLevel.objects.all()
    serializer_class = GradeLevelSerializer
    permission_classes = [IsAuthenticated]


# ClassYear Views
class ClassYearListCreateView(generics.ListCreateAPIView):
    queryset = ClassYear.objects.all()
    serializer_class = ClassYearSerializer
    permission_classes = [IsAuthenticated]


class ClassYearDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassYear.objects.all()
    serializer_class = ClassYearSerializer
    permission_classes = [IsAuthenticated]


# ReasonLeft Views
cl
...[truncated]...

### api/exceptions.py
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status
import traceback


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        return Response(
            {"error": response.status_code, "detail": response.data},
            status=response.status_code,
        )

    # Handle non-DRF errors (500 errors)
    return Response(
        {"error": "Server Error", "detail": str(exc)},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

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

### attendance/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import TeachersAttendance, StudentAttendance, PeriodAttendance
from .serializers import (
    TeacherAttendanceSerializer,
    StudentAttendanceSerializer,
    PeriodAttendanceSerializer,
)


class TeacherAttendanceListView(APIView):

    queryset = TeachersAttendance.objects.all()
    serializer_class = TeacherAttendanceSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ["teacher__fname", "date"]

    def get(self, request):
        attendances = TeachersAttendance.objects.all()
        serializer = TeacherAttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherAttendanceDetailView(APIView):
    def get(self, request, pk):
        try:
            attendance = TeachersAttendance.objects.get(pk=pk)
        except TeachersAttendance.DoesNotExist:
            raise NotFound(detail="Teacher Attendance record not found.")

        serializer = TeacherAttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            attendance = TeachersAttendance.objects.get(pk=pk)
        except TeachersAttendance.DoesNotExist:
            raise NotFound(detail="Teacher Attendance record not found.")

        serializer = TeacherAttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            attendance = TeachersAttendance.objects.get(pk=pk)
        except TeachersAttendance.DoesNotExist:
            raise NotFound(detail="Teacher Attendance record not found.")

        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentAttendanceListView(APIView):
    def get(self, request):
        attendances = StudentAttendance.objects.all()
       
...[truncated]...