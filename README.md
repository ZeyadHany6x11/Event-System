# Event System

A Django-based web application for managing university events and seminars.

The system allows users to:
- View events
- Search events dynamically
- Open event details pages
- Book tickets
- Display available seats
- Manage events using Django Admin Dashboard

---

# Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap 5
- SQLite

---

# Features

## Home Page
- Displays all events
- Responsive Bootstrap cards
- Event images
- Event availability
- Countdown until event date

## Search System
- Search events by title
- Uses Django QuerySets and `__icontains`

## Event Details Page
- Full event information
- Event image
- Date and remaining time
- Available seats

## Booking System
- Book tickets dynamically
- Reduces available seats automatically
- Displays "Sold Out" when seats reach 0

## Admin Dashboard
- Add events
- Edit events
- Delete events
- Manage seats and images

## Reusable Design
- Master template using `base.html`
- Global CSS styling using `style.css`

---

# Project Structure

```text
Home/
│
├── manage.py
├── db.sqlite3
│
├── Home/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── events/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    │
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── details.html
    │   └── 404.html
    │
    ├── static/
    │   └── css/
    │       └── style.css
    │
    └── migrations/
```

---

# Installation & Setup

## 1. Clone the Repository

```bash
git clone <repository-url>
```

---

## 2. Open Project Folder

```bash
cd Home
```

---

## 3. Install Django

```bash
pip install django
```

---

## 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Create Superuser

```bash
python manage.py createsuperuser
```

Enter:
- username
- email
- password

---

## 6. Run the Server

```bash
python manage.py runserver
```

---

## 7. Open Browser

Home Page:

```text
http://127.0.0.1:8000/
```

Admin Dashboard:

```text
http://127.0.0.1:8000/admin
```

---

# Main Django Concepts Used

- Django ORM
- Models
- Views
- Templates
- Template Inheritance
- Static Files
- QuerySets
- `order_by()`
- `__icontains`
- Django Admin
- Template Tags (`{% if %}`, `{% for %}`)

---

# License

This project was developed for educational purposes as part of the Advanced Software Engineering course.
