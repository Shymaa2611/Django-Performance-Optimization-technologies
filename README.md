## Project
 - it is blog API project where author can create , update , list and delete post .

 ## Objective Of Project 
 - Using Django Optimization Techniques :- 
           - celery and redis to handle background tasks that take long time to process .
           - debug-toolbar that helps to identify the part of code that need to optimize .
           - code profiling technique used to determine how programs use resources such as 
             RAM,time to execute, etc.
           -  Sentry provides a diagnostic metric that shows you where your application is slow 
             and how to solve it. It does this by showing a performance dashboard that features the total time taken by each request-response cycle as well as the level of satisfaction of your users.
 </h2>

## Technologies  
 - Django
 - RESTAPI
 - Celery and redis  
 - swagger-ui
 - debug-toolbar
 - profiling
 - Sentry

## Usage
 - git clone https://github.com/Shymaa2611/Django-project-celery.git
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

