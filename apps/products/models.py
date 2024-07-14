from django.db import models

# Create your models here.


from apps.producers.models import Producer

class Category(models.Model):
    name = models.CharField(max_length=50, default="Food")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"



class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_desc = models.TextField()    
    p_img = models.ImageField(upload_to='img/products/', default='img/products/OliveOil.jpg')
    p_likes = models.IntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f"{self.p_name}"

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['p_name']