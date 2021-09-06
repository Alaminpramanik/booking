from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import BookingForm
from .serializers import BookingFormListSerializers
# Create your views here.


class BookingCreate(CreateAPIView):
    serializer_class = BookingFormListSerializers