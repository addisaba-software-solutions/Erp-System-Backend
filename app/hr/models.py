from django.db import models


class DepartmentModel(models.Model): 
    departmentId = models.AutoField(primary_key=True,unique=True) 
    departmentName=models.CharField(max_length=20,blank=True)
    def __str__(self):
       return self.departmentName

       
class EmployeModel(models.Model): 
    employeId = models.AutoField(primary_key=True,unique=True ) 
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    email=models.CharField(max_length=30,blank=True,unique=True )
    hiredDate=models.DateField(max_length=15)
    telephone=models.CharField(max_length=15)
    birthDate=models.DateField(max_length=15)
    termOfEmployment=models.DateField(max_length=10)
    role=models.CharField(max_length=10)
    level=models.CharField(max_length=10)
    country=models.CharField(max_length=20,blank=True,)
    region=models.CharField(max_length=25)
    city=models.CharField(max_length=10)
    # department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,to_field='departmentId')

  
    def __str__(self):
        return self.firstName


class AccountModel(models.Model): 
    accountId = models.AutoField(primary_key=True,unique=True) 
    userName=models.CharField(max_length=20,blank=True)
    password=models.DateField(max_length=25)
    # employe=models.OneToOneField(EmployeModel,  on_delete=models.CASCADE,to_field='employeId')
    
    def __str__(self):
       return self.userName

