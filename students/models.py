from django.db import models
from datetime import datetime

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    isRegister = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)



