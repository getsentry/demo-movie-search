from signal import signal
from django.apps import AppConfig
from django.core.signals import request_started

class ShowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'show'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        # Explicitly connect a signal handler.
        request_started.connect(signals.receive_request_started)
        signals.show_viewed.connect(signals.receive_show_viewed)
        signals.show_viewed.connect(signals.increase_counter)
