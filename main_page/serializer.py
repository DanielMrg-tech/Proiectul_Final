from rest_framework import serializers
from main_page.models import Meniu


# Serializer-ul transformă obiectele din modelul Meniu
# în JSON (sau alte formate) și invers.
class MeniuSerializer(serializers.ModelSerializer):
    class Meta:
        # Modelul de bază pe care îl serializăm
        model = Meniu
        # Câmpurile care vor fi expuse în API
        fields = ['title', 'client', 'meniu_number', 'date_created']