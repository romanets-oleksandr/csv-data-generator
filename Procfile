web: gunicorn core.wsgi
release: python manage.py migrate
worker: celery --app=core worker -l INFO
