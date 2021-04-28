from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name="sito"),
    path('menu', views.menu, name="menu"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts"),
    path('navdev', views.navdev, name="navdev"),
]