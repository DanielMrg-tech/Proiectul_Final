from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# Modelul Meniu - reprezintă un preparat/meniu din aplicație
class Meniu(models.Model):
    title = models.CharField(max_length=255)
    produs = models.CharField(max_length=255)
    meniu_number = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meniu')
    date_created = models.DateTimeField(default=timezone.now)
    thumbnail_image = models.ImageField(upload_to='meniu_thumbnails/', blank=True, null=True)

    # Reprezentarea text a obiectului (apare în admin sau la print(meniu)).
    def __str__(self):
        return "{}, by {}, number {}".format(self.title, self.produs, self.meniu_number)