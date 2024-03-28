from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        
        #self.send("{'type':'accept', 'status':'accepted'}")
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
        
        #async_to_sync(self.channel_layer.group_add)('test', self.channel_name)
        
        
    def receive(self, text_data):
        
        text_data = json.loads(text_data)
        print(text_data.get('type'))
        print(text_data.get('message'))
        # print(text_data)
        # self.send("{'type':'arrive', 'status':'arrived'}")

        
    
    # def disconnect(self,code):
    #     print("Disconnecting")
        
    
    # def receiver_func(self,data_come_from_layer):
    #     pass