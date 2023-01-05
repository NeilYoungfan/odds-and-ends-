# Just a simple, fun one to find song lyrics and print them in the terminal

from lyrics_extractor import SongLyrics
from secrets import GCS_API_KEY, GCS_ENGINE_ID

extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)

song = input("Enter song title")

print(song)

data = extract_lyrics.get_lyrics(song)

print(data)
