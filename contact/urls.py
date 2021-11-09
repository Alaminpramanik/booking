from django.urls import path
from django.contrib.auth.views import LoginView

from .views import  Booking,BookingList, BookingView, AdminView, AdLogin, MLogin, Home, AdminViewList

urlpatterns = [
    path('', Home, name='home'),
    path('list/', BookingList, name='bookinglist'),
    path('list/<int:id>/', BookingView, name='bookingview'),
    path('adminviewlist/', AdminViewList, name='bookingview'),
    path('adminview/<int:id>/', AdminView, name='bookingview'),
    path('adminsign/', AdLogin, name='adminsign'),
    path('msign/', MLogin, name='msign'),
    path('adminv/', AdminView, name='adminv'),
    path('book/', Booking, name='carbooking'),
]