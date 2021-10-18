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
    ExampleModel_obj= ExampleModel.objects.filter(example_type=example_type)
    # ExampleModel_obj= ExampleModel.objects.all()
    
    for i in ExampleModel_obj:
        created_at = i.created_at
        example_type = i.example_type
        description = i.description
        # i.description = 'description2'
        # i.save()
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
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, DestroyAPIView, \
                                    ListCreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
import json
from . consumers import MessageConsumer


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

    def put(self, request, *args, **kwargs):
        # query = ExampleModel.objects.get(example_id='52b1f004-ec68-4dce-8cd3-fd352457af87')
        # query.delete()
        query = ExampleModel.objects.get(example_type=4)
        serializer  = ExampleModelerializer(query, data=request.data)

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
 
 

class UserRegisterView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer


    def get(self, request, *args, **kwargs):
        # query = UserModel.objects.filter(user_id='5da73767-1cff-4214-a441-eb7fc1dd8128')
        query = UserModel.objects.all()
        user_list = []
        for user in query:
            user_dic = {}
            user_dic['name'] = user.name
            user_dic['email'] = user.email
            user_dic['profile_url'] = user.profile_url
            user_dic['status'] = user.status
            user_dic['is_online'] = user.is_online
            user_dic['position'] = user.position
            user_dic['deviceToken'] = user.deviceToken
            user_list.append(user_dic)
        
        return Response(
            data={
                "Status":status.HTTP_200_OK,
                "Message":"User list",
                "Results": user_list},
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        
        serializer = UserRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"Status": status.HTTP_400_BAD_REQUEST,
                                  "Message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        # try:
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        profile_url = serializer.validated_data['profile_url']
        statuss = serializer.validated_data['status']
        is_online = serializer.validated_data['is_online']
        position = serializer.validated_data['position']

        data=request.data
        deviceToken = data['deviceToken']
        
        deviceToken = json.loads(deviceToken)
        print('deviceToken', deviceToken)
        print(type(deviceToken))

        # deviceToken = {"mobile":["token","token"], "desktop":["token","token"],"web":["token","token"]}

        UserModel.objects.create(name=name, email=email,profile_url=profile_url,
                        status=statuss, position=position, is_online=is_online,deviceToken=deviceToken)
           
        return Response(data={"Status": status.HTTP_201_CREATED,
                                "Message": "User Registered",
                                "Results": serializer.data},
                        status=status.HTTP_201_CREATED)
      


class UserUpdateView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer


    def put(self, request, *args, **kwargs):

        id = self.kwargs.get('id')
        print('id', id)
        UserModel_obj = UserModel.objects.get(user_id=id)
        print('UserModel_obj', UserModel_obj)
        
        serializer = UserRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"Status": status.HTTP_400_BAD_REQUEST,
                                  "Message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        # try:
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        profile_url = serializer.validated_data['profile_url']
        profile = serializer.validated_data['profile']
        statuss = serializer.validated_data['status']
        is_online = serializer.validated_data['is_online']
        position = serializer.validated_data['position']

        data=request.data
        deviceToken = data['deviceToken']
        
        deviceToken = json.loads(deviceToken)
        print('deviceToken', deviceToken)
        print(type(deviceToken))

        # profile = data['profile'].read()
        # print('profile', profile)


        # deviceToken = {"mobile":["token","token"], "desktop":["token","token"],"web":["token","token"]}

        UserModel.objects.filter(user_id=id).update(name=name, email=email,profile_url=profile_url,
                        status=statuss, position=position, is_online=is_online,deviceToken=deviceToken)
           
        # serializer.save()
        return Response(data={"Status": status.HTTP_200_OK,
                                "Message": "User update",
                                "Results": serializer.data},
                        status=status.HTTP_200_OK)
      


    def delete(self, request, *args, **kwargs):

        id = self.kwargs.get('id')
        print('id', id)
        UserModel_obj = UserModel.objects.get(user_id=id)
        print('UserModel_obj', UserModel_obj)
        UserModel_obj.delete()
        
        return Response(data={"Status": status.HTTP_200_OK,
                                "Message": "User deleted"},
                        status=status.HTTP_200_OK)




class CreateGroupView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = GroupModel.objects.all()
    serializer_class = CreateGroupSerializer


    def get(self, request, *args, **kwargs):
        # query = UserModel.objects.filter(user_id='5da73767-1cff-4214-a441-eb7fc1dd8128')
        query = GroupModel.objects.all()
        group_list = []

        for grp in query:
            grp_dic = {}
            grp_dic['group_id'] = grp.group_id
            grp_dic['admin_id'] = grp.admin_id
            grp_dic['group_profile'] = grp.group_profile
            grp_dic['group_name'] = grp.group_name
            grp_dic['group_type'] = grp.group_type
            grp_dic['is_channel'] = grp.is_channel
            grp_dic['type'] = grp.type
            grp_dic['members'] = grp.members
            grp_dic['read_by'] = grp.read_by
            grp_dic['recent_message'] = grp.recent_message
            group_list.append(grp_dic)
        
        return Response(
            data={
                "Status":status.HTTP_200_OK,
                "Message":f"group list",
                "Results": group_list},
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        
        serializer = CreateGroupSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"Status": status.HTTP_400_BAD_REQUEST,
                                  "Message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        # try:
        admin_id = serializer.validated_data['admin_id']
        group_profile = serializer.validated_data['group_profile']
        group_name = serializer.validated_data['group_name']
        group_type = serializer.validated_data['group_type']
        is_channel = serializer.validated_data['is_channel']
        type1 = serializer.validated_data['type']

        admin_id = uuid.UUID(admin_id)

        members =  [admin_id, admin_id, admin_id]
        read_by = [{"read_at": "timestamp", "user_id": str(admin_id)},{"read_at": "timestamp", "user_id": str(admin_id)}]
        recent_message = {"message": "message", 
                        "messageTime": "timestamp", 
                        "senderId": str(admin_id), 
                        "senderName": "name"}

        GroupModel.objects.create(admin_id=admin_id, group_profile=group_profile,group_name=group_name,
                        group_type=group_type, is_channel=is_channel, type=type1,
                        members=members,read_by=read_by, recent_message=recent_message)
           
        return Response(data={"Status": status.HTTP_201_CREATED,
                                "Message": "Group created",
                                "Results": serializer.data},
                        status=status.HTTP_201_CREATED)
      


class UpdateGroupView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = GroupModel.objects.all()
    serializer_class = CreateGroupSerializer

    def put(self, request, *args, **kwargs):

        id = self.kwargs.get('id')
        print('id', id)
        GroupModel_obj = GroupModel.objects.get(group_id=id)
        print('GroupModel_obj', GroupModel_obj)
        
        
        serializer = CreateGroupSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"Status": status.HTTP_400_BAD_REQUEST,
                                  "Message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        # try:
        admin_id = serializer.validated_data['admin_id']
        group_profile = serializer.validated_data['group_profile']
        group_name = serializer.validated_data['group_name']
        group_type = serializer.validated_data['group_type']
        is_channel = serializer.validated_data['is_channel']
        type1 = serializer.validated_data['type']

        admin_id = uuid.UUID(admin_id)

        members =  [admin_id, admin_id, admin_id]
        read_by = [{"read_at": "timestamp", "user_id": str(admin_id)},{"read_at": "timestamp", "user_id": str(admin_id)}]
        recent_message = {"message": "message", 
                        "messageTime": "timestamp", 
                        "senderId": str(admin_id), 
                        "senderName": "name"}

        GroupModel.objects.filter(group_id=id).update(admin_id=admin_id, group_profile=group_profile,group_name=group_name,
                        group_type=group_type, is_channel=is_channel, type=type1,
                        members=members,read_by=read_by, recent_message=recent_message)
           
        return Response(data={"Status": status.HTTP_200_OK,
                                "Message": "Group updated",
                                "Results": serializer.data},
                        status=status.HTTP_200_OK)
      
    
    def delete(self, request, *args, **kwargs):

        id = self.kwargs.get('id')
        print('id', id)
        GroupModel_obj = GroupModel.objects.get(group_id=id)
        print('GroupModel_obj', GroupModel_obj)
        GroupModel_obj.delete()
        
        return Response(data={"Status": status.HTTP_200_OK,
                                "Message": "Group deleted"},
                        status=status.HTTP_200_OK)



class CreateMessageView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


    def get(self, request, *args, **kwargs):
        # query = UserModel.objects.filter(user_id='5da73767-1cff-4214-a441-eb7fc1dd8128')
        query = MessageModel.objects.all()
        message_list = []
        for msg in query:
            msg_dic = {}
            msg_dic['message_id'] = msg.message_id
            msg_dic['gif_url'] = msg.gif_url
            msg_dic['is_reply'] = msg.is_reply
            msg_dic['message'] = msg.message
            msg_dic['sender_id'] = msg.sender_id
            msg_dic['sender_name'] = msg.sender_name
            msg_dic['is_deleted'] = msg.is_deleted
            msg_dic['delete_type'] = msg.delete_type
            msg_dic['type'] = msg.type
            msg_dic['file'] = msg.file
            msg_dic['image'] = msg.image
            msg_dic['reply_data'] = msg.reply_data
            msg_dic['read_by'] = msg.read_by
            message_list.append(msg_dic)
        
        return Response(
            data={
                "Status":status.HTTP_200_OK,
                "Message":f"message list",
                "Results": message_list},
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        
        serializer = MessageSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"Status": status.HTTP_400_BAD_REQUEST,
                                  "Message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        # try:
        gif_url = serializer.validated_data['gif_url']
        is_reply = serializer.validated_data['is_reply']
        message = serializer.validated_data['message']
        sender_id = serializer.validated_data['sender_id']
        sender_name = serializer.validated_data['sender_name']
        is_deleted = serializer.validated_data['is_deleted']
        delete_type = serializer.validated_data['delete_type']
        type1 = serializer.validated_data['type']

        sender_id = uuid.UUID(sender_id)

        file = ["fileUrl","fileUrl","fileUrl"]
        image = ["imageUrl","imageUrl","imageUrl"]		
        reply_data  = {"parentId":"userId", "parentMessage": "message", 
                        "parentMessageId": "messageId", "time": "timestamp"}	
        
        read_by = [{"read_at": "timestamp", "user_id": str(sender_id)},
                    {"read_at": "timestamp", "user_id": str(sender_id)}]

        # MessageModel.objects.create(gif_url=gif_url, is_reply=is_reply, message=message,
        #                 sender_id=sender_id, sender_name=sender_name, is_deleted=is_deleted,
        #                 delete_type=delete_type, type=type1, file=file, image=image,
        #                 reply_data=reply_data, read_by=read_by)

        content = {"command":"send",
                        "message":"d9c194b6-ebfe-42b6-86c3-957edaefd37c"}

        # from websocket import create_connection
        # ws = create_connection("ws://127.0.0.1:8010/ws/7dcdbe64-0f2f-4a7c-8fdd-8d7ee35bfe99/7dcdbe64-0f2f-4a7c-8fdd-8d7ee35bfe99/")
        # ws.send(json.dumps(content))
        # result =  ws.recv()
        # print (result)
        # ws.close()


        # MessageConsumer_class = MessageConsumer('7dcdbe64-0f2f-4a7c-8fdd-8d7ee35bfe99', '7dcdbe64-0f2f-4a7c-8fdd-8d7ee35bfe99')
        # print('MessageConsumer_class', MessageConsumer_class)
        # a = MessageConsumer_class.receive_json(content)
        # print('a', a)

           
        return Response(data={"Status": status.HTTP_201_CREATED,
                                "Message": "Message created",
                                "Results": serializer.data},
                        status=status.HTTP_201_CREATED)
      


class UpdateMessageView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer

    def put(self, request, *args, **kwargs):

        id = self.kwargs.get('id')
        print('id', id)
        MessageModel_obj = MessageModel.objects.get(message_id=id)
        print('MessageModel_obj', MessageModel_obj)
        
        
        serializer = MessageSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={"Status": status.HTTP_400_BAD_REQUEST,
                                  "Message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        # try:
        gif_url = serializer.validated_data['gif_url']
        is_reply = serializer.validated_data['is_reply']
        message = serializer.validated_data['message']
        sender_id = serializer.validated_data['sender_id']
        sender_name = serializer.validated_data['sender_name']
        is_deleted = serializer.validated_data['is_deleted']
        delete_type = serializer.validated_data['delete_type']
        type1 = serializer.validated_data['type']

        sender_id = uuid.UUID(sender_id)

        file = ["fileUrl","fileUrl","fileUrl"]
        image = ["imageUrl","imageUrl","imageUrl"]		
        reply_data  = {"parentId":"userId", "parentMessage": "message", 
                        "parentMessageId": "messageId", "time": "timestamp"}	
        
        read_by = [{"read_at": "timestamp", "user_id": str(sender_id)},
                    {"read_at": "timestamp", "user_id": str(sender_id)}]

        MessageModel.objects.filter(message_id=id).update(gif_url=gif_url, is_reply=is_reply, message=message,
                        sender_id=sender_id, sender_name=sender_name, is_deleted=is_deleted,
                        delete_type=delete_type, type=type1, file=file, image=image,
                        reply_data=reply_data, read_by=read_by)
           
        return Response(data={"Status": status.HTTP_200_OK,
                                "Message": "Message updated",
                                "Results": serializer.data},
                        status=status.HTTP_200_OK)
      
    
    def delete(self, request, *args, **kwargs):

        id = self.kwargs.get('id')
        print('id', id)
        MessageModel_obj = MessageModel.objects.get(message_id=id)
        print('MessageModel_obj', MessageModel_obj)
        MessageModel_obj.delete()
        
        return Response(data={"Status": status.HTTP_200_OK,
                                "Message": "Message deleted"},
                        status=status.HTTP_200_OK)




# from rest_framework.decorators import api_view

 
# @api_view(['GET'])
# def overview(request):
#     api_urls = {
#         'List': 'products/list/',
#         'Detail View': 'products/detail/<str:pk>/',
#         'Create': 'products/create/',
#         'Create From List': 'products/create_list/',
#         'Update': 'products/update/<str:pk>/',
#         'Delete': 'products/delete/<str:pk>/',
#     }
#     return Response(api_urls)