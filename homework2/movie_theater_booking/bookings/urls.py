from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet,
    SeatViewSet,
    BookingViewSet,
    movie_list_view,
    book_seat_view
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', movie_list_view, name='movie_list'),
    path('book/<int:movie_id>/', book_seat_view, name='book_seat'),
    path('api/', include(router.urls)),
]
