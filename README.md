# Smart Preschool Learning Platform

A complete Preschool Learning Management System built with Django 5 and Bootstrap 5.

## Features

- Student Management
- Teacher Management
- Parent Dashboard
- Classroom Management
- Attendance Tracking
- Behaviour Analysis
- AI Behaviour Reports (Google Gemini)
- Announcements
- Role-Based Authentication (Admin, Teacher, Parent)

## Technologies

- Python 3.12
- Django 5
- Bootstrap 5
- SQLite
- Google Gemini AI
- HTML, CSS, JavaScript

## Installation

```bash
git clone https://github.com/Neptunescorp/smart_preschool.git
cd smart_preschool

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

## Project Structure

- Students
- Teachers
- Parents
- Classrooms
- Attendance
- Behaviour Analysis
- Announcements
- Authentication
- Dashboard

## Future Improvements

- Email notifications
- Parent mobile application
- AI attendance prediction
- Cloud deployment
- PostgreSQL support

## Author

**Nurbek Turdimuratov**

Software Engineering Student
