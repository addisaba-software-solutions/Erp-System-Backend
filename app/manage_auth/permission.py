from rest_framework import permissions
from utilities.token import get_claim, get_department, get_role, get_token, is_admin

from rest_framework.authtoken.models import Token

DANGER_METHODS = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]
CRITICAL_METHODS = [
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "OPTIONS",
]
SAFE_METHODS = ["GET", "HEAD", "POST", "OPTIONS"]


class AdminPermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """

    def has_permission(self, request, view):
        token = get_token(request)
        admin = is_admin(token)
        if admin:
            return True
        else:
            return False


class FinancePermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """

    def has_permission(self, request, view):
        token = get_token(request)

        department = get_department(token)
        role = get_role(token)
        claim = get_claim(token)
        if str(department) == "Finance":
            if str(claim) == "Manager":
                return True

            elif str(claim) == "Senior" and request.method in CRITICAL_METHODS:
                return True

            elif str(claim) == "Junior" and request.method in SAFE_METHODS:
                return True
            else:
                return False

        else:
            return False


class HrPermissionsAll(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """

    def has_permission(self, request, view):
        token = get_token(self, request)
        if token is not False:
            department = get_department(token)
            role = get_role(token)
            claim = get_claim(token)

            if str(department) == "HR":
                if str(claim) == "Manager":
                    return True

                elif str(claim) == "Senior" and request.method in CRITICAL_METHODS:
                    return True

                elif str(claim) == "Junior" and request.method in SAFE_METHODS:
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
        token = get_token(request)
        department = get_department(token)
        role = get_role(token)
        claim = get_claim(token)
        if str(department) == "Sales":
            if str(claim) == "Manager":
                return True

            elif str(claim) == "Senior" and request.method in CRITICAL_METHODS:
                return True

            elif str(claim) == "Junior" and request.method in SAFE_METHODS:
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
        token = get_token(request)
        department = get_department(token)
        role = get_role(token)
        claim = get_claim(token)
        if str(department) == "Logistics":
            if str(claim) == "Manager":
                return True

            elif str(claim) == "Senior" and request.method in CRITICAL_METHODS:
                return True

            elif str(claim) == "Junior" and request.method in SAFE_METHODS:
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
        token = get_token(request)
        department = get_department(token)
        role = get_role(token)
        claim = get_claim(token)
        if str(department) == "Inventory":
            if str(claim) == "Manager":
                return True

            elif str(claim) == "Senior" and request.method in CRITICAL_METHODS:
                return True

            elif str(claim) == "Junior" and request.method in SAFE_METHODS:
                return True
            else:
                return False

        else:
            return False
