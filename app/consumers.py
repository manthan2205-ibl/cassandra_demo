import json

from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer# The class we're using
from asgiref.sync import sync_to_async
from django.db.models import manager # Implement later

from .models import *


class MessageConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.admin_id = self.scope['url_route']['kwargs']['admin_id']
        print('group_id', self.group_id)
        print('admin_id', self.admin_id)
        await self.accept()

        self.room_group_name = 'chat_%s' % self.group_id

        # Join room group
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name
        )

        message_data = await self.get_message_data(self.group_id, self.admin_id)
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
            message = content['message']

            print('message', message)
            
            self.room_name = "room" + str(self.group_id)
            # message_data = await self.send_message_data(self.room_id, self.user_id, message)

            # await self.send_json(message_data)

            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'recieve_group_message',
                    'message': message
                }
            )



    # @sync_to_async
    # def send_message_data(self, room_id, user_id, message):
    #     try:
    #         Room_obj = Room.objects.get(id=room_id,is_delete=0)
    #     except:
    #         result = {'result': 'false', 'Message': 'room id does not match', 'internalCode': '001'}
    #         return result
    #     try:
    #         User_obj = Chat_User.objects.get(id=user_id,is_delete=0)
    #     except:
    #         result = {'result': 'false', 'Message': 'user id does not match', 'internalCode': '002'}
    #         return result

    #     Participants_obj = Participants.objects.get(room=Room_obj)
    #     users = Participants_obj.users.all()
    #     if User_obj in users:
    #         Messages_obj = Messages.objects.create(room=Room_obj,user=User_obj,message=message)
    #         Messages_obj_dic = {}
    #         Messages_obj_dic['message_id'] = Messages_obj.id
    #         Messages_obj_dic['room_name'] = Messages_obj.room.room_name
    #         Messages_obj_dic['username'] = Messages_obj.user.username
    #         Messages_obj_dic['message'] = ''
    #         Messages_obj_dic['file'] = ''
    #         if Messages_obj.file:
    #             Messages_obj_dic['file'] = Messages_obj.file.url
    #         if Messages_obj.message:
    #             Messages_obj_dic['message'] = Messages_obj.message
    #         result = {'result': 'true', 'Message': Messages_obj_dic, 'internalCode': '003'}
    #     else:
    #         result = {'result': 'false', 'Message': 'user id does not in group', 'internalCode': '005'}
    #     return result



    @sync_to_async
    def get_message_data(self, group_id,admin_id):
        try:
            GroupModel_obj = GroupModel.objects.get(group_id=group_id)
        except:
            result = {'result': 'false', 'Message': 'group id does not match', 'internalCode': '004'}
            return result
        
        try:
            User_obj = UserModel.objects.get(user_id=admin_id)
        except:
            result = {'result': 'false', 'Message': 'admin id does not match', 'internalCode': '005'}
            return result

        GroupModel_obj = GroupModel.objects.filter(admin_id=admin_id)
        print('GroupModel_obj', GroupModel_obj)
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

            result = {'result': 'true', 'Message': GroupModel_obj_list, 'internalCode': '006'}
        # else:
        #     result = {'result': 'false', 'Message': 'user id does not in group', 'internalCode': '007'}

        return result
