from django.contrib import admin

from .models import Utilities

class UtilitiesAdmin(admin.ModelAdmin):
    list_display = ( 'formonth', 'foryear', 'utname', 'accountid', 'amount', 'date_utcreated', 'date_due', 'utdescription' )
# Register your models here.
admin.site.register(Utilities, UtilitiesAdmin)