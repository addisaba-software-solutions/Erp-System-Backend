from django.db import models

class EmployeModel(models.Model): 
    employeId = models.AutoField(primary_key=True,unique=True ) 
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    email=models.CharField(max_length=20,blank=True,unique=True )
    hiredDate=models.DateField(max_length=15)
    telephone=models.CharField(max_length=15)
    birthDate=models.DateField(max_length=15)
    termOfEmployment=models.DateField(max_length=10)
    role=models.CharField(max_length=10)
    level=models.CharField(max_length=10)
    country=models.CharField(max_length=20,blank=True,)
    region=models.CharField(max_length=25)
    city=models.CharField(max_length=10)
    def __str__(self):
        return self.firstName


class AccountModel(models.Model): 
    employe=models.OneToOneField(EmployeModel,  on_delete=models.CASCADE)
    accountId = models.AutoField(primary_key=True,auto_created=True) 
    userName=models.CharField(max_length=20,blank=True)
    password=models.DateField(max_length=25)
    
    def __str__(self):
       return self.userName

class EmployAddressModel(models.Model): 
    employe=models.OneToOneField(EmployeModel,  on_delete=models.CASCADE)
    locationId = models.AutoField(primary_key=True,auto_created=True) 
    country=models.CharField(max_length=20,blank=True)
    region=models.CharField(max_length=25)
    city=models.CharField(max_length=10)
    
    def __str__(self):
     return self.country

""" Order model which have many to many relation with item model"""

class Order(models.Model): 
    orderId = models.AutoField(primary_key=True,auto_created=True) 
    orderName=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    orderDate=models.DateField(max_length=20)
    discount=models.FloatField(null=False)
    
    def __str__(self):
     return self.orderName 

"""Item model which have many to many realtion with Order model"""
class Item(models.Model): 
    employeID=models.ManyToManyField(EmployeModel)
    orderId=models.ManyToManyField(Order)
    itemId = models.AutoField(primary_key=True,auto_created=True) 
    itemName=models.CharField(max_length=20,blank=True)
    quantity=models.IntegerField(null=False)
    catagory=models.CharField(max_length=10)
    subCatagory=models.CharField(max_length=10)
    retailPrice=models.FloatField(null=False)
    packaging=models.CharField(max_length=20)
    
    def __str__(self):
     return self.itemName    

"""Status model realted to Order, employe models"""
class Status(models.Model): 
    orderId = models.AutoField(primary_key=True,auto_created=True) 
    orderName=models.CharField(max_length=20)
    location=models.CharField(max_length=50)
    date=models.DateField(max_length=20)
    
    def __str__(self):
     return self.orderName  

"""ShipmentStatus table realted to siv and order"""
class ShipmentStatus(models.Model): 
    shipmentId = models.AutoField(primary_key=True,auto_created=True) 
    orderName=models.CharField(max_length=20)
    location=models.CharField(max_length=50)
    date=models.DateField(max_length=20)
    
    def __str__(self):
     return self.orderName 

"""invoice table related to Order and Employe tables"""
class Invoice(models.Model): 
    invoiceId = models.AutoField(primary_key=True,auto_created=True) 
    quantity = models.IntegerField()
    invoiceNo = models.IntegerField()
    ItemId = models.IntegerField()
    subTotal =models.FloatField()
    Total =models.FloatField()
    Tax =models.FloatField()
    retailPrice =models.IntegerField()
    date=models.DateField(max_length=20)
    
    def __str__(self):
     return self.invoiceNo 

"""siv models which is related to Order model"""
class siv(models.Model): 
    sivId = models.AutoField(primary_key=True,auto_created=True) 
    sivDate= models.DateField()
    
    def __str__(self):
     return self.sivId 

"""shipment model eralted to employe model"""
class Shipment(models.Model): 
    shipmentId = models.AutoField(primary_key=True,auto_created=True) 
    quantity= models.FloatField()
    receivedStatus= models.CharField(max_length=30)
    conditionOnTrack= models.CharField(max_length=30)
    receivedBy= models.CharField(max_length=20)
    dateOnTrack= models.DateField()
    arrivalDate= models.DateField()
    departureDate= models.DateField()
    
    def __str__(self):
     return self.shipmentId 
     
"""comapny model reated to employe and order models"""    
class company(models.Model): 
    companyId = models.AutoField(primary_key=True,auto_created=True) 
    quantity= models.FloatField()
    companyName= models.CharField(max_length=30)
    generalManger= models.CharField(max_length=30)
    contactPerson= models.CharField(max_length=20)
    workingField= models.CharField(max_length=20)
    paymentOption= models.CharField(max_length=20)
    email = models.EmailField(max_length = 30)
    tinNumber= models.IntegerField()
    
    def __str__(self):
     return self.companyName 
         
"""departemtn model realted to employe model"""
class Department(models.Model):
    departmentId = models.AutoField(primary_key= True, auto_created=True)
    departmentName= models.CharField(max_length=20)
