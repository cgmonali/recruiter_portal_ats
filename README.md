# Recruiter Portal ATS (Applicant Tracking System)

A simple Django REST API for managing candidates with search functionality.

## Features

- Create, read, update, and delete candidate records
- Search candidates by name with relevance-based sorting
- Secure API endpoints
- Paginated results

## API Endpoints

### Candidates
- `GET /api/candidates/` - List all candidates
- `POST /api/candidates/` - Create new candidate
- `GET /api/candidates/<id>/` - Get specific candidate
- `PUT /api/candidates/<id>/` - Update candidate
- `DELETE /api/candidates/<id>/` - Delete candidate

### Search
- `GET /api/candidates/search/?q=<query>` - Search candidates by name
- `GET /api/candidates/search/` - UI view for candidate search
## Setup

1. Clone the repository:
```bash
git clone git@github.com:cgmonali/recruiter_portal_ats.git
cd recruiter_portal_ats
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework


## Admin Interface

Access the admin panel at `http://localhost:8000/admin/` after creating a superuser.
