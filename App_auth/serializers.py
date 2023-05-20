from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from App_auth.models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],  
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

