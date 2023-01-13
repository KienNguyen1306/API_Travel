
from rest_framework import viewsets
# Create your views here.
from .models import Travels
from .serializers import *

class Travelviewset(viewsets.ModelViewSet):
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializers


class TestimonialsDataviewset(viewsets.ModelViewSet):
    queryset = TestimonialsData.objects.all()
    serializer_class = TestimonialsDataSerializers

class FrequentlyAskedDatasviewset(viewsets.ModelViewSet):
    queryset = FrequentlyAskedDatas.objects.all()
    serializer_class = FrequentlyAskedDatasSerializers



class PostDatasviewset(viewsets.ModelViewSet):
    queryset = PostDatas.objects.all()
    serializer_class = PostDatasSerializers


class Teamsdataviewset(viewsets.ModelViewSet):
    queryset = Teamsdata.objects.all()
    serializer_class = TeamsdataSerializers


class FeaturedServicwesDatasviewset(viewsets.ModelViewSet):
    queryset = FeaturedServicwesDatas.objects.all()
    serializer_class = FeaturedServicwesDatasSerializers