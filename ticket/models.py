from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

class Ticket(models.Model):
    title = models.CharField(max_length=96)
    description = models.TextField(max_length=2048)
    time_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
