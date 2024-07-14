from django.db import models

# Create your models here.

class Producer(models.Model):
    company = models.CharField(max_length=150, default="Greek Producer")
    # address = models.CharField(max_length=50)
    # city = models.CharField(max_length=50)
    desc= models.TextField(default="Greek Product")
    epost = models.EmailField(null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    producer_logo = models.ImageField(upload_to='img/producers/', default='/img/producers/olive_branch.jpg')


    def __str__(self):
        return f"{self.company}"

    class Meta:
        verbose_name_plural = "Producers"


