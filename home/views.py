from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def goofy(request):
    return HttpResponse("Goofy Goober Rock!")

def index(request):
    return HttpResponse("Hello World!")
