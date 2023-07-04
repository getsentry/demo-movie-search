from django.http import HttpResponse
from django.shortcuts import render
from sentry_sdk.hub import Hub


def root(request):
    context = {}
    return render(request, "root.html", context)


def server_side(request):
    context = {"meta": Hub.current.trace_propagation_meta}
    return render(request, "server_side.html", context)
