from rest_framework import viewsets

from dorayaki.user.models import User
from dorayaki.user.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer