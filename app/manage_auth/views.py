from django.core.exceptions import ValidationError
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions
from .models import User, UserManager
from .serializers import UserSerializer, LoginUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins
from utilities.token import get_token, get_role
from .permission import AdminPermissionsAll
from hr.models import EmployeModel, RoleModel, claimModel, DepartmentModel
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_409_CONFLICT,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

class AccountRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "accountId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, accountId=None):
        # token = get_token(request)
        return self.retrieve(request, id)

    def put(self, request, accountId=None):
        # token = get_token(request)
        return self.update(request, id)


class AccountListAdd(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"
    # permission_classes = (AdminPermissionsAll,)
    def get(self, request):
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, context={"request": request}, many=True)
        return Response(serializer.data)

    def delete(self, request):
        account = User.objects.get(email=request.data.get('email'))
        account.delete()
        emp = EmployeModel.objects.get(email=request.data.get('email'))
        emp.has_account = False
        emp.save()
        return Response({"success": "Delete"}, status=200)

    def post(self, request, *args, **kwargs):  # changed  to desired serializer
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            employe = EmployeModel.objects.get(employeId=request.data.get("employe"))
            department = DepartmentModel.objects.get(
                departmentId=request.data.get("department")
            )
            role = RoleModel.objects.get(roleId=request.data.get("roles"))
            claim = claimModel.objects.get(levelId=request.data.get("claim"))

            try:
                User.objects.create_user(
                    email=request.data.get("email"),
                    username=request.data.get("username"),
                    password=request.data.get("password"),
                    is_admin=request.data.get("is_admin"),
                    employe=employe,
                    department=department,
                    roles=role,
                    claim=claim,
                )
                employe = EmployeModel.objects.get(employeId=request.data.get("employe"))
                employe.has_account = True
                employe.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"errors": e.args}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

class LoginAPIView(APIView):
    serializer_class = LoginUserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(
            data=request.data
        )  # changed  to desired serializer
        if serializer.is_valid():
            return serializer.validated_data
        else:
            return Response({"errors": serializer.errors}, status=403)

