from django.db import models

class Feedback(models.Model):
    feed_name = models.CharField(max_length=30, default='')
    feed_rate = models.CharField(max_length=1, default='0')

    def __str__(self):
        return self.feed_name

