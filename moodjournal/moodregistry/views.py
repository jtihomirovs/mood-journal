from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import PersonMood
from .serializers import MoodSerializer


# Create your views here.
class MoodViewSet(viewsets.ModelViewSet):
    # This view is for adding a new entry
    queryset = PersonMood.objects.all().order_by('created_at')
    serializer_class = MoodSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.id)


class MoodStatisticsView(views.APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        excited_days = PersonMood.objects.all().filter(
            user=self.request.user.id, mood='Excited').count()
        happy_days = PersonMood.objects.all().filter(
            user=self.request.user.id, mood='Happy').count()
        neutral_days = PersonMood.objects.all().filter(
            user=self.request.user.id, mood='Neutral').count()
        bored_days = PersonMood.objects.all().filter(
            user=self.request.user.id, mood='Bored').count()
        sad_days = PersonMood.objects.all().filter(
            user=self.request.user.id, mood='Sad').count()
        angry_days = PersonMood.objects.all().filter(
            user=self.request.user.id, mood='Angry').count()

        sunny_days = PersonMood.objects.all().filter(
            user=self.request.user.id, weather='Sunny').count()
        rainy_days = PersonMood.objects.all().filter(
            user=self.request.user.id, weather='Rainy').count()
        cloudy_days = PersonMood.objects.all().filter(
            user=self.request.user.id, weather='Cloudy').count()
        snowy_days = PersonMood.objects.all().filter(
            user=self.request.user.id, weather='Snowy').count()
        windy_days = PersonMood.objects.all().filter(
            user=self.request.user.id, weather='Windy').count()

        healthy_days = PersonMood.objects.all().filter(
            user=self.request.user.id, health='Healthy').count()
        sick_days = PersonMood.objects.all().filter(
            user=self.request.user.id, health='Sick').count()

        work_days = PersonMood.objects.all().filter(
            user=self.request.user.id, activity='Work').count()
        free_days = PersonMood.objects.all().filter(
            user=self.request.user.id, activity='Free').count()

        response_data = {
            'mood': {
                'excited_days': excited_days,
                'happy_days': happy_days,
                'neutral_days': neutral_days,
                'bored_days': bored_days,
                'sad_days': sad_days,
                'angry_days': angry_days
            },
            'weather': {
                'sunny_days': sunny_days,
                'rainy_days': rainy_days,
                'cloudy_days': cloudy_days,
                'snowy_days': snowy_days,
                'windy_days': windy_days
            },
            'health': {
                'healthy_days': healthy_days,
                'sick_days': sick_days
            },
            'activity': {
                'work_days': work_days,
                'free_days': free_days
            }
        }

        return Response(data=response_data)
