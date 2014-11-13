# -*- coding: utf-8 -*-
import model
from model import db_session
from sys import argv
from api_calls import algorithm
from time import sleep



import json


def add_to_db(session):

    songs = [("Radiohead", "Weird Fishes"), ("Cyndi Lauper", "True Colors")]

    for song in songs:

        song_data = algorithm(song[0], song[1])

        values = song_data["patterns"]
        values_json = json.dumps(values)

        #TO DO check to see if song is already in db
        track = model.Track()

        track.song_id = song_data["song_id"]
        track.key = song_data["key"]
        track.title = song_data["title"]
        track.tempo = song_data["tempo"]
        track.energy = song_data["energy"]
        track.liveness = song_data["liveness"]
        track.speechiness = song_data["speechiness"]
        track.artist_name = song_data["artist_name"]
        track.mode = song_data["mode"]
        track.acousticness = song_data["acousticness"]
        track.danceability = song_data["danceability"]
        track.time_signature = song_data["time_signature"]
        track.duration = song_data["duration"]
        track.loudness = song_data["loudness"]
        track.artist_id = song_data["artist_id"]
        track.valence = song_data["valence"]    
        track.audio_md5 = song_data["audio_md5"]
        track.instrumentalness = song_data["instrumentalness"]
        track.spotify_track_uri = song_data["spotify_track_uri"]
        track.patterns = values_json

        db_session.add(track)
        db_session.commit()
        sleep(10)


if __name__ == "__main__":

    # script, artist, title = argv
    add_to_db(db_session)
