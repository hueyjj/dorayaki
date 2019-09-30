from rest_framework import (
    viewsets, 
    generics, 
    status,
)
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny, 
    IsAuthenticatedOrReadOnly,
)

from dorayaki.api.user.models import User
from dorayaki.api.user.serializers import (
    UserSerializer, 
    RegisterUserSerializer,
)
from dorayaki.permissions import IsOwner

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly, 
        IsOwner,
    ]

class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwner,
    ]