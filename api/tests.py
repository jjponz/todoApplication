from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Todo
from .serializers import TodoSerializer

# initialize the APIClient app
client = Client()


class TodoTests(TestCase):
    def test_add_todo(self):
        todo = Todo(description="Do the webpage")
        todo_serializer = TodoSerializer(todo)

        response = client.post(reverse('todo_management'),
                               data=todo_serializer.data,
                               content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
