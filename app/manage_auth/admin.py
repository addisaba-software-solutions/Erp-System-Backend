from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . models import UserManager

from .models import User

# class CustomUserAdmin(UserAdmin):
#     model = User
#     objects = UserManager()
#     list_display = ('email',  'username',)
    
   
    
#     fieldsets = (
#         (None, {'fields': ('email', 'password','username')}),
#     )
  

#     search_fields = ('username',)
#     ordering = ('username',)


admin.site.register(User)