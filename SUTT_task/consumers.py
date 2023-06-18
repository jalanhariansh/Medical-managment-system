import json
from channels.generic.websocket import AsyncWebsocketConsumer
from patient_dashboard.models import chats
from asgiref.sync import sync_to_async


class ChatRoomConsumer(AsyncWebsocketConsumer):
    @sync_to_async
    def save_message(self, room_name, messages):
        chat_room = chats.objects.get(room_name=room_name)
        chat_room.message += messages+'\n'
        chat_room.save()
    
    @sync_to_async
    def get_messages(self, room_name):
        chat_obj, created = chats.objects.get_or_create(room_name=room_name)
        if created:
            chat_obj.save()
        return chat_obj.message,created

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        history,created = await self.get_messages(self.room_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        if not created:
            await self.send(text_data=json.dumps({
                'message': history,
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.save_message(self.room_name,message)
        

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message + '\n',
        }))

    pass

class AppsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'apps'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
        }))

    pass