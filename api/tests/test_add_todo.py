from datetime import datetime
from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Todo, Project
from api.serializers import TodoSerializer

# initialize the APIClient app
client = Client()


class AddTodoTest(TestCase):
    def setUp(self):
        self.WEBPAGE = "webpage"

    def test_add_todo(self):
        todo = self.__build_todo()
        todo_serializer = TodoSerializer(todo)

        response = client.post(reverse('todo_management'),
                               data=todo_serializer.data,
                               content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_todo_with_creational_date(self):
        todo = self.__build_todo()
        todo_serializer = TodoSerializer(todo)

        response = client.post(reverse('todo_management'),
                               data=todo_serializer.data,
                               content_type='application/json')

        created_todo = Todo.objects.get(pk=response.data['id'])
        self.assertEqual(self.__today(), created_todo.creation_date)

    def test_add_todo_with_project(self):
        project = Project(description=self.WEBPAGE)
        todo = self.__build_todo_with(project)
        todo_serializer = TodoSerializer(todo)

        response = client.post(reverse('todo_management'),
                               data=todo_serializer.data,
                               content_type='application/json')

        created_todo = Todo.objects.get(pk=response.data['id'])
        self.assertEqual(self.WEBPAGE, created_todo.project_description())

    def __build_todo(self):
        todo = Todo(description="Do the webpage")
        return todo

    def __build_todo_with(self, project):
        todo = self.__build_todo()
        todo.projects = project
        return todo

    def __today(self):
        return datetime.today().date()
