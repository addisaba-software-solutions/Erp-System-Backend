from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from manage_auth.models import User


def get_token(self,request):
    PREFIX = 'Bearer'
  

    header=request.headers.get('Authorization')
    if(header is None):
       return False
    else:
        try:
                bearer, _, token = header.partition(' ')
                if bearer != PREFIX:
                    return False
                else:
                 
                 return token

        except expression as identifier:
             return False
                


        
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