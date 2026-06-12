from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Contributor, Project
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


class ProjectViewsetTestCase(APITestCase):
    def test_project_author_is_automatically_added_as_contributor(self):
        author = User.objects.create_user(
            username="author",
            password="password",
            age=18,
        )
        self.client.force_authenticate(user=author)

        response = self.client.post(
            reverse("project-list"),
            {
                "title": "SoftDesk",
                "description": "API de suivi des problemes",
                "type": Project.BACKEND,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project = Project.objects.get()
        self.assertEqual(project.author, author)
        self.assertTrue(
            Contributor.objects.filter(user=author, project=project).exists()
        )
