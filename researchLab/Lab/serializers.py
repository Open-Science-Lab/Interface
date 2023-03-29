from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models
from django.db.models import fields

from .models import operation , stream ,operationV2, experiment


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# User Register Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user



class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        user=authenticate(**data)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials Passed .")


# operations serializer

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model=operation
        fields='__all__'


class OperationV2Serializer(serializers.ModelSerializer):
    class Meta:
        model=operationV2
        fields='__all__'





# stream serializer

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model=stream
        fields='__all__'


# experiment serializer

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model=experiment
        fields='__all__'