from django.urls import path
from django.contrib.auth.views import LoginView

from .views import  car,BookingList, BookingView, AdminView, AdLogin, MLogin

urlpatterns = [
    # path('login/', LoginView.as_view()),
    path('list/', BookingList, name='bookinglist'),
    path('list/<int:id>/', BookingView, name='bookingview'),
    path('adminsign/', AdLogin, name='adminsign'),
    path('msign/', MLogin, name='msign'),
    path('adminv/', AdminView, name='adminv'),
    path('', car, name='carbooking'),
]