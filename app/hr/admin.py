from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import EmployeModel,DepartmentModel,RoleModel,CatagoryModel,claimModel,ItemModel,  OrderModel, CompanyModel, StatusModel, ShipmentScheduleModel, sivModel, InventoryItemModel

# Register your models here.
admin.site.register(EmployeModel)
admin.site.register(DepartmentModel)
admin.site.register(RoleModel)
admin.site.register(claimModel)
admin.site.register(ItemModel)
admin.site.register(CatagoryModel)
admin.site.register(OrderModel)
admin.site.register(CompanyModel)
admin.site.register(StatusModel)
admin.site.register(ShipmentScheduleModel)
admin.site.register(sivModel)
admin.site.register(InventoryItemModel)

