from django.contrib import admin
from django.urls import include, path, re_path

from dorayaki.api.routers import api_urls
from dorayaki.api.user.views import RegisterUserAPIView

API_VERSION = '^(?P<version>(api/)(v1|v2))'

urlpatterns = [
    re_path(f'{API_VERSION}/', include(api_urls), name='root'),
    # re_path(r'^(api)/auth/', include('rest_framework.urls')),
    # re_path(f'{API_VERSION}/login', views.LoginView.as_view(), name='login'),
    # re_path(f'{API_VERSION}/logout', views.LogoutView.as_view(), name='logout'),
    re_path(f'{API_VERSION}/auth/', include('django.contrib.auth.urls')),
    re_path(f'{API_VERSION}/auth/register/', RegisterUserAPIView.as_view(), name='register'),
]
