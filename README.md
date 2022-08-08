# ZSSN Backend

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

| Item | id | points
| ------ | ------ | -----|
| Ammuntion | 4 | 1 |
| Medication | 3 | 2 |
| Food | 1 | 3 |
| Water | 2 | 4 | 

Write about 1-2 paragraphs describing the purpose of your project.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Python==3.10.5
Django==4.0.6
Django-RestFramework==3.13.1
PostgreSQL
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Clone the repository

```
git clone https://github.com/ailsonazevedo/zssn-api
```

Create virtual environment

```
$ python -m venv 'nameEnv'
```
Activate venv
```
$ 'nameEnv'\Scripts\activate
```
Install dependencies
```
$ pip install -r requirements.txt
```
Connect to database
```
settings.py

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'NAMEDB',

        'USER': 'USERNAME',

        'PASSWORD': 'PASSWORD',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}
```
Migrate
```
$ py manage.py migrate
```
Create SuperUser
```
$ py manage.py createsuperuser
```
Start Server
```
$ py manage.py runserver
```


## Endpoints
```

```
End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
