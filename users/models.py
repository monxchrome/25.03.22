import uuid

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True, db_index=True)
    f_name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    l_name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    dt_birth = models.DateField(null=True, blank=True)

    # optional fields

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joinuser = models.DateField(auto_now_add=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager

    def __str__(self):
        return self.email
