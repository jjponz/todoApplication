from rest_framework import serializers
from todo.models import Todo, Project
from api.serializers.ProjectSerializer import ProjectSerializer


class TodoSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(allow_null=True)

    class Meta:
        model = Todo
        fields = ("id", "description", "creation_date", "completed",
                  "projects")

    def create(self, validated_data):
        # TODO jjpv20190521: this business logic should be embebbed in a action to can test independtly and
        # has a correct arquitecture.
        # the action should be named TodoCreator and return the todo that I returned
        project = validated_data.pop('projects')
        todo = Todo.objects.create(**validated_data)
        if (project is not None):
            project = Project.objects.create(**project)
            todo.projects = project
            todo.save()
        return todo
