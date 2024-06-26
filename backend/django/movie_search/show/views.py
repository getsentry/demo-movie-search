from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.cache.decorators import cache_response

from show.models import Show, Person
from show.serializers import ShowListSerializer, ShowSerializer, PersonSerializer

from . import signals


def index(request):
    bla = 1 / 0
    return HttpResponse("Hello, world. You're at the SHOW index.")


import asyncio
from django.http import HttpResponse
from django.views import View


class ShowAsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform view logic using await.
        await asyncio.sleep(0.2)

        async for show in Show.objects.filter(title__startswith="A"):
            print(f"AAA {show.title} ({show.release_year})")
            # book = await show.books.afirst()

        async for show in Show.objects.filter(title__startswith="B"):
            print(f"BBB {show.title} ({show.release_year})")
            # book = await show.books.afirst()self

        async for show in Show.objects.filter(title__startswith="C"):
            print(f"CCC {show.title} ({show.release_year})")
            # book = await show.books.afirst()

        return HttpResponse("Hello async world!")


class PersonViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """

    serializer_class = PersonSerializer

    def get_queryset(self):
        """
        This view should return a list of all Persons
        containing the search string in name.
        """
        queryset = Person.objects.all()
        q = self.request.query_params.get("q", None)
        if q:
            search_filter = Q(name__icontains=q)
            queryset = queryset.filter(search_filter)

        return queryset


class ShowViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows shows to be viewed or edited.
    """

    serializer_class = ShowListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShowListSerializer
        return ShowSerializer

    def get_queryset(self):
        """
        This view should return a list of all Shows
        containing the search string in title, director, or cast.
        """
        queryset = Show.objects.all()
        q = self.request.query_params.get("q", None)
        if q:
            search_filter = (
                Q(title__icontains=q)
                | Q(director__name__icontains=q)
                | Q(cast__name__icontains=q)
            )
            queryset = queryset.filter(search_filter).distinct()

        return queryset

    @cache_response()
    def retrieve(self, request, *args, **kwargs):
        """
        Return a list of all shows.
        """
        show = self.get_object()
        serializer = ShowSerializer(show, context={"request": self.request})

        signals.show_viewed.send(sender=self.__class__)

        return Response(serializer.data)
