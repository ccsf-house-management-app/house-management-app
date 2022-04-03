from rest_framework import serializers
from .models import Rooms, RoomsAssign

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ( 'roomId', 'roomName', 'roomDescription', 'rent', 'capacity', 'date_created' )

class RoomsAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsAssign
        fields = ( 'roomid', 'tenantid', 'date_start', 'date_end', 'date_transaction', 'transactionId', 'remarks')