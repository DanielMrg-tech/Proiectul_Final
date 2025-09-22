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
from django.contrib.auth.models import AnonymousUser




def main_page(request):
    # obține parametru "sort" din query string (ex: ?sort=title_asc)
    sort = request.GET.get('sort', 'date_desc')
    # dacă user-ul este anonim, se afișează toate meniurile
    # dacă e autentificat, se afișează doar meniurile lui
    if isinstance(request.user, AnonymousUser):
        queryset = Meniu.objects.all()
    else:
        queryset = Meniu.objects.filter(created_by = request.user)
    # sortarea listei în funcție de parametru
    if sort == 'date_asc':
        queryset = queryset.order_by('date_created')
    elif sort == 'date_desc':
        queryset = queryset.order_by('-date_created')
    elif sort == 'title_asc':
        queryset = queryset.order_by('title')
    elif sort == 'title_desc':
        queryset = queryset.order_by('-title')

    meniu = list(queryset)
    # datele transmise către template
    context = {
        'user': request.user,
        'menus': meniu,
        'logged_in': request.user.is_authenticated,
        'current_time': datetime.now(),
        'sort': sort,
    }
    return render(request, 'Main_page.html', context)

def create_meniu(request):
    # creează rapid un meniu hardcodat și îl salvează în DB
    meniu1 = Meniu()
    meniu1.title = "Breakfast"
    meniu1.produs = "rosii"
    meniu1.meniu_number = 2
    meniu1.save()
    return HttpResponse("Boon Apetit")

def about_restaurant(request):
    return render(request, 'about_restaurant.html')

class MainViewSet(viewsets.ModelViewSet):
    # viewset pentru API REST (CRUD pe modelul Meniu)
    queryset = Meniu.objects.all()
    serializer_class = MeniuSerializer
# listă simplă pentru testare / debug
menus_list = ['Salad', "Daniel", '12']

def meniu_by_user(request: HttpRequest, user_id: int):
    # filtrează meniurile după ID-ul userului
    menus = list(Meniu.objects.filter(created_by=user_id))
    # sortează descrescător după data creării
    menus.sort(key = (lambda x: x.date_created), reverse=True)

    context = {
        'menus': menus
    }
    return render(request, 'meniu.html', context)

@csrf_exempt
def meniu_view_simple(request: HttpRequest):
    # versiune simplificată fără autentificare
    if request.method == 'GET':
        menus_list.sort(reverse=True)
        context = {
            'menus': menus_list
        }
        return render(request, 'main_page/meniu.html', context)
    elif request.method == "POST":
        # citește datele din request body (JSON)
        data = json.loads(request.body)
        meniu_title = data["title"]
        menus_list.append(meniu_title)
        return HttpResponse("")

@csrf_exempt
@login_required
def meniu_view(request: HttpRequest):
    # dacă metoda este GET → trimite formularul gol către template
    if request.method == "GET":
        context = {
            'form': MeniuForm()
        }
        return render(request, 'create_meniu.html', context)
    elif request.method == "POST":
        # dacă metoda este POST → verifică și salvează datele introduse
        form_with_data = MeniuForm(request.POST, request.FILES)
        if form_with_data.is_valid():
            meniu_instance = form_with_data.save(commit=False)
            meniu_instance.created_by = request.user    # setează user-ul curent
            meniu_instance.save()
            return redirect('meniu_by_user', user_id=request.user.id)
        else:
            return HttpResponse(form_with_data.errors)


@login_required()
def update_meniu(request, pk):
    # găsește meniu-ul după pk și user curent
    meniu = get_object_or_404(Meniu, pk=pk, created_by=request.user)
    if request.method == "POST":
        # dacă trimitem formularul → actualizează
        form = MeniuForm(request.POST, request.FILES, instance=meniu)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        # dacă doar intrăm pe pagină → arată formularul cu datele existente
        form = MeniuForm(instance=meniu)

    return render(request, 'meniu_form.html', {'form': form, 'meniu': meniu})


@login_required()
def delete_meniu(request, pk):
    # găsește meniu-ul după pk și user curent
    meniu = get_object_or_404(Meniu, pk=pk, created_by=request.user)
    if request.method == "POST":
        # șterge și redirecționează către pagina principală
        meniu.delete()
        return redirect('main_page')
    else:
        # cere confirmare înainte de ștergere
        return render(request, "meniu_confirm_delete.html", {'meniu': meniu})
