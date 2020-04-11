from django.db import models
from model_utils import Choices

STATUS = Choices('Pending', 'Approved')
PAYMENTOPTION = Choices('VAT', 'TOT')

"""Employee has one department and one role"""
class EmployeModel(models.Model): 
    employeId = models.AutoField(primary_key=True,unique=True ) 
    firstName=models.CharField(max_length=15,verbose_name="First name")
    lastName=models.CharField(max_length=15,verbose_name="Last name")
    email=models.CharField(max_length=30,blank=True,unique=True )
    hiredDate=models.DateField(max_length=15,verbose_name="Hired date")
    telephone=models.CharField(max_length=15)
    birthDate=models.DateField(max_length=15,verbose_name="Birth date")
    
    department=models.ForeignKey("DepartmentModel", verbose_name="Department" , to_field="departmentId",on_delete=models.CASCADE)
   
    termOfEmployment=models.CharField(max_length=10,verbose_name="Term of Employment")
    country=models.CharField(max_length=20)
    region=models.CharField(max_length=25)
    city=models.CharField(max_length=20)
  
    def __str__(self):
        return self.firstName 

"""Department has many employee"""
class DepartmentModel(models.Model): 
    departmentId = models.AutoField(primary_key=True,unique=True) 
    departmentName=models.CharField(max_length=20,blank=True,verbose_name="Department Name")

    def __str__(self):
        return self.departmentName        

"""Role has many employee and has many claims"""
class RoleModel(models.Model): 
    roleId = models.AutoField(primary_key=True,auto_created=True) 
    role=models.CharField(max_length=20,blank=True)
    department=models.ForeignKey("DepartmentModel", verbose_name="Department" , to_field="departmentId",on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.department)
       
class claimModel(models.Model): 
    levelId = models.AutoField(primary_key=True,auto_created=True) 
    level=models.CharField(max_length=20,blank=True)
    role=models.ForeignKey("RoleModel", verbose_name="Role" , to_field="roleId",on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.role)

"""Order has many items and many company"""
class OrderModel(models.Model): 
    orderNumber=models.IntegerField(primary_key=True)
    company=models.ForeignKey("CompanyModel", to_field="companyId", on_delete=models.CASCADE)
    item=models.ForeignKey("InventoryItemModel", to_field="itemId", on_delete=models.CASCADE)
    orderName=models.CharField(max_length=100)
    salesPerson=models.CharField(max_length=100)
    description=models.CharField(max_length=50)
    orderDate=models.DateField(max_length=20)
    shipmentAddress= models.CharField(max_length=100)
    
    def __str__(self):
     return str(self.orderNumber)

"""Item which have one to many relation with Order and many to one with catagory"""
class ItemModel(models.Model):     
    itemId = models.AutoField(primary_key=True,auto_created=True)
    order= models.ForeignKey(OrderModel, related_name="item_order", on_delete=models.CASCADE, null=True, blank=True) 
    itemName=models.CharField(max_length=100)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return str(self.itemName)  

"""item in the inventory"""
class InventoryItemModel(models.Model): 
    catagory= models.ForeignKey("CatagoryModel", verbose_name="Catagory" , to_field="catagoryId",on_delete=models.CASCADE)
    itemId = models.AutoField(primary_key=True,auto_created=True) 
    itemName=models.CharField(max_length=100)
    warehouseName=models.CharField(max_length=100)
    quantity=models.IntegerField(null=False)
    retailPrice=models.FloatField(null=False)
    packaging=models.CharField(max_length=100)
    discount=models.IntegerField(null=True)

    def __str__(self):
        return str(self.itemName + "(  " + str(self.quantity) + " ) ")           

"""Catagory has many items"""
class CatagoryModel(models.Model): 
    catagoryId=models.AutoField(primary_key=True,unique=True) 
    catagory = models.CharField(auto_created=True,max_length=100,unique=True) 
    subCatagory = models.CharField(auto_created=True,max_length=100,unique=True) 

    def __str__(self):
        return str(self.catagory + " " + self.subCatagory) 

"""Status a weak entity depends on Order"""
class StatusModel(models.Model): 
    status=models.CharField(max_length=100)
    order= models.ForeignKey("OrderModel", to_field= "orderNumber",on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    date=models.DateField(max_length=20)

    class Meta:
        unique_together = ("order", "status")
    
    def __str__(self):
        return str(self.status)  

"""ShipmentStatus realted to Order and siv"""
class ShipmentScheduleModel(models.Model): 
    shipmentId = models.AutoField(primary_key=True,auto_created=True) 
    order=models.OneToOneField(OrderModel,on_delete=models.CASCADE)
    shipmentNumber= models.CharField(max_length=100, unique=True)
    date=models.DateField(max_length=20)
    departureDate=models.DateField(max_length=50)
    deliveryDate=models.DateField(max_length=50)
    deliveryPerson=models.CharField(max_length=100)
    receivedStatus= models.CharField(max_length=100,verbose_name="Recieved Status")
    conditionOnTrack= models.CharField(max_length=100,verbose_name="Condition on truack")
    receivedBy= models.CharField(max_length=100,verbose_name="Recieved By")

    def __str__(self):
        return str(self.shipmentNumber) 

"""comapny model reated to employe and order models"""    
class CompanyModel(models.Model): 
    companyId = models.AutoField(primary_key=True,auto_created=True) 
    companyName= models.CharField(max_length=100,verbose_name="Company name", unique=True)
    generalManger= models.CharField(max_length=100,verbose_name="General manager")
    contactPerson= models.CharField(max_length=100,verbose_name="Contact person")
    workingField= models.CharField(max_length=100,verbose_name="Working Field")
    paymentOption= models.CharField(max_length=100, choices= PAYMENTOPTION)
    email = models.EmailField(max_length = 100)
    tinNumber= models.IntegerField(verbose_name="Tin number")
    
    def __str__(self):
        return str(self.companyName)         

"""invoice table related to Order and Employe tables"""
class InvoiceModel(models.Model): 
    invoiceId = models.AutoField(primary_key=True,auto_created=True) 
    salesPerson=models.CharField(max_length=100)
    subTotal =models.FloatField(verbose_name="Sub total")
    Total =models.FloatField()
    Tax =models.FloatField()
    date=models.DateField(max_length=20)
    
    def __str__(self):
        return str(self.invoiceId) 

class InvoiceLineItemModel(models.Model):
    invoice=models.ForeignKey("InvoiceModel",to_field="invoiceId", on_delete=models.CASCADE)
    itemName=models.CharField(max_length=100)
    unitPrice=models.FloatField(max_length=100)
    quantity = models.IntegerField()
    ItemId = models.IntegerField()
    item_discount=models.FloatField(max_length=100)    

    def __str__(self):
        return str(self.invoice) 

"""siv models which is related to Order model"""
class sivModel(models.Model): 
    sivId = models.AutoField(primary_key=True,auto_created=True) 
    itemId=models.IntegerField()
    itemName=models.CharField(max_length=100)
    quantity=models.IntegerField()
    sivDate= models.DateField()
    warehouseName=models.CharField(max_length=100)
    approve=models.CharField(max_length=100, choices=STATUS, default=STATUS.Pending)


    
    def __str__(self):
        return str(self.sivId) 


        