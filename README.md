# Do Nation: Developer Test

A basic Django project.

## Setup

Run the following commands:

- `pip install pipenv`
- `pipenv install --dev`
- `./bootstrap.sh`
- `cd devtest && python manage.py runserver`

Visit [the admin page](http://localhost:8000/admin/) and verify you can log in as:

```
u: admin
p: admin
```

## Pages

- [Home](http://localhost:8000/)
- [Current user](http://localhost:8000/users/)
- [User 0](http://localhost:8000/users/2)
- [User 1](http://localhost:8000/users/3)
- [User 2](http://localhost:8000/users/4)


## Testing

- `pipenv run test`
