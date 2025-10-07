# Homework 2: Movie Theater Booking System 

## Creating the Booking App 

Created a Django app named `bookings`
- Movie: title, description, release date, duration
- Seat: seat number, booking status
- Booking: movie, seat, user, booking date

## Implementing the MVT Architecture 
- Created and migrated database tables
Views:
  - MovieViewSet for movie CRUD
  - SeatViewSet for seat availability and booking
  - BookingViewSet for booking history
Templates:
  - Movie listings
  - Seat booking
  - Booking history

## Creating an User Interface 

Created templates in `bookings/templates/bookings/`:
- base.html: shared layout and Bootstrap CSS
- movie_list.html: displays movies with "Book Now" buttons
- seat_booking.html: interactive seat grid with glowing selection
- booking_history.html: shows past bookings with delete buttons(never got delete to work)

## RESTful API Implementation 

Configured API routes in `urls.py`:
- /api/movies/: list and manage movies
- /api/seats/: check and book seats
- /api/bookings/: view and create bookings

## Testing & Running Locally 

cd ~/cs4300/homework2/movie_theater_booking
source myenv/bin/activate
python3 manage.py runserver 0.0.0.0:3000

- Wasn't able to use it inside render

## Project Structure

- `movie_theater_booking/` — Django project root  
- `bookings/` — Main app with models, views, templates  
- `templates/bookings/` — HTML templates  
- `static/` — Custom CSS and JS  
- `db.sqlite3` — Default database file  
- `requirements.txt` — Dependency list for deployment  
- `render.yaml` — Optional Render config  

## Resources Used

- Django Documentation  
- Django REST Framework  
- Bootstrap  
- Testing in Django  
- Copilot to Refactor views and templates and to Improve UI/UX



