from django import  forms
from .models import CarBooking
from django.contrib.auth.models import User

class CarBookingForm(forms.ModelForm):
    class Meta:
        model=CarBooking
        fields = ['subject','name', 'email', 'number', 'pickup_location', 'meassage']
        


class LoginForm(forms.Form):
    class Meta:
    model=User
    fields = ['subject','name', 'email', 'number', 'pickup_location', 'meassage']

   