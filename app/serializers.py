from django.http import request
from rest_framework import serializers
from . models import *
from rest_framework.serializers import ModelSerializer, Serializer
 
from django_cassandra_engine.rest.serializers import DjangoCassandraModelSerializer
 
 
class ExampleModelerializer(DjangoCassandraModelSerializer):

    class Meta:
        model = ExampleModel
        fields = ['example_type', 'description']



# Logout
class UserLogoutSerializer(Serializer):

    token_type = serializers.CharField(required=True)
    device_token = serializers.CharField(required=True)

    class Meta:
        fields = ['token_type','device_token']


# otp 
class OTPSerializer(Serializer):

    email = serializers.EmailField(required=True)
    otp = serializers.IntegerField(required=True)
    token_type = serializers.CharField(required=True)
    device_token = serializers.CharField(required=True)

    class Meta:
        fields = ['email', 'otp', 'token_type','device_token']


# login
class UserLoginSerializer(Serializer):

    email = serializers.EmailField(required=True)
    
    class Meta:
        fields = ['email']



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


class ListGroupSerializer(Serializer):

    group_id = serializers.CharField(required=True)
    admin_id = serializers.CharField(required=True)
    group_profile = serializers.CharField(required=True)
    group_name = serializers.CharField(required=True)
    group_type = serializers.CharField(required=True)
    is_channel = serializers.BooleanField(required=True)
    type = serializers.CharField(required=True)
    members = serializers.ListField(required=True)
    read_by = serializers.ListField(required=True)
    recent_message = serializers.JSONField(required=True)
    deleted_record = serializers.SerializerMethodField()

    class Meta:
        fields = ['group_id','admin_id', 'group_profile', 'group_name',  'group_type',
                  'is_channel', 'type', 'members', 'read_by', 'recent_message', 'deleted_record']

    def get_deleted_record(self, obj):
        deleted_record = obj.deleted_record
        return deleted_record


# team 
class CreateTeamSerializer(Serializer):

    admin_id = serializers.CharField(required=True)
    is_public = serializers.BooleanField(required=True)
    team_name = serializers.CharField(required=True)
    profile = serializers.CharField(required=True)

    class Meta:
        fields = ['admin_id', 'is_public', 'team_name',  'profile']
                 

class ListTeamSerializer(Serializer):

    team_id = serializers.CharField(required=True)
    admin_id = serializers.CharField(required=True)
    is_public = serializers.BooleanField(required=True)
    team_name = serializers.CharField(required=True)
    profile = serializers.CharField(required=True)
    members = serializers.ListField(required=True)
    deleted_record = serializers.BooleanField(required=True)

    class Meta:
        fields = ['team_id', 'admin_id', 'is_public', 'team_name',  
                    'profile', 'members', 'deleted_record']

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


class ListMessageSerializer(Serializer):

    message_id = serializers.CharField(required=False)
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
    file = serializers.ListField(required=True)

    class Meta:
        fields = ['message_id', 'group_id', 'team_id', 'gif_url', 'is_reply', 'message',  'sender_id',
                  'sender_name', 'is_deleted', 'delete_type', 'type']