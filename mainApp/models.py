from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.utils import timezone


class Device(models.Model):
    serial = models.CharField(max_length=64, blank=False, primary_key=True)
    accuracy = models.FloatField(blank=False)
    mode = models.BooleanField(blank=False)
    open = models.BooleanField(blank=False, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class KnownFace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    pic_address = models.CharField(max_length=1024, blank=False, default=' ')
    first_name = models.CharField(max_length=1024, blank=False, default=' ')
    pic_link = models.CharField(max_length=1024, blank=False, default=' ')
    last_name = models.CharField(max_length=1024, blank=False, default=' ')
    datetime = jmodels.jDateTimeField(default=timezone.now())


class Face(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    pic_address = models.CharField(max_length=1024, blank=False)
    pic_link = models.CharField(max_length=1024, blank=False, default=' ')
    datetime = jmodels.jDateTimeField(default=timezone.now())
    known_face = models.ForeignKey(KnownFace, on_delete=models.CASCADE, blank=True, null=True)
    need_to_check = models.BooleanField(blank=False, default=True)
    acc = models.FloatField(blank=False, null=True)
