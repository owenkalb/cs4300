from django.db import models
from django.contrib.auth.models import User

# Represents a movie available for booking
class Movie(models.Model):
    # Movie title
    title = models.CharField(max_length=100)
    # Desc for movie
    description = models.TextField()
    # Release date
    release_date = models.DateField()
    # Length
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title


# Represents a seat in the theater
class Seat(models.Model):
    # Unique seat identifier
    seat_number = models.CharField(max_length=10)
    # Booking status: True if booked
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number


# Represents a user's booking for a specific movie and seat
class Booking(models.Model):
    # Movie booked
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # Seat reserved
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    # User who made the booking
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Timestamp of booking
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"
