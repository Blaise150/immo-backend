release: python manage.py migrate --noinput && python create_superuser.py
web: gunicorn immo_api.wsgi --log-file -