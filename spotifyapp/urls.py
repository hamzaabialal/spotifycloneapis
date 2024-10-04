from django.urls import path

from .views import SpotifyView, SpotifyCOnView,PlaylistView,ArtistTemplate, ServeralArtists, ArtistListTemplate

urlpatterns = [
    path('spotify/', SpotifyView.as_view(), name='spotify'),
    path('token/', SpotifyCOnView.as_view(), name='token'),
    path('playlist/', PlaylistView.as_view(), name='playlist'),
    path('artist/', ArtistTemplate.as_view(), name='artist'),
    path('artists/', ServeralArtists.as_view(), name='artists'),
    path('list-artists/', ArtistListTemplate.as_view(), name='list-artists')
]