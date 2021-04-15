from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('url_immagine', 'ruolo', 'posizione')

admin.site.register(Photo, PhotoAdmin)