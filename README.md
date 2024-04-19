## Project
 
 - it is blog API project where author can create , update , list and delete post .

 ## Objective Of Project 
 
 - using celery and redis to handle background tasks that take long time to process .
 

## Technologies 
 
 - Django
 - RESTAPI
 - Celery and redis
 - swagger-ui

## Usage

 - git clone 
 - pip install -r requirements.txt
 - python manage.py runsever

## Run Celery and process tasks

 - celery -A project worker --loglevel=info  

## Run Project

 - python mangae.py runserver 


## Endpoint urls

 - http://127.0.0.1:8000/blog/
 - http://127.0.0.1:8000/blog/id/

## Swagger-ui
- http://127.0.0.1:8000/docs/

## API SCHEMA URL
- http://127.0.0.1:8000/api_schema/