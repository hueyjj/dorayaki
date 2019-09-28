from rest_framework import serializers

from dorayaki.thread.models import Thread

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['pk', 'title', 'link', 'created']