from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'phone_number', 'language',  'currency',
            'auth_token'
        )

    def update(self, instance, validated_data):
        """
        Update username when updating email
        """
        email = validated_data.get('email', None)
        if email is not None:
            validated_data['username'] = email
        return super(UserSerializer, self).update(instance, validated_data)


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Shows only general information about a provider.
    """
    class Meta:
        model = User
        fields = (
            'id', 'name', 'phone_number', 'language',  'currency', 'url'
        )


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email', 'name', 'phone_number', 'password', 'language',
            'currency', 'auth_token'
        )
        read_only_fields = ('auth_token', )
        write_only_fields = ('password',)
        EXISTING_EMAIL = 'duplicate_email'
        errors_messages = {
            EXISTING_EMAIL: _("This email address is already used")
        }
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(Q(username=value) | Q(email=value)).exists():
            msg = self.Meta.errors_messages[self.Meta.EXISTING_EMAIL]
            raise serializers.ValidationError(msg)
        return value

    def create(self, validated_data):
        """
        - username is email
        - call create_user on user object.
          Without this the password will be stored in plain text.

        :type validated_data: dict
        :rtype: users.models.User
        """
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        return user
