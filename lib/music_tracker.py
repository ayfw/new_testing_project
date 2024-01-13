class MusicTracker():
    def __init__(self):
        self._songs = []

    def music_playlist(self):
        return self._songs
    
    def add(self, song):
        self._songs.append(song)

    def remove(self, index):
        if index < 0 or index >= len(self._songs):
            raise Exception("This song does not exist!")
        del self._songs[index]
