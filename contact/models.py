from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CarBooking(models.Model):
    subject = models.CharField(max_length=300, blank=True)
    username = models.CharField(max_length=300, blank=True)
    email = models.EmailField(max_length=100, blank=True )
    number= models.CharField(max_length=20)
    pickup = models.CharField(max_length=300, blank=True)
    message = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.subject


class CurierBooking(models.Model):
    name = models.CharField(max_length=300, blank=True)
    email = models.EmailField(max_length=100, blank=True )
    number= models.CharField(max_length=20)
    pickup_location = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=300, blank=True)
    
    

    def __str__(self):
        return self.name        