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



class EmployeApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=EmployeSerializer
    queryset= EmployeModel.objects.all()
    lookup_field='employeId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,employeId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
         if employeId:
            return self.retrieve(request,employeId)
         else:
            return self.list(request)

    # def post(self,request,employeId=None):
    #     return self.create(request)

    def put(self,request,employeId=None):
         return self.update(request,employeId) 

    def delete(self,request,employeId=None):
         return self.destroy(request,employeId)  

class ListAddEmploye(generics.ListCreateAPIView):
    serializer_class=EmployeSerializer
    queryset= EmployeModel.objects.all()
    lookup_field='employeId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)


  
class AccountApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=AccountSerializer
    queryset= AccountModel.objects.all()
    lookup_field='accountId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,accountId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if accountId:
           return self.retrieve(accountId)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,accountId=None):
         return self.update(request,accountId) 

    def delete(self,request,accountId=None):
         return self.destroy(request,accountId) 

class AccountListAdd(generics.ListCreateAPIView):
    serializer_class=AccountSerializer
    queryset= AccountModel.objects.all()
    lookup_field='accountId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
   
  
class DepartmentApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=DepartmentSerializer
    queryset= DepartmentModel.objects.all()
    lookup_field='departmentId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,departmentId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if id:
            return self.retrieve(departmentId)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,departmentId=None):
         return self.update(request,departmentId) 

    def delete(self,request,departmentId=None):
         return self.destroy(request,departmentId)  

class DepartmentListAdd(generics.ListCreateAPIView):
    serializer_class=DepartmentSerializer
    queryset= DepartmentModel.objects.all()
    lookup_field='departmentId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
 
   
  

class RoleApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=RoleSerializer
    queryset= RoleModel.objects.all()
    lookup_field='roleId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,roleId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if roleId:
            return self.retrieve(request,roleId)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,roleId=None):
         return self.update(request,roleId) 

    def delete(self,request,id=None):
         return self.destroy(request,roleId) 

class RoleListAdd(generics.ListCreateAPIView):
    serializer_class=RoleSerializer
    queryset= RoleModel.objects.all()
    lookup_field='roleId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)




   
class LevelApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ClaimSerializer
    queryset= claimModel.objects.all()
    lookup_field='levelId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,levelId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if levelId:
            return self.retrieve(request,levelId)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,levelId=None):
         return self.update(request,levelId) 

    def delete(self,request,levelId=None):
         return self.destroy(request,levelId)  

class LevelListAdd(generics.ListCreateAPIView):
    serializer_class=ClaimSerializer
    queryset= claimModel.objects.all()
    lookup_field='levelId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
 
   
  

class ItemApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ItemSerializer
    queryset= ItemModel.objects.all()
    lookup_field='ItemId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,ItemId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if ItemId:
            return self.retrieve(request,ItemId)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,ItemId=None):
         return self.update(request,ItemId) 

    def delete(self,request,ItemId=None):
         return self.destroy(request,ItemId) 

class ItemListAdd(generics.ListCreateAPIView):
    serializer_class=ItemSerializer
    queryset= ItemModel.objects.all()
    lookup_field='ItemId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)


  
   
class CatagoryApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=CatagorySerializer
    queryset= CatagoryModel.objects.all()
    lookup_field='catagoryId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,catagoryId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if catagoryId:
            return self.retrieve(request,catagoryId)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,catagoryId=None):
         return self.update(request,catagoryId) 

    def delete(self,request,catagoryId=None):
         return self.destroy(request,catagoryId)  

class CatagoryListAdd(generics.ListCreateAPIView):
    serializer_class=CatagorySerializer
    queryset= CatagoryModel.objects.all()
    lookup_field='catagoryId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
 

class OrderApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=OrderSerializer
    queryset= OrderModel.objects.all()
    lookup_field='orderId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,orderId=None): 
     #   token = get_token(request)
     #   print(get_role(token))
        if orderId:
            return self.retrieve(request,orderId)
        else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,orderId=None):
         return self.update(request,orderId) 
    def delete(self,request,orderId=None):
         return self.destroy(request,orderId)   

class OrderListAdd(generics.ListCreateAPIView):
    serializer_class=OrderSerializer
    queryset= OrderModel.objects.all()
    lookup_field='orderId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
    


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

class CompanyListAdd(generics.ListCreateAPIView):
    serializer_class=CompanySerializer
    queryset= companyModel.objects.all()
    lookup_field='companyId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
          
 



    

    




