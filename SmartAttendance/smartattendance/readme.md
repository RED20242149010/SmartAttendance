# SmartAttendance - Django Project Configuration

## Overview

The `smartattendance` folder contains the main Django project configuration for the Smart Attendance Management System.

It manages the overall Django application settings, URL routing, and server configuration.

## Technologies Used

- Python
- Django
- MySQL

## Folder Structure

```text
smartattendance/
│
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
├── wsgi.py
└── README.md
```

## Main Files and Their Functions

### 1. settings.py

Contains the main configuration of the Django project.

Responsibilities:

- Configure installed Django applications.
- Configure middleware.
- Set the database connection.
- Configure templates and static files.
- Define security and application settings.

### 2. urls.py

Manages the main URL routing of the project.

It connects the Django Admin Panel and the attendance application API.

Main routes:

```text
/admin/
/api/
```

The attendance API is connected through the `attendance_system` application.

### 3. asgi.py

Provides the ASGI application entry point for asynchronous server deployment.

### 4. wsgi.py

Provides the WSGI application entry point for traditional Django server deployment.

### 5. __init__.py

Marks this directory as a Python package.

## Database Configuration

The project uses MySQL as its database.

**Database Name:** `smartattendance`

The database configuration is maintained in `settings.py`.

Database credentials should be kept private and must not be published on GitHub.

## Running the Django Project

Run the following command from the main project directory:

```bash
python manage.py runserver
```

The development server runs at:

```text
http://127.0.0.1:8000/
```

## Project Information

**Project:** Smart Attendance Management System

**Module:** Django Project Configuration

**Framework:** Django

**Database:** MySQL

**Purpose:** Manage the main configuration and routing of the attendance software.
