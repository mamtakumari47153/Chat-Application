from rest_framework import serializers
from .models import User, Team, Channel, DirectMessageThread, Message
from django.contrib.auth import get_user_model

User = get_user_model()

# ✅ User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_online', 'last_seen']


# ✅ Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )


# ✅ Team Serializer
class TeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    size = serializers.IntegerField(required=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'size', 'created_by', 'created_at']

    def create(self, validated_data):
        request_user = self.context['request'].user
        validated_data.pop('created_by', None)
        team = Team.objects.create(created_by=request_user, **validated_data)
        team.members.add(request_user)
        return team


# ✅ Channel Serializer
class ChannelSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Channel
        fields = ['id', 'name', 'team', 'is_private', 'members', 'created_by', 'created_at']

    def create(self, validated_data):
        request_user = self.context['request'].user
        validated_data.pop('created_by', None)
        members = validated_data.pop('members', [])
        channel = Channel.objects.create(created_by=request_user, **validated_data)
        channel.members.add(*members)
        return channel


# ✅ Direct Message Thread Serializer (for reading/display)
class DirectMessageThreadSerializer(serializers.ModelSerializer):
    user1 = UserSerializer(read_only=True)
    user2 = UserSerializer(read_only=True)

    class Meta:
        model = DirectMessageThread
        fields = ['id', 'user1', 'user2', 'created_at']


# ✅ Direct Message Thread Create Serializer (for creating via other_user_id)
class DirectMessageThreadCreateSerializer(serializers.ModelSerializer):
    other_user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = DirectMessageThread
        fields = ['id', 'user1', 'user2', 'created_at', 'other_user_id']
        read_only_fields = ['id', 'user1', 'user2', 'created_at']

    def create(self, validated_data):
        request_user = self.context['request'].user
        other_user_id = validated_data.pop('other_user_id')
        other_user = User.objects.get(id=other_user_id)

        # Ensure user1 < user2 for uniqueness
        user1, user2 = sorted([request_user, other_user], key=lambda u: u.id)
        thread, created = DirectMessageThread.objects.get_or_create(user1=user1, user2=user2)
        return thread


# ✅ Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    channel = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), required=False, allow_null=True)
    thread = serializers.PrimaryKeyRelatedField(queryset=DirectMessageThread.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp', 'channel', 'thread']

    def create(self, validated_data):
        request = self.context['request']
        return Message.objects.create(sender=request.user, **validated_data)
