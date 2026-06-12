from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectAuthorOrContributorReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        contributors = obj.contributors

        if request.method in SAFE_METHODS:
            return contributors.filter(user=request.user).exists()

        return obj.author == request.user


class IsIssueAuthorOrProjectContributorReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        project = obj.project

        if request.method in SAFE_METHODS:
            return project.contributors.filter(user=request.user).exists()

        return obj.author == request.user or project.author == request.user
