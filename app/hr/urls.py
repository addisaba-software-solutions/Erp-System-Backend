from django.urls import path,include
from .views import EmployeApiView,EmployePostApiView,AccountApiView,DepartmentApiView,RoleApiView,LevelApiView,OrderApiView,CatagoryApiView,ItemApiView

urlpatterns = [
    path('api/v1/employe/', EmployePostApiView.as_view()),
    path('api/v1/employe/<int:employeId>/', EmployeApiView.as_view()),

    path('api/v1/account/', AccountApiView.as_view()),
    path('api/v1/account/<int:accountId>/', AccountApiView.as_view()),

    path('api/v1/department/', DepartmentApiView.as_view()),
    path('api/v1/department/<int:departmentId>/', DepartmentApiView.as_view()),

    path('api/v1/role/', RoleApiView.as_view()),
    path('api/v1/role/<int:roleId>/', RoleApiView.as_view()),

    path('api/v1/level/', LevelApiView.as_view()),
    path('api/v1/level/<int:levelId>/', LevelApiView.as_view()),

    path('api/v1/item/', ItemApiView.as_view()),
    path('api/v1/item/<int:itemId>/', ItemApiView.as_view()),

    path('api/v1/catagory/', CatagoryApiView.as_view()),
    path('api/v1/catagory/<int:catagoryId>/', CatagoryApiView.as_view()),

    path('api/v1/order/', OrderApiView.as_view()),
    path('api/v1/order/<int:orderId>/', OrderApiView.as_view()),

    path('api/v1/company/', CompanyApiView.as_view()),
]