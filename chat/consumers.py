# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = 'chat_%s' % self.room_name
        # print('chat_%s' % self.room_name)
        # Join room group
        print("self.scope['url_route']['kwargs']",self.scope['url_route']['kwargs'])
        id1 = self.scope['url_route']['kwargs']['id1']
        id2 = self.scope['url_route']['kwargs']['id2']
        if id1<id2:
            id=id2
            id2=id1
            id1=id
        room_name=str(id1)+str(id2)
        print("room_name",room_name)
        self.room_name = room_name
        self.room_group_name = 'chat_%s' % self.room_name


        """
        # 打印调试信息
        print("self.room_group_name",self.room_group_name)
        print(self.scope['url_route']['kwargs'])
        print("channel_name",self.channel_name)
        """

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))