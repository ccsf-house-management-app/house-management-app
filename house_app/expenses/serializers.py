from rest_framework import serializers
from .models import Utilities, DuePerTenant, MonthlyDuePerTenant,MonthlyTotal

class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = ( 'formonth', 'foryear', 'utname', 'accountid', 'amount', 'date_utcreated', 'date_due', 'utdescription' )

class MonthlyDueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        # fields = ( 'formonth', 'foryear', 'utname', 'accountid', 'amount', 'date_utcreated', 'date_due', 'utdescription' )
        fields = ( 'formonth', 'foryear', 'amount' )

class MonthlyTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = ( 'formonth', 'foryear', 'amount' )

class DuePerTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuePerTenant
        fields = ( 'id', 'formonth', 'foryear', 'amount' )

class MonthlyDuePerTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyDuePerTenant
        fields = ('id', 'monthly_due', 'monthly_tenants', 'dues_perTenant', 'formonth', 'foryear')


class MonthlyTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyTotal
        fields = ('id', 'firstname', 'lastname', 'rent', 'utilities', 'monthly_total','formonth', 'foryear')
