from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pieces/', views.pieces_index, name='index'),
  path('pieces/<int:piece_id>/', views.pieces_detail, name='detail'),
  path('pieces/create/', views.PieceCreate.as_view(), name='pieces_create'),
  path('pieces/<int:pk>update', views.PieceUpdate.as_view(), name='pieces_update'),
  path('pieces/<int:pk>delete', views.PieceDelete.as_view(), name='pieces_delete'),
]