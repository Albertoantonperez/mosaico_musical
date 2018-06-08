#!/usr/bin/env python

# import utils as u
import pandas as pd

if __name__ == '__main__':
    print ("Reading songs dataframe....")
    songs = pd.read_pickle('songs.pkl')
    print (songs.song_id.unique().shape[0])
    # print ("Reading listenings dataframe....")
    # listenings_df = u.read_listenings_df()
    # print ("Reading songs dataframe....")
    # all_songs_df = u.read_songs_df()
    # print ("Selecting unique songs in listenings...")
    # songs = u.songs_in_listenings(listenings_df, all_songs_df)
    entrada = input("Y ahora dime argo, payo ")
    print (type(entrada))