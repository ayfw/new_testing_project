import pytest
from lib.music_tracker import *

"""
initially there are no songs
"""
def test_initially_no_songs():
    music_tracker = MusicTracker()
    assert music_tracker.music_playlist() == []

"""
given a single song
returns a list containing that single song
"""
def test_given_single_song_adds_to_playlist():
    music_tracker = MusicTracker()
    music_tracker.add("song")
    assert music_tracker.music_playlist() == ["song"]

"""
given multiple songs
returns a list containing all songs
"""
def test_given_multiple_songs_adds_to_playlist():
    music_tracker = MusicTracker()
    music_tracker.add("song")
    music_tracker.add("song2")
    music_tracker.add("song3")
    assert music_tracker.music_playlist() == ["song", "song2", "song3"]

"""
given an index number to remove a single song
returns a list removing that single song
"""
def test_given_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add("song")
    music_tracker.add("song2")
    music_tracker.remove(0)
    assert music_tracker.music_playlist() == ["song2"]

"""
given an index number that is too LOW to remove a single song
returns an error
"""
def test_given_too_low_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add("song")
    music_tracker.add("song2")
    with pytest.raises(Exception) as e:
        music_tracker.remove(-1)
    error_message = str(e.value)
    assert error_message == "This song does not exist!"
    assert music_tracker.music_playlist() == ["song", "song2"]

"""
given an index number that is too HIGH to remove a single song
returns an error
"""
def test_given_too_high_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add("song")
    music_tracker.add("song2")
    with pytest.raises(Exception) as e:
        music_tracker.remove(2)
    error_message = str(e.value)
    assert error_message == "This song does not exist!"
    assert music_tracker.music_playlist() == ["song", "song2"]