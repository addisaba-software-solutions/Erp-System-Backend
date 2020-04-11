from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import EmployeModel,DepartmentModel,RoleModel,claimModel,ItemModel,CatagoryModel,OrderModel, CompanyModel
from .serializers import EmployeSerializer,DepartmentSerializer,RoleSerializer,ClaimSerializer,ItemSerializer,CatagorySerializer,OrderSerializer, CompanySerializer
from rest_framework.views import APIView
from utilities.token import get_token,get_role
from  manage_auth.permission import HrPermissionsAll



class EmployeRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=EmployeSerializer
    queryset= EmployeModel.objects.all()
    lookup_field='employeId'
    # authentication_classes=[TokenAuthentication]
    permission_classes=[HrPermissionsAll]

    def get(self,request,employeId=None): 
        return self.retrieve(request,employeId)

    def put(self,request,employeId=None):
        return self.update(request,employeId) 

    def delete(self,request,employeId=None):
        return self.destroy(request,employeId)  

class EmployeListAdd(generics.ListCreateAPIView):
    serializer_class=EmployeSerializer
    queryset= EmployeModel.objects.all()
    lookup_field='employeId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[HrPermissionsAll]
    
    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
    
class DepartmentRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=DepartmentSerializer
    queryset= DepartmentModel.objects.all()
    lookup_field='departmentId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[HrPermissionsAll]
    
    def get(self,request,departmentId=None): 
        # token = get_token(request)
        return self.retrieve(request,departmentId)
  
    def put(self,request,departmentId=None):
        # token = get_token(request)
        return self.update(request,departmentId) 

    def delete(self,request,departmentId=None):
        # token = get_token(request)
        return self.destory(request,departmentId)

class DepartmentListAdd(generics.ListCreateAPIView):
    serializer_class=DepartmentSerializer
    queryset= DepartmentModel.objects.all()
    lookup_field='departmentId'
    permission_classes=[HrPermissionsAll]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
  
class RoleRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=RoleSerializer
    lookup_field='roleId'
    permission_classes=[HrPermissionsAll]
    
    def get(self,request,roleId=None): 
        # token = get_token(request)
        return self.retrieve(request,roleId)

    def put(self,request,roleId=None):
        # token = get_token(request)
        return self.update(request,roleId) 

    def delete(self,request,roleId=None):
        # token = get_token(request)
        return self.destroy(request,roleId) 

class RoleListAdd(generics.ListCreateAPIView):
    serializer_class=RoleSerializer
    queryset= RoleModel.objects.all()
    lookup_field='roleId'
    # authentication_classes=[TokenAuthentication]
    permission_classes=[HrPermissionsAll]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)

class LevelRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ClaimSerializer
    queryset= claimModel.objects.all()
    lookup_field='levelId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[HrPermissionsAll]
    
    def get(self,request,levelId=None): 
        # token = get_token(request)
        return self.retrieve(request,levelId)

    def put(self,request,levelId=None):
        # token = get_token(request)
        return self.update(request,levelId) 

    def delete(self,request,levelId=None):
        # token = get_token(request)
        return self.destroy(request,levelId)  

class LevelListAdd(generics.ListCreateAPIView):
    serializer_class=ClaimSerializer
    queryset= claimModel.objects.all()
    lookup_field='levelId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[HrPermissionsAll]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
 
class ItemRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ItemSerializer
    queryset= ItemModel.objects.all()
    lookup_field='ItemId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,ItemId=None): 
        # token = get_token(request)
        return self.retrieve(request,ItemId)
     
    def put(self,request,ItemId=None):
        # token = get_token(request)
        return self.update(request,ItemId) 

    def delete(self,request,ItemId=None):
        # token = get_token(request)
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
   
class CatagoryRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CatagorySerializer
    queryset= CatagoryModel.objects.all()
    lookup_field='catagoryId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,catagoryId=None): 
        # token = get_token(request)
        return self.retrieve(request,catagoryId)
    
    def put(self,request,catagoryId=None):
        # token = get_token(request)
        return self.update(request,catagoryId) 

    def delete(self,request,catagoryId=None):
        # token = get_token(request)
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

class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer
    queryset= OrderModel.objects.all()
    lookup_field='orderId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,orderId=None): 
        # token = get_token(request)
        return self.retrieve(request,orderId)
      
    def put(self,request,orderId=None):
        # token = get_token(request)
        return self.update(request,orderId) 

    def delete(self,request,orderId=None):
        # token = get_token(request)
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

class CompanyRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CompanySerializer
    queryset= CompanyModel.objects.all()
    lookup_field='companyId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,companyId=None): 
        # token = get_token(request)
        return self.retrieve(request,companyId)

    def put(self,request,companyId=None):
        # token = get_token(request)
        return self.update(request,companyId) 

    def delete(self,request,companyId=None):
        # token = get_token(request)
        return self.destroy(request,companyId)  

class CompanyListAdd(generics.ListCreateAPIView):
    serializer_class=CompanySerializer
    queryset= CompanyModel.objects.all()
    lookup_field='companyId'
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request): 
        # token = get_token(request)
        return self.list(request)

    def post(self,request):
        # token = get_token(request)
        return self.create(request)
          
 


    

    




