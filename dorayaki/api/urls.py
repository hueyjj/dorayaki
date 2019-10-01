from django.contrib import admin
from django.urls import include, path, re_path

from dorayaki.api.routers import api_urls

API_VERSION = '^(?P<version>(api/)(v1|v2))'

urlpatterns = [
    re_path(f'{API_VERSION}/', include(api_urls), name='root'),
]
