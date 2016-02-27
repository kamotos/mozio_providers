import json

from django.contrib.gis.geos import GEOSGeometry
import factory

from services_areas.test.fake_geo_data import polygon


class ServiceAreaFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    area = GEOSGeometry(json.dumps(polygon))

    class Meta:
        model = 'services_areas.ServiceArea'
