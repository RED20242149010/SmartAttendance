# Attendance System

## Overview

The `attendance_system` is a Django application responsible for managing and storing student attendance records in the Smart Attendance Management System.

It receives recognized student information from the face recognition program through a Django API and stores attendance data in the MySQL database.

## Features

- Receive student names through an API.
- Automatically record student attendance.
- Store attendance date and time.
- Prevent duplicate attendance on the same day.
- Manage attendance records using Django models.
- View attendance records through the Django Admin Panel.

## Technologies Used

- Python
- Django
- MySQL
- Django REST-style JSON API

## Folder Structure

```text
attendance_system/
│
├── migrations/
│   └── Database migration files
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py
├── views.py
└── README.md
```

## Main Files and Their Functions

### 1. models.py

Defines the Attendance database model.

The model contains:

- `name` – Student name.
- `date` – Attendance date.
- `time` – Attendance time.

### 2. views.py

Contains the `mark_attendance` API function.

Main responsibilities:

- Accept POST requests.
- Receive student information in JSON format.
- Check existing attendance records.
- Save new attendance records.
- Prevent duplicate attendance for the same student on the same date.

### 3. urls.py

Defines the API URL:

```text
/api/mark-attendance/
```

### 4. admin.py

Registers the Attendance model with Django Admin so administrators can view attendance records.

### 5. migrations/

Contains database migration files used to create and update database tables.

## API Information

**Endpoint:**

```text
http://127.0.0.1:8000/api/mark-attendance/
```

**Request Method:** POST

**Request Format:** JSON

Example request:

```json
{
    "name": "Sunzidul"
}
```

Example successful response:

```json
{
    "message": "Attendance marked",
    "name": "Sunzidul"
}
```

If attendance already exists:

```json
{
    "message": "Attendance already marked today",
    "name": "Sunzidul"
}
```

## Database Information

**Database:** MySQL

**Table Name:** `attendance_system_attendance`

| Field | Description |
|---|---|
| id | Attendance record ID |
| name | Student name |
| date | Attendance date |
| time | Attendance time |

## How to Run

Run these commands from the main project directory:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Django server:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Purpose

The main purpose of this application is to handle attendance data received from the face recognition system and maintain organized attendance records in the MySQL database.

**Project:** Smart Attendance Management System  
**Module:** Attendance System  
**Framework:** Django  
**Database:** MySQL
