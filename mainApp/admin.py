from django.contrib import admin
from .models import Face, KnownFace, Device

# Register your models here.
admin.site.register(Face)
admin.site.register(KnownFace)
admin.site.register(Device)
