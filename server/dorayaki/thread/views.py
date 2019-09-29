from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from dorayaki.permissions import IsOwner
from dorayaki.thread.models import Thread
from dorayaki.thread.serializers import ThreadSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly, 
        IsOwner,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)