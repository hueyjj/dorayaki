from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from dorayaki.thread import views

router = DefaultRouter()
router.register(r'threads', views.ThreadViewSet)

urlpatterns = [
    url('', include(router.urls))
]