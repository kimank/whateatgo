from django.shortcuts import render
from django.http import HttpResponse

from .models import Food

def index(request):
    return HttpResponse("Hello world")