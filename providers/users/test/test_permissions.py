from django.test import TestCase, RequestFactory
from nose.tools import eq_
from services_areas.test.factories import ServiceAreaFactory

from users.permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from users.test.factories import UserFactory


class TestIsOwnerOrReadOnly(TestCase):
    def test_only_authenticated_user_has_permission(self):
        request = RequestFactory()
        user = UserFactory()

        request.user = user
        request.method = 'POST'

        eq_(IsOwnerOrReadOnly().has_object_permission(request, None, user), True)


class TestIsOwnerOrAdmin(TestCase):
    def test_only_authenticated_user_has_permission(self):
        request = RequestFactory()
        user = UserFactory()

        obj = ServiceAreaFactory(provider=user)
        request.user = user
        request.method = 'POST'

        permission = IsOwnerOrAdmin()
        permission.get_user_for_permission = lambda obj: obj.provider
        eq_(permission.has_object_permission(request, None, obj), True)
