from rest_framework import authentication, permissions, viewsets
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from dorayaki.user.models import User
from dorayaki.user.serializers import UserSerializer


@ensure_csrf_cookie
@api_view(['GET'])
def login(request):
    return Response({"message": "hello world"})