from datetime import datetime
from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Todo
from .serializers import TodoSerializer

# initialize the APIClient app
client = Client()


class ManageTodoTests(TestCase):
    def test_add_todo(self):
        todo = Todo(description="Do the webpage")
        todo_serializer = TodoSerializer(todo)

        response = client.post(reverse('todo_management'),
                               data=todo_serializer.data,
                               content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_todo_with_creational_date(self):
        todo = Todo(description="Do the webpage")
        todo_serializer = TodoSerializer(todo)

        response = client.post(reverse('todo_management'),
                               data=todo_serializer.data,
                               content_type='application/json')

        created_todo = Todo(**response.data)
        self.assertEqual(self.__today(), created_todo.creation_date)

        #TODO: Estoy haciendo el test para completar un todo, esto lo voy a hacer pasando unicamente un json personalizado, podria hacerlo
        # pasando simplemente todo el objeto para así poder hacerlo más facil, pero entonces no se como coño lo desacoplaria
        # y de está maner aya lo tengo desacoplado =)
    def test_complete_todo(self):
        todo = Todo(id=5, description="Do the webpage")
        todo_serializer = TodoSerializer(todo)
        data = {"id": todo.id}
        data_json = json.dumps(data)

        response = client.post(
            reverse('complete_todo'),
            data=todo_serializer.data,
            #data=data_json,
            content_type='application/json')

        print("hoooolis")
        print(response.data)
        # completed_todo = Todo(**response.data)
        # self.assertTrue(completed_todo.is_completed())

    def __today(self):
        return datetime.today().date().strftime('%Y-%m-%d')
