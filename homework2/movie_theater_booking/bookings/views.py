from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .forms import BookingForm
from django.utils import timezone

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

def booking_history_view(request):
    bookings = Booking.objects.select_related('movie', 'seat').order_by('-booking_date')
    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })


def book_seat_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seat = form.cleaned_data['seat']
            if seat.is_booked:
                form.add_error('seat', 'This seat is already booked.')
            else:
                Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    booking_date=timezone.now() 
                )
                seat.is_booked = True
                seat.save()
                return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats,
        'form': form
    })

