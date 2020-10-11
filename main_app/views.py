from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Piece
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def pieces_index(request):
  pieces = Piece.objects.filter(user=request.user)
  return render(request, 'pieces/index.html', {'pieces': pieces})

@login_required
def pieces_detail(request, piece_id):
  piece = Piece.objects.get(id=piece_id)
  return render(request, 'pieces/detail.html', {'piece': piece})
  
class PieceCreate(LoginRequiredMixin, CreateView):
  model = Piece
  fields = ['name', 'composer', 'period', 'instrument', 'voice', 'own']

  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the cat
    return super().form_valid(form)
  
class PieceUpdate(LoginRequiredMixin, UpdateView):
  model = Piece
  fields = ['name', 'composer', 'period', 'instrument', 'voice', 'own']

class PieceDelete(LoginRequiredMixin, DeleteView):
  model = Piece
  success_url = '/pieces/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)