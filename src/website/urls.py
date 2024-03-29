from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name="index"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts"),
    path('photo/<str:pk>', views.photo, name="photo"),
]