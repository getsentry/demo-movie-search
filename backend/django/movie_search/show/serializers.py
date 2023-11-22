from show.models import Person
from show.models import Show
from rest_framework import serializers
from rest_framework.reverse import reverse_lazy
from django.db.models.expressions import RawSQL

import sentry_sdk


def recursive_something(level=0):
    if level > 100:
        return 1 / "a"

    return recursive_something(level + 1)


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    href = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            "pk",
            "href",
            "name",
        ]

    def get_href(self, obj):
        return reverse_lazy(
            "persons-detail", args=[obj.pk], request=self.context["request"]
        )


class ShowListSerializer(serializers.HyperlinkedModelSerializer):
    href = serializers.SerializerMethodField()

    director = PersonSerializer(many=True)
    cast = PersonSerializer(many=True)

    class Meta:
        model = Show
        fields = [
            "pk",
            "href",
            "show_type",
            "title",
            "director",
            "cast",
        ]

    def get_href(self, obj):
        return reverse_lazy(
            "shows-detail", args=[obj.pk], request=self.context["request"]
        )


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    href = serializers.SerializerMethodField()

    director = PersonSerializer(many=True)
    director_special = serializers.SerializerMethodField()
    cast = PersonSerializer(many=True)

    class Meta:
        model = Show
        fields = [
            "pk",
            "href",
            "show_type",
            "title",
            "director",
            "director_special",
            "cast",
            "countries",
            "date_added",
            "release_year",
            "rating",
            "duration",
            "categories",
            "description",
        ]

    def get_director_special(self, obj):

        # Add more information to Sentry events.
        from django.conf import settings

        settings_dict = settings.__dict__["_wrapped"].__dict__
        sentry_sdk.set_context("django_settings", settings_dict)

        for key in settings_dict:
            val = settings_dict[key]
            if isinstance(val, str) and val and len(key) < 32:
                sentry_sdk.set_tag(key, val)

        make_query_slow = RawSQL("select pg_sleep(%s)", (0.02,))

        if (
            obj.director.all().first()
            and "scorsese" in obj.director.all().first().name.lower()
        ):
            return obj.director.filter(name__contains="Martin Scorsese").first()
            return recursive_something()

        # Try to trigger an N+1 performance error:
        for country in obj.countries.split(","):
            newest_shows_of_country = Show.objects.filter(
                countries__contains=country
            ).order_by("-release_year")[:10]
            for show in newest_shows_of_country:
                show_detail = Show.objects.filter(pk=show.id).annotate(
                    sleep=make_query_slow
                )[0]
                print(f"{show_detail.title} ({show_detail.release_year})")

        return f"~~~ {obj.director.all().first()} ~~~"

    def get_href(self, obj):
        return reverse_lazy(
            "shows-detail", args=[obj.pk], request=self.context["request"]
        )
