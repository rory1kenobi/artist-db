from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository


def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre)  VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s, %s, %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'])
    return album

def select_all():  
    album = [] 
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['user_id'])
        album = Album(row['title'], artist, row['genre'] )
        album.append(album)
    return album