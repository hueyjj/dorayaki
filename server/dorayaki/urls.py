"""dorayaki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from dorayaki.routers import router, urlpatterns2

API_VERSION = '^(?P<version>(api/)(v1|v2))'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(f'{API_VERSION}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(f'{API_VERSION}/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(f'{API_VERSION}/', include(router.urls), name='root'),
    re_path(f'{API_VERSION}/', include(urlpatterns2), name='root'),
]
