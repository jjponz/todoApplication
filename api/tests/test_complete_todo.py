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


class CompleteTodoTest(TestCase):
    def test_complete_todo(self):
        todos = self.__build_todos()
        todo_serializer = TodoSerializer(todos, many=True)

        response = client.post(reverse('complete_todo'),
                               data=todo_serializer.data,
                               content_type='application/json')

        for todo in response.data:
            self.__assertTodoIsComplete(todo)

    def __build_todos(self):
        result = Todo.objects.bulk_create(
            [Todo(description="foo"),
             Todo(description="bar")])

        for todo in result:
            todo.save()

        return result

    def __assertTodoIsComplete(self, todo):
        todo_serializer = TodoSerializer(todo)
        todo = Todo.objects.get(pk=todo_serializer.data['id'])
        self.assertTrue(todo.is_completed())
