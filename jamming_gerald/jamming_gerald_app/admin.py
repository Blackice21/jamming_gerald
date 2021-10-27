from django.contrib import admin
from .models import Music, My_pictures
# Register your models here.
admin.site.register(Music)
admin.site.register(My_pictures)
admin.site.site_header='Jamming Gerald'