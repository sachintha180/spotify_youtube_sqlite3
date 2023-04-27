# spotify_youtube_sqlite3
A normalized, cleaned and refactored SQLite3 database of the "Spotify &amp; YouTube" dataset from Kaggle.com

## Files ##
```
  - script.py : Python code used for converting the .csv dataset into an SQLite3 database
  - create.sql: The SQL DDL commands used to create the entities prior to adding records from the .csv dataset
  - Spotify_Youtube.csv: The original .csv file from Kaggle
  - music.db: The dumped SQLite3 database
```
 
## Link to original dataset ##
<https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube>

## Relational schema ##

```
CREATE TABLE artist(
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT NOT NULL
);

CREATE TABLE song(
    song_id INTEGER PRIMARY KEY,
    song_name TEXT NOT NULL,
    danceability REAL,
    energy REAL,
    song_key INTEGER,
    loudness REAL,
    speechiness REAL,
    acousticness REAL,
    instrumentalness REAL,
    liveness REAL,
    valence REAL,
    tempo REAL,
    duration_ms INTEGER,
    streams INTEGER,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id) ON DELETE CASCADE
);

CREATE TABLE channel(
    channel_id INTEGER PRIMARY KEY,
    channel_name NOT NULL
);

CREATE TABLE video(
    song_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    views INTEGER,
    likes INTEGER,
    comments INTEGER,
    description TEXT,
    licensed TEXT,
    official TEXT,
    channel_id INTEGER NOT NULL,
    FOREIGN KEY (song_id) REFERENCES song(song_id) ON DELETE CASCADE
    FOREIGN KEY (channel_id) REFERENCES channel(channel_id) ON DELETE CASCADE
);
```
