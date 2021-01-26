from django.db import models
from uuid import uuid4

# Create your models here

class Bands(models.Model):
    id_band = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    sub_genre = models.CharField(max_length=255)
    release_year = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

