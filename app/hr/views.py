from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import EmployeModel,AccountModel,EmployAddressModel
from .serializers import EmployeSerializer,AccountSerializer,EmployeAddressSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from utilities.token import get_token,get_role



class EmployeApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=EmployeSerializer
    queryset= EmployeModel.objects.all()
    lookup_field='EmployeId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
       if id:
            return self.retrieve(request,id)
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
            return self.retrieve(request,id)
       else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   
  
class EmployeAddressApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=EmployeAddressSerializer
    queryset= EmployAddressModel.objects.all()
    lookup_field='locationId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None): 
     #   token = get_token(request)
     #   print(get_role(token))
       if id:
            return self.retrieve(request,id)
       else:
              return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
         return self.update(request,id) 

    def delete(self,request,id=None):
         return self.destroy(request,id)   
   


    




