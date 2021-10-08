
from rest_framework import serializers
from . models import *
 
from django_cassandra_engine.rest.serializers import DjangoCassandraModelSerializer
 
 
class ExampleModelerializer(DjangoCassandraModelSerializer):
 
    class Meta:
        model = Person
        fields = '__all__'
 