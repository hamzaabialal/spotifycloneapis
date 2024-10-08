from django.urls import path

from .views import SpotifyView, AlbumsTemplate,SpotifyCOnView,PlaylistView,ArtistTemplate, ServeralArtists, SPotifyAlbums,ArtistListTemplate

urlpatterns = [
    path('spotify/', SpotifyView.as_view(), name='spotify'),
    path('token/', SpotifyCOnView.as_view(), name='token'),
    path('playlist/', PlaylistView.as_view(), name='playlist'),
    path('artist/', ArtistTemplate.as_view(), name='artist'),
    path('artists/', ServeralArtists.as_view(), name='artists'),
    path('list-artists/', ArtistListTemplate.as_view(), name='list-artists'),
    path('albums/', SPotifyAlbums.as_view(), name='albums'),
    path('albumtemplate/', AlbumsTemplate.as_view(), name='albumtemplate'),
]