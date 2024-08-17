# Pollster App

Pollster is a web application built using Django that allows users to create polls with multiple choices and vote on them. The application is styled using Bootstrap for a responsive and modern interface.

## Features

- Create polls with multiple choices.
- Vote on polls and view live results.
- Manage polls via the Django admin interface.
- Responsive design using Bootstrap.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: Bootstrap (CSS framework)
- **Database**: SQLite (default for Django)
- **Template Engine**: Django Templates

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Virtual environment (recommended)

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pollster.git
   cd pollster

2. Set up a virtual environment:

    ```
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

    ```

3. Install dependencies:
    
    ```
    pip install -r requirements.txt

    ```

4. Apply migrations to set up the database:
   
   ```
   python manage.py migrate

   ```


5. Run the development server:

    ```
    python manage.py runserver

    ```

6. Create a superuser to access the Django admin:

    ```
    python manage.py createsuperuser

    ```
7. ### Project Structure

    ```
    pollster/
    │
    ├── polls/                   # The polls app
    │   ├── migrations/          # Database migrations
    │   ├── static/              # Static files (CSS, JS, images)
    │   ├── templates/           # HTML templates
    │   ├── models.py            # Database models
    │   ├── views.py             # Application logic and views
    │   ├── urls.py              # URL routing for the polls app
    │   └── admin.py             # Admin configuration for polls
    │
    ├── pollster/                # Main project directory
    │   ├── settings.py          # Project settings
    │   ├── urls.py              # URL routing for the project
    │   └── wsgi.py              # WSGI entry point for the application
    │
    ├── manage.py                # Django management script
    └── requirements.txt         # List of Python dependencies

    ```
