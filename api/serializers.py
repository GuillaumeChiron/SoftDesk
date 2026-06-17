from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    CharField,
)

from api.models import Project, Contributor, Issue, Comment
from authentication.serializers import UserSerializer


class ContributorListSerializer(ModelSerializer):

    username = CharField(source="user.username", read_only=True)

    class Meta:
        model = Contributor
        fields = ["id", "user", "username", "created_time"]


class ContributorSerializer(ModelSerializer):

    username = CharField(source="user.username", read_only=True)
    project_title = CharField(source="project.title", read_only=True)

    class Meta:
        model = Contributor
        fields = ["id", "user", "username", "project", "project_title", "created_time"]


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

    project_name = CharField(source="project.title", read_only=True)
    author_name = CharField(source="author.username", read_only=True)
    assign_name = CharField(source="assign.username", read_only=True)

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
            "project_name",
            "author",
            "author_name",
            "assign",
            "assign_name",
            "created_time",
        ]
        read_only_fields = ["author", "author_name", "assign_name", "created_time"]

    def validate(self, attrs):
        project = attrs.get("project", self.instance.project if self.instance else None)
        assign = attrs.get("assign", self.instance.assign if self.instance else None)

        if assign and project and not project.contributors.filter(user=assign).exists():
            raise ValidationError({
                "assign": "L'utilisateur assigné doit être contributeur du projet."
            })

        return attrs


class CommentSerializer(ModelSerializer):

    author_name = CharField(source="author.username", read_only=True)
    issue_name = CharField(source="issue.title", read_only=True)

    class Meta:
        model = Comment
        fields = ["uuid", "description", "author", "author_name", "issue", "issue_name", "created_time"]
        read_only_fields = ["author", "created_time"]
