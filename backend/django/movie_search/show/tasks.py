import random
import time

from project.celery import app


@app.task
def trigger_notifications(show_id):
    print("Triggering notifications for show: %s" % show_id)
    time.sleep(random.random())


@app.task
def random_task():
    print("This task does nothing")


@app.task
def tell_the_world(msg):
    print("My message to you: %s" % msg)