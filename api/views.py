from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAuthorOrReadOnly

from api.serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from api.models import Project, Contributor, Issue, Comment


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return Project.objects.all()


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
