import os

from celery import Celery, signals
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("project")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# import sentry_sdk
# from sentry_sdk.integrations.celery import CeleryIntegration

# @signals.celeryd_init.connect
# def bla(**kwargs):
#     sentry_sdk.init(
#         dsn='https://d655584d05f14c58b86e9034aab6817f@o447951.ingest.sentry.io/5461230',
#         integrations=[CeleryIntegration(monitor_beat_tasks=True)],
#         environment="local.dev.grace",
#         release="v1.0.7-a1",
#         debug=True,
#     )


# if __name__ == "__main__":
#     setup_scheduled_tasks()
