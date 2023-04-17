from sentry_sdk.crons import monitor

from project.celery import app

@app.task
# @sentry_sdk.monitor(monitor_slug='529d421b-29e5-4aa4-bc25-6d825c8302a3')
def tell_the_world(msg):
    print("Thats my message to the world: %s" % msg)


@app.task
# @sentry_sdk.monitor(monitor_slug='eb938fc5-9c7d-4812-a9c9-d660754884c8')
def random_task():
    print("Just a random task")

