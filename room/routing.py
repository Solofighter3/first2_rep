from django.urls import path
from room import consumers

websocket_urlpatterns=[
                path(r'ws/<str:room_name>/',consumers.Chatconsumer.as_asgi())
        ]
