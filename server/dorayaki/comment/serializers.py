from rest_framework import serializers

from dorayaki.comment.models import Comment

# Modified version from https://stackoverflow.com/questions/13376894/django-rest-framework-nested-self-referential-objects#answer-27236783
class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CommentSerializer(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveCommentSerializer(source="comment_set", required=False, many=True)
    class Meta:
        model = Comment
        fields = ['pk', 'owner', 'thread', 'parent', 'text', 'created', 'replies']
        read_only_fields = ['owner']