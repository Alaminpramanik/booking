from django.contrib import admin


from .models import CarBooking, CurierBooking
# Register your models here.

admin.site.register(CarBooking)
admin.site.register(CurierBooking)