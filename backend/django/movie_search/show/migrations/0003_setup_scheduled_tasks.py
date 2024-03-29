# Generated by Django 4.1.7 on 2023-04-17 09:55
import json

from django.db import migrations


def setup_scheduled_tasks(apps, schema_editor):
    CrontabSchedule = apps.get_model("django_celery_beat", "CrontabSchedule")
    IntervalSchedule = apps.get_model("django_celery_beat", "IntervalSchedule")
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")

    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=10,
        period="seconds",
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name="Doing some random stuff",
        task="show.tasks.random_task",
    )

    cron_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="*",
        hour="*",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
    )

    PeriodicTask.objects.create(
        crontab=cron_schedule,
        name="Tell the world something",
        args=json.dumps(
            [
                "*Something*",
            ]
        ),
        task="show.tasks.tell_the_world",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("show", "0002_data_load_show_data"),
    ]

    operations = [
        migrations.RunPython(
            setup_scheduled_tasks, reverse_code=migrations.RunPython.noop
        ),
    ]
