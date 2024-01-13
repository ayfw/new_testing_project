from lib.music_library import *
from lib.track import *

"""
add multiple tracks to music library
"""
def test_add_multiple_tracks_to_library():
    music_library = MusicLibrary()
    track_1 = Track("my title 1", "my artist 1")
    track_2 = Track("my title 2", "my artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.all() == [track_1, track_2]

"""
search for track by title
"""
def test_search_by_title():
    music_library = MusicLibrary()
    track_1 = Track("my title 1", "my artist 1")
    track_2 = Track("my title 2", "my artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("my title 1") == [track_1]

"""
search for track by a part of the title
"""
def test_search_by_part_of_title():
    music_library = MusicLibrary()
    track_1 = Track("my title 1", "my artist X")
    track_2 = Track("my title 2", "my artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("1") == [track_1]

"""
initially search for track should return empty list
"""
def test_initial_search_title_return_empty():
    music_library = MusicLibrary()
    assert music_library.search_by_title("my title 1") == []