from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from .views import movie_list_view
# Creates RESTful routes for viewsets
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

# Path to mount
urlpatterns = [
    path('', movie_list_view, name='movie_list'),
    path('api/', include(router.urls)),
]