# Smart Attendance Management System
### Face Recognition Based Attendance Software

## 1. Introduction

The Smart Attendance Management System is a software-based attendance solution developed using Python, OpenCV, Django, and MySQL.

The system uses a webcam to detect and recognize registered students' faces. When a student is successfully recognized, their attendance is automatically recorded with the current date and time.

The main objective is to reduce manual attendance work and make attendance management faster and more efficient.

## 2. Software Features

- **Face Detection:** Detects human faces using OpenCV YuNet.
- **Face Recognition:** Identifies registered students using OpenCV SFace.
- **Multiple Face Recognition:** Processes multiple faces in a single webcam frame.
- **Student Registration:** Loads student images from the faces folder.
- **Automatic Attendance:** Marks attendance when a registered student is recognized.
- **Duplicate Prevention:** Prevents a student from being marked present more than once per day.
- **MySQL Database:** Stores attendance records through Django.
- **CSV Storage:** Maintains an additional attendance record.
- **Date and Time Tracking:** Records the attendance date and time.
- **Admin Panel:** Allows administrators to view attendance records.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Face detection and recognition |
| YuNet | Face detection model |
| SFace | Face recognition model |
| Django | Backend framework |
| MySQL | Database management |
| CSV | Attendance file storage |
| Requests | Communication with Django API |

## 4. Project Structure

```text
SmartAttendance/
│
├── attendance_system/
│   ├── migrations/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   └── urls.py
│
├── faces/
│   └── Student Images
│
├── models/
│   ├── face_detection_yunet_2023mar_int8.onnx
│   └── face_recognition_sface_2021dec_int8.onnx
│
├── smartattendance/
│   ├── settings.py
│   └── urls.py
│
├── face_detection.py
├── face_recognition.py
├── attendance.py
├── camera_test.py
├── manage.py
├── attendance.csv
├── .gitignore
└── README.md
```

## 5. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd SmartAttendance
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Required Packages

```bash
pip install django opencv-python requests mysqlclient numpy
```

### Step 4: Configure MySQL Database

1. Install MySQL Server.
2. Create a database named `smartattendance`.
3. Open `smartattendance/settings.py`.
4. Configure your MySQL database credentials.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartattendance',
        'USER': 'root',
        'PASSWORD': 'YOUR_MYSQL_PASSWORD',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Replace `YOUR_MYSQL_PASSWORD` with your own password. Do not upload real database credentials to GitHub.

### Step 5: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Register Student Images

Place student images inside the `faces` folder.

Example:

```text
faces/
├── Sunzidul.jpg
├── Fatema.jpg
├── Rafi.jpg
└── Naim.jpg
```

The image filename is used as the student's name.

Use clear, front-facing images for better recognition.

Make sure you have permission to use the registered students' photos.

## 6. Running the Software

The software requires two separate terminals.

### Terminal 1: Run Django Server

```bash
venv\Scripts\activate
python manage.py runserver
```

Django server address:

```text
http://127.0.0.1:8000/
```

### Terminal 2: Run Face Recognition

```bash
venv\Scripts\activate
python face_recognition.py
```

The webcam will start and begin detecting and recognizing faces.

Press **Q** to close the camera window.

Keep both terminals running while using the software.

## 7. Django Admin Panel

The Django admin panel is used to manage and view attendance records.

URL:

```text
http://127.0.0.1:8000/admin/
```

Create an administrator account using:

```bash
python manage.py createsuperuser
```

Then log in using your superuser credentials.

## 8. Attendance API

The face recognition program communicates with Django through the following API:

```text
http://127.0.0.1:8000/api/mark-attendance/
```

When a student is recognized:

1. The student's name is identified.
2. The face recognition program sends the name to Django.
3. Django checks whether attendance already exists for that student on the current date.
4. If no record exists, attendance is saved.
5. If a record already exists, duplicate attendance is prevented.

## 9. Database Information

**Database:** MySQL

**Database Name:** `smartattendance`

**Attendance Table:** `attendance_system_attendance`

Stored information:

- Student Name
- Attendance Date
- Attendance Time

The software also maintains an additional CSV attendance file.

## 10. System Workflow

```text
        Webcam
           |
           v
   Face Detection (YuNet)
           |
           v
  Face Recognition (SFace)
           |
           v
 Compare Registered Faces
           |
           v
   Identify Student
           |
           v
   Django Attendance API
           |
           v
      MySQL Database
           |
           v
   Attendance Records
```

## 11. Software Requirements

- Windows operating system
- Python
- MySQL Server 8.4 or compatible version
- Webcam
- Internet connection for initial package installation

## 12. Limitations

- Recognition accuracy depends on lighting, camera quality, and image quality.
- Only registered students can be identified.
- The current system does not include face liveness detection.
- The software should be tested thoroughly before being used for official attendance.

## 13. Future Software Improvements

- Web-based teacher dashboard.
- Attendance reports and downloadable records.
- Student management interface.
- Improved face recognition accuracy.
- Face liveness detection.
- Better attendance analytics.

## 14. Author

**Project:** Smart Attendance Management System

**Project Category:** Software Development

**Technologies:** Python, OpenCV, Django, MySQL

**Purpose:** Automated student attendance using face recognition.
