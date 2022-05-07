from rest_framework import serializers
from .models import Rooms, RoomsAssign, JoinRoom, MonthlyTenant
from users.models import UserInfo

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ( 'roomId', 'roomName', 'roomDescription', 'rent', 'capacity', 'date_created' )

class RoomsAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsAssign
        fields = ( 'roomid', 'tenantid', 'date_start', 'date_end', 'date_transaction', 'transactionId', 'remarks', 'formonth', 'foryear')


class JoinRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRoom
        fields = ( 'id','roomid', 'tenantid', 'date_start', 'date_end', 'date_transaction', 'transactionId', 'remarks', 'roomName', 'roomDescription', 'rent', 'capacity', 'date_created', 'firstname','lastname')

class TenantRoomSerializer(serializers.Serializer):
    # rooms = RoomsSerializer(many=True)
    # roomsassign = RoomsAssignSerializer(many=True)
    roomid = RoomsAssignSerializer()
    #tenant = serializers.StringRelatedField(many=True)
    class Meta:
        model = Rooms
        fields = ('roomId', 'roomName', 'roomDescription', 'rent', 'capacity', 'date_created', 'roomid')

class MonthlyTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyTenant
        fields=('id','formonth', 'foryear', 'tenants', 'monthly_tenants')

# class MonthlyTenantSerializer(serializers.ModelSerializer):
#     monthly_tenants = serializers.SerializerMethodField()
#
#     def get_monthly_tenants(self, object):
#         """getter method to add field retrieved_time"""
#         return None
#     class Meta:
#         model =RoomsAssign
#         fields=('formonth', 'foryear', 'monthly_tenants')

