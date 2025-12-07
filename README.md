# Mood Tracker API

A RESTful API for tracking daily moods, built with **Django** and **Django REST Framework (DRF)**.  
Users can log their daily mood, add optional notes, and retrieve, update, or delete mood entries. Authentication ensures that each user’s data remains private and secure.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Database Schema](#database-schema)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User registration and authentication using Django’s built-in User model.
- Create, read, update, and delete daily mood entries.
- Restrict access to logged-in users only (`IsAuthenticated` permission).
- Unique mood entry per user per day.
- Optional note for each mood entry.
- Automatic timestamps (`created_at` and `updated_at`).
- RESTful API design with browsable interface via DRF.

---

## Technologies

- Python 3.11+
- Django 4.x
- Django REST Framework
- SQLite (default database; can be replaced)
- Git for version control

---

## Database Schema

### Entities

**User** (Django built-in `auth_user`)  
Attributes: `id`, `username`, `email`, `password`, `first_name`, `last_name`, `is_active`, `is_staff`, `date_joined`

**MoodEntry**  
Attributes:  
- `id` (PK)  
- `user` (FK → User)  
- `date` (date of mood)  
- `mood` (`Happy`, `Sad`, `Neutral`, `Anxious`, `Excited`)  
- `note` (optional text)  
- `created_at`, `updated_at` (timestamps)

**Relationship**:  
- One-to-many: One user can have multiple mood entries.  
- Unique constraint on (`user`, `date`) to ensure one entry per day.

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Geeblacck/mood_tracker_api.git
cd mood_tracker_api

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
