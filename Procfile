release: python manage.py migrate --noinput && python create_properties.py
web: gunicorn immo_api.wsgi --log-file -