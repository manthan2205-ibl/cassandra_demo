from django.db import models
import datetime

# Create your models here.

import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class ExampleModel(DjangoCassandraModel):
    example_id   = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at   = columns.DateTime(default=datetime.datetime.now())
    description  = columns.Text(required=False)




# extra 
# from cassandra.cqlengine.models import Model
# class Person(Model):
#     id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     first_name  = columns.Text()
#     last_name = columns.Text()