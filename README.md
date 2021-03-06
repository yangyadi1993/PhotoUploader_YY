# PhotoUploader_YY
This application is using Django framework with Python 3.

## Installation

1. Install pip. The easiest is to use the [standalone pip installer](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py). If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.
2. Take a look at [virtualenv](https://virtualenv.pypa.io/en/stable/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). These tools provide isolated Python environments, which are more practical than installing packages systemwide. They also allow installing packages without administrator privileges. The [contributing tutorial](https://docs.djangoproject.com/en/1.10/intro/contributing/) walks through how to create a virtualenv on Python 3.
3. After you’ve created and activated a virtual environment, enter the command `pip install Django` at the shell prompt.
4. Clone the django project to the virtual environment.

5. Install the relevant packages.

```
pip install django-braces
```

## Preparation
Under app/ create models and migrate.

```
python manage.py makemigrations file_upload
python manage.py migrate
```


Run the server


```
python manage.py runserver
```

## Visit web application
Go to http://127.0.0.1:8000/file_upload

## Reference
I used Bootstrap and DropzoneJS library.
