from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_staff=False):
        if not email:
            raise ValueError("Users must have an email address")
            
        user = self.model(
            email=self.normalize_email(email), 
            username=username,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            is_staff=True,
        )
        user.is_superuser=True
        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email", unique=True, blank=True, null=True)
    username = models.CharField("username", max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
