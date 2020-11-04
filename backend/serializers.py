from rest_framework import serializers
from .models import *


class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop
        fields = '__all__'


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = '__all__'


class FarmCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = '__all__'


class TopLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TopLevel
        fields = '__all__'


class MiddleLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MiddleLevel
        fields = '__all__'


class BottomLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BottomLevel
        fields = '__all__'


class PredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediction
        fields = '__all__'
