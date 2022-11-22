from django.db import models
from django.conf import settings

# Create your models here.

# Person mood model


class PersonMood(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    EXCITED = 'Excited'
    HAPPY = 'Happy'
    NEUTRAL = 'Neutral'
    BORED = 'Bored'
    SAD = 'Sad'
    ANGRY = 'Angry'

    SUNNY = 'Sunny'
    RAINY = 'Rainy'
    CLOUDY = 'Cloudy'
    SNOWY = 'Snowy'
    WINDY = 'Windy'

    HEALTHY = 'Healthy'
    SICK = 'Sick'

    WORK = 'Work'
    FREE = 'Free'

    MOOD_CHOICES = [
        (EXCITED, 'Excited'),
        (HAPPY, 'Happy'),
        (NEUTRAL, 'Neutral'),
        (BORED, 'Bored'),
        (SAD, 'Sad'),
        (ANGRY, 'Angry')
    ]

    WEATHER_CHOICES = [
        (SUNNY, 'Sunny'),
        (RAINY, 'Rainy'),
        (CLOUDY, 'Cloudy'),
        (SNOWY, 'Snowy'),
        (WINDY, 'Windy')
    ]

    HEALTH_CHOICES = [
        (HEALTHY, 'Healthy'),
        (SICK, 'Sick')
    ]

    ACTIVITY_CHOICES = [
        (WORK, 'Work'),
        (FREE, 'Free')
    ]

    mood = models.CharField(
        null=False,
        max_length=20,
        choices=MOOD_CHOICES
    )

    weather = models.CharField(
        null=False,
        max_length=20,
        choices=WEATHER_CHOICES
    )

    health = models.CharField(
        null=False,
        max_length=20,
        choices=HEALTH_CHOICES
    )

    activity = models.CharField(
        null=False,
        max_length=20,
        choices=ACTIVITY_CHOICES
    )

    note = models.TextField(
        null=False,
        max_length=200,
        default='',
        blank=True
    )

    mood_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ', ' + str(self.created_at)
