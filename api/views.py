from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.decorators import action

from todo.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False)
    def complete_todo(self, request):
        # TODO jjpv 20190421: this business logic should be embebbed in a domain service to can test indepently and
        # has a correct arquitecture, in the same way,
        # the access to the database should be abstracted via repository pattern
        # the final call should be:
        # completed_todos = complete_todos.Do(request.data)
        # and inside Do do all the business logic
        completed_todos = self.__complete_todos(request.data)
        serializer = TodoSerializer(completed_todos, many=True)
        return Response(serializer.data)

    def __complete_todos(self, serialized_todos):
        serializer = self.get_serializer(data=serialized_todos,
                                         many=isinstance(
                                             serialized_todos, list))
        serializer.is_valid(raise_exception=True)
        result = []
        for serialized_todo in serialized_todos:
            result.append(self.__complete_todo(serialized_todo))
        return result

    def __complete_todo(self, serialized_todo):
        todo = Todo(**serialized_todo)
        todo.complete()
        todo.save()
        return todo
