from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from faker import Faker
from ..models import User
from .factories import UserFactory

fake = Faker()


class TestUserAPI(APITestCase):
    """
    Tests the /users endpoint.
    """

    def setUp(self):
        self.url = reverse('user-list')
        self.user_data = model_to_dict(UserFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, 400)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.user_data)
        eq_(response.status_code, 201)

        user = User.objects.get(pk=response.data.get('id'))
        eq_(user.username, self.user_data.get('email'))
        (check_password(self.user_data.get('password'), user.password))


class TestUserDetailAPI(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user2 = UserFactory()
        self.admin = UserFactory(is_staff=True)
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.user.auth_token))

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        eq_(response.status_code, 200)

    def test_put_request_updates_a_user(self):
        company = fake.company()
        payload = {
            'name': company,
            'phone_number': '+1-212-545'
        }
        response = self.client.put(self.url, payload)
        eq_(response.status_code, 200)

        user = User.objects.get(pk=self.user.id)
        eq_(user.name, company)

    def _test_provider_deletion_permission(self, auth_token, expected_status_code):
        """
        :type auth_token: string
        :type expected_status_code: int
        """
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(auth_token)
        )
        response = self.client.delete(self.url)
        eq_(response.status_code, expected_status_code)

    def test_provider_can_delete_himself(self):
        self._test_provider_deletion_permission(self.user.auth_token, 204)

    def test_admin_can_delete_a_provider(self):
        self._test_provider_deletion_permission(self.admin.auth_token, 204)

    def test_provider_can_not_delete_another_provider(self):
        self._test_provider_deletion_permission(self.user2.auth_token, 403)

    def test_get_services_areas_returns_services_specific_to_user(self):
        response = self.client.get(reverse('user-services-areas', kwargs={'pk': self.user.pk}))

        eq_(response.status_code, 200)
        features = response.json()['features']
        eq_(self.user.servicearea_set.count(), len(features))
        eq_(
            set(map(str, self.user.servicearea_set.values_list('id', flat=True))),
            set(map(lambda o: o['id'], features))
        )

    def test_get_me_returns_current_user(self):
        response = self.client.get(reverse('user-me'))

        eq_(response.status_code, 200)
        eq_(response.json()['id'], str(self.user.id))

    def test_get_providers_list_not_showing_auth_token(self):
        response = self.client.get(reverse('user-list'))
        eq_(response.status_code, 200)
        ok_('auth_token' not in response.json()['results'][0])
