from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # aici trebuie sa legam importul User de acest registration ca servarul sa stie de unde e si asta facem prin clasa meta
    class Meta:
        model = User
        fields = ['username', 'email']