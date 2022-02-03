from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = (
        (SUBSCRIBER, 'Abonné')
    )
    profile_photo = models.ImageField(verbose_name='photo de profil')
