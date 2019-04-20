from django.db import models


class Todo(models.Model):
    description = models.TextField(blank=False)
    creation_date = models.DateField(auto_now=True)

    class Meta:
        app_label = "todo"
