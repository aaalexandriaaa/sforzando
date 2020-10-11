from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pieces/', views.pieces_index, name='index'),
  path('pieces/<int:piece_id>/', views.pieces_detail, name='detail'),
]