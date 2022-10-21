from django.shortcuts import HttpResponse, render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello there and Welcome to my very first application!")