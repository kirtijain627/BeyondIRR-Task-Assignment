from rest_framework import serializers
from .models import Post, Notification


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'state', 'user']

class NotificationSerializer(serializers.ModelSerializer):
    post = serializers.CharField(source='post.title')
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Notification
        fields = ['id', 'post', 'action', 'user']