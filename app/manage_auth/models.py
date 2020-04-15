from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from hr.models import EmployeModel, DepartmentModel, RoleModel,claimModel
from rest_framework.response import Response

class UserManager(BaseUserManager):
    
   def create_user(self, email, username, password=None,department=None,employe=None,roles=None,claim=None,**extra_fields):
        # if not DepartmentModel.objects.get(departmentId=department).exists()):
        #    department=DepartmentModel.objects.get(departmentId=department)
        # else:
        #    DepartmentModel.objects.create(departmentId=department,departmentName="It")

        # employe=EmployeModel.objects.get(employeId=employe)
        # roles=RoleModel.objects.get(roleId=roles)
        # claim=claimModel.objects.get(levelId=claim)

        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
    
        user = self.model(email=self.normalize_email(email),
                          username=username,
                          department=department,
                          employe=employe,
                          roles=roles,
                          claim=claim,
                          **extra_fields)

        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user
     

   def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user
        

        


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    employe = models.OneToOneField(EmployeModel, related_name='user_profile',to_field='employeId',on_delete=models.CASCADE,null=True,blank=True,unique=True)
    department = models.ForeignKey(DepartmentModel, related_name='user_department',to_field='departmentId',on_delete=models.CASCADE,null=True,blank=True)
    roles = models.ForeignKey(RoleModel, related_name='user_role',to_field='roleId',on_delete=models.CASCADE,null=True,blank=True)
    claim = models.ForeignKey(claimModel, related_name='user_claim',to_field='levelId',on_delete=models.CASCADE,null=True,blank=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
   

    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_label):
        return True

   