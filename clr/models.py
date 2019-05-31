from django.db import models

from django.utils import timezone


class Data(models.Model):
    title = models.CharField(max_length=200)
    
    text = models.TextField()

    url = models.TextField()

    totalUrl = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title