from rest_framework import serializers
from .models import EmployeModel,DepartmentModel,RoleModel,claimModel,ItemModel,CatagoryModel,OrderModel,CompanyModel,StatusModel,ShipmentScheduleModel, sivModel

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeModel
        fields = '__all__' 
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentModel
        fields = '__all__' 

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoleModel
        fields = '__all__' 

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model=claimModel
        fields = '__all__'        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemModel
        fields = '__all__'        

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CatagoryModel
        fields = '__all__'     

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderModel
        fields = '__all__'                       

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyModel
        fields = '__all__'  

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatusModel
        fields = '__all__'          


class ShipmentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShipmentScheduleModel
        fields = '__all__' 

class SivSerializer(serializers.ModelSerializer):
    class Meta:
        model=sivModel
        fields = '__all__' 