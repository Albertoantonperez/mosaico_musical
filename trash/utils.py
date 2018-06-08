import numpy as np
import pandas as pd
import io
import os
import sys

data_root = "data"

def read_listenings_df():
    columns = ['user_id', 'song_id', 'num_plays']
    datafile = os.path.join(data_root, "train_triplets.txt")
    return pd.read_csv(datafile, 
                       sep='\t', 
                       header = None,
                       names = columns,
                       dtype={'num_plays':int})

def read_songs_df():
    columns = ["foo", "song_id", "artist", "title"]
    datafile = os.path.join(data_root, "unique_tracks.txt")
    return pd.read_csv(datafile, 
                        header = None,
                        sep = '<SEP>',
                        names = columns,
                        usecols = ["song_id", "artist", "title"],
                        encoding =  "utf-8",
                        engine = "python")
                            
def songs_in_listenings(data, all_songs):
    unique_songs_tmp = data.song_id.unique()
    unique_songs_df = pd.DataFrame(unique_songs_tmp, columns = ['song_id'])
    songs = unique_songs_df.merge(all_songs,
                               left_on = "song_id",
                               right_on = "song_id",
                               how = "left")[["song_id", "artist", "title"]]
    return songs.drop_duplicates(subset = "song_id") 

# Funcion that returns the artist and title of a song_id
def which_song(sid):
    return songs[songs["song_id"] == sid][["artist", "title"]]

# Function that shows the songs of an artist
def songs_by(artist_name):
    return songs[songs["artist"] == artist_name][["song_id", "title"]]