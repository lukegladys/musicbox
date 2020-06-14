playlists = list()

class Playlist():

    def __init__(self, name, track_list, author=None):
        self.name = name
        self.track_list = track_list
        self.author = author

class SpotifyPlaylist(Playlist):
    
    def __init__(self, spotify_id, name=None, track_list=None, author=None):
        self.spotify_id = spotify_id
        super().__init__(name, track_list, author)