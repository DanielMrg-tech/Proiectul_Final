from django import forms
from main_page.models import Meniu


class MeniuForm(forms.ModelForm):
    class Meta:
        model = Meniu
        fields = ['thumbnail_image', 'title', 'produs', 'meniu_number']
