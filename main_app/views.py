from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pieces_index(request):
  pieces = Piece.objects.all()
  return render(request, 'pieces/index.html', { 'pieces': pieces })   