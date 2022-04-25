from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import HouseAppUser


admin.site.register(HouseAppUser, UserAdmin)
