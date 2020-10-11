from django.shortcuts import render
from django.http import HttpResponse
from .models import Piece
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pieces_index(request):
  pieces = Piece.objects.all()
  return render(request, 'pieces/index.html', {'pieces': pieces})

def pieces_detail(request, piece_id):
  piece = Piece.objects.get(id=piece_id)
  return render(request, 'pieces/detail.html', {'piece': piece})
  
class PieceCreate(CreateView):
  model = Piece
  fields = ['name', 'composer', 'period', 'instrument', 'voice', 'own']
  success_url = '/pieces/'
  
class PieceUpdate(UpdateView):
  model = Piece
  fields = ['name', 'composer', 'period', 'instrument', 'voice', 'own']

class PieceDelete(DeleteView):
  model = Piece
  success_url = '/pieces/'