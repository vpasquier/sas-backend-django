# Backend

## Build and Run

- `poetry shell`
- `export CUSTOM_DEBUG_FLAG=True`
- `python manage.py runserver`

## Model updates

If first time to use or models change:

- `python manage.py makemigrations`
- `python manage.py migrate`

## URLs

- `http://127.0.0.1:8000/api` for swagger
- `http://127.0.0.1:8000/admin` for admin and crud
- `http://localhost:8000/silk/` : https://github.com/jazzband/django-silk

## Databases

- `open db.sqlite3`
- Or use Postgres

## Diagram Generator

`python manage.py graph_models -a -o myapp_models.png` to create UML Data Model from the Django Models

## Docker

- `docker build -t sas-backend .`
- `docker run -p 8000:8000 sas-backend`