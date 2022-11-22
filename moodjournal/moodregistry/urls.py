from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoodViewSet
from moodregistry.views import MoodStatisticsView

router = DefaultRouter()
router.register(r'mood', MoodViewSet, basename='mood')

urlpatterns = [
    # provide username of user which is currently connected
    path('', include(router.urls)),
    path('stats/', MoodStatisticsView.as_view()),
]
