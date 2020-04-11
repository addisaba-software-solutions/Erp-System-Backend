from django.db import models

class EmployeModel(models.Model): 
    employeId = models.AutoField(primary_key=True,unique=True ) 
    firstName=models.CharField(max_length=15,verbose_name="First name")
    lastName=models.CharField(max_length=15,verbose_name="Last name")
    email=models.CharField(max_length=30,unique=True )
    hiredDate=models.DateField(max_length=15,verbose_name="Hired date")
    telephone=models.CharField(max_length=15)
    birthDate=models.DateField(max_length=15,verbose_name="Birth date")
    department=models.ForeignKey("DepartmentModel", verbose_name="Department" , db_column="departmentId",on_delete=models.CASCADE)
  
    termOfEmployment=models.DateField(max_length=10,verbose_name="Term of Employment")
    country=models.CharField(max_length=20)
    region=models.CharField(max_length=25)
    city=models.CharField(max_length=20)
  
    def __str__(self):
        return self.firstName 

class DepartmentModel(models.Model): 
    departmentId = models.AutoField(primary_key=True,unique=True) 
    departmentName=models.CharField(max_length=20,verbose_name="Department Name")

    def __str__(self):
        return self.departmentName        

class RoleModel(models.Model): 
    roleId = models.AutoField(primary_key=True,auto_created=True) 
    role=models.CharField(max_length=20)
    department=models.ForeignKey("DepartmentModel", verbose_name="Department" , db_column="departmentId",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.role
       
class claimModel(models.Model): 
    levelId = models.AutoField(primary_key=True,auto_created=True) 
    level=models.CharField(max_length=20)
    role=models.ForeignKey("RoleModel", verbose_name="Role" , db_column="roleId",on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.level)



class OrderModel(models.Model): 
    orderId = models.AutoField(primary_key=True,auto_created=True) 
    orderNumber=models.IntegerField(verbose_name="Order number")
    quantity=models.IntegerField()
    description=models.CharField(max_length=50)
    orderDate=models.DateField(max_length=20)
    discount=models.FloatField(null=False)
    item= models.ForeignKey("ItemModel", verbose_name="Item" , db_column="itemId",on_delete=models.CASCADE)
    def __str__(self):
     return self.orderName 

"""Item model which have many to many realtion with Order model and many to one with catagory model"""
class ItemModel(models.Model): 
    itemId = models.AutoField(primary_key=True,auto_created=True) 
    itemName=models.CharField(max_length=20)
    quantity=models.IntegerField(null=False)
    retailPrice=models.FloatField(null=False)
    packaging=models.CharField(max_length=20)
    catagory= models.ForeignKey("CatagoryModel", verbose_name="Catagory" , db_column="catagoryId",on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName    

""" Catagory model related to Item"""
class CatagoryModel(models.Model): 
    catagoryId=models.AutoField(primary_key=True,unique=True) 
    catagory = models.CharField(auto_created=True,max_length=20) 
    subCatagory = models.CharField(auto_created=True,max_length=20) 

    def __str__(self):
        return self.catagory  

"""Status model realted to Order, employe models"""
class StatusModel(models.Model): 
    orderId = models.AutoField(primary_key=True,auto_created=True) 
    orderName=models.CharField(max_length=20,verbose_name="Order name")
    location=models.CharField(max_length=50)
    date=models.DateField(max_length=20)
    
    def __str__(self):
        return self.orderName  

"""ShipmentStatus table realted to siv and order"""
class ShipmentStatusModel(models.Model): 
    shipmentId = models.AutoField(primary_key=True,auto_created=True) 
    orderName=models.CharField(max_length=20,verbose_name="Order name")
    location=models.CharField(max_length=50)
    date=models.DateField(max_length=20)
    
    def __str__(self):
        return self.orderName 

"""invoice table related to Order and Employe tables"""
class InvoiceModel(models.Model): 
    invoiceId = models.AutoField(primary_key=True) 
    quantity = models.IntegerField()
    invoiceNo = models.IntegerField(verbose_name="Invoice number")
    ItemId = models.IntegerField()
    subTotal =models.FloatField(verbose_name="Sub total")
    Total =models.FloatField()
    Tax =models.FloatField()
    retailPrice =models.IntegerField()
    date=models.DateField(max_length=20)
    
    def __str__(self):
        return self.invoiceNo 

"""siv models which is related to Order model"""
class sivModel(models.Model): 
    sivId = models.AutoField(primary_key=True,auto_created=True) 
    sivDate= models.DateField()
    
    def __str__(self):
        return self.sivId 

"""shipment model eralted to employe model"""
class ShipmentModel(models.Model): 
    shipmentId = models.AutoField(primary_key=True,auto_created=True) 
    quantity= models.FloatField()
    receivedStatus= models.CharField(max_length=30,verbose_name="Recieved Status")
    conditionOnTrack= models.CharField(max_length=30,verbose_name="Condition on truack")
    receivedBy= models.CharField(max_length=20,verbose_name="Recieved By")
    dateOnTrack= models.DateField(verbose_name="Date on truck")
    arrivalDate= models.DateField(verbose_name="Arrival date")
    departureDate= models.DateField()
    
    def __str__(self):
        return self.shipmentId 
     
"""comapny model reated to employe and order models"""    
class CompanyModel(models.Model): 
    companyId = models.AutoField(primary_key=True,auto_created=True) 
    companyName= models.CharField(max_length=30,verbose_name="Company name")
    generalManger= models.CharField(max_length=30,verbose_name="General manager")
    contactPerson= models.CharField(max_length=20,verbose_name="Contact person")
    workingField= models.CharField(max_length=20,verbose_name="Working Field")
    paymentOption= models.CharField(max_length=20,verbose_name="Payment option")
    email = models.EmailField(max_length = 30)
    tinNumber= models.IntegerField(verbose_name="Tin number")
    
    def __str__(self):
        return self.companyName 
         
