from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from .models import Movie, Seat, Booking
from django.contrib.auth import get_user_model

User = get_user_model()


class MovieModelTests(TestCase):
    def test_create_movie(self):
        m = Movie.objects.create(
            title="Test Movie",
            description="A test movie.",
            release_date="2020-01-01",
            duration=100
        )
        self.assertEqual(str(m.title), "Test Movie")
        self.assertEqual(Movie.objects.count(), 1)


class SeatModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Seat Movie",
            description="Seat test",
            release_date="2020-01-01",
            duration=90
        )

    def test_create_seat(self):
        s = Seat.objects.create(movie=self.movie, seat_number="A1", is_booked=False)
        self.assertEqual(str(s.seat_number), "A1")
        self.assertFalse(s.is_booked)
        self.assertEqual(Seat.objects.count(), 1)


class BookingModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Booking Movie",
            description="Booking test",
            release_date="2020-01-01",
            duration=90
        )
        self.seat = Seat.objects.create(movie=self.movie, seat_number="B1", is_booked=False)

    def test_create_booking(self):
        b = Booking.objects.create(movie=self.movie, seat=self.seat, booking_date=timezone.now())
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(b.movie, self.movie)
        self.assertEqual(b.seat, self.seat)


class TemplateViewTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Template Movie",
            description="Template test",
            release_date="2020-01-01",
            duration=95
        )

    def test_movie_list_view_status_and_content(self):
        url = reverse('movie_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Available Movies")
        self.assertContains(resp, self.movie.title)

    def test_book_seat_view_status(self):
        url = reverse('book_seat', kwargs={'movie_id': self.movie.id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.movie.title)


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # create a user and authenticate if your API requires auth for write ops
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # If your API requires login for POST/PUT, uncomment the next line:
        # self.client.force_authenticate(user=self.user)

        self.movie1 = Movie.objects.create(
            title="API Movie 1", description="API test", release_date="2020-01-01", duration=100
        )
        self.seat1 = Seat.objects.create(movie=self.movie1, seat_number="C1", is_booked=False)
        self.seat2 = Seat.objects.create(movie=self.movie1, seat_number="C2", is_booked=False)

    def test_get_movies_list(self):
        resp = self.client.get('/api/movies/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(resp.json(), list))

    def test_create_movie_via_api(self):
        payload = {
            "title": "New API Movie",
            "description": "Created via tests",
            "release_date": "2022-01-01",
            "duration": 110
        }
        resp = self.client.post('/api/movies/', payload, format='json')
        self.assertIn(resp.status_code, (status.HTTP_201_CREATED, status.HTTP_200_OK))
        self.assertTrue(Movie.objects.filter(title="New API Movie").exists())

    def test_get_seats_for_movie(self):
        resp = self.client.get('/api/seats/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        self.assertTrue(any(str(self.seat1.id) in str(item.get('id', '')) or item.get('seat_number') == self.seat1.seat_number for item in data))

    def test_create_booking_via_api(self):
        payload = {
            "movie": self.movie1.id,
            "seat": self.seat1.id,
            "booking_date": timezone.now().isoformat()
        }
        resp = self.client.post('/api/bookings/', payload, format='json')
        self.assertIn(resp.status_code, (status.HTTP_201_CREATED, status.HTTP_200_OK))
        self.seat1.refresh_from_db()
        # depending on logic, seat may not auto-mark booked; test booking exists
        self.assertTrue(Booking.objects.filter(movie=self.movie1, seat=self.seat1).exists())
