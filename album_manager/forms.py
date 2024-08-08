from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'year_release', 'gender', 'artist']