# Mosaico Musical

Mosaico Musical is Alberto Anton's musical recommender and it's his master's thesis for the Master in Data Science of KSchool.

The data comes from the listening history of a million Last.fm users. They are about 500MB compressed and can be found [here](http://labrosa.ee.columbia.edu/millionsong/sites/default/files/challenge/train_triplets.txt.zip). Due to its size, the data files won't be included in this repository.

Temporary list of files:

##[train_triplets.txt](http://labrosa.ee.columbia.edu/millionsong/sites/default/files/challenge/train_triplets.txt.zip)
File with the listening history of about 1 million users in the form of user_id - song_id - play count triplets.
Some figures:
* 1.019.318 unique users
* 384.546 unique MSD songs
* 48.373.586 user - song - play count triplets

##[unique_tracks.txt](http://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/unique_tracks.txt)
File with info on 1 million songs in the form of unknown_id - song_id - performer - song_title
Some figures:
* 1.000.000 values in column1
* 999.056 song ids
* 72.665 artists
* 702.429 song titles.


Because the data is part of a closed competition (from 2012), the test set is no longer available, so I will have to build it.