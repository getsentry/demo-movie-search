
FROM python:3

#
# Build:
# docker build -t django_backend:v0 .
#
# Run with setting Sentry configuration:
# docker run --rm -p 8000:8000 -it -e DJANGO_SENTRY_DSN=https://1@o1.ingest.sentry.io/1 -e DJANGO_SENTRY_TRACES_SAMPLE_RATE=0.1 django_backend:v0
#

WORKDIR /app

COPY backend/django/requirements.txt ./

RUN pip install -U pip && pip install -r requirements.txt

COPY backend/django/movie_search .
COPY data/netflix_titles.csv /data/
COPY backend/django/docker-entrypoint.sh docker-entrypoint.sh

RUN python ./manage.py collectstatic --clear --no-input

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# You could use the same Docker image to run celery, by giving the celery command to your "docker run"
CMD ["gunicorn", "-b", "0.0.0.0:8000", "project.wsgi:application"]
