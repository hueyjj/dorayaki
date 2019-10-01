from rest_framework import serializers

from dorayaki.api.thread.models import Thread

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['pk', 'owner', 'title', 'link', 'created']
        read_only_fields = ['owner']