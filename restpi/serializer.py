
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetails, EmpolyeeDetails


class EmpolyeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpolyeeDetails
        fields = ['orgnization_name', 'emoplye_id']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # id = EmpolyeeDetailsSerializer(many=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
