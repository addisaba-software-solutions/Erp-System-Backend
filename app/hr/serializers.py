from rest_framework import serializers
from .models import EmployeModel,AccountModel

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeModel
        fields = '__all__' 
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountModel
        fields = '__all__' 

