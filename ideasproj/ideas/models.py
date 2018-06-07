from django.db import models

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    idea_id = models.IntegerField(default=0000)
    def __str__(self):
        return self.title