from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from dorayaki.api.user.views import UserViewSet
from dorayaki.api.thread.views import ThreadViewSet
from dorayaki.api.comment.views import CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'threads', ThreadViewSet, basename="threads")
router.register(r'comments', CommentViewSet, basename="comments")

from dorayaki.api.user.views import RegisterUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

dorayaki_urls = [
    re_path(r'^register/$', RegisterUserAPIView.as_view(), name="register"),
    re_path(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
dorayaki_urls += router.urls
