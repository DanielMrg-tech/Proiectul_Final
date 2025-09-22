from http.client import HTTPResponse

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.template.context_processors import request

from accounts.forms import RegistrationForm

# View pentru înregistrarea unui utilizator nou
def register_view(request):
    if request.method == "GET":
        # Dacă e cerere GET → afișează formularul gol de înregistrare
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    # Dacă e cerere POST → procesăm datele trimise din formular
    form = RegistrationForm(request.POST)
    if form.is_valid():
        # Salvăm utilizatorul nou și îl logăm automat
        user = form.save()
        login(request, user)
        return redirect('/')
    else:
        # Aici returnezi erorile ca HTTPResponse brut →
        return HTTPResponse(form.errors)

# View pentru autentificarea utilizatorilor existenți
def login_view(request):
    if request.method == "POST":
        # Procesăm datele primite prin POST
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Dacă datele sunt corecte → logăm utilizatorul
            user = form.get_user()
            login(request, user)
            return redirect("main_page")
        else:
            # Dacă sunt erori → reafișăm pagina de login cu erorile
            return render(request, "login.html", {"form": form})
    else:
        # Dacă e cerere GET → afișăm formularul gol
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})