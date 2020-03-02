import todo
from itemCatalogo import ItemCatalogo


def descargaPeliculas(pPagina=1):
    resp = todo.get_movie_popular()

    if resp.status_code != 200:
        raise ApiError('Cannot fetch movies: {}'.format(resp.status_code))

    fichero_json = resp.json()

    paginaActual = fichero_json['page']
    paginasTotales = fichero_json['total_pages']

    for result in fichero_json['results']:
        item = ItemCatalogo(
            'Movie',
            result['popularity'],
            result['vote_count'],
            result['poster_path'],
            result['id'],
            result['adult'],
            result['backdrop_path'],
            result['original_language'],
            result['original_title'],
            result['title'],
            result['vote_average'],
            result['overview'],
            result['release_date']
        )

        for genre in result['genre_ids']:
            item.insertGenreId(genre)

        print(item)


if __name__ == '__main__':
    descargaPeliculas()
