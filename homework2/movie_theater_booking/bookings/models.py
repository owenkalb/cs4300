from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seats')  # ✅ Added this line
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.seat.seat_number}"
