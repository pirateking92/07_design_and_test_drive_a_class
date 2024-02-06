import pytest

from lib.music_listening import *


"""
On initialisation,
returns an empty list
"""
def test_for_empty_list():
    music_list = MusicListening()
    assert music_list.music_history == []

"""
given a string of "Mamma Mia"
adds to empty list
"""
def test_for_add_music_to_list():
    music_list = MusicListening()
    music_list.add_tracks("Mamma Mia")
    assert music_list.music_history == ["Mamma Mia"]

"""
given many strings
adds to empty list
"""
def test_for_add_multiple_songs_to_list():
    music_list = MusicListening()
    music_list.add_tracks("Mamma Mia")
    music_list.add_tracks("Hail mary")
    music_list.add_tracks("Master of puppets")
    assert music_list.music_history == ["Mamma Mia", "Hail mary", "Master of puppets"]

def test_voiding_duplicate_songs():
    music_list = MusicListening()
    music_list.add_tracks("Mamma Mia")
    music_list.add_tracks("Mamma Mia")
    music_list.add_tracks("Master of puppets")
    assert music_list.show_list() == ["Mamma Mia", "Master of puppets"]

def test_for_integers():
    with pytest.raises(Exception) as err:
        music_list = MusicListening()
        music_list.add_tracks(1212)
    assert str(err.value) == "Track names only"