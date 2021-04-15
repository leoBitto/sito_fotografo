from django.shortcuts import render
from django.http import HttpResponse

#pagina iniziale
def index(request):
    return HttpResponse('index')


#pagina menu
def menu(request):
    return HttpResponse('menu')


#pagina portfolio
def portfolio(request):
    return HttpResponse('portfolio')


#pagina about
def about(request):
    return HttpResponse('about')
    

#pagina contacts
def contacts(request):
    return HttpResponse('contacts')