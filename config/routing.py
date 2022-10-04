from django.urls import path

from chatgram.chats.consumers import ChatConsumer

websocket_urlpatterns = [
    path('', ChatConsumer.as_asgi())
]
