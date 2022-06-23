# Block-Watch

This is an app that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

# User Stories

- A user can sign in into the application
- A user can see and update their profile
- A user can view, join or leave a neighborhood
- A user can create posts that will be visible to everyone in the neighborhood
- A user can find contact information for the health department and the police authority for the specific neighborhood
- A user can see a list of businesses in the neighborhood
- A user can post a business

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

## Known Bugs

Currently there are no known bugs but pull requests are allowed incase you spot any.

## Authors

- Ann Wanjeri
- Mohammed Lee
