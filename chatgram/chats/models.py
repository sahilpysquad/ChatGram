import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

User = get_user_model()


class Conversation(models.Model):
    id = models.UUIDField(verbose_name=_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("Name"), max_length=128)
    online = models.ManyToManyField(verbose_name=_("Online"), to=User, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f"{self.name} ({self.get_online_count()})"


class Message(models.Model):
    id = models.UUIDField(verbose_name=_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(
        verbose_name=_("Conversation"), to=Conversation, on_delete=models.CASCADE, related_name="messages"
    )
    from_user = models.ForeignKey(
        verbose_name=_("Message By"), to=User, on_delete=models.CASCADE, related_name="message_from_me"
    )
    to_user = models.ForeignKey(
        verbose_name=_("Message To"), to=User, on_delete=models.CASCADE, related_name="message_to_me"
    )
    content = models.CharField(verbose_name=_("Content"), max_length=512)
    timestamp = models.DateTimeField(verbose_name=_("Send AT"), auto_now_add=True)
    read = models.BooleanField(verbose_name=_("Message Read"), default=False)

    def __str__(self):
        return f"From {self.from_user.username} To {self.to_user.username}: {self.content} [{self.timestamp}]"
