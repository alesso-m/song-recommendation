# song-recommendation
Uses the Spotify API and KNN algorithm to create a recommendation of 10 songs for Spotify user based on one of their playlists.

The user inputs their Spotify username and a unique ID of one of their public playlists. The features of each song in the playlist are then extracted, such as 'genre', 'length', and 'danceability'. The features of each song in the song database are also extracted. The K Nearest Neighbor algorithm then finds which songs are most similar to the ones in the playlist by comparing the features multidimensionally. The top 10 songs are then returned.
