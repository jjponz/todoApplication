from django.db import models


class Project(models.Model):
    description = models.TextField(blank=False)
