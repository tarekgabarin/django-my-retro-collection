"""
Database models.
"""
# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """Class for managing users"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates, saves, and returns new user"""
        if not email:
            raise ValueError("Email required when creating new user")
        created_user = self.model(email=self.normalize_email(email), **extra_fields)
        created_user.set_password(password)
        created_user.save(using=self._db)

        return created_user

class User(AbstractBaseUser, PermissionsMixin):
    """User in database"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

