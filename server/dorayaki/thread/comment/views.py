from rest_framework import viewsets

from dorayaki.thread.comment.models import Comment
from dorayaki.thread.comment.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer