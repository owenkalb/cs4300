from django.contrib import admin
from .models import Movie, Seat, Booking

# Register models to appear in the admin dashboard
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)
