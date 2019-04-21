from django.db import models


class Todo(models.Model):
    description = models.TextField(blank=False)
    creation_date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = "todo"

    def is_completed(self):
        return self.completed is True

    def complete(self):
        self.completed = True
