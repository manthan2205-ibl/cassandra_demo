from django.db import models
import datetime

# Create your models here.

import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from django.contrib.auth.models import AbstractBaseUser

class ExampleModel(DjangoCassandraModel):
    example_id   = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at   = columns.DateTime(default=datetime.datetime.now())
    description  = columns.Text(required=False)


class UserTokenModel(DjangoCassandraModel):
    user_token_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    user_id = columns.UUID(required=False) #UserModel
    token = columns.Text(required=False)

    created_at = columns.DateTime(default=datetime.datetime.utcnow())
    created_by = columns.UUID(required=False) #UserModel
    updated_at = columns.DateTime(default=datetime.datetime.utcnow())
    updated_by = columns.UUID(required=False) #UserModel
    deleted_at = columns.DateTime(required=False)
    deleted_by = columns.UUID(required=False) #UserModel
    deleted_record = columns.Boolean(default=False)
   

class UserModel(DjangoCassandraModel, AbstractBaseUser):
    user_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text(required=False)
    email = columns.Text(required=False)
    profile_url = columns.Text(required=False)
    # profile = columns.Blob(required=False) # image binary
    report_to = columns.UUID(required=False) #UserModel
    status = columns.Text(required=False)
    position = columns.Text(required=False)
    is_online = columns.Boolean(default=False)
    deviceToken = columns.Map(key_type=columns.Text, value_type=columns.List(value_type=columns.Text, 
                                            default=list,required=False), default=dict,required=False)
    blocked_by = columns.UUID(required=False) #UserModel

    created_at = columns.DateTime(default=datetime.datetime.utcnow())
    created_by = columns.UUID(required=False) #UserModel
    updated_at = columns.DateTime(default=datetime.datetime.utcnow())
    updated_by = columns.UUID(required=False) #UserModel
    deleted_at = columns.DateTime(required=False)
    deleted_by = columns.UUID(required=False) #UserModel
    deleted_record = columns.Boolean(default=False)
    

class GroupModel(DjangoCassandraModel):
    group_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    admin_id = columns.UUID(required=False) #UserModel
    group_profile = columns.Text(required=False)
    group_name = columns.Text(required=False)
    group_type = columns.Text(required=False)
    is_channel = columns.Boolean(default=False)
    members = columns.List(value_type=columns.UUID, default=list,required=False)
    # read_by = columns.Map(key_type=columns.Text, value_type=columns.Text, default=dict,required=False)
    read_by = columns.List(value_type=columns.Map(key_type=columns.Text, 
                            value_type=columns.Text, default=dict,required=False), 
                        default=list,required=False)
    recent_message = columns.Map(key_type=columns.Text, value_type=columns.Text, default=dict,required=False)
    team_id = columns.UUID(required=False)  #TeamModel
    type = columns.Text(required=False)

    created_at = columns.DateTime(default=datetime.datetime.utcnow())
    created_by = columns.UUID(required=False) #UserModel
    updated_at = columns.DateTime(default=datetime.datetime.utcnow())
    updated_by = columns.UUID(required=False) #UserModel
    deleted_at = columns.DateTime(required=False)
    deleted_by = columns.UUID(required=False) #UserModel
    deleted_record = columns.Boolean(default=False)
    

class MessageModel(DjangoCassandraModel):
    message_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    group_id = columns.UUID(required=False) #GroupModel
    team_id = columns.UUID(required=False) #TeamModel
    file = columns.List(value_type=columns.Text, default=list,required=False)
    gif_url = columns.Text(required=False)
    image = columns.List(value_type=columns.Text, default=list,required=False)
    is_reply = columns.Boolean(default=False)
    message = columns.Text(required=False)
    reply_data = columns.Map(key_type=columns.Text, value_type=columns.Text, default=dict,required=False)
    sender_id = columns.UUID(required=False) #UserModel
    sender_name = columns.Text(required=False)
    # read_by = columns.Map(key_type=columns.Text, value_type=columns.Text, default=dict,required=False)
    read_by = columns.List(value_type=columns.Map(key_type=columns.Text, 
                            value_type=columns.Text, default=dict,required=False), 
                        default=list,required=False)
    is_deleted = columns.Boolean(default=False)
    delete_type = columns.Text(required=False)
    time = columns.DateTime(required=False)
    type = columns.Text(required=False)

    created_at = columns.DateTime(default=datetime.datetime.utcnow())
    created_by = columns.UUID(required=False) #UserModel
    updated_at = columns.DateTime(default=datetime.datetime.utcnow())
    updated_by = columns.UUID(required=False) #UserModel
    deleted_at = columns.DateTime(required=False)
    deleted_by = columns.UUID(required=False) #UserModel
    deleted_record = columns.Boolean(default=False)
    

class BadgeModel(DjangoCassandraModel):
    badge_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    group_id = columns.UUID(required=False) #GroupModel
    user_id = columns.UUID(required=False) #UserModel
    badge = columns.Integer(required=False)

    created_at = columns.DateTime(default=datetime.datetime.utcnow())
    created_by = columns.UUID(required=False) #UserModel
    updated_at = columns.DateTime(default=datetime.datetime.utcnow())
    updated_by = columns.UUID(required=False) #UserModel
    deleted_at = columns.DateTime(required=False)
    deleted_by = columns.UUID(required=False) #UserModel
    deleted_record = columns.Boolean(default=False)
    

class TeamModel(DjangoCassandraModel):
    team_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    admin_id = columns.UUID(required=False) #GroupModel
    is_public = columns.Boolean(default=False)
    members = columns.List(value_type=columns.UUID, default=list,required=False)
    team_name = columns.Text(required=False)
    profile = columns.Text(required=False)
    time = columns.DateTime(required=False)

    created_at = columns.DateTime(default=datetime.datetime.utcnow())
    created_by = columns.UUID(required=False) #UserModel
    updated_at = columns.DateTime(default=datetime.datetime.utcnow())
    updated_by = columns.UUID(required=False) #UserModel
    deleted_at = columns.DateTime(required=False)
    deleted_by = columns.UUID(required=False) #UserModel
    deleted_record = columns.Boolean(default=False)



# extra 
# from cassandra.cqlengine.models import Model
# class Person(Model):
#     id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     first_name  = columns.Text()
#     last_name = columns.Text()