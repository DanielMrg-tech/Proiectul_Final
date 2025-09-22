from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
# Formular pentru înregistrare utilizator, moștenește UserCreationForm
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adaugă câmp obligatoriu pentru email

    # Legăm formularul de modelul User
    class Meta:
        model = User  # Formularul va salva date în modelul User
        fields = ['username', 'email']  # Câmpurile disponibile în formular