# Backend

## Build and Run

- `poetry shell`
- `python manage.py runserver`

## Model updates

- `python manage.py makemigrations`
- `python manage.py migrate`

## URLs

- `http://127.0.0.1:8000/api` for swagger
- `http://127.0.0.1:8000/admin` for admin and crud

## Dev database

- `open db.sqlite3`

## Diagram Generator

`python manage.py graph_models -a -o myapp_models.png` to create UML Data Model from the Django Models

## Docker

- `docker build -t sas-backend .`
- `docker run -p 8000:8000 sas-backend`