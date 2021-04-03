from django.urls import path
from . import views


urlpatterns=[
    path('', views.sito, name="sito")
]