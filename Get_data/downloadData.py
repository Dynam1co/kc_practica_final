import todo
from itemCatalogo import ItemCatalogo
from genero import Genero
from prodCompany import ProductionCompany
from actor import Actor
import time


def descarga_imagenes_pelicula():
    print('Descargando imágenes de películas')
    print('------------------------------------------')
    print('')

    tipo = 'Movie'
    item = ItemCatalogo(None, None, None, None, None, None, None, None, None, None, None, None, None)

    lista_elementos = item.get_poster_url(tipo)
    i = 0
    total_elementos = len(lista_elementos)

    for elemento in lista_elementos:
        i += 1
        print('Película:', i, 'de:', total_elementos)

        elemento.local_poster_path = todo.download_image(elemento.id, elemento.poster_path)
        elemento.actualiza_ruta_imagen_local()

        print(elemento.local_poster_path)



def descargaIdExternoPelicula():
    print('Descargando id IMDb películas')
    print('------------------------------------------')
    print('')

    tipo = 'Movie'

    # Obtener todas las películas de la BBDD Postgre
    listaElementos = ItemCatalogo.getAll(tipo, False, False)
    i = 0
    totalElementos = len(listaElementos)

    # Por cada película obtengo id externo atacando a la API
    for elemento in listaElementos:
        time.sleep(2)

        i += 1
        print('Película:', i, 'de:', totalElementos)

        resp = todo.get_external_id_movie(elemento)

        if resp.status_code != 200:
            print('Error al descargar. Error:', resp.status_code)
        else:
            fichero_json = resp.json()

            if 'imdb_id' in fichero_json:
                imdbId = fichero_json['imdb_id']

                ItemCatalogo.actualizaIdExterno(tipo, elemento, imdbId)


def descargaPresupuestoPelicula():
    print('Descargando presupuesto películas')
    print('------------------------------------------')
    print('')

    tipo = 'Movie'

    # Obtener todas las películas de la BBDD Postgre
    listaElementos = ItemCatalogo.getAll(tipo, False, False)
    i = 0
    totalElementos = len(listaElementos)

    # Por cada película obtengo su presupuesto atacando a la API
    for elemento in listaElementos:
        time.sleep(2)

        i += 1
        print('Película:', i, 'de:', totalElementos)

        resp = todo.get_budget_movie(elemento)

        if resp.status_code != 200:
            print('Error al descargar. Error:', resp.status_code)
        else:
            fichero_json = resp.json()

            if 'budget' in fichero_json:
                presupuesto = fichero_json['budget']

                ItemCatalogo.actualizaPresupuesto(tipo, elemento, presupuesto)


def descargaCreditsPelicula():
    print('Descargando créditos películas')
    print('------------------------------------------')
    print('')

    tipo = 'Movie'

    # Obtener todas las películas de la BBDD Postgre
    listaElementos = ItemCatalogo.getAll(tipo, False, True)
    i = 0
    totalElementos = len(listaElementos)

    # Por cada película obtengo sus créditos atacando a la API
    for elemento in listaElementos:
        time.sleep(2)

        i += 1
        print('Película:', i, 'de:', totalElementos)

        resp = todo.get_credits_movie(elemento)

        if resp.status_code != 200:
            print('Error al descargar. Error:', resp.status_code)
        else:
            fichero_json = resp.json()

            if 'cast' in fichero_json:
                for actor in fichero_json['cast']:
                    idActor = None
                    nombreActor = None
                    generoActor = None

                    if 'id' in actor:
                        idActor = actor['id']

                    if 'name' in actor:
                        nombreActor = actor['name']

                    if 'gender' in actor:
                        generoActor = actor['gender']

                    miActor = Actor(tipo, idActor, nombreActor, generoActor, elemento)
                    miActor.insertar()


def descargaCreditsSerie():
    print('Descargando créditos series')
    print('------------------------------------------')
    print('')

    tipo = 'TV'

    # Obtener todas las películas de la BBDD Postgre
    listaElementos = ItemCatalogo.getAll(tipo, False, True)
    i = 0
    totalElementos = len(listaElementos)

    # Por cada serie obtengo sus créditos atacando a la API
    for elemento in listaElementos:
        time.sleep(2)

        i += 1
        print('Serie:', i, 'de:', totalElementos)

        resp = todo.get_credits_tv(elemento)

        if resp.status_code != 200:
            print('Error al descargar. Error:', resp.status_code)
        else:
            fichero_json = resp.json()

            if 'cast' in fichero_json:
                for actor in fichero_json['cast']:
                    idActor = None
                    nombreActor = None
                    generoActor = None

                    if 'id' in actor:
                        idActor = actor['id']

                    if 'name' in actor:
                        nombreActor = actor['name']

                    if 'gender' in actor:
                        generoActor = actor['gender']

                    miActor = Actor(tipo, idActor, nombreActor, generoActor, elemento)
                    miActor.insertar()


def descargaProdCompanyPelicula():
    print('Descargando productoras películas')
    print('------------------------------------------')
    print('')

    listaElementos = []
    tipo = 'Movie'

    # Obtener todas las películas de la BBDD Postgre
    listaElementos = ItemCatalogo.getAll(tipo, True, False)
    i = 0
    totalElementos = len(listaElementos)

    # Por cada película obtengo sus productoras atacando a la API
    for elemento in listaElementos:
        time.sleep(2)

        i += 1
        print('Película:', i, 'de:', totalElementos)

        resp = todo.get_prod_company_movie(elemento)

        if resp.status_code != 200:
            print('Error al descargar. Error:', resp.status_code)
        else:
            fichero_json = resp.json()

            # Insertar productora en BBDD
            if 'production_companies' in fichero_json:
                for compan in fichero_json['production_companies']:
                    miCompania = ProductionCompany(tipo, elemento, compan['id'], compan['name'])
                    miCompania.insertar()


def descargaProdCompanySerie():
    print('Descargando productoras series')
    print('------------------------------------------')
    print('')

    listaElementos = []
    tipo = 'TV'

    # Obtener todas las películas de la BBDD Postgre
    listaElementos = ItemCatalogo.getAll(tipo, True, False)
    i = 0
    totalElementos = len(listaElementos)

    # Por cada película obtengo sus productoras atacando a la API
    for elemento in listaElementos:
        time.sleep(2)

        i += 1
        print('Serie:', i, 'de:', totalElementos)

        resp = todo.get_prod_company_tv(elemento)

        if resp.status_code != 200:
            print('Error al descargar. Error:', resp.status_code)
        else:
            fichero_json = resp.json()

            # Insertar productora en BBDD
            if 'production_companies' in fichero_json:
                for compan in fichero_json['production_companies']:
                    miCompania = ProductionCompany(tipo, elemento, compan['id'], compan['name'])
                    miCompania.insertar()


def descargaPeliculas(pPagina=1):
    print('Descargando películas')
    print('------------------------------------------')
    print('')

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

        print('Descargando página:', paginaActual + 1, 'de', paginasTotales)

        descargaPeliculas(paginaActual + 1)


def descargaSeries(pPagina=1):
    print('Descargando series')
    print('------------------------------------------')
    print('')

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

        print('Descargando página:', paginaActual + 1, 'de', paginasTotales)

        descargaSeries(paginaActual + 1)


def descargaGenerosPeliculas():
    print('Descargando géneros de películas')
    print('------------------------------------------')
    print('')

    resp = todo.get_genres_movies()

    if resp.status_code != 200:
        raise Exception('Cannot fetch movies: {}'.format(resp.status_code))

    fichero_json = resp.json()

    for item in fichero_json['genres']:
        miGenero = Genero(item['id'], item['name'])
        miGenero.insertar()


def descargaGenerosSeries():
    print('Descargando géneros de series')
    print('------------------------------------------')
    print('')

    resp = todo.get_genres_tv()

    if resp.status_code != 200:
        raise Exception('Cannot fetch movies: {}'.format(resp.status_code))

    fichero_json = resp.json()

    for item in fichero_json['genres']:
        miGenero = Genero(item['id'], item['name'])
        miGenero.insertar()


if __name__ == '__main__':
    descargaGenerosPeliculas()
    descargaGenerosSeries()
    descargaPeliculas()
    descargaSeries()
    descargaProdCompanyPelicula()
    descargaProdCompanySerie()
    descargaCreditsPelicula()
    descargaCreditsSerie()
    descargaPresupuestoPelicula()
    descargaIdExternoPelicula()
    descarga_imagenes_pelicula()

