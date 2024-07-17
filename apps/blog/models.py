from django.db import models

# Create your models here.


class Post(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.titel