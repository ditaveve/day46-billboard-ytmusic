import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
from pprint import pprint

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
response = requests.get(URL, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
all_songs = [film_tag.getText() for film_tag in soup.find_all(name="h3", class_="chart-entry__title")]
all_artists = [artist_tag.getText() for artist_tag in soup.find_all(name="span", class_="chart-entry__artist")]
print(all_songs)

yt = YTMusic("browser.json")

playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")
playlist_title = f"{date} Billboard 100"
playlistExists = False
for playlist in yt.get_library_playlists():
    if playlist["title"] == playlist_title:
        playlistExists = True
    
if playlistExists == False:
    playlist_id = yt.create_playlist(title=playlist_title, description=f"This playlist will bring you back to the great year of {date.split('-')[0]}!")
    for song in all_songs:
        try:
            identify_song = [yt.search(query=f"{song} {all_artists[0]}", filter="songs")[0]["videoId"]]
            all_artists.pop(0)
            yt.add_playlist_items(playlistId=playlist_id, videoIds=identify_song)
            print(f"Added: {song}")
        except Exception:
            print("Something went wrong")
    