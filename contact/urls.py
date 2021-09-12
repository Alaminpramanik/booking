from django.urls import path


from .views import   car

urlpatterns = [
    # path('cars/', CarBooked.as_view(), name='car-form'),
   
    path('car/', car, name='carbooking'),
    # path('/name/', StylishDetailView.as_view(), name='list'),
]