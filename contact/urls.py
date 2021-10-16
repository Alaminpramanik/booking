from django.urls import path


from .views import  car,BookingList, BookingView, admin

urlpatterns = [
    path('', car, name='carbooking'),
    path('list/', BookingList, name='bookinglist'),
    path('list/<int:id>/', BookingView, name='bookingview'),
    path('login/', admin, name='admin'),
    # path('blog/<int:id>/', post_model_detail_view, name='detail'),
    # path('/name/', StylishDetailView.as_view(), name='list'),
]