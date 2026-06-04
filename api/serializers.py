from rest_framework.serializers import ModelSerializer, ValidationError

from api.models import Project


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author", "created_time"]
