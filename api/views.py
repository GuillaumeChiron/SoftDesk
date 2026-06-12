from rest_framework.viewsets import ModelViewSet
from django.db import transaction

from api.serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from api.models import Project, Contributor, Issue, Comment


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    @transaction.atomic
    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)

        Contributor.objects.create(user=project.author, project=project)


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
