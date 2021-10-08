from uuid import SafeUUID
from django.shortcuts import render
from django.utils.translation import deactivate
from . models import*
from . serializers import *
import datetime
# Create your views here.

def homepage(request):
    print('homepage')
    example_type = 2
    created_at = datetime.datetime.now()
    description = 'description2'
    # ExampleModel_obj = ExampleModel.objects.create(example_type=example_type,
    #                           created_at=created_at,description=description)
    ExampleModel_obj= ExampleModel.objects.filter(example_id='52b1f004-ec68-4dce-8cd3-fd352457af87')
    # ExampleModel_obj= ExampleModel.objects.all()
    
    for i in ExampleModel_obj:
        created_at = i.created_at
        example_type = i.example_type
        description = i.description
        i.example_type = 5
        i.save()
        print('created_at', created_at)
        print('example_type', example_type)
        print('description', description)
    print('ExampleModel_obj', ExampleModel_obj)

    # ExampleModel_obj= ExampleModel.objects.get(example_type=example_type)

    return render(request,'home.html')


from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
 


class TestView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        a= 2
        query = ExampleModel.objects.all()
        serializer  = ExampleModelerializer(query, many=True)
        return Response(
            data={
                "Status":status.HTTP_200_OK,
                "Message":f"No Mini Lesson Category Found using ID ({a}).",
                "Results": serializer.data},
            status=status.HTTP_200_OK
        )
    
    def post(self, request, *args, **kwargs):
        serializer  = ExampleModelerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "Status":status.HTTP_200_OK,
                    "Message":"",
                    "Results": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(
            data={
                "Status":status.HTTP_400_BAD_REQUEST,
                "Results":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
 

from rest_framework.decorators import api_view

 
@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': 'products/list/',
        'Detail View': 'products/detail/<str:pk>/',
        'Create': 'products/create/',
        'Create From List': 'products/create_list/',
        'Update': 'products/update/<str:pk>/',
        'Delete': 'products/delete/<str:pk>/',
    }
    return Response(api_urls)