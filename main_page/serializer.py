from rest_framework import serializers
from main_page.models import Meniu

class MeniuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meniu
        fields = ['title', 'client', 'maniu_number', 'date_created']