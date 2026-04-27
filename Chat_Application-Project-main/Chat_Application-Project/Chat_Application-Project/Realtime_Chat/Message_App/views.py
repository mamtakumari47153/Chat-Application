from rest_framework import generics, permissions
from django.db.models import Q
from django.shortcuts import render
from .models import User, Team, Channel, Message, DirectMessageThread
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    TeamSerializer,
    ChannelSerializer,
    MessageSerializer,
    DirectMessageThreadSerializer,
)


# ✅ Register User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# ✅ List All Users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Create a Team
class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# ✅ List Teams for current user
class TeamListView(generics.ListAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Team.objects.filter(members=self.request.user)


# ✅ Create a Channel
class ChannelCreateView(generics.CreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}


# ✅ List Channels of a Team where user is a member
class ChannelListView(generics.ListAPIView):
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        team_id = self.kwargs.get("team_id")
        return Channel.objects.filter(team_id=team_id, members=self.request.user)


# ✅ Create a Message
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}


# ✅ List Messages
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        channel_id = self.request.query_params.get("channel")
        if channel_id:
            return Message.objects.filter(channel_id=channel_id).order_by('-timestamp')
        return Message.objects.all().order_by('-timestamp')


# ✅ Search Messages
class MessageSearchView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Message.objects.all()
        keyword = self.request.query_params.get('q')
        channel_id = self.request.query_params.get('channel')
        sender_id = self.request.query_params.get('sender')

        if keyword:
            queryset = queryset.filter(content__icontains=keyword)

        if channel_id:
            queryset = queryset.filter(channel_id=channel_id)

        if sender_id:
            queryset = queryset.filter(sender_id=sender_id)

        return queryset.order_by('-timestamp')


# ✅ Create or Get DM Thread
class DirectMessageThreadCreateView(generics.CreateAPIView):
    queryset = DirectMessageThread.objects.all()
    serializer_class = DirectMessageThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}


# ✅ List All DM Threads for current user
class DirectMessageThreadListView(generics.ListAPIView):
    serializer_class = DirectMessageThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return DirectMessageThread.objects.filter(Q(user1=user) | Q(user2=user))




def websocket_test_view(request):
    return render(request, 'websocket_test.html')
