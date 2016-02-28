from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from services_areas.serializers import ServiceAreaSerializer

from services_areas.test.factories import ServiceAreaFactory


class TestCreateUserSerializer(TestCase):

    def setUp(self):
        self.service_area_data = model_to_dict(ServiceAreaFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = ServiceAreaSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ServiceAreaSerializer(data=self.service_area_data)
        ok_(serializer.is_valid(True))

    def test_provider_owns_created_service_area(self):
        pass
