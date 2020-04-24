from rest_framework import permissions
from utilities.token import *

from rest_framework.authtoken.models import Token
DANGER_METHODS = ['GET','POST','PUT','DELETE', 'HEAD', 'OPTIONS']
CRITICAL_METHODS = ['GET', 'HEAD','POST','PUT', 'OPTIONS',]
SAFE_METHODS = ['GET', 'HEAD','POST', 'OPTIONS']

class AdminPermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """
    def has_permission(self, request, view):
        token = get_token(request)
        if not token:
          return False
        if is_admin(token):
          return True
        elif is_superuser(token):
          return True
        else:
          return False



class HrPermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """
    def has_permission(self, request, view):
        token=get_token(request)
        if(token!=False):
          department=get_department(token)
          role=get_role(token)
          claim=get_claim(token)
          if is_superuser(token):
               return True
          elif str(department) == 'HR':
               if str(claim) == 'Manager':
                    return True

               elif str(claim) == 'Senior' and request.method in CRITICAL_METHODS:
                    return True

               elif str(claim) == 'Junior' and request.method in SAFE_METHODS:
                    return True
               else:
                    return False

          else:
               return False

class FinancePermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """
    def has_permission(self, request, view):
        token = get_token(request)
        if(token!=False):
          department=get_department(token)
          role=get_role(token)
          claim=get_claim(token)
          if is_superuser(token):
               return True
          
        elif str(department) == 'Finance':
            if str(claim) == 'Manager':
               return True

            elif str(claim) == 'Senior' and request.method in CRITICAL_METHODS:
               return True

            elif str(claim) == 'Junior' and request.method in SAFE_METHODS:
                 return True
            else:
                 return False
        else:
            return False

class SalesPermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """
    def has_permission(self, request, view):
        token=get_token(request)
        if(token!=False):
               department=get_department(token)
               role=get_role(token)
               claim=get_claim(token)
               if is_superuser(token):
                 return True
        elif str(department) == 'Sales':   
            if str(claim) == 'Manager':
                  return True

            elif str(claim) == 'Senior' and request.method in CRITICAL_METHODS:
                 return True

            elif str(claim) == 'Junior' and request.method in SAFE_METHODS:
                 return True
            else:
                 return False

        else:
            return False


class LogisticsPermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """
    def has_permission(self, request, view):
        token=get_token(request)
        if(token!=False):
          department=get_department(token)
          role=get_role(token)
          claim=get_claim(token)
          if is_superuser(token):
             return True
        elif str(department) == 'Logistics':   
            if str(claim) == 'Manager':
                  return True

            elif str(claim) == 'Senior' and request.method in CRITICAL_METHODS:
                 return True

            elif str(claim) == 'Junior' and request.method in SAFE_METHODS:
                 return True
            else:
                 return False

        else:
            return False

class InventoryPermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """
    def has_permission(self, request, view):
        token=get_token(request)
        if(token!=False):
               department=get_department(token)
               role=get_role(token)
               claim=get_claim(token)
               if is_superuser(token):
                    return True
        elif str(department) == 'Inventory':   
            if str(claim) == 'Manager':
                  return True

            elif str(claim) == 'Senior' and request.method in CRITICAL_METHODS:
                 return True

            elif str(claim) == 'Junior' and request.method in SAFE_METHODS:
                 return True
            else:
                 return False

        else:
            return False                               