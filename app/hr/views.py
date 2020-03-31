from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from utilities.token import get_token,get_role



class UserApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=UserSerializer
    queryset= UserModel.objects.all()
    lookup_field='id'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    

    def get(self,request,id=None): 

       token = get_token(request)
       print(get_role(token))

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
   
  


        




    




