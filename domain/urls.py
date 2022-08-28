from django.contrib import admin
from django.urls import path
from domain import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("index1", views.about, name = "index1" ),
    path("contact", views.contact, name = "contact" ),
    path("about", views.about, name = "about" ),
    
]
