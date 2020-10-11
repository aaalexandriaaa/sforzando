from django.shortcuts import render
from django.http import HttpResponse
from .models import Piece, pieces

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def pieces_index(request):
    return render(request, 'pieces/index.html', { 'pieces': pieces })   