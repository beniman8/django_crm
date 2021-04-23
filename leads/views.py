from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context={

    }

    return render(request, 'leads/home.html', context)
