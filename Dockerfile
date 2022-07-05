
FROM python:3

#
# Build:
# docker build -t django_backend:v0 .
#
# Run with setting Sentry configuration:
# docker run --rm -p 8000:8000 -it -e DJANGO_SENTRY_DSN=https://1@o1.ingest.sentry.io/1 -e DJANGO_SENTRY_TRACES_SAMPLE_RATE=0.1 django_backend:v0
#

ARG DJANGO_SENTRY_DSN
ENV DJANGO_SENTRY_DSN=$DJANGO_SENTRY_DSN

ARG DJANGO_SENTRY_RELEASE
ENV DJANGO_SENTRY_RELEASE=$DJANGO_SENTRY_RELEASE

ARG DJANGO_SENTRY_ENVIRONMENT
ENV DJANGO_SENTRY_ENVIRONMENT=$DJANGO_SENTRY_ENVIRONMENT

ARG DJANGO_SENTRY_TRACES_SAMPLE_RATE=1.0
ENV DJANGO_SENTRY_TRACES_SAMPLE_RATE=$DJANGO_SENTRY_TRACES_SAMPLE_RATE

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