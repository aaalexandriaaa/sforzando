from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Piece(models.Model):
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    voice = models.CharField(max_length=100)
    own = models.CharField(max_length=100)
# fields: 'name', 'composer', 'period', 'instrument', 'voice', 'own'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'piece_id': self.id})

