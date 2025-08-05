import re
import spotipy
import os
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from dotenv   import load_dotenv

class ConnectSpotify():

    def __init__(self):

        SPOTIFY_CLIENT_ID = os.getenv('spotifyID')
        SPOTIFY_CLIENT_SECRET = os.getenv('spotifySecret')
        SPOTIFY_REDIRECT_URI = "http://127.0.0.1:1410"  # Check your API port number
        SCOPE = "playlist-modify-public playlist-modify-private user-read-private user-read-email"

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id = SPOTIFY_CLIENT_ID,
            client_secret = SPOTIFY_CLIENT_SECRET,
            redirect_uri = SPOTIFY_REDIRECT_URI,
            scope = SCOPE
        ),
        requests_timeout=20)

        self.userid = self.sp.current_user()["id"]
        self.playlistID = ''

    def create_playlist(self, genre):
        self.playlist_name = f"GenreFinder - {genre}"
        playlist = self.sp.user_playlist_create(
            self.userid,
            self.playlist_name,
            public=True,
            description=f"GenreFinder - {genre}"
        )

        return playlist["id"]


    def remove_from_playlist(self, track_uris):
        if track_uris:
            for i in range(0, len(track_uris), 100):
                batch = track_uris[i:i+100]
                self.sp.playlist_remove_all_occurrences_of_items(self.playlistID, batch)
            print('✅ - Playlist Updated!')
        else:
            print("❌ - No songs found to remove from the playlist.")


    def get_playlist_songs(self):
        uri_list = []
        offset = 0
        limit = 100
        while True:
            playlist = self.sp.playlist_items(self.playlistID, limit=limit, offset=offset)
            batch = [item['track']['uri'] for item in playlist['items'] if item['track'] is not None]
            if not batch:
                break
            uri_list.extend(batch)
            offset += limit
            if len(batch) < limit:
                break
        return uri_list

    
    def add_to_playlist(self, track_uris, playlistID):

        # Add Songs to the playlist
        if track_uris:
            self.sp.playlist_add_items(playlistID, track_uris)
            print('✅ - Playlist Updated!')
            print(f"{len(track_uris)} songs added to playlist '{self.playlist_name}' successfully!")
        else:
            print("❌ - No songs found to add to the playlist.")

    
    def search_song(self, trackList):
        
        result = self.sp.tracks(trackList)

        if result:
            track_artist_spotify_list = []
            genre_list = []
            for result in result['tracks']:

                track_artist_spotify = result['artists'][0]['name']
                artist_id = result['artists'][0]['id']
                artist_info = self.sp.artist(artist_id)
                genres = artist_info.get('genres', [])
                genre = classify_genre(genres)

                track_artist_spotify_list.append(track_artist_spotify)
                genre_list.append(genre)

            return track_artist_spotify_list, genre_list

        else:
            return  None, None


def classify_genre(genres):
    genre_map = [
        ('metal', 'Metal'),
        ('core', 'Metal'),
        ('djent', 'Metal'),
        ('rock', 'Rock'),
        ('punk', 'Punk'),
        ('emo', 'Emo'),
        ('pop', 'Pop'),
        ('hip-hop', 'Hip-Hop'),
        ('rap', 'Rap'),
        ('indie', 'Indie'),
        ('alternative', 'Alternative'),
        ('folk', 'Folk'),
        ('jazz', 'Jazz'),
        ('blues', 'Blues'),
        ('country', 'Country'),
        ('reggae', 'Reggae'),
        ('electronic', 'Electronic'),
        ('house', 'House'),
        ('techno', 'Techno'),
        ('edm', 'EDM'),
        ('grunge', 'Grunge'),
        ('funk', 'Funk'),
        ('soul', 'Soul'),
        ('disco', 'Disco'),
        ('trap', 'Trap'),
        ('gospel', 'Gospel'),
        ('classical', 'Classical'),
        ('opera', 'Opera'),
        ('ambient', 'Ambient'),
        ('drum and bass', 'Drum & Bass'),
        ('dubstep', 'Dubstep'),
        ('samba', 'Samba'),
        ('pagode', 'Pagode'),
        ('sertanejo', 'Sertanejo'),
        ('forro', 'Forró'),
        ('axé', 'Axé'),
        ('mpb', 'MPB'),
        ('bossa nova', 'Bossa Nova'),
        ('reggaeton', 'Reggaeton'),
        ('latin', 'Latin'),
        ('k-pop', 'K-Pop'),
        ('j-pop', 'J-Pop'),
        ('lo-fi', 'Lo-Fi'),
        ('hardcore', 'Hardcore'),
        ('ska', 'Ska'),
        ('bluegrass', 'Bluegrass'),
        ('world', 'World'),
        ('new age', 'New Age'),
    ]
    if not genres:
        return 'Unknown'
    for key, value in genre_map:
        if any(key in genre for genre in genres):
            return value
    return 'Other'


if __name__ == "__main__":

    load_dotenv(".env")
    spotify = ConnectSpotify()
    trackDataList = []
    trackFinalDataFrame = pd.DataFrame()
    
    # Solicita o link da playlist ao usuário e extrai o ID
    playlist_url = input("Cole o link da playlist do Spotify: ").strip()
    match = re.search(r"(playlist\/|playlist:)([a-zA-Z0-9]+)", playlist_url)
    if match:
        spotify.playlistID = match.group(2)
    else:
        print("❌ - Link de playlist inválido.")
        exit(1)

    track_uris = spotify.get_playlist_songs()
    batch_frames = []
    for i in range(0, len(track_uris), 50):
        batch = track_uris[i:i+50]
        if batch:
            artists, genres = spotify.search_song(batch)
            batch_frame = pd.DataFrame({'artist': artists, 'genre': genres, 'trackURI': batch})
            batch_frames.append(batch_frame)
    if batch_frames:
        trackDataFrame = pd.concat(batch_frames, ignore_index=True)
        trackDataFrame.reset_index(drop=True, inplace=True)
        trackFinalDataFrame = pd.concat([trackFinalDataFrame, trackDataFrame], ignore_index=True)


    genreList = trackFinalDataFrame['genre'].unique().tolist()
    #trackFinalDataFrame.to_excel('playlist_genres.xlsx', index=False)
    for genre in genreList:
        playlist_id = spotify.create_playlist(genre)
        track_uris = trackFinalDataFrame[trackFinalDataFrame['genre'] == genre]['trackURI'].tolist()
        for i in range(0, len(track_uris), 100):
            batch = track_uris[i:i+100]
            spotify.add_to_playlist(batch, playlist_id)
