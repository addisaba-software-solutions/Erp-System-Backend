from rest_framework import serializers
from .models import EmployeModel,AccountModel,DepartmentModel

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

