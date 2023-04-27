DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS channel;
DROP TABLE IF EXISTS song_artist;
DROP TABLE IF EXISTS artist_album;
DROP TABLE IF EXISTS song_album;

PRAGMA foreign_keys = TRUE;

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
