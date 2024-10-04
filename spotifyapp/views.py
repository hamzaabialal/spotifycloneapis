import base64
import os
import json
from requests import post, get
from dotenv import load_dotenv
from django.db.models.expressions import result
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse

load_dotenv()

# Create your views here.
client_id =os.getenv('SPOTIFY_CLIENT_ID', "b4ee39c6b21941d8aa02cee362848d2a")
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', "9fdb4a5bf35d4312bec80a2db7415fee")
class SpotifyView(TemplateView):
    template_name = "spotify.html"

class SpotifyCOnView(APIView):
    def get(self, request):
        token = self.get_token()
        return HttpResponse({
            "token": token
        })
    def get_token(self):
        auth_string = client_id + ':' + client_secret
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data  = {
            "grant_type": "client_credentials"
        }
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        return json_result['access_token']

def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data  = {
        "grant_type": "client_credentials"
    }
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    return json_result['access_token']

class PlaylistView(APIView):
    def get(self, request):
        query  = self.request.query_params.get('query')
        playlist = self.get_playlist(query)
        return JsonResponse({
            "playlist": playlist
        })

    def get_playlist(self, query):
        try:
            token = get_token()
            url = f"https://api.spotify.com/v1/artists/{query}"
            headers = {
                "Authorization": "Bearer " + token
            }
            result = get(url, headers=headers)
            json_result = json.loads(result.content)
            return json_result
        except Exception as e:
            return str(e)

class ArtistTemplate(TemplateView):
    template_name = "artist.html"

class ServeralArtists(APIView):
    def get(self, request):
        query = self.request.query_params.get('query')


        playlist = self.get_playlist(query)
        return JsonResponse({
            "playlist": playlist
        })

    def get_playlist(self, query):
        try:
            token = get_token()
            url = f"https://api.spotify.com/v1/artists?ids={query}"
            headers = {
                "Authorization": "Bearer " + token
            }
            result = get(url, headers=headers)
            json_result = json.loads(result.content)
            return json_result
        except Exception as e:
            return str(e)
class ArtistListTemplate(TemplateView):
    template_name = "artists.html"