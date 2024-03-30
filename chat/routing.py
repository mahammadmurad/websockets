from django.urls import path
from . import consumers

ASGI_urlpatterns = [
    path("websocket/<int:pk>", consumers.ChatConsumer.as_asgi()),
]
