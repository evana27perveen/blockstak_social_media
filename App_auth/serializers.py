from django.contrib.auth.models import Group
from django.contrib.auth.tokens import PasswordResetTokenGenerator
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
            username=validated_data['username'],  # we can also write like this: validated_data.get('username')
        )

        user.set_password(validated_data['password'])
        grp_name = self.context.get('group_name')
        user.save()
        group = Group.objects.get_or_create(
            name=grp_name
        )  # group, created = Group.objects.get_or_create(name....)
        group[0].user_set.add(user)
        return user

