# movie_theater_booking/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin dashboard
    path('admin/', admin.site.urls),

    # Include URLs from the bookings app
    path('', include('bookings.urls')),
]
