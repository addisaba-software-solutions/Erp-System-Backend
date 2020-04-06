from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import EmployeModel,AccountModel,DepartmentModel,RoleModel,claimModel,ItemModel,CatagoryModel,OrderModel, companyModel
from .serializers import EmployeSerializer,AccountSerializer,DepartmentSerializer,RoleSerializer,ClaimSerializer,ItemSerializer,CatagorySerializer,OrderSerializer, CompanySerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from utilities.token import get_token,get_role



class EmployeApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=EmployeSerializer
    queryset= EmployeModel.objects.all()
    lookup_field='employeId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
         if id:
            return self.list(request,id)
         else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   
  
class AccountApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=AccountSerializer
    queryset= AccountModel.objects.all()
    lookup_field='accountId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   
  
class DepartmentApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=DepartmentSerializer
    queryset= DepartmentModel.objects.all()
    lookup_field='departmentId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   
  

class RoleApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=RoleSerializer
    queryset= RoleModel.objects.all()
    lookup_field='roleId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   
class LevelApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ClaimSerializer
    queryset= claimModel.objects.all()
    lookup_field='levelId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   
  

class ItemApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ItemSerializer
    queryset= ItemModel.objects.all()
    lookup_field='ItemId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   
class CatagoryApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=CatagorySerializer
    queryset= CatagoryModel.objects.all()
    lookup_field='catagoryId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   

class OrderApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=OrderSerializer
    queryset= OrderModel.objects.all()
    lookup_field='orderId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id) 


class CompanyApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=CompanySerializer
    queryset= companyModel.objects.all()
    lookup_field='companyId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.list(request,id)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)            



    

    




