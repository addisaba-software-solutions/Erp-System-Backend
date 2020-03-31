from django.db import models

class UserModel(models.Model):
    fName=models.CharField(max_length=100)
    lName=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.fName

