import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pprint as pp
from datetime import datetime

CLIENT_ID = "d9cefe00aa584d26b14ad0cc7e3bca01"
CLIENT_SECRET = "08b7241f01ee489fb3e105b32e8f803f"

# ------------------------------------------ Creating Spotify Playlist ------------------------------------------------ #


class SpotifyAuthoriser:
    def __init__(self, user) -> None:
        self.user_id = user
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.redirect_uri = "http://127.0.0.1:5000/music/generated_list/connect_spotify/complete"
        # self.redirect_uri = "http://127.0.0.1:5000/callback"

        self.scope = "playlist-modify-private playlist-modify-public"
        # self.scope = "user-library-read"
        # self.cache_path = r"project source codes\source code\token.txt"
        # self.show_dialog = True

        auth_manager = SpotifyOAuth(
            scope=self.scope,
            redirect_uri=self.redirect_uri,
            client_id=self.client_id,
            client_secret=self.client_secret,
            # show_dialog=self.show_dialog,
            # cache_path=self.cache_path,
            # username=self.user_id,
            open_browser=True
        )
        print(auth_manager.get_access_token())
        print(auth_manager.get_auth_response())

        self.sp = spotipy.Spotify(
            auth_manager=auth_manager
        )

    def add_playlist_to_profile(self, song_list, mood):
        # Add songs to the playlist
        song_uris = []
        for song in song_list:
            result = self.sp.search(q=f"track:{song}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                pass
                # print(f"{song} doesn't exist in Spotify. Skipped.")

        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%y")

        # Creating a new private playlist in Spotify
        playlist = self.sp.user_playlist_create(
            user=self.user_id, name=f"Feeling {mood} {formatted_date}", public=False)

        # Adding songs found into the new playlist
        self.sp.user_playlist_add_tracks(
            user=self.user_id, playlist_id=playlist["id"], tracks=song_uris)

    def create_spotify_playlist(self, playlist_name):
        # Check if the playlist already exists
        playlists = self.sp.current_user_playlists()
        for playlist in playlists["items"]:
            if playlist["name"] == playlist_name:
                return playlist

        # Create a new private playlist in Spotify
        playlist = self.sp.user_playlist_create(
            user=self.user_id, name=playlist_name, public=False)
        return playlist
