from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>about</a>")
def about(request):
    return HttpResponse("Rango says here is the about page <br/> <a href='/rango'>index</a>")
