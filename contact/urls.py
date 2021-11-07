from django.urls import path
from django.contrib.auth.views import LoginView

from .views import  car,BookingList, BookingView, Login, AdminView

urlpatterns = [
    # path('login/', LoginView.as_view()),
    path('list/', BookingList, name='bookinglist'),
    path('list/<int:id>/', BookingView, name='bookingview'),
    path('signin/', Login, name='login'),
    path('adminv/', Login, name='adminv'),
    path('', car, name='carbooking'),
]