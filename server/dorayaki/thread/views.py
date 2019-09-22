from rest_framework import viewsets

from dorayaki.thread.models import Thread
from dorayaki.thread.serializers import ThreadSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
