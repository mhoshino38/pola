from django.db import models
from django.utils import timezone

class Day(models.Model):
    title = models.CharField('Title', max_length=15)
    text = models.TextField('Text', max_length=200)
    date = models.DateTimeField('Date', default=timezone.now)
    def __str__(self):
        return self.title
