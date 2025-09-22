from django import forms
from main_page.models import Meniu

# Formular bazat pe modelul Meniu
class MeniuForm(forms.ModelForm):
    class Meta:
        # Spune că formularul se bazează pe modelul Meniu
        model = Meniu
        # Câmpurile care vor apărea în formularul HTML
        fields = ['thumbnail_image', 'title', 'produs', 'meniu_number']
