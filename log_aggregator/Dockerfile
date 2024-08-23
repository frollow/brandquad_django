FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'log_aggregator.settings'
ENV PGSSLCERT /tmp/postgresql.crt

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini
COPY nginx_json_logs.txt nginx_json_logs.txt

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && apt-get update \
     && apt-get install -y --no-install-recommends gettext \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

RUN chmod +x run_uwsgi.sh
RUN chown -R www-data:www-data /var/www/media/ && chmod -R 775 /var/www/media/

COPY . .

EXPOSE 8000

ENTRYPOINT ["./run_uwsgi.sh"]
