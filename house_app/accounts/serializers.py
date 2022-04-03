from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ( 'formonth', 'foryear', 'user', 'bill_type', 'accountid', 'paidamount', 'date_paid', 'description')