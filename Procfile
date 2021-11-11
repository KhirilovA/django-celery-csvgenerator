web: gunicorn CSVGenerator.wsgi
worker: celery -A generator worker -B --loglevel=info