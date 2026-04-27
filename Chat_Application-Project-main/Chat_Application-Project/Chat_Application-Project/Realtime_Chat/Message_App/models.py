from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# ✅ Custom User model
class User(AbstractUser):
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


# ✅ Team model
class Team(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams_created')
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Size: {self.size})"


# ✅ Channel model
class Channel(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='channels')
    is_private = models.BooleanField(default=False)
    members = models.ManyToManyField(User, related_name='channels')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channels_created', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} in {self.team.name}"


# ✅ Direct Message Thread model
class DirectMessageThread(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dm_threads_1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dm_threads_2')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1.username} ↔ {self.user2.username}"


# ✅ Message model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE, related_name='messages')
    thread = models.ForeignKey(DirectMessageThread, null=True, blank=True, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        if self.channel:
            target = f"#{self.channel.name}"
        elif self.thread:
            target = f"{self.thread}"
        else:
            target = "Unknown"
        return f"[{self.timestamp.strftime('%H:%M')}] {self.sender.username} → {target}: {self.content[:30]}"
