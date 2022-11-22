#from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import PersonMood


class MoodSerializer(serializers.ModelSerializer):
    """
    This serializer defines fields for mood registration.
    It will try to register the users mood when validated.
    """

    class Meta:
        model = PersonMood
        fields = ('user', 'mood', 'weather', 'health', 'activity', 'note',
                  'mood_date', 'created_at', 'updated_at')
