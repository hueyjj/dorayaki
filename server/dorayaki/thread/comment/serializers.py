from rest_framework import serializers

from dorayaki.thread.comment.models import Comment

# https://stackoverflow.com/questions/13376894/django-rest-framework-nested-self-referential-objects#answer-27236783
class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.Serializer):
    replies = RecursiveSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['pk', 'owner', 'thread', 'parent', 'text', 'created']