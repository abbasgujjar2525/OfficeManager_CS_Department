from django.db import models
from datetime import datetime

class Application(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=999)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
