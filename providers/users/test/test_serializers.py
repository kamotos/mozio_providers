from django.test import TestCase
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import eq_, ok_, raises
from rest_framework.exceptions import ValidationError
from .factories import UserFactory
from ..serializers import CreateUserSerializer, UserSerializer


class TestCreateUserSerializer(TestCase):

    def setUp(self):
        self.user_data = model_to_dict(UserFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateUserSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CreateUserSerializer(data=self.user_data)
        ok_(serializer.is_valid())

    def test_serializer_hashes_password(self):
        serializer = CreateUserSerializer(data=self.user_data)
        ok_(serializer.is_valid())

        user = serializer.save()
        ok_(check_password(self.user_data.get('password'), user.password))

    def test_serializer_with_invalid_currency(self):
        pass

    def test_serializer_with_invalid_language(self):
        pass

    @raises(ValidationError)
    def test_serializer_with_non_unique_email(self):
        user = UserFactory()
        self.user_data['email'] = user.email
        serializer = CreateUserSerializer(data=self.user_data)
        serializer.is_valid(True)

    def test_serializer_create_user_with_username_eq_email(self):
        serializer = CreateUserSerializer(data=self.user_data)
        serializer.is_valid()
        created_user = serializer.create(serializer.validated_data)
        ok_(created_user.username, created_user.email)

    def test_serializer_update_user_with_username_eq_email(self):
        instance = UserFactory()
        data = model_to_dict(instance)
        data['email'] = "newemail@gmail.com"

        serializer = UserSerializer(instance=UserFactory, data=data)
        serializer.is_valid()
        updated_user = serializer.update(instance, serializer.validated_data)

        ok_(updated_user.username, updated_user.email)
