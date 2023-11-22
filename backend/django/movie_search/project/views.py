from django.http import HttpResponse
from django.shortcuts import render
from sentry_sdk.hub import Hub


def root(request):
    context = {}
    return render(request, "root.html", context)


def server_side(request):
    context = {"meta": Hub.current.trace_propagation_meta}
    return render(request, "server_side.html", context)


def page_not_found_view(request, exception):
    context = {
        exception: exception,
    }
    import time
    time.sleep(1)
    return render(request, "404.html", context)
