from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import BaseModel

# Create your models here.
class BookingForm(BaseModel):
    name = models.CharField(max_length=300, blank=True)
    email = models.EmailField(max_length=100, blank=True )
    phone= models.CharField(max_length=20)
    address = models.CharField(max_length=300, blank=True)
    start_time = models.TimeField(_(u"Booking Start Time"), auto_now_add=True, blank=True,null=True)
    end_time = models.TimeField(_(u"Booking End Time"), auto_now_add=True, blank=True,null=True)
    language = models.CharField(verbose_name=_('language'), max_length=3, choices=PREFERRED_LANGUAGE, default=ENGLISH)
    image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.name