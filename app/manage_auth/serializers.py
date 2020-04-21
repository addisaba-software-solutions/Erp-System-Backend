from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import serializers, exceptions
from django.core import serializers as jsonParse
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from hr.serializers import *

from hr.models import *

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_409_CONFLICT,
)
from .models import UserManager, EmployeModel
from utilities.token import *


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    employe = serializers.CharField()
    department = serializers.CharField()
    claim = serializers.CharField()
    role = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, val):
        """
        Validates user data.
        """
        if User.objects.filter(username=val).exists():
            raise serializers.ValidationError("This username already exists")

        return val

    def validate_email(self, val):
        """
        Validates user data.
        """
        if User.objects.filter(email=val).exists():
            raise serializers.ValidationError("This email already exists")

        return val

    def validate_employe(self, val):
        """
        Validates user data.
        """
        if User.objects.filter(employe=val).exists():
            raise serializers.ValidationError("This employe has already account")
        elif not EmployeModel.objects.filter(employeId=val).exists():
            raise serializers.ValidationError(
                "This employe has not been registered yet"
            )
        return val

    def validate_department(self, val):
        """
        Validates user data.
        """
        if not DepartmentModel.objects.filter(departmentId=val).exists():
            raise serializers.ValidationError("This department not exist")
        return val

    def validate_claim(self, val):
        """
        Validates user data.
        """
        if not claimModel.objects.filter(levelId=val).exists():
            raise serializers.ValidationError("This claim not exist")
        return val

    def validate_role(self, val):
        """
        Validates user data.
        """
        if not RoleModel.objects.filter(roleId=val).exists():
            raise serializers.ValidationError("This role not exist")
        return val

    class Meta:
        fields = "__all__"
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        depth = 1


class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # added missing fields for serializer
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, data):
      
        """
        Validates user data.
        """
        user = authenticate(
            username=data.get("username", None), password=data.get("password", None)
        )

        if not user:
            return Response({"errors": {"Unauthorized": "Invalid Credentials"}}, status=401)

        if not user.is_active:
            return Response({"errors": "This user has been deactivated."})
        role = None
        if not user.roles:
            role = None
        else:
            role = {
                "roleId": user.roles.roleId,
                "role": user.roles.role,
            }
        department = None
        if not user.department:
            department = None
        else:
            department = {
                "departmentId": user.department.departmentId,
                "departmentName": user.department.departmentName,
            }
        level = None
        if not user.claim:
            level = None
        else:
            level = {
                "levelId": user.claim.levelId,
                "level": user.claim.level,
            }

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "department": department,
                "role": role,
                "level": level,
            },
            status=200,
        )

