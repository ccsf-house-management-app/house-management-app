from django.contrib import admin

from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ( 'formonth', 'foryear', 'user', 'bill_type', 'accountid', 'paidamount', 'date_paid', 'description')
# Register your models here.
admin.site.register(Account, AccountAdmin)
