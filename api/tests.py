from django.test import TestCase

from api.models import Project
from api.serializers import ProjectSerializer
from authentication.models import User


class ProjectSerializerTestCase(TestCase):
    def test_author_is_serialized_as_a_single_user(self):
        author = User.objects.create_user(
            username="author",
            password="password",
            age=18,
        )
        project = Project.objects.create(
            title="SoftDesk",
            description="API de suivi des problemes",
            type=Project.BACKEND,
            author=author,
        )

        data = ProjectSerializer(project).data

        self.assertEqual(data["author"]["id"], author.id)
        self.assertEqual(data["author"]["username"], author.username)
