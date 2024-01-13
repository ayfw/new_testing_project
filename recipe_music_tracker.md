1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
"""
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
"""
2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def music_tracker(text):
    """add songs that I have listened to a music playlist

    Parameters: (list all parameters and their types)
        text: a string containing words and punctuation (e.g. "song")

    Returns: (state the return value and its type)
        a music list of songs I have listened to

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

"""
initially there are no songs
"""
def test_initially_no_songs():
    music_tracker = MusicTracker()
    => []

"""
given a single song
returns a list containing that single song
"""
def test_given_single_song_adds_to_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    => ["song"]

"""
given multiple songs
returns a list containing all songs
"""
def test_given_multiple_songs_adds_to_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.add(song3)
    => ["song", "song2", "song3"]

"""
given an index number to remove a single song
returns a list removing that single song
"""
def test_given_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.remove(0)
    => ["song2"]

"""
given an index number that is too LOW to remove a single song
returns an error
"""
def test_given_too_low_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.remove(-1)
    raise error "This song does not exist!"
    => ["song", "song2"]

"""
given an index number that is too HIGH to remove a single song
returns an error
"""
def test_given_too_high_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.remove(2)
    raise error "This song does not exist!"
    => ["song", "song2"]

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.music_tracker import *

"""
initially there are no songs
"""
def test_initially_no_songs():
    music_tracker = MusicTracker()
    => []

"""
given a single song
returns a list containing that single song
"""
def test_given_single_song_adds_to_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    => ["song"]

"""
given multiple songs
returns a list containing all songs
"""
def test_given_multiple_songs_adds_to_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.add(song3)
    => ["song", "song2", "song3"]

"""
given an index number to remove a single song
returns a list removing that single song
"""
def test_given_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.remove(0)
    => ["song2"]

"""
given an index number that is too LOW to remove a single song
returns an error
"""
def test_given_too_low_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.remove(-1)
    raise error "This song does not exist!"
    => ["song", "song2"]

"""
given an index number that is too HIGH to remove a single song
returns an error
"""
def test_given_too_high_index_removes_single_song_from_playlist():
    music_tracker = MusicTracker()
    music_tracker.add(song)
    music_tracker.add(song2)
    music_tracker.remove(2)
    raise error "This song does not exist!"
    => ["song", "song2"]