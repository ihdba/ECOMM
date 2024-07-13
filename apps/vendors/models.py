from django.db import models

# Create your models here.

# Vendor is the person or company that produces or imports the products
# 


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_desc = models.TextField()    
    vendor_img = models.ImageField(upload_to='img/vendors/', default=None)
    
    
    def __str__(self):
        return f"{self.vendor_name}"

    class Meta:
        verbose_name_plural = "Vendors"
        ordering = ['vendor_name']