from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from .serializers import CreateUserSerializer, UserSerializer, ProviderSerializer
from services_areas.serializers import ServiceAreaSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.exclude(is_staff=True)
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_user_for_permission(self, obj):
        return obj

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny, )
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsOwnerOrAdmin, )
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = ProviderSerializer
        return super(UserViewSet, self).list(request, *args, **kwargs)

    @list_route(permission_classes=(IsAuthenticated, ))
    def me(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ProviderSerializer
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    @detail_route(url_path="services-areas")
    def services_areas(self, request, *args, **kwargs):
        serializer = ServiceAreaSerializer(
            self.get_object().servicearea_set.all(),
            many=True
        )
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = (IsOwnerOrAdmin, )
        return super(UserViewSet, self).destroy(request, *args, **kwargs)
