from django.db import models
from .project import Project


class Todo(models.Model):
    description = models.TextField(blank=False)
    creation_date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    projects = models.ForeignKey(Project,
                                 on_delete=models.CASCADE,
                                 related_name='projects',
                                 blank=True,
                                 null=True)

    class Meta:
        app_label = "todo"

    def is_completed(self):
        return self.completed is True

    def complete(self):
        self.completed = True

    def project_description(self):
        return self.projects.description
