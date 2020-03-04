import todo
from itemCatalogo import ItemCatalogo
from genero import Genero
import time


def descargaPeliculas(pPagina=1):
    resp = todo.get_movie_popular(pPagina)

    if resp.status_code != 200:
        raise Exception('Cannot fetch movies: {}'.format(resp.status_code))

    fichero_json = resp.json()

    paginaActual = fichero_json['page']
    paginasTotales = fichero_json['total_pages']

    for result in fichero_json['results']:
        if 'release_date' in result:
            releaseDate = result['release_date']
        else:
            releaseDate = None

        if releaseDate == '':
            releaseDate = None

        if 'backdrop_path' in result:
            backPath = result['backdrop_path']
        else:
            backPath = None

        item = ItemCatalogo(
            'Movie',
            result['popularity'],
            result['vote_count'],
            result['poster_path'],
            result['id'],
            result['adult'],
            backPath,
            result['original_language'],
            result['original_title'],
            result['title'],
            result['vote_average'],
            result['overview'],
            releaseDate
        )

        for genre in result['genre_ids']:
            item.insertGenreId(genre)

        item.insertar()

    if paginaActual < paginasTotales:
        time.sleep(5)

        print('Descargando página:', paginaActual + 1)

        descargaPeliculas(paginaActual + 1)


def descargaSeries(pPagina=1):
    resp = todo.get_tv_popular(pPagina)

    if resp.status_code != 200:
        raise Exception('Cannot fetch movies: {}'.format(resp.status_code))

    fichero_json = resp.json()

    paginaActual = fichero_json['page']
    paginasTotales = fichero_json['total_pages']

    for result in fichero_json['results']:
        if 'first_air_date' in result:
            releaseDate = result['first_air_date']
        else:
            releaseDate = None

        if releaseDate == '':
            releaseDate = None

        if 'backdrop_path' in result:
            backPath = result['backdrop_path']
        else:
            backPath = None

        item = ItemCatalogo(
            'TV',
            result['popularity'],
            result['vote_count'],
            result['poster_path'],
            result['id'],
            False,  # Adult
            backPath,
            result['original_language'],
            result['original_name'],
            result['name'],
            result['vote_average'],
            result['overview'],
            releaseDate
        )

        for genre in result['genre_ids']:
            item.insertGenreId(genre)

        item.insertar()

    if paginaActual < paginasTotales:
        time.sleep(5)

        print('Descargando página:', paginaActual + 1)

        descargaSeries(paginaActual + 1)


def descargaGenerosPeliculas():
    resp = todo.get_genres_movies()

    if resp.status_code != 200:
        raise Exception('Cannot fetch movies: {}'.format(resp.status_code))

    fichero_json = resp.json()

    for item in fichero_json['genres']:
        miGenero = Genero(item['id'], item['name'])
        miGenero.insertar()


def descargaGenerosSeries():
    resp = todo.get_genres_tv()

    if resp.status_code != 200:
        raise Exception('Cannot fetch movies: {}'.format(resp.status_code))

    fichero_json = resp.json()

    for item in fichero_json['genres']:
        miGenero = Genero(item['id'], item['name'])
        miGenero.insertar()


if __name__ == '__main__':    
    #descargaGenerosPeliculas()
    #descargaGenerosSeries()
    descargaPeliculas()
    descargaSeries()
