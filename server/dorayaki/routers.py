from rest_framework.routers import DefaultRouter

from dorayaki.user.views import UserViewSet
from dorayaki.thread.views import ThreadViewSet
from dorayaki.comment.views import CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'threads', ThreadViewSet)
router.register(r'comments', CommentViewSet, basename="comments")