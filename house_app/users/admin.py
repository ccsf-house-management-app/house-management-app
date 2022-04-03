from django.contrib import admin
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('userid', 'firstname', 'lastname', 'birthdate', 'email', 'phone', 'date_created')

# Register your models here.
admin.site.register(UserInfo, UserInfoAdmin)
