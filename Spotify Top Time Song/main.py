from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

_date_ = input(
    "Which year blockbuster you want to hear tell the Year in format YYYY-MM-DD -> "
)
response = requests.get(f"https://www.billboard.com/charts/hot-100/{_date_}/")
my_html = response.text

soup = BeautifulSoup(my_html, "html.parser")
songs = []

song_title = soup.select("li ul li h3")

for tag in song_title:
    song_name = tag.text.strip()
    songs.append(song_name)


SPOTIFY_CLIENT_ID = "4d1cd8de30724c75935f9a0986d543b1"
SPOTIFY_CLIENT_SECRET = "482596001a214cac895630d466c27016"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://localhost:8888/callback/",
        scope="user-library-read playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()

song_uris = []
year = _date_.split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(f"Number of songs {len(song_uris)}")

playlsit = sp.user_playlist_create(user=user_id["id"], name=f"{_date_} Top 100 Billboard", public=None)

sp.user_playlist_add_tracks(user=user_id["id"], playlist_id=playlsit["id"], tracks=song_uris)