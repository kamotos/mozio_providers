web: newrelic-admin run-program gunicorn --pythonpath="$PWD/providers" wsgi:application
worker: python providers/manage.py rqworker default