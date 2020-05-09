from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    ctx = {
        'projects': Project.objects.all().order_by('-id')[:6]
    }

    return render(request, 'index.html', ctx)


def pricing(request):
    return render(request, 'pricing.html')


def about(request):
    partners = Partner.objects.all().order_by('-id')
    ctx = {
        'partners': partners
    }

    return render(request, 'about.html', ctx)


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    ctx = {
        'projects': Project.objects.all()
    }
    return render(request, 'projects_grid.html', ctx)


def project(request, slug):

    return render(request, 'project.html')
