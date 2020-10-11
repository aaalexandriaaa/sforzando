from django.db import models
from django.contrib.auth.models import User

class Piece(models.Model):
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    voice = models.CharField(max_length=100)
    own = models.CharField(max_length=100)

    def __str__(self):
        return self.name