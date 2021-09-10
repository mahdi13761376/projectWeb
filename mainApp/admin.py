from django.contrib import admin
from .models import Face, KnownFace, Device
import django_jalali.admin as jadmin

# Register your models here.
admin.site.register(Face)
admin.site.register(KnownFace)
admin.site.register(Device)
