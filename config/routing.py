from django.urls import path

from chatgram.chats.consumers import ChatConsumer, NotificationConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
    # path("<slug>/", ChatConsumer.as_asgi()),
    path("chats/<conversation_name>/", ChatConsumer.as_asgi()),
    path("notifications/", NotificationConsumer.as_asgi()),
]
