from show.models import Show
from rest_framework import serializers


class ShowListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = [
            'pk',
            'show_type',
            'title',
            'director',
            'cast',
        ]

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    director_special = serializers.SerializerMethodField()
    
    class Meta:
        model = Show
        fields = [
            'pk',
            'show_type',
            'title',
            'director',
            'director_special',
            'cast',
            'countries',
            'date_added',
            'release_year',
            'rating',
            'duration',
            'categories',
            'description',
        ]


    def get_director_special(self, obj):

        if "scorsese" in obj.director.lower():
            bla = 1 / 0

        return f'~~~ {obj.director} ~~~'