from django.shortcuts import render
from django.utils.translation import deactivate
from . models import*
from . serializers import *
import datetime
# Create your views here.

def homepage(request):
    print('homepage')
    example_type = 1
    created_at = datetime.datetime.now()
    description = 'description'
    # ExampleModel.objects.create(example_type=example_type,created_at=created_at,description=description)
    print('ExampleModel', ExampleModel)
    
    # person = Person(first_name='white', last_name='patel')
    # first_name = person.first_name  #returns 'Blake'
    # last_name = person.last_name  #returns 'Eggleston'
    # print('first_name', first_name)
    # print('last_name', last_name)

    all_objects = Person.objects.all()
    # all_objects = Person.objects.create(first_name='black', last_name='patel')
    all_objects = Person.objects.get(first_name='black')
    print('all_objects', all_objects)
    return render(request,'home.html')


from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
 
class ThingMultiplePKViewSet(ViewSet):
    def list(self, request):
        queryset = Person.objects.all()
        serializer =ExampleModelerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

class ThingMultiplePKListCreateAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = ExampleModelerializer
    permission_classes = ()
 
 