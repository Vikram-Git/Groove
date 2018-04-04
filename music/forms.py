from django import forms
from .models import Artist, Song

class ArtistCreateForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Artist Name',
        required=True
    )
    genre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Genre',
        required=False
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label='Artist Image',
        required=True
    )
    class Meta:
        model = Artist
        fields = ['name', 'genre', 'image']


class CreateSongForm(forms.ModelForm):

    album_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Album Name',
        required=False
    )
    song_title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Song Title',
        required=True
    )
    audio_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label='Audio File',
        required=True
    )
    class Meta:
        model = Song
        fields = ['album_name', 'song_title', 'audio_file']
