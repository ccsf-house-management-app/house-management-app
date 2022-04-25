from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class HouseAppUser(AbstractUser):
    pass
    # class Meta:
    #     db_table = 'auth_user'