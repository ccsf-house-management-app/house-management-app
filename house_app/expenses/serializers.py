from rest_framework import serializers
from .models import Utilities

class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = ( 'formonth', 'foryear', 'utname', 'accountid', 'amount', 'date_utcreated', 'date_due', 'utdescription' )