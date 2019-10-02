from django.contrib import admin
from django.urls import include, path, re_path

from dorayaki.views.home import HomeView
from dorayaki.views.register import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('register/', RegisterView.as_view(), name="register"),
]

from dorayaki.api.urls import urlpatterns as api_urls
urlpatterns += api_urls
