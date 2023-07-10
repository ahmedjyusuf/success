from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
User = get_user_model()

from django.http import JsonResponse
@api_view(['GET'])
def get_current_user(request):
    data = {'user': 'the main one'}
    # return Response({'user': 'the main one'})
    return JsonResponse(data)

@api_view(['GET'])
def names(request):
    user = request.user 
    print(dir(user))
    person = {
        'fist_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return Response(person)
