from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import viewsets
from .models import *
from .serializers import *


def index(request):
    return render(
        request,
        'backend/index.html',
    )


class CropViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class FarmViewSet(viewsets.ModelViewSet):

    serializer_class = FarmSerializer

    def get_queryset(self):
        return Farm.objects.filter(owner=self.request.user)


class TopLevelViewSet(viewsets.ModelViewSet):

    serializer_class = TopLevelSerializer

    def get_queryset(self):
        node_id = self.request.GET['node_id']
        return TopLevel.objects.filter(node=node_id)


class MiddleLevelViewSet(viewsets.ModelViewSet):

    serializer_class = MiddleLevelSerializer

    def get_queryset(self):
        node_id = self.request.GET['node_id']
        return MiddleLevel.objects.filter(node=node_id)


class BottomLevelViewSet(viewsets.ModelViewSet):

    serializer_class = BottomLevelSerializer

    def get_queryset(self):
        node_id = self.request.GET['node_id']
        return BottomLevel.objects.filter(node=node_id)


class PredictionViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = PredictionSerializer

    def get_queryset(self):
        farm_id = self.request.GET['farm_id']
        return Prediction.objects.filter(farm=farm_id)
