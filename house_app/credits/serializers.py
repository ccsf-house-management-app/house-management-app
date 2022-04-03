from rest_framework import serializers
from .models import Credit

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ( 'cruserid', 'formonth', 'foryear', 'crname', 'cracccount', 'cramount', 'date_cr', 'date_done', 'crdescription' )