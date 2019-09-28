from django.db import models
from django.conf import settings

from dorayaki.user.models import User

class Thread(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.TextField()
    link = models.TextField()
    created = models.DateTimeField(auto_now_add=True)