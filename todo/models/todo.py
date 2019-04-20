from django.db import models


class Todo(models.Model):
    description = models.TextField(blank=False)

    class Meta:
        app_label = "todo"
