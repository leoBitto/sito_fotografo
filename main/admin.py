from django.contrib import admin
from .models import *

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_immagine', 'ruolo', 'posizione')

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('testo',)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Description, DescriptionAdmin)