from django import  forms
from .models import CarBooking

class CarBookingForm(forms.ModelForm):
    class Meta:
        model=CarBooking
        fields = ['subject','name', 'email', 'number', 'pickup_location', 'meassage']
        


