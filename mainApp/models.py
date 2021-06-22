from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    serial = models.CharField(max_length=64, blank=False, primary_key=True)
    accuracy = models.FloatField(blank=False)
    mode = models.BooleanField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Face(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    pic_address = models.CharField(max_length=1024, blank=False)


class KnownFace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    pic_address = models.CharField(max_length=1024, blank=False)
