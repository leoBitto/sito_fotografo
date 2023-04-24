from django.contrib import admin
from django.utils.html import format_html
from .models import *

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'ruolo',
                    'sezione',
                    'posizione',
                    #'tag_list',
                    'image_tag',
                    )

    #def get_queryset(self, request):
     #   return super().get_queryset(request).prefetch_related('tags')

   # def tag_list(self, obj):
     #   return u", ".join(o.name for o in obj.tags.all())
    def image_tag(self,obj):
        return format_html('<img src="{0}" style="height:100px;" />'.format(obj.url_immagine.url))

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('testo',)


class SezioneAdmin(admin.ModelAdmin):
    list_display = ('posizione', 'immagini')

    def immagini(self,obj):
        urls = obj.photo_set.all()
        s = ''
        for f in urls:
            s += '<img src="/media/{0}" style="height:100px; padding:5px" />'.format(f)
        return format_html(s)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Sezione, SezioneAdmin)