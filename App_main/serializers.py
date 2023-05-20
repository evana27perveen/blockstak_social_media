from rest_framework import serializers

from App_auth.models import CustomUser
from .models import Profile, Post, Comment, Connection, Share, Like
from App_auth.serializers import UserSerializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fullName', 'profile_picture', 'bio', 'social_media_accounts']

    def create(self, validated_data):
        get_user = self.context.get('user')
        user = CustomUser.objects.get(id=get_user)
        profile = Profile(
            user=user,
            **validated_data
        )
        profile.save()
        return profile


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'image', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created_at')


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('id', 'post', 'user', 'created_at')

    def create(self, validated_data):
        like = Like.objects.create(
            post=validated_data['post'],
            user=validated_data['user']
        )
        return like


class ShareSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Share
        fields = ('id', 'user', 'post', 'created_at')


class ConnectionSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    connection = UserSerializers()

    class Meta:
        model = Connection
        fields = ['user', 'connection', 'created_at']
