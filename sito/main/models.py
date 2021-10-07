from django.db import models
#from taggit.managers import TaggableManager


class Sezione(models.Model):
    posizione = models.IntegerField(blank=True, null=True)
   
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

        print(pos_pari)

        return pos_pari
    
    @property
    def dispari(self):
        foto_della_sezione = self.photo_set.all()
        pos_dispari = []
        
        for f in foto_della_sezione:
            if f.posizione%2 == 1:
                pos_dispari.append(f)

        print(pos_dispari)

        return pos_dispari


class Photo(models.Model):
    url_immagine = models.ImageField(upload_to='', null=True, blank=True)
    ruolo = models.CharField(
        choices=[
            ('immagine_profilo', 'about'),
            ('foto_portfolio', 'portfolio')
            ],  
        max_length=100,
        null=True)
    sezione = models.ForeignKey(Sezione, models.SET_NULL, blank=True, null=True)
    posizione = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4)], blank=True, null=True, default=1)
    #tags = TaggableManager(blank=True)

    def __str__(self):
        return str(self.url_immagine) + '(p:' + str(self.posizione) + ',s:' + str(self.sezione) + ')'

class Description(models.Model):
    testo = models.TextField(blank=True, null=True)

