import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from main_page.models import Meniu
from main_page.serializer import MeniuSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required




def main_page(request):
    meniu = list(Meniu.objects.all())
    meniu.sort(key = (lambda x: x.date_created))

    context = {
        'username': 'Daniel',
        'logged_in': True,
        'current_time': datetime.now(),
        'meniu': meniu
    }

    return render(request, 'Main_page.html', context)

def create_meniu(request):
    meniu1 = Meniu()
    meniu1.title = "Breakfast"
    meniu1.client = "Daniel"
    meniu1.maniu_number = 2
    meniu1.save()
    return HttpRequest("Boon Apetit")

def about_restaurant(request):
    return render(request, 'about_restaurant')

class MainViewSet(viewsets.ModelViewSet):
    queryset = Meniu.objects.all()
    serializer_class = MeniuSerializer
