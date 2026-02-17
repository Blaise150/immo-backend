release: python manage.py migrate --noinput && python manage.py create_admin
web: gunicorn immo_api.wsgi --log-file -