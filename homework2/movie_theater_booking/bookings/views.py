from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .forms import BookingForm
from django.utils import timezone
from django.http import JsonResponse, HttpResponseNotAllowed


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

    if request.method == 'POST':
        selected_ids = request.POST.get('seats', '').split(',')
        for seat_id in selected_ids:
            if seat_id:
                seat = Seat.objects.get(id=seat_id)
                if not seat.is_booked:
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
        'seats': seats
    })

def delete_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        booking.seat.is_booked = False
        booking.seat.save()
        booking.delete()
        return JsonResponse({'success': True})
    return HttpResponseNotAllowed(['POST'])


