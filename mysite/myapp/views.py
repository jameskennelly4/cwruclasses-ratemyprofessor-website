from django.shortcuts import render

from django.http import HttpResponse

from .models import Class

def index(request):
    AllClasses = Class.objects.all()
    return render(request, 'HomePage.html', {'AllClasses':AllClasses})

def class_by_id(request, Class_id):
    CLASS = Class.objects.get(pk=Class_id)
    return render(request, 'HomePage.html', {'CLASS':CLASS})
