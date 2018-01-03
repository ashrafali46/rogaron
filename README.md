
# MyRecommendations

Recommendation applications developed using Django, including for the moment just:

- MyRestaurants

I write this based on [rogargo](https://github.com/rogargon/myrecommendations) tutorial and I am trying to add some new features on my own.

## Tools
Key tools used in this Django project are:

* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/python)
* [SQLite](https://www.sqlite.org/)
* [Gunicorn](http://gunicorn.org/)
* [Whitenoise](https://pypi.python.org/pypi/whitenoise)
* [WSGI](https://wsgi.readthedocs.io/en/latest/)

## How to run:
1. Clone the whole repository to your machine.
2. cd into root folder, use command `pip install -r requirements.txt`
3. build new user like
```
user@host> manage.py shell
>>> from django.contrib.auth.models import User
>>> user=User.objects.create_user('foo', password='bar')
>>> user.is_superuser=True
>>> user.is_staff=True
>>> user.save()
```
4. Run the server by command `python manage.py runserver`