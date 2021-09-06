from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.UserRegistrationApiView.as_view(), name='contact-form'),
         
]
