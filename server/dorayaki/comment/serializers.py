from rest_framework import serializers

from dorayaki.comment.models import Comment

# https://stackoverflow.com/questions/13376894/django-rest-framework-nested-self-referential-objects#answer-27236783
class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    #parent = RecursiveSerializer(many=True)
    children = RecursiveSerializer(source="comment_set", many=True)
    class Meta:
        model = Comment
        fields = ['pk', 'owner', 'thread', 'children', 'text', 'created']