web: gunicorn CSVgenerator.wsgi
worker: celery -A generator worker -B --loglevel=info