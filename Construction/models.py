from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from geoposition.fields import GeopositionField


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

