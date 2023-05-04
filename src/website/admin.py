from django.contrib import admin
from django.utils.html import format_html
from .models import *


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('button_id', 
                    'immagine_profilo',
                    'sezione',
                    'posizione',
                    'image_tag',
                    )
    list_filter=[
        'immagine_profilo',
        'sezione',
    ]

    def button_id(self, obj):
        return 'apri foto: {0}'.format(obj.id)
        #return obj.id



class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('short_text',)

    def short_text(self,obj):
        return format_html("<p>{0} [...]</p>".format(obj.testo[:10]))


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    #show_change_link = True
    readonly_fields=('image_tag',)
    exclude=('immagine_profilo',)
    
    


class SezioneAdmin(admin.ModelAdmin):
    list_display = ('section_position', 'immagini')
    inlines=(PhotoInline,)
    def section_position(self,obj):
        return format_html("sezione {}".format(obj.posizione))

    def immagini(self,obj):     

        urls = obj.photo_set.all()
        s = '<div style="box-sizing: border-box; display:flex; flex-wrap:wrap; justify-content: space-around; margin-top:0.5rem; margin-bottom:0.5rem; padding:0">'
        if urls.count() == 1 :
            s += '<img src="/media/{0}" style="max-width:100px; padding:3rem; margin:auto" />'.format(urls[0])
        else:
            s += '<div style="flex: 0 0 50%; max-width: 50%;  display:block;">'
            for par in obj.pari:
                s += '<img src="/media/{0}" style="display:block; max-width:100px; padding:1em 0 1em 0; margin:auto" />'.format(par)
            s += '</div>'
            s += '<div style="flex: 0 0 50%; max-width: 50%; display:block;">'
            for dis in obj.dispari:
                s += '<img src="/media/{0}" style="display:block; max-width:100px; padding:1em 0 1em 0; margin:auto" />'.format(dis)
            s += '</div>'
             
        s += '</div>'
        return format_html(s)




admin.site.register(Photo, PhotoAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Sezione, SezioneAdmin)