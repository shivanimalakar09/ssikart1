from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"home.html")

def about (request):
    return HttpResponse("<h1> e-commerce website project1 by shivani </h1>")

def home(request):
    return HttpResponse("<h1> welcome to ssikart </h1>")
