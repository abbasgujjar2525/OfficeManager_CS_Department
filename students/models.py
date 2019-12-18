from django.db import models
from datetime import datetime

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    isRegister = models.BooleanField(default=True)
    std_email = models.EmailField(max_length=50, default="16201519-001@uog.edu.pk")
    std_password = models.CharField(max_length=50, default="16201519-001")
    date = models.DateTimeField(default=datetime.now, blank=True)

class Courses(models.Model):
    course_id = models.CharField(max_length=50 ,primary_key=True)
    course_name = models.CharField(max_length=50)
    course_credits = models.CharField(max_length=50)

class Rooms(models.Model):
    room_id = models.CharField(max_length=50 ,primary_key=True)
    room_name = models.CharField(max_length=50)
    room_cap = models.IntegerField()

class Teachers(models.Model):
    teach_id = models.CharField(max_length=50 , primary_key=True)
    teach_name = models.CharField(max_length=50)
    teach_desi = (
        ('AL', 'Assistant Lecturer '),
        ('L', 'Lecturer '),
        ('AP', 'Assistant Professor'),
        ('P', 'Professor'),
    )
    teach_designation = models.CharField(max_length=50, default="designation",choices=teach_desi)

class DateSheet(models.Model):
    file = models.FileField();