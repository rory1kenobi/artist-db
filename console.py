import pdb 
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository  

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist("Name1")
artist_repository.save(artist1)
artist2 = Artist("name2")
artist_repository.save(artist2)
artist3 = Artist("Name3")
artist_repository.save(artist3)
artist4 = Artist("name4")
artist_repository.save(artist4)

album1 = Album("title1", artist1, "rock")
album_repository.save(album1)
album2 = Album("title2", artist2, "punk")
album_repository.save(album2)
album3 = Album("title3", artist3, "pop")
album_repository.save(album3)
album4 = Album("title4", artist4, "jazz")
album_repository.save(album4)

# for album in album.repository.select_all():
#     print(album.__dict__)

pdb.set_trace()