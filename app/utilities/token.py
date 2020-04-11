from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def get_token(request):
    PREFIX = 'Bearer'
    header=request.headers.get('Authorization')
    bearer, _, token = header.partition(' ')
    if bearer != PREFIX:
      return ValueError('Invalid token')
    return token
        
def get_role(token) :
    role=Token.objects.get(key=token).user.roles
    return role

def get_claim(token) :
    claim=Token.objects.get(key=token).user.claim
    return claim

def is_admin(token) :
    is_admin=Token.objects.get(key=token).user.is_admin
    return is_admin    

def get_department(token) :
    role=Token.objects.get(key=token).user.department
    return role    