import base64
import os
import json
from requests import post, get
from dotenv import load_dotenv
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse

load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID', "b4ee39c6b21941d8aa02cee362848d2a")
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', "9fdb4a5bf35d4312bec80a2db7415fee")

class SpotifyView(TemplateView):
    template_name = "spotify.html"

class SpotifyCOnView(APIView):
    """
    API View to handle Spotify token requests.
    """
    def get(self, request):
        token = self.get_token()
        return JsonResponse({"token": token})

    def get_token(self):
        """
        Retrieves Spotify access token using client credentials.
        """
        auth_string = f"{client_id}:{client_secret}"
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}

        response = post(url, headers=headers, data=data)
        json_result = response.json()
        return json_result['access_token']

def get_token():
    """
    Retrieves Spotify access token (helper function).
    """
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = post(url, headers=headers, data=data)
    json_result = response.json()
    return json_result['access_token']

class PlaylistView(APIView):
    """
    API View to handle Spotify playlist queries by artist ID.
    """
    def get(self, request):
        query = request.query_params.get('query')
        playlist = self.get_playlist(query)
        return JsonResponse({"playlist": playlist})

    def get_playlist(self, query):
        """
        Retrieves Spotify playlist based on artist query.
        """
        try:
            token = get_token()
            url = f"https://api.spotify.com/v1/artists/{query}"
            headers = {"Authorization": f"Bearer {token}"}

            response = get(url, headers=headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

class ArtistTemplate(TemplateView):
    template_name = "artist.html"

class ServeralArtists(APIView):
    """
    API View to handle requests for multiple artists.
    """
    def get(self, request):
        query = request.query_params.get('query')
        playlist = self.get_playlist(query)
        return JsonResponse({"playlist": playlist})

    def get_playlist(self, query):
        """
        Retrieves Spotify playlists for multiple artists based on query.
        """
        try:
            token = get_token()
            url = f"https://api.spotify.com/v1/artists?ids={query}"
            headers = {"Authorization": f"Bearer {token}"}

            response = get(url, headers=headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

class ArtistListTemplate(TemplateView):
    template_name = "artists.html"


class SPotifyAlbums(APIView):
    """
    API View to handle Spotify album queries by artist ID.
    """
    def post(self, request):
        query = request.data.get('query')
        albums = self.get_albums(query)
        return JsonResponse({"albums": albums})

    def get_albums(self, query):
        """
        Retrieves Spotify albums based on artist query.
        """
        try:
            token = get_token()
            url = f"https://api.spotify.com/v1/artists/{query}/albums"
            headers = {"Authorization": f"Bearer {token}"}

            response = get(url, headers=headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}


class AlbumsTemplate(TemplateView):
    template_name = "albums.html"