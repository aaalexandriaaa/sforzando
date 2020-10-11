from django.shortcuts import render
from django.http import HttpResponse
from .models import Piece

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pieces_index(request):
  pieces = Piece.objects.all()
  return render(request, 'pieces/index.html', {'pieces': pieces})

def pieces_detail(request, piece_id):
  piece = Piece.objects.get(id=piece_id)
  return render(request, 'pieces/detail.html', { 'piece': piece })