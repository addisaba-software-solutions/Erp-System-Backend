from rest_framework import serializers
from .models import EmployeModel,AccountModel,DepartmentModel,RoleModel,claimModel,ItemModel,CatagoryModel,OrderModel,companyModel

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeModel
        fields = '__all__' 
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountModel
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
        model=companyModel
        fields = '__all__'  