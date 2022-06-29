
FROM python:3

#
# Build:
# docker build -t django_backend:v0 .
#
# Run with setting Sentry configuration:
# docker run --rm -p 8000:8000 -it -e SENTRY_DSN_BACKEND=https://1@o1.ingest.sentry.io/1 -e SENTRY_TRACES_SAMPLE_RATE_BACKEND=0.1 django_backend:v0
#

ARG SENTRY_DSN_BACKEND
ENV SENTRY_DSN_BACKEND=$SENTRY_DSN_BACKEND

ARG SENTRY_TRACES_SAMPLE_RATE_BACKEND=1.0
ENV SENTRY_TRACES_SAMPLE_RATE_BACKEND=$SENTRY_TRACES_SAMPLE_RATE_BACKEND

ARG DJANGO_DEBUG=False
ENV DJANGO_DEBUG=$DJANGO_DEBUG

WORKDIR /app

COPY requirements.txt ./

RUN pip install -U pip && pip install -r requirements.txt

COPY movie_search/ .
COPY data/netflix_titles.csv /data/
COPY docker-entrypoint.sh docker-entrypoint.sh

RUN python ./manage.py collectstatic --clear --no-input && python ./manage.py migrate --no-input && python ./manage.py initadmin

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# You could use the same Docker image to run celery, by giving the celery command to your "docker run"
CMD ["gunicorn", "-b", "0.0.0.0:8000", "project.wsgi:application"]