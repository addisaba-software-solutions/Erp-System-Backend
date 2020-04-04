from django.urls import path,include
from .views import EmployeApiView,AccountApiView,DepartmentApiView,RoleApiView,LevelApiView,OrderApiView,CatagoryApiView,ItemApiView

urlpatterns = [
    path('emp/', EmployeApiView.as_view()),
    path('act/', AccountApiView.as_view()),
    path('dep/', DepartmentApiView.as_view()),
    path('role/', RoleApiView.as_view()),
    path('level/', LevelApiView.as_view()),
    path('item/', ItemApiView.as_view()),
    path('catagory/', CatagoryApiView.as_view()),
    path('order/', OrderApiView.as_view()),
]