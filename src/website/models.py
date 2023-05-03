from django.db import models
from django.utils.html import format_html
from django.contrib import admin
#from taggit.managers import TaggableManager


class Sezione(models.Model):
    posizione = models.IntegerField(
        blank=True, null=True,
        help_text="posizione della sezione")
   
    class Meta:
        ordering = ['posizione']
        verbose_name_plural = "sezioni"
    
    def __str__(self):
        return 'Sezione ' + str(self.posizione)

    @property
    def pari(self):
        foto_della_sezione = self.photo_set.all()
        pos_pari = []
        
        for f in foto_della_sezione:
            if f.posizione%2 == 0:
                pos_pari.append(f)

        return pos_pari
    
    @property
    def dispari(self):
        foto_della_sezione = self.photo_set.all()
        pos_dispari = []
        
        for f in foto_della_sezione:
            if f.posizione%2 == 1:
                pos_dispari.append(f)

        return pos_dispari
        

class Photo(models.Model):
    url_immagine = models.ImageField(
        upload_to='', 
        null=True, 
        blank=True,
        help_text="seleziona una immagine dal computer, verrà caricata sul server"
        )
    immagine_profilo = models.BooleanField(
        blank=True, 
        default=False,
        help_text="seleziona vero solo se vuoi l'immagine nella parte about in caso contrario farà parte del profilo"
        )
    sezione = models.ForeignKey(
        Sezione, 
        models.SET_NULL, 
        blank=True, 
        null=True,
        help_text="""
            per mostrare questa foto nella sezione portfolio, devi selezionare 
            una sezione di appartenenza
        """
        )
    posizione = models.IntegerField(
        choices=[(1,1),(2,2),(3,3),(4,4)], 
        blank=True, null=True, default='1',
        help_text="le posizioni pari saranno a destra, mentre quelle dispari a sinistra"
        )

    class Meta:
        ordering = ['posizione']

    def image_tag(self):
        return format_html('<img src="{0}" style="height:100px;" />'.format(self.url_immagine.url))

    def __str__(self):
        return str(self.url_immagine)


class Description(models.Model):
    testo = models.TextField(blank=True, null=True)


