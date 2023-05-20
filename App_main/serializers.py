from rest_framework import serializers

from App_auth.models import CustomUser
from .models import Profile, Post, Comment, Connection
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
    user = UserSerializers()
    likes = UserSerializers(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    shared_by = UserSerializers(many=True, read_only=True)

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        return CommentSerializer(comments, many=True).data

    class Meta:
        model = Post
        fields = ['user', 'text', 'image', 'created_at', 'likes', 'comments', 'shared_by']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Comment
        fields = ['user', 'text', 'created_at']


class ConnectionSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    connection = UserSerializers()

    class Meta:
        model = Connection
        fields = ['user', 'connection', 'created_at']
