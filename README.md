# Django/celery CSVgenerator

It is a service for generating CSV files with fake data based on the types you passed into.
[Heroku](https://djangocsvgenerator.herokuapp.com/scheme_list/)

## Running localy

To run localy you need to clone the repository
 ```
 git clone git@github.com/KhirilovA/django-celery-csvgenerator.git
 ```
 Install requirements
 ```
 pip install requirements.txt
 ```
 Make your own SECRET_KEY and put it in settings
 
 Connect to yoour AWS S3 Bucket or save data to media/
 
 And run the project applying migrations:
 ```
 python manage.py migrate
 python manage.py runserver
 ```
 If you using windows then:
 ```
 celery -A generator.celery worker --pool=solo -l info
 ```
 else:
 ```
 celery -A generator.celery worker -l info
 ```
