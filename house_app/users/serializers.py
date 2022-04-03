from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserInfo
        fields = ('userid', 'firstname', 'lastname', 'birthdate', 'email', 'phone', 'date_created')