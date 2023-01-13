from rest_framework import serializers
from .models import *

class TravelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ['id','image','name','sub']

class TestimonialsDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestimonialsData
        fields = "__all__"

class FrequentlyAskedDatasSerializers(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedDatas
        fields = "__all__"


class PostDatasSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostDatas
        fields = "__all__"


class TeamsdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teamsdata
        fields = "__all__"


class FeaturedServicwesDatasSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeaturedServicwesDatas
        fields = "__all__"