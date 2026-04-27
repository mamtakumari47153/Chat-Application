from django.urls import path
from .views import (
    RegisterView, UserListView,
    TeamCreateView, TeamListView,
    ChannelCreateView, ChannelListView,
    MessageCreateView, MessageListView, MessageSearchView,
    DirectMessageThreadCreateView, DirectMessageThreadListView,
    websocket_test_view,
)

urlpatterns = [
    # 🔐 Auth & Users
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/users/', UserListView.as_view(), name='user-list'),

    # 👥 Teams
    path('api/teams/create/', TeamCreateView.as_view(), name='team-create'),
    path('api/teams/', TeamListView.as_view(), name='team-list'),

    # 📢 Channels
    path('api/channels/create/', ChannelCreateView.as_view(), name='channel-create'),
    path('api/channels/<int:team_id>/', ChannelListView.as_view(), name='channel-list'),

    # 💬 Messages
    path('api/messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('api/messages/', MessageListView.as_view(), name='message-list'),
    path('api/messages/search/', MessageSearchView.as_view(), name='message-search'),

    # 📩 Direct Messages (Threads)
    path('api/dm-threads/create/', DirectMessageThreadCreateView.as_view(), name='dm-thread-create'),
    path('api/dm-threads/', DirectMessageThreadListView.as_view(), name='dm-thread-list'),
    path('websocket-test/', websocket_test_view, name='websocket-test'),

]
