from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Todo, Project
from api.serializers import ProjectSerializer

# initialize the APIClient app
client = Client()


class AddProjectTest(TestCase):
    def test_add_todo(self):
        project = Project(description="description")
        project_serializer = ProjectSerializer(project)

        response = client.post(reverse('project_management'),
                               data=project_serializer.data,
                               content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
