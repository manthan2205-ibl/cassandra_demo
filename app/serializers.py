from django.http import request
from rest_framework import serializers
from . models import *
from rest_framework.serializers import ModelSerializer, Serializer
 
from django_cassandra_engine.rest.serializers import DjangoCassandraModelSerializer
 
 
class ExampleModelerializer(DjangoCassandraModelSerializer):

    class Meta:
        model = ExampleModel
        fields = ['example_type', 'description']



# Login
class UserLogoutSerializer(Serializer):

    token_type = serializers.CharField(required=True)
    device_token = serializers.CharField(required=True)

    class Meta:
        fields = ['token_type','device_token']


# logout
class UserLoginSerializer(Serializer):

    email = serializers.EmailField(required=True)
    token_type = serializers.CharField(required=True)
    device_token = serializers.CharField(required=True)

    class Meta:
        fields = ['email', 'token_type','device_token']



class UserListSerializer(Serializer):

    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    profile_url = serializers.CharField(required=True)
    profile_url = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    position = serializers.CharField(required=True)
    is_online = serializers.BooleanField(required=True)
    deleted_record = serializers.BooleanField(required=True)
    deviceToken = serializers.JSONField(required=True)

    class Meta:
        fields = ['name', 'email', 'profile_url',
                  'status', 'position','is_online','deleted_record','deviceToken']


# Register
class UserRegisterSerializer(Serializer):

    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    profile_url = serializers.CharField(required=True)
    profile_url = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    position = serializers.CharField(required=True)
    # profile = serializers.FileField(required=True)
    # is_online = serializers.BooleanField(required=True)


    class Meta:
        fields = ['name', 'email', 'profile_url',
                  'status', 'position']


# group 
class CreateGroupSerializer(Serializer):

    admin_id = serializers.CharField(required=True)
    group_profile = serializers.CharField(required=True)
    group_name = serializers.CharField(required=True)
    group_type = serializers.CharField(required=True)
    is_channel = serializers.BooleanField(required=True)
    type = serializers.CharField(required=True)

    class Meta:
        fields = ['admin_id', 'group_profile', 'group_name',  'group_type',
                  'is_channel', 'type']


# team 
class CreateTeamSerializer(Serializer):

    admin_id = serializers.CharField(required=True)
    is_public = serializers.BooleanField(required=True)
    team_name = serializers.CharField(required=True)
    profile = serializers.CharField(required=True)

    class Meta:
        fields = ['admin_id', 'is_public', 'team_name',  'profile']
                 

# message 
class MessageSerializer(Serializer):

    group_id = serializers.CharField(required=False)
    team_id = serializers.CharField(required=False)

    gif_url = serializers.CharField(required=True)
    is_reply = serializers.BooleanField(required=True)
    message = serializers.CharField(required=True)
    sender_id = serializers.CharField(required=True)
    sender_name = serializers.CharField(required=True)
    is_deleted = serializers.BooleanField(required=True)
    delete_type = serializers.CharField(required=True)
    type = serializers.CharField(required=True)

    class Meta:
        fields = ['group_id', 'team_id', 'gif_url', 'is_reply', 'message',  'sender_id',
                  'sender_name', 'is_deleted', 'delete_type', 'type']