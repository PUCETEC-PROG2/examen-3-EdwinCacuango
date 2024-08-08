# Ingresar tus URLs de la app aquí
from django.urls import path
from . import views
app_name = 'album_manager'

urlpatterns = [
    path('', views.index, name='index'),
    
   # URLs para Artist
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artists/new/', views.artist_create, name='artist_create'),
    path('artists/<int:pk>/edit/', views.artist_update, name='artist_update'),
    path('artists/<int:pk>/delete/', views.artist_delete, name='artist_delete'),

    # URLs para Album
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('albums/new/', views.album_create, name='album_create'),
    path('albums/<int:pk>/edit/', views.album_update, name='album_update'),
    path('albums/<int:pk>/delete/', views.album_delete, name='album_delete'),

]