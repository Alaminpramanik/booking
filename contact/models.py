from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timesince import timesince


class StyletModelQuerySet(models.query.QuerySet):
    def active(self):

        return self.filter(active=True)

    def post_name_items(self, value):
        return self.filter(name__icontains=value)
class styleModelManager(models.Manager):
    def get_queryset(self):
        return StyletModelQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        #qs = super(PostModelManager, self).all(*args, **kwargs).active() #.filter(active=True)
        #print(qs)
        qs = self.get_queryset().active()
        return qs

    def get_timeframe(self, date1, date2):
        #assume datetime objects
        qs = self.get_queryset()
        qs_time_1 = qs.filter(publish_date__gte=date1)
        qs_time_2 = qs_time_1.filter(publish_date__lt=date2) # Q Lookups
        
        return qs_time_2
        
# Create your models here.
class CarBooking(models.Model):
    # id = models.BigAutoField(primary_key=True)
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