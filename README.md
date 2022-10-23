# Django REST GIS App with JWT & Swagger
## Overview
A simple demo site and REST API for below features.
## TODO
- Address normalization, geocode / reverse geocode, etc.

## Features
- admin page
- Swagger API doc and test
- user register, login, logout
- location GIS Point CRUD
- JWT authentication and token refresh
- devconatiner config with postGIS backend on Docker Desktop with WLS2

## Note
- It is a Development version that use HTTP. Production version should use HTTPS 
- Production version should disable swagger / Django REST API tester
- Swagger API doc and test

## Installation
Install and Activate Python VEnv
```sh
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies.
```sh
cd locationapp/
pip install -r requirements.txt
```

Migrate model to postGIS DB.
```sh
python manage.py migrate
```

## Test

Start the server
```sh
python manage.py createsuperuser
python manage.py runserver
```

Deactivate Python VEnv Afer test
```sh
deactivate
```

Django Admin page
```sh
http://127.0.0.1:8000/admin
```
Django REST test page
```sh
http://127.0.0.1:8000/locations/
```
Swagger UI
```sh
http://127.0.0.1:8000/docs/
```

## Reference
* [DRF CRUD + JWT tutorial](https://medium.com/django-rest/django-rest-framework-b3028b3f0b9)
* [Set default lat for GISModelAdmin](https://stackoverflow.com/questions/70568847/how-to-set-default-lon-default-lat-for-admin-page-using-gismodeladmin)
* [Customize admin display](https://juhanajauhiainen.com/posts/customize-django-admin-with-list-display-property)
* [DRF Swagger](https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje)
* [GeoDjango GIS postGIS App using REST API](https://hvitis.dev/geolocation-tutorial-geodjango-demo-and-gis-postgis-data-to-build-app-using-rest-api)
* [GeoDjango Tutorial](https://realpython.com/location-based-app-with-geodjango-tutorial/)

## License

MIT

