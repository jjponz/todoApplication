from datetime import datetime
from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Todo
from api.serializers import TodoSerializer

# initialize the APIClient app
client = Client()


class AddTodoTest(TestCase):
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

        created_todo = Todo(**response.data)
        self.assertEqual(self.__today(), created_todo.creation_date)

    def __build_todo(self):
        return Todo(description="Do the webpage")

    def __today(self):
        return datetime.today().date().strftime('%Y-%m-%d')
