web: gunicorn CSVgenerator.wsgi
celery: celery -A generator.celery worker -B --loglevel=info