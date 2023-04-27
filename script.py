import pandas as pd
import sqlite3

# source: https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube

df = pd.read_csv("Spotify_YouTube.csv").dropna().reset_index(drop=True).rename(columns={
    "Artist": "artist_name",
    "Url_spotify": "spotify_url",
    "Track": "song_name",
    "Album": "album_name",
    "Album_type": "album_type",
    "Uri": "spotify_uri",
    "Danceability": "danceability",
    "Energy": "energy",
    "Key": "key",
    "Loudness": "loudness",
    "Speechiness": "speechiness",
    "Acousticness": "acousticness",
    "Instrumentalness": "instrumentalness",
    "Liveness": "liveness",
    "Valence": "valence",
    "Tempo": "tempo",
    "Duration_ms": "duration_ms",
    "Url_youtube": "youtube_url",
    "Title": "title",
    "Channel": "channel",
    "Views": "views",
    "Likes": "likes",
    "Comments": "comments",
    "Description": "description",
    "Licensed": "licensed",
    "official_video": "official",
    "Stream": "streams"
}).drop(columns=['spotify_url', 'spotify_uri', 'album_name', 'album_type', 'youtube_url'])
df.index.name = "song_id"

connection = sqlite3.connect("music.db")
db = connection.cursor()

with open('create.sql', 'r') as create_file:
    ddl_script = create_file.read();

db.executescript(ddl_script)

# each artist_name and song_name combination is unique

new_artist, current_artist = True, ''
new_channel, current_channel = True, ''
artist_id, channel_id = -1, -1

for i in df.index:
    row = df.iloc[i]

    if current_artist != row['artist_name']:
        new_artist = True
        artist_id += 1

    if current_channel != row['channel']:
        new_channel = True
        channel_id += 1

    if new_artist:
        current_artist = row['artist_name']
        db.execute('INSERT INTO artist VALUES(?, ?);', (artist_id, current_artist))
        new_artist = False

    if new_channel:
        current_channel = row['channel']
        db.execute('INSERT INTO channel VALUES(?, ?);', (channel_id, current_channel))
        new_channel = False

    # (song_id, song_name, danceability, energy, song_key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, streams)
    db.execute('INSERT INTO song VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', tuple(
        [i] + row[['song_name', 'danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'streams']].values.tolist() + [artist_id]
    ))

    # (song_id, title, views, likes, comments, description, licensed, official, channel_id)
    db.execute('INSERT INTO video VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);', tuple(
        [i] + row[['title', 'views', 'likes', 'comments', 'description', 'licensed', 'official']].values.tolist() + [channel_id]
    ))

connection.commit()

connection.close()