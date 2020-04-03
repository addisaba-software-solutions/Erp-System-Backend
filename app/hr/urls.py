from django.urls import path,include
from .views import EmployeApiView,AccountApiView,EmployeAddressApiView

urlpatterns = [
    path('emp/', EmployeApiView.as_view()),
    path('act/', AccountApiView.as_view()),
    path('add/', EmployeAddressApiView.as_view()),

]