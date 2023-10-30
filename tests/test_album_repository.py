from lib.album_repository import *
from lib.album import *

# when we call album_repository.all we get a list of all the albums 
# which reflects the seed data 

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1, 'Doolittle', 1989, 1), 
        Album(2, 'Surfer Rosa', 1988, 1), 
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
]
    
# find a single album by its id 

def test_with_id_returns_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album ==  Album(3, 'Waterloo', 1974, 2)

# when we call album.create we create a new album record in the database

# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = AlbumRepository(db_connection)

#     repository.create(Album(None, "Dark Side", 1998, 5))

#     result = repository.all()
#     assert result == [
#         Album(1, 'Doolittle', 1989, 1), 
#         Album(2, 'Surfer Rosa', 1988, 1), 
#         Album(3, 'Waterloo', 1974, 2),
#         Album(4, 'Super Trouper', 1980, 2),
#         Album(5, 'Bossanova', 1990, 1),
#         Album(6, 'Lover', 2019, 3),
#         Album(7, 'Folklore', 2020, 3),
#         Album(8, 'I Put a Spell on You', 1965, 4),
#         Album(9, 'Baltimore', 1978, 4),
#         Album(10, 'Here Comes the Sun', 1971, 4),
#         Album(11, 'Fodder on My Wings', 1982, 4),
#         Album(12, 'Ring Ring', 1973, 2),
#         Album(13, "Dark Side", 1998, 5)
#]