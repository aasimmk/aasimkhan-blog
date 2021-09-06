web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn myblog.wsgi --error-logfile - --log-file - --bind="0.0.0.0:$PORT"
