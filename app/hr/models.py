from django.db import models

class EmployeModel(models.Model): 
    employeId = models.AutoField(primary_key=True,auto_created=True) 
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    email=models.CharField(max_length=20,blank=True)
    hiredDate=models.DateField(max_length=15)
    telephone=models.CharField(max_length=15)
    birthDate=models.DateField(max_length=15)
    termOfEmployment=models.DateField(max_length=10)

    def __str__(self):
        return self.firstName
    
    
class AccountModel(models.Model): 
    accountId = models.AutoField(primary_key=True,auto_created=True) 
    userName=models.CharField(max_length=20,blank=True)
    password=models.DateField(max_length=25)
    role=models.CharField(max_length=10)
    level=models.CharField(max_length=10)
    employe=models.OneToOneField(EmployeModel,  on_delete=models.CASCADE)
    
    def __str__(self):
     return self.userName

class EmployAddressModel(models.Model): 
    locationId = models.AutoField(primary_key=True,auto_created=True) 
    country=models.CharField(max_length=20,blank=True)
    region=models.CharField(max_length=25)
    city=models.CharField(max_length=10)
    employe=models.OneToOneField(EmployeModel,  on_delete=models.CASCADE)
    
    def __str__(self):
     return self.country

     
    
    