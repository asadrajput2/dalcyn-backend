from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'crop', CropViewSet)
router.register(r'farm', FarmViewSet, basename='farm')
router.register(r'top_level',
                TopLevelViewSet, basename='top_level')
router.register(r'middle_level',
                MiddleLevelViewSet, basename='middle_level')
router.register(r'bottom_level',
                BottomLevelViewSet, basename='bottom_level')
router.register(r'prediction',
                PredictionViewSet, basename='prediction')

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
]
