import json
from django.contrib.gis.geos import GEOSGeometry, Point
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from services_areas.models import ServiceArea
from services_areas.serializers import ServiceAreaSerializer
from users.permissions import IsOwnerOrAdmin


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ServiceAreaSerializer
    get_user_for_permission = lambda view, obj: obj.provider

    def list(self, request, *args, **kwargs):
        lat, lng = request.query_params.get('lat'), request.query_params.get('lng')
        if lat and lng:
            try:
                point = Point(float(lng), float(lat))
            except TypeError:
                raise ValidationError('Invalid lat/lng parameters')
            else:
                self.queryset = self.queryset.filter(area__contains=point)
        return super(ServiceAreaViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsOwnerOrAdmin, )
        return super(ServiceAreaViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = (IsOwnerOrAdmin, )
        return super(ServiceAreaViewSet, self).destroy(request, *args, **kwargs)
