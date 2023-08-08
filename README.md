# cookie-stand-api

- Lab: Class 34
- Author: Manuch Sadri

## Overview

Build out a Restful API as well as a user facing site for a Cookie company.

## Feature Tasks and Requirements

### Templates
Choose one:
  - [ ] Use your own template
  - [X] Use API Quick Start Template

### Models
- [X] The `CookieStand` model must contain:
```python
    location = models.CharField(max_length=256)
        owner = models.ForeignKey(
            get_user_model(), on_delete=models.CASCADE, null=True, blank=True
        )
        description = models.TextField(blank=True)
        hourly_sales = models.JSONField(default=list, null=True)
        minimum_customers_per_hour = models.IntegerField(default=0)
        maximum_customers_per_hour = models.IntegerField(default=0)
        average_cookies_per_sale = models.FloatField(default=0)

        def __str__(self):
            return self.location
```
- [X] Once changes are complete make migrations, migrate, and test locally.

### Database Deployment
- [X] Host your Database at ElephantSQL

### Site Deployment:
- [X] Run your site locally, but the Database should be remote.

## Stretch Goals
- [ ] Add functionality so that when a JSON array of hourly_sales is not provided at creation time it will be generated with random numbers based on minimum/maximum customers per hour and average cookies per sale.

## Set-up

- create+run virtual environment:
  - $ ```python3.11 -m venv .venv```
  - $ ```source .venv/bin/activate```
- install requirements:
  - $ ```pip install -r requirements.txt```
- run app/server:
  - $ ```python manage.py runserver```
- front-end URLs:
  - http://localhost:8000/ - home
  - http://localhost:8000/admin/ - admin panel
  - http://localhost:8000/api/v1/cookie_stand/ - non-styled Django front-end

## Tests

- n/a

---

# api-quick-start

Template Project for starting up CRUD API with Django Rest Framework

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `things` folder to the app name of your choice
- Search through entire code base for `Thing`,`Things` and `things` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update ThingModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`
