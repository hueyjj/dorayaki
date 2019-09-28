from rest_framework import viewsets

from dorayaki.permissions import IsAuthenticatedAndOwner
from dorayaki.thread.models import Thread
from dorayaki.thread.serializers import ThreadSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    permission_classes = [IsAuthenticatedAndOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)