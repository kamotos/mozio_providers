from rest_framework import serializers
from services_areas.models import ServiceArea
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceArea
        read_only_fields = ('id', 'provider', 'provider_name')
        geo_field = "area"

    def create(self, validated_data):
        validated_data['provider'] = self.context['request'].user
        return super(ServiceAreaSerializer, self).create(validated_data)

    def get_provider_name(self, obj):
        return obj.provider.name
