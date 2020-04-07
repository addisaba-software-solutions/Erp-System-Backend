from django.urls import path,include
from .views import EmployeRUD,AccountRUD,DepartmentRUD,RoleRUD,LevelRUD,OrderRUD,CatagoryRUD,ItemRUD,CompanyRUD,EmployeListAdd, AccountListAdd, DepartmentListAdd, RoleListAdd, LevelListAdd, ItemListAdd, CatagoryListAdd, OrderListAdd,CompanyListAdd
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Erp System API",
      default_version='v1',
      description="Integrated Erp System that manage main business processes.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@iwork.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/employe/<int:employeId>/', EmployeRUD.as_view()),
    path('api/v1/employe/', EmployeListAdd.as_view()),

    path('api/v1/account/<int:accountId>/', AccountRUD.as_view()),
    path('api/v1/account/', AccountListAdd.as_view()),

    path('api/v1/department/<int:departmentId>/', DepartmentRUD.as_view()),
    path('api/v1/department/', DepartmentListAdd.as_view()),

    path('api/v1/role/<int:roleId>/', RoleRUD.as_view()),
    path('api/v1/role/', RoleListAdd.as_view()),

    path('api/v1/level/<int:levelId>/', LevelRUD.as_view()),
    path('api/v1/level/', LevelListAdd.as_view()),

    path('api/v1/item/<int:itemId>/', ItemRUD.as_view()),
    path('api/v1/item/', ItemListAdd.as_view()),

    path('api/v1/catagory/<int:catagoryId>/', CatagoryRUD.as_view()),
    path('api/v1/catagory/', CatagoryListAdd.as_view()),

    path('api/v1/order/<int:orderId>/', OrderRUD.as_view()),
    path('api/v1/order/', OrderListAdd.as_view()),
    
    path('api/v1/company/<int:companyId>/', CompanyRUD.as_view()),
    path('api/v1/company/', CompanyListAdd.as_view()),
]