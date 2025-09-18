from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Meniu(models.Model):
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    meniu_number = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meniu')
    date_created = models.DateTimeField(default=timezone.now)
    thumbnail_image = models.ImageField(upload_to='book_thumbnails/', blank=True, null=True)


    def __str__(self):
        return "{}, by {}, number {}".format(self.title, self.client, self.meniu_number)