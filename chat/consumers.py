from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Message
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

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
        print(text_data.get("type"))
        print(text_data.get("message"))
        new_message = Message()
        new_message.from_who = self.scope.get('user')
        new_message.to_who = User.objects.get(id=self.person_id)
        new_message.message = text_data.get('message')
        new_message.date = 
        new_message.time =
        new_message.has_been_seen = False
        new_message.save()
        
        # print(text_data)
        # self.send("{'type':'arrive', 'status':'arrived'}")

    # def disconnect(self,code):
    #     print("Disconnecting")

    def receiver_func(self, data_come_from_layer):
        print(data_come_from_layer)
