from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    CharField,
    StringRelatedField,
)

from api.models import Project, Contributor, Issue, Comment
from authentication.serializers import UserSerializer


class ContributorListSerializer(ModelSerializer):

    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = Contributor
        fields = ["user", "project", "created_time"]


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ["user", "project", "created_time"]


class ProjectSerializer(ModelSerializer):

    contributors = SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author",
            "created_time",
            "contributors",
        ]

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializer = ContributorListSerializer(queryset, many=True)
        return serializer.data


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "project",
            "author",
            "assign",
            "created_time",
        ]


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["description", "author", "issue", "created_time"]
