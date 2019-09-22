from django.db import models
from django.conf import settings
from django.utils import timezone

from dorayaki.user.models import User
from dorayaki.thread.models import Thread

class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    thread = models.ForeignKey(Thread)
    parent = models.ForeignKey('self')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)