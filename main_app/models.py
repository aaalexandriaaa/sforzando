from django.db import models
from django.contrib.auth.models import User

class Piece:
    def __init__(self, 'name', 'composer', 'period', 'instrument', 'voice', 'own'):
        self.name = name
        self.composer = composer
        self.period = period
        self.instrument = instrument
        self.voice = voice
        self.own = own

pieces = [
    Piece('I know that my redeemer Liveth', 'GF Handel', 'Baroque', 'Piano', 'Soprano', True),
    Piece('Come Unto Him', 'GF Handel', 'Baroque', 'Piano', 'Soprano', True),
    Piece('Fugue No. 2', 'JS Bach', 'Baroque', 'Piano', 'n/a', True)
]