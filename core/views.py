from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    ctx = {
        'projects': Project.objects.all()[:4]
    }

    return render(request, 'index.html', ctx)


def pricing(request):
    return render(request, 'pricing.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    ctx = {
        'projects': Project.objects.all()
    }
    return render(request, 'projects_grid.html', ctx)


def project(request, id):
    return render(request, 'project.html')
