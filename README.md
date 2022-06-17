# Block-Watch

This is an app that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Getting started

To get a copy of the project up and running on your local machine for development and testing purposes;

1. Clone the repository

   > git clone https://github.com/Wannjer1/Block-Watch.git

2. Create a virtual environment

   > virtual3 -m venv env

   > source env/bin/activate

3. Install the project dependencies

   > (venv) $ pip install -r requirements.txt

4. Create a postgress db
5. Apply all migrations

   > (venv) $ python manage.py migrate

6. Create admin account

   > (venv) $ python manage.py createsuperuser(username=superuser, password=superuser)

7. Make migrations to your database

   > (venv) $ python manage.py makemigrations (appname)

   > (venv) $ python manage.py migrate

8. Start development server
   > (venv) $ python3 manage.py runserver
