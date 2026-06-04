from rest_framework.viewsets import ModelViewSet

from api.serializers import ProjectSerializer
from api.models import Project


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()
