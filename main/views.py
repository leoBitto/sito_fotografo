from django.shortcuts import render
from .models import *

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
    context={}
    return render(request, 'about.html', context)
    

#pagina contacts
def contacts(request):
    context={}
    return render(request, 'contacts.html', context)