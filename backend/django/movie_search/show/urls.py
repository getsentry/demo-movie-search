from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("async/", views.ShowAsyncView.as_view()),
]
