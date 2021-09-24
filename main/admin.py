from django.contrib import admin
from .models import *

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_immagine', 'ruolo', 'sezione', 'posizione', 'tag_list',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('testo',)


class SezioneAdmin(admin.ModelAdmin):
    list_display = ('posizione', )


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Sezione, SezioneAdmin)