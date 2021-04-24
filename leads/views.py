from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def home_page(request):
    leads = Lead.objects.all()
    context={
        'leads':leads,

    }

    return render(request, 'leads/home.html', context)


def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead':lead,
    }
    return render(request, 'leads/detail.html', context)