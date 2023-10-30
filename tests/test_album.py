from lib.album import *


#constructs with id, title, release_year, artist_id

def test_constructs_with_specified_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id ==1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2

# when i construct an album, it formats into a readable string

def test_artists_format_nicely():
    album = Album(1, "Dark Side", 1995, 2)
    assert str(album) == "Album(1, Dark Side, 1995, 2)"

# when two albums with the same fields are constructed, they are made equal

def test_with_two_equal_albums_are_equal():
    album1 = Album(1, "Dark Side", 1995, 2)
    album2 = Album(1, "Dark Side", 1995, 2)
    assert album1 == album2
