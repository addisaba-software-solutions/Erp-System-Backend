 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def get_token(request):
        PREFIX = 'Bearer'
        header=request.headers.get('Authorization')
        bearer, _, token = header.partition(' ')
        if bearer != PREFIX:
          return ValueError('Invalid token')
        return token
        
def get_role(token):
        role=Token.objects.get(key=token).user.id
        level=Token.objects.get(key=token).user.id
        roles = {
          "role": role,
          "level":level
            }

        return Response(roles)