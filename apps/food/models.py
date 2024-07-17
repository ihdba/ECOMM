from django.db import models

# Create your models here.


class Food_Channel(models.Model):
    channel_name = models.CharField(max_length=255)
    channel_rating = models.CharField(max_length=5)
    channel_description = models.TextField()    
    channel_img = models.ImageField(upload_to='img/foodies/', default=None)
    channel_link = models.URLField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.channel_name}"

    class Meta:
        verbose_name_plural = "Food Channels"
        ordering = ['channel_name']