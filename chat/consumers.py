from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Message, UserChannel
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        try:
            user_channels = UserChannel.objects.get(user=self.scope.get("user"))
            user_channels.channel_name = self.channel_name
            user_channels.save()

        except:
            user_channels = UserChannel()
            user_channels.user = self.scope.get("user")
            user_channels.channel_name = self.channel_name
            user_channels.save()

        self.person_id = self.scope.get("url_route").get("kwargs").get("id")
        # self.send("{'type':'accept', 'status':'accepted'}")
        # print(self.scope.get('user'))
        # print(self.scope.get('session'))
        # print(self.scope.get('session').get('me_from_user'))
        # async_to_sync(self.channel_layer.group_add)('test', self.channel_name)
        # print(self.channel_layer.groups)

        # dta = {
        #     'type': 'receiver_func',
        # }

        # async_to_sync(self.channel_layer.send)(self.channel_name, dta)
        # async_to_sync(self.channel_layer.group_send)(self.channel_name, dta)

        # async_to_sync(self.channel_layer.group_add)('test', self.channel_name)

    def receive(self, text_data):

        text_data = json.loads(text_data)
        # print(text_data.get("type"))
        # print(text_data.get("message"))
        new_message = Message()
        new_message.from_who = self.scope.get('user')
        new_message.to_who = User.objects.get(id=self.person_id)
        new_message.message = text_data.get('message')
        new_message.date = '10-03-2024'
        new_message.time = '21:00'
        new_message.has_been_seen = False
        new_message.save()

        data = {
            "type": "receiver_function",
            "type_of_data": "new_message",
            "data": text_data.get("message"),
        }
        async_to_sync(self.channel_layer.send)("name_channel", data)

        # print(text_data)
        # self.send("{'type':'arrive', 'status':'arrived'}")

    # def disconnect(self,code):
    #     print("Disconnecting")

    def receiver_function(self, data_come_from_layer):
        print(data_come_from_layer)
