from django.urls import path,include
from .views import EmployeApiView,AccountApiView,DepartmentApiView

urlpatterns = [
    path('emp/', EmployeApiView.as_view()),
    path('act/', AccountApiView.as_view()),
    path('dep/', DepartmentApiView.as_view()),
]