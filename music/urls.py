from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create-artist/$', views.create_artist, name='create-artist'),
    url(r'^delete-artist/(?P<artist_pk>((\d)+))/$', views.delete_artist, name='delete-artist'),
    url(r'^edit-artist/(?P<artist_pk>((\d)+))/$', views.edit_artist, name='edit-artist'),
    url(r'^fav-artist/(?P<artist_pk>((\d)+))/$', views.fav_artist, name='fav-artist'),
    url(r'^(?P<artist_pk>((\d)+))/song-list/$', views.song_list, name='song-list'),
    url(r'^(?P<artist_pk>((\d)+))/add-song/$', views.add_song, name='add-song'),
    url(r'^delete-song/(?P<song_pk>((\d)+))/$', views.delete_song, name='delete-song'),
    url(r'^fav-song/(?P<song_pk>((\d)+))$', views.fav_song, name='fav-song'),
    url(r'^all-songs/$', views.all_song_list, name='all-songs'),
    url(r'^favourites/$', views.favourites, name='favourites'),
    url(r'^search/$', views.search, name="search"),
]