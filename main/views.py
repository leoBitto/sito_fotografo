from django.shortcuts import render
from .models import *
from django.conf import settings

#pagina iniziale
def index(request):
    context={}
    return render(request, 'index.html', context)


#pagina menu
def menu(request):
    context={}
    return render(request, 'menu.html', context)


#pagina portfolio
def portfolio(request):
    context={}
    return render(request, 'portfolio.html', context)


#pagina about
def about(request):
    photo = Photo.objects.get(ruolo='immagine_profilo')
    context={
        'photo':photo,
        'media_url':settings.MEDIA_URL,
    }
    return render(request, 'about.html', context)
    

#pagina contacts
def contacts(request):
    context={}
    return render(request, 'contacts.html', context)