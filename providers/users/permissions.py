from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object or admins to edit it.
    """
    def get_user_for_permission(self, obj):
        return obj.user

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        get_user_for_permission = getattr(
            view, 'get_user_for_permission', self.get_user_for_permission
        )
        return get_user_for_permission(obj) == request.user or request.user.is_staff
