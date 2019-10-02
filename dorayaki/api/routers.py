from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from dorayaki.api.user.views import UserViewSet
from dorayaki.api.thread.views import ThreadViewSet
from dorayaki.api.comment.views import CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'threads', ThreadViewSet, basename="threads")
router.register(r'comments', CommentViewSet, basename="comments")


from dorayaki.api.user.views import RegisterUserAPIView
from rest_framework import urls
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
print(urls)


api_urls = router.urls
api_urls += [
    re_path(r'^register/$', RegisterUserAPIView.as_view(), name="register"),
    # re_path(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # re_path(r'^refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^rest-auth/', include('rest_auth.urls'), name='token_refresh'),
    # re_path(r'^auth/', include('rest_framework.urls', namespace="auth")),
]
