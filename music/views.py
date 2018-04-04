from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtistCreateForm, CreateSongForm
from .models import Artist, Song
from django.db.models import Q
from django.http import JsonResponse


def index(request):
    all_artists = Artist.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'all_artists': all_artists})


def create_artist(request):
    if request.method == 'POST':
        form = ArtistCreateForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user
            artist.save()
            return redirect('music:song-list', artist_pk=artist.pk)
        else:
            return redirect('music:create-artist')
    else:
        form = ArtistCreateForm()
        return render(request, 'music/create-artist.html', {'form': form})


def delete_artist(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    artist.delete()
    return redirect('music:index')


def edit_artist(request, artist_pk):
    this_artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'POST':
        form = ArtistCreateForm(data=request.POST, files=request.FILES, instance=this_artist)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user
            artist.save()
            return redirect('music:index')
        else:
            return redirect('music:edit-artist', artist_pk=artist_pk)
    else:
        form = ArtistCreateForm(instance=this_artist)
        return render(request, 'music/create-artist.html', {'form': form})


def fav_artist(request, artist_pk):
    this_artist = get_object_or_404(Artist, pk=artist_pk)
    if this_artist.is_fav:
        this_artist.is_fav = False
    else:
        this_artist.is_fav = True
    this_artist.save()
    return JsonResponse({'success': True})


def song_list(request, artist_pk):
    this_artist = get_object_or_404(Artist, pk=artist_pk)
    return render(request, 'music/song-list.html', {'this_artist': this_artist})


def add_song(request, artist_pk):
    this_artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'POST':
        form = CreateSongForm(request.POST, request.FILES)
        audio_formats = ['wav', 'mp3']
        if form.is_valid():
            song = form.save(commit=False)
            song.artist = this_artist
            song.audio_file = request.FILES['audio_file']
            audio_file_format = song.audio_file.url.split('.')[-1]
            audio_file_format = audio_file_format.lower()
            if audio_file_format not in audio_formats:
                kwargs = {'this_artist': this_artist,
                          'form': form,
                          'error_message': 'File uploaded must be WAV, MP3'}
                return render(request, 'music/add-song.html', kwargs)
            song.save()
            return redirect('music:song-list', artist_pk=artist_pk)
    else:
        form = CreateSongForm()
        return render(request, 'music/add-song.html', {'this_artist': this_artist, 'form': form})


def delete_song(request, song_pk):
    this_song = get_object_or_404(Song, pk=song_pk)
    this_song.delete()
    return JsonResponse({'success': True})


def fav_song(request, song_pk):
    this_song = get_object_or_404(Song, pk=song_pk)
    if this_song.is_fav :
        this_song.is_fav = False
    else:
        this_song.is_fav = True
    this_song.save()
    return JsonResponse({'success': True})


def all_song_list(request):
    user_artists = Artist.objects.filter(user=request.user)
    user_songs_pk = []
    for artist in user_artists:
        for song in artist.song_set.all():
            user_songs_pk.append(song.pk)
    user_songs = Song.objects.filter(pk__in=user_songs_pk)
    return render(request, 'music/all-songs.html', {'user_songs': user_songs})


def search(request):
    all_artists = Artist.objects.filter(user=request.user)
    user_songs_pk = []
    for artist in all_artists:
        for song in artist.song_set.all():
            user_songs_pk.append(song.pk)
    all_user_songs = Song.objects.filter(pk__in=user_songs_pk)

    query = request.GET.get("q")

    if query:
        artist = all_artists.filter(
            Q(name__icontains=query)
        ).distinct()
        if artist:
            return render(request, 'music/index.html', {'all_artists': artist})

        song = all_user_songs.filter(
            Q(song_title__icontains=query) |
            Q(album_name__icontains=query)
        ).distinct()
        if song:
            return render(request, 'music/all-songs.html', {'user_songs': song})

    return render(request, 'music/search.html')






