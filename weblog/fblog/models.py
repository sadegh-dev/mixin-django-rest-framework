from django.db import models
from django.utils import timezone

class Post(models.Model):
    context = models.TextField()
    release_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)+" | "+ str(self.context)
    
    class Meta:
        verbose_name_plural = 'My Posts'






