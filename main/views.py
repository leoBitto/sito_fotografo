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
    # richiama tutte le foto portfolio
    photo_portfolio = Photo.objects.filter(ruolo='foto_portfolio')
    print(photo_portfolio)

    # dividile in due queryset, pari e dispari
    foto_pari =[]
    foto_dispari=[]
    for photo in photo_portfolio:
        if photo.posizione % 2 == 0:  # se la posizione è pari
            foto_pari.append(photo)   # aggiungi a foto pari
        else:
            foto_dispari.append(photo)# aggiungi a foto dispari

    # inserisci i dizionari nel context
    context={
        'foto_pari': foto_pari,
        'foto_dispari': foto_dispari,
        'media_url': settings.MEDIA_URL,
    }
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