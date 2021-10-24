from django.urls import path
from django.contrib.auth.views import LoginView

from .views import  car,BookingList, BookingView, admin,LoginView

urlpatterns = [
    path('', car, name='carbooking'),
    path('login/', LoginView.as_view()),
    path('list/', BookingList, name='bookinglist'),
    path('list/<int:id>/', BookingView, name='bookingview'),
    path('login/', admin, name='admin'),
    # path('blog/<int:id>/', post_model_detail_view, name='detail'),
    # path('/name/', StylishDetailView.as_view(), name='list'),
]