from rest_framework.serializers import ModelSerializer
from .models import BookingForm


class BookingFormListSerializers(ModelSerializer):
    class Meta:
        model = Gmap
        fields = '__all__'