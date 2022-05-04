from django.contrib import admin 
from django.urls import path
from home.view import home

urlpatterns = [
    path("", home, name="ssi-home"),   
    path("", about, name="ssi-about",)    
    path("", home, name="ssi-home")    
    
]
