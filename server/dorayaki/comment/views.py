from rest_framework import viewsets

from dorayaki.comment.models import Comment
from dorayaki.comment.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer