from django.shortcuts import render
from django.http import HttpResponse

from .models import Food

def index(request):
    return render(request, 'mealrcmds/index.html')

def region(request):
	foods = Food.objects.all()
	return render(request, 'mealrcmds/select.html', {"region" : request.POST['choice']})

def select(request):
	foods = Food.objects.all()
	print(request.POST['choice'])
	context = {'foods': foods}
	return render(request, 'mealrcmds/result.html', context)