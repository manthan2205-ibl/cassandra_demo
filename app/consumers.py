import json

from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer# The class we're using
from asgiref.sync import sync_to_async
from django.db.models import manager # Implement later

from .models import *


class MessageConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        print('group_id', self.group_id)
        print('admin_id', self.user_id)
        await self.accept()

        self.room_group_name = 'chat_%s' % self.group_id

        # Join room group
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name
        )

        message_data = await self.get_message_data(self.group_id, self.user_id)
        message_data = {"result": "true", "Message": "connected"}
        await self.send_json(message_data)


    async def disconnect(self, event):
        print("disconnected", event)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
    )



    # Receive message from WebSocket
    async def receive_json(self, content):
        print("CONTENT", content)
        if content['command'] == "send":
            message_id = content['message_id']

            print('message_id', message_id)
            
            self.room_name = "room" + str(self.group_id)
            message_data = await self.send_message_data(message_id)

            await self.send_json(message_data)

            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'recieve_group_message',
                    'message': message_id
                }
            )



    @sync_to_async
    def send_message_data(self, message_id):
        try:
            msg = MessageModel.objects.get(message_id=message_id)
        except:
            result = {'result': 'false', 'Message': 'group id does not match', 'internalCode': '004'}
            return result
        msg_dic = {}
        msg_dic['message_id'] = str(msg.message_id)
        msg_dic['gif_url'] = msg.gif_url
        msg_dic['is_reply'] = msg.is_reply
        msg_dic['message'] = msg.message
        msg_dic['sender_id'] = str(msg.sender_id)
        msg_dic['sender_name'] = msg.sender_name
        msg_dic['is_deleted'] = msg.is_deleted
        msg_dic['delete_type'] = msg.delete_type
        msg_dic['type'] = msg.type
        msg_dic['file'] = msg.file
        msg_dic['image'] = msg.image
        msg_dic['reply_data'] = msg.reply_data
        msg_dic['read_by'] = msg.read_by

        result = {'result': 'true', 'Message': msg_dic, 'internalCode': '003'}
    
        return result



    @sync_to_async
    def get_group_data(self, group_id,user_id):
        try:
            GroupModel_obj = GroupModel.objects.get(group_id=group_id)
        except:
            result = {'result': 'false', 'Message': 'group id does not match', 'internalCode': '004'}
            return result
        
        try:
            User_obj = UserModel.objects.get(user_id=user_id)
        except:
            result = {'result': 'false', 'Message': 'admin id does not match', 'internalCode': '005'}
            return result

        GroupModel_obj = GroupModel.objects.filter(admin_id=user_id)
        # print('GroupModel_obj', GroupModel_obj)
        GroupModel_obj_list = []
        for i in GroupModel_obj:
            GroupModel_obj_dic = {}
            GroupModel_obj_dic['admin_id'] = str(i.admin_id)
            GroupModel_obj_dic['group_profile'] = i.group_profile
            GroupModel_obj_dic['group_name'] = i.group_name
            GroupModel_obj_dic['group_type'] = i.group_type
            GroupModel_obj_dic['is_channel'] = i.is_channel
            GroupModel_obj_dic['type'] = i.type
            GroupModel_obj_list.append(GroupModel_obj_dic)

        if GroupModel_obj_list:
            result = {'result': 'true', 'Message': GroupModel_obj_list, 'internalCode': '006'}
        else:
            result = {'result': 'false', 'Message': 'GroupModel_obj_list is empty', 'internalCode': '007'}

        return result

    
    @sync_to_async
    def get_message_data(self, group_id,user_id):
        try:
            GroupModel_obj = GroupModel.objects.get(group_id=group_id)
        except:
            result = {'result': 'false', 'Message': 'group id does not match', 'internalCode': '004'}
            return result
        
        try:
            User_obj = UserModel.objects.get(user_id=user_id)
        except:
            result = {'result': 'false', 'Message': 'admin id does not match', 'internalCode': '005'}
            return result

        MessageModel_obj = MessageModel.objects.filter(sender_id=user_id)
        print('MessageModel_obj', MessageModel_obj)
        message_list = []
        for msg in MessageModel_obj:
            msg_dic = {}
            msg_dic['message_id'] = str(msg.message_id)
            msg_dic['gif_url'] = msg.gif_url
            msg_dic['is_reply'] = msg.is_reply
            msg_dic['message'] = msg.message
            msg_dic['sender_id'] = str(msg.sender_id)
            msg_dic['sender_name'] = msg.sender_name
            msg_dic['is_deleted'] = msg.is_deleted
            msg_dic['delete_type'] = msg.delete_type
            msg_dic['type'] = msg.type
            msg_dic['file'] = msg.file
            msg_dic['image'] = msg.image
            msg_dic['reply_data'] = msg.reply_data
            msg_dic['read_by'] = msg.read_by
            message_list.append(msg_dic)

        if message_list:
            result = {'result': 'true', 'Message': message_list, 'internalCode': '006'}
        else:
            result = {'result': 'false', 'Message': 'message_list is empty', 'internalCode': '007'}

        return result
