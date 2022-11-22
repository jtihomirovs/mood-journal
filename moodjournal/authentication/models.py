from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, default='')
    image = models.ImageField(
        default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return self.username

    # Resize image on save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.image.path)
