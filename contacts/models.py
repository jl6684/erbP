from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.listing.title}"
    
    class Meta:
        ordering = ['-contact_date']
