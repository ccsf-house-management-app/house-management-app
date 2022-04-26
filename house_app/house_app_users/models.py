# house_app/house_app_users/models.py
from django.db import models

from django.contrib.auth.models import BaseUserManager, PermissionsMixin

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class HouseUserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class HouseAppUser(AbstractUser):
    # pass
    class Meta:
        db_table = 'houseappusers'
        managed = True
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False
