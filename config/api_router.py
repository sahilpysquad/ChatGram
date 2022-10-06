from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from chatgram.chats.api.views import ConversationViewSet, MessageViewSet
from chatgram.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("conversations", ConversationViewSet)
router.register("messages", MessageViewSet)


app_name = "api"
urlpatterns = router.urls
