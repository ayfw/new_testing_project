from lib.music_library import *

"""
initially no tracks in music library
"""
def test_initially_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []