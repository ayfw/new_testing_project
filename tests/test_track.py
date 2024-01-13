from lib.track import *

"""
we create new title and artist
returns the title and artist
"""
def test_construct_new_title_and_artist():
    track = Track("my title 1", "my artist 1")
    assert track.title == "my title 1"
    assert track.artist == "my artist 1"

"""
formats the title and artist as "TITLE by ARTIST"
"""
def test_format_title_and_artist():
    track = Track("my title 1", "my artist 1")
    assert track.format() == "my title 1 by my artist 1"