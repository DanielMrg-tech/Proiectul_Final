import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from main_page.forms import MeniuForm
from main_page.models import Meniu
from main_page.serializer import MeniuSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



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
    meniu1.meniu_number = 2
    meniu1.save()
    return HttpResponse("Boon Apetit")

def about_restaurant(request):
    return render(request, 'about_restaurant.html')

class MainViewSet(viewsets.ModelViewSet):
    queryset = Meniu.objects.all()
    serializer_class = MeniuSerializer

menus_list = ['Salad', "Daniel", '12']

def meniu_by_user(request: HttpRequest, user_id: int):
    menus = list(Meniu.objects.filter(created_by=user_id))
    menus.sort(key = (lambda x: x.date_created), reverse=True)

    context = {
        'menus': menus
    }
    return render(request, 'meniu.html', context)

@csrf_exempt
def meniu_view_simple(request: HttpRequest):
    if request.method == 'GET':
        menus_list.sort(reverse=True)
        context = {
            'menus': menus_list
        }
        return render(request, 'main_page/meniu.html', context)
    elif request.method == "POST":
        data = json.loads(request.body)
        meniu_title = data["title"]
        menus_list.append(meniu_title)
        return HttpResponse("")

@csrf_exempt
@login_required
def meniu_view(request: HttpRequest):
    if request.method == "GET":
        context = {
            'form': MeniuForm()
        }
        return render(request, 'create_meniu.html', context)
    elif request.method == "POST":
        form_with_data = MeniuForm(request.POST, request.FILES)
        if form_with_data.is_valid():
            meniu_instance = form_with_data.save(commit=False)
            meniu_instance.created_by = request.user
            meniu_instance.save()
            return redirect('meniu_by_user', user_id=request.user.id)
        else:
            return HttpResponse(form_with_data.errors)


@login_required()
def update_meniu(request, pk):
    meniu = get_object_or_404(Meniu, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = MeniuForm(request.POST, request.FILES, instance=meniu)
        if form.is_valid():
            form.save()
            return redirect('meniu_by_user', user_id=request.user.id)
    else:
        form = MeniuForm(instance=meniu)

    return render(request, 'meniu_form.html', {'form': form, 'meniu': meniu})


@login_required()
def delete_meniu(request, pk):
    meniu = get_object_or_404(Meniu, pk=pk, created_by=request.user)
    if request.method == "POST":
        meniu.delete()
        return redirect('meniu_by_user', user_id=request.user.id)
    else:
        return render(request, "meniu_confirm_delete.html", {'meniu': meniu})
