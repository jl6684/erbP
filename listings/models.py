from django.db import models
from django.utils import timezone
from realtors.models import Realtor
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    clubhouse = models.BooleanField(default=False)
    sqrt = models.DecimalField(max_digits=5, decimal_places=2)
    estate_size = models.FloatField(default=0.0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-list_date']  # Order by list_date descending
        indexes = [
            models.Index(fields=['-list_date']),
        ]