from django.contrib import admin

from .models import Credit

class CreditAdmin(admin.ModelAdmin):
    list_display = ( 'cruserid', 'formonth', 'foryear', 'crname', 'cracccount', 'cramount', 'date_cr', 'date_done', 'crdescription' )

# Register your models here.
admin.site.register(Credit,CreditAdmin)

