from django.db import models

# Create your models here.


# class Category(models.Model):
# Use CHOICES
                                


class Music(models.Model):
    m_name = models.CharField(max_length=255)
    m_description = models.TextField()    
    m_img = models.ImageField(upload_to='img/foodies/', default=None, null=True, blank=True)
    m_link = models.URLField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.m_name}"

    class Meta:
        verbose_name_plural = "Music"
        ordering = ['m_name']