from django.shortcuts import render
from .models import *
from django.conf import settings

#pagina iniziale
def index(request):
    context={}
    return render(request, 'index.html', context)
    

#pagina portfolio
def portfolio(request):

    sezioni = Sezione.objects.all()
    context={
        'sezioni':sezioni,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, 'portfolio.html', context)

#foto ingrandita
def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'foto':photo,
        'media_url':settings.MEDIA_URL,
    }
    return render(request, 'photo.html', context)


#pagina about
def about(request):
    photo = Photo.objects.get(ruolo='immagine_profilo')
    description = Description.objects.all()
    context={
        'photo':photo,
        'description':description,
        'media_url':settings.MEDIA_URL,
    }
    return render(request, 'about.html', context)
    

#pagina contacts
def contacts(request):
    context={}
    return render(request, 'contacts.html', context)