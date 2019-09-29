from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from dorayaki.user.views import (
    UserViewSet, 
    RegisterUserAPIView,
)
from dorayaki.thread.views import ThreadViewSet
from dorayaki.comment.views import CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'threads', ThreadViewSet, basename="threads")
router.register(r'comments', CommentViewSet, basename="comments")

urlpatterns2 = [
    path('register/', RegisterUserAPIView.as_view()),
]
urlpatterns2 += router.urls
