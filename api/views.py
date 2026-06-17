from rest_framework.viewsets import ModelViewSet
from django.db import transaction

from api.serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from api.models import Project, Contributor, Issue, Comment
from rest_framework.permissions import IsAuthenticated
from api.permissions import (
    IsProjectAuthorOrContributorReadOnly,
    IsIssueAuthorOrProjectContributorReadOnly,
    IsCommentAuthorOrContributorReadOnly,
    IsProjectAuthorForContributor,
)


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Project.objects.filter(contributors__user=self.request.user)

    @transaction.atomic
    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)

        Contributor.objects.create(user=project.author, project=project)


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorForContributor]

    def get_queryset(self):
        return Contributor.objects.filter(project__contributors__user=self.request.user)


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsIssueAuthorOrProjectContributorReadOnly]

    def get_queryset(self):
        return Issue.objects.filter(project__contributors__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthorOrContributorReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(
            issue__project__contributors__user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
