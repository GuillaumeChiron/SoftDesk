from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import Project, Issue


class IsProjectAuthorOrContributorReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        contributors = obj.contributors

        if request.method in SAFE_METHODS:
            return contributors.filter(user=request.user).exists()

        return obj.author == request.user


class IsIssueAuthorOrProjectContributorReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method != "POST":
            return True

        project_id = request.data.get("project")

        if not project_id:
            return False

        return Project.objects.filter(
            id=project_id,
            contributors__user=request.user,
        ).exists()

    def has_object_permission(self, request, view, obj):
        project = obj.project

        if request.method in SAFE_METHODS:
            return project.contributors.filter(user=request.user).exists()

        return obj.author == request.user or project.author == request.user


class IsCommentAuthorOrProjectAuthor(BasePermission):

    def has_permission(self, request, view):
        if request.method != "POST":
            return True
        
        issue_id = request.data.get("issue")

        if not issue_id:
            return False
        
        return Issue.objects.filter(id=issue_id, project__contributors__user=request.user).exists()

    def has_object_permission(self, request, view, obj):
        project = obj.issue.project

        return obj.author == request.user or project.author == request.user


class IsProjectAuthorForContributor(BasePermission):

    def has_permission(self, request, view):
        if request.method != "POST":
            return True

        project_id = request.data.get("project")

        if not project_id:
            return False

        return Project.objects.filter(id=project_id, author=request.user).exists()

    def has_object_permission(self, request, view, obj):
        project = obj.project

        if request.method in SAFE_METHODS:
            return project.contributors.filter(user=request.user).exists()

        if request.method == "DELETE" and obj.user == project.author:
            return False

        return project.author == request.user
