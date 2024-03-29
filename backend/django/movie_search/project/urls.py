"""shows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from show import views as show_views

from project import views

router = routers.DefaultRouter()
router.register(r"shows", show_views.ShowViewSet, basename="shows")
router.register(r"persons", show_views.PersonViewSet, basename="persons")


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", views.root),
    path("server_side/app/", views.server_side),
    path("admin/", admin.site.urls),
    path("show/", include("show.urls")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("sentry-debug/", trigger_error),
]

handler404 = "project.views.page_not_found_view"