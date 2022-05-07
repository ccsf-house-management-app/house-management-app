from rest_framework import serializers
from .models import Utilities, DuePerTenant

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
        # fields = ( 'formonth', 'foryear', 'utname', 'accountid', 'amount', 'date_utcreated', 'date_due', 'utdescription' )
        fields = ( 'formonth', 'foryear', 'amount' )

class DuePerTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuePerTenant
        fields = ( 'id', 'formonth', 'foryear', 'amount' )