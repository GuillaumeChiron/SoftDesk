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

    class Meta:
        model = Contributor
        fields = ["user", "created_time"]


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ["user", "project", "created_time"]


class ProjectSerializer(ModelSerializer):

    author = UserSerializer(read_only=True)
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
        read_only_fields = ["author", "created_time"]

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializer = ContributorListSerializer(queryset, many=True)
        return serializer.data


class IssueSerializer(ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
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

    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["uuid", "description", "author", "issue", "created_time"]
