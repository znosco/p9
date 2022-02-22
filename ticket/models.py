from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
class Ticket(models.Model):
    def __str__(self):
        return self.title
    IMAGE_MAX_SIZE = (100, 100)
    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
    
    title = models.CharField(max_length=96)
    description = models.TextField(max_length=2048)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    def __str__(self):
        return self.headline
    
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    description = models.TextField(max_length=8192, blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)