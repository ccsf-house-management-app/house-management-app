from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'id')

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserInfo
        fields = ('userid', 'firstname', 'lastname', 'birthdate', 'email', 'phone', 'date_created')
