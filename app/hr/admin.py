from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import EmployeModel,DepartmentModel,RoleModel,CatagoryModel,ItemModel,claimModel

# Register your models here.
admin.site.register(EmployeModel)
admin.site.register(DepartmentModel)
admin.site.register(RoleModel)
admin.site.register(claimModel)
admin.site.register(CatagoryModel)
admin.site.register(ItemModel)
