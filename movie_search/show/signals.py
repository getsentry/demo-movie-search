import django.dispatch
import time


show_viewed = django.dispatch.Signal()


def receive_request_started(sender, **kwargs):
    time.sleep(0.123)
    print("[SIGNAL] Request started!")


def receive_show_viewed(sender, **kwargs):
    time.sleep(0.234)
    print(f"[SIGNAL] Show viewed by {sender}")


def increase_counter_orig(sender, **kwargs):
    time.sleep(0.345)
    print(f"[SIGNAL] Increase counter for {sender}")



from functools import partial

increase_counter = partial(increase_counter_orig)