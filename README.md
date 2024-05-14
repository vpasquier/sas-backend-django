# Backend

## Build and Run

- `poetry shell`
- `python manage.py runserver`

## Model updates

- `python manage.py makemigrations`
- `python manage.py migrate`

## Digram Generator

`python manage.py graph_models -a -o myapp_models.png` to create UML Data Model from the Django Models
