## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KishanParmar1818/jwt-auth-system.git
$ cd jwt-auth-system
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venev env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
