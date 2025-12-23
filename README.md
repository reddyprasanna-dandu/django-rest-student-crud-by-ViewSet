# Student CRUD API – Django REST Framework

A simple CRUD REST API using Django REST Framework.

## Features
- Create Student
- Retrieve Students
- Update Student
- Partial Update
- Delete Student

## Tech Stack
- Python
- Django
- Django REST Framework

## API Endpoints

| Method | URL | Description |
|------|-----|------------|
| GET | /app/StudentCRUDVS/ | List students |
| GET | /app/StudentCRUDVS/{id}/ | Retrieve student |
| POST | /app/StudentCRUDVS/ | Create student |
| PUT | /app/StudentCRUDVS/{id}/ | Update student |
| PATCH | /app/StudentCRUDVS/{id}/ | Partial update |
| DELETE | /app/StudentCRUDVS/{id}/ | Delete student |

## Run Project
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
