from rest_framework import serializers
from .models import Movie, Seat, Booking

# Converts Movie model to JSON
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# Converts Seat model to JSON
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

# Converts Booking model to JSON
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
