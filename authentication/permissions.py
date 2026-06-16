from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ["DELETE", "PUT", "PATCH"]:
            return obj == request.user
