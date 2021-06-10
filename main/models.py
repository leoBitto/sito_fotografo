from django.db import models

# Create your models here.
class Photo(models.Model):
    url_immagine = models.ImageField(upload_to='', null=True, blank=True)
    ruolo = models.CharField(max_length=100, null=True)
    posizione = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['posizione']

class Description(models.Model):
    testo = models.TextField(blank=True, null=True)