import django.dispatch
import time

from opentelemetry import trace

show_viewed = django.dispatch.Signal()

tracer = trace.get_tracer(__name__)

@tracer.start_as_current_span("receive_request_started")
def receive_request_started(sender, **kwargs):
    time.sleep(0.123)
    print("[SIGNAL] Request started!")

@tracer.start_as_current_span("receive_show_viewed")
def receive_show_viewed(sender, **kwargs):
    time.sleep(0.234)
    print(f"[SIGNAL] Show viewed by {sender}")

@tracer.start_as_current_span("increase_counter_orig")
def increase_counter_orig(sender, **kwargs):
    time.sleep(0.345)
    print(f"[SIGNAL] Increase counter for {sender}")


from functools import partial

increase_counter = partial(increase_counter_orig)