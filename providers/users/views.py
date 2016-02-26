from rest_framework import decorators, viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from .serializers import CreateUserSerializer, UserSerializer, ProviderSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.exclude(is_staff=True)
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )

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

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = (IsOwnerOrAdmin, )
        return super(UserViewSet, self).destroy(request, *args, **kwargs)
