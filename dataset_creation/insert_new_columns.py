import psycopg2
from DDBB import config
from Get_data.actor import Actor


def update_productora_pelicula(lista):
    for pelicula in lista:
        contador = 0
        lista_productoras = get_productoras_from_id(pelicula)

        for productora in lista_productoras:
            contador += 1

            campo_productora = 'productora' + str(contador)

            actualiza_productora(pelicula, campo_productora, productora)


def actualiza_productora(id_pelicula, campo_productora, valor_productora):
    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        sql = "UPDATE dataset_final SET " + campo_productora + " = %s WHERE id = %s;"

        data = (valor_productora, id_pelicula)

        cursor.execute(sql, data)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.commit()
            connection.close()


def get_productoras_from_id(id_pelicula):
    lista_productoras = []

    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        sql = "select name from item_production_companies where iditem = %s and type = %s limit 2;"

        data = (id_pelicula, 'Movie')

        cursor.execute(sql, data)
        record = cursor.fetchall()

        for row in record:
            lista_productoras.append(row[0])

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

    return lista_productoras


def update_genero_pelicula(lista):
    for pelicula in lista:
        contador = 0
        lista_generos = get_generos_from_id(pelicula)

        for genero in lista_generos:
            contador += 1

            campo_genero = 'genero' + str(contador)

            actualiza_genero(pelicula, campo_genero, genero)


def actualiza_genero(id_pelicula, campo_genero, valor_genero):
    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        sql = "UPDATE dataset_final SET " + campo_genero + " = %s WHERE id = %s;"

        data = (valor_genero, id_pelicula)

        cursor.execute(sql, data)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.commit()
            connection.close()


def get_generos_from_id(id_pelicula):
    lista_generos = []

    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        sql = """
            select gen.name
            from item_genres itG
            inner join genre gen ON gen.id = itG.idgenre
            where itG.iditem = %s and itG.type = %s limit 2;
        """

        data = (id_pelicula, 'Movie')

        cursor.execute(sql, data)
        record = cursor.fetchall()

        for row in record:
            lista_generos.append(row[0])

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

    return lista_generos


def update_actores_generos(lista):
    for pelicula in lista:
        contador = 0
        lista_actores = get_actores_from_id(pelicula)

        for actor in lista_actores:
            contador += 1

            campo_actor = 'actor' + str(contador)
            campo_genero = 'genero_actor' + str(contador)

            update_actor_genero(pelicula, campo_actor, campo_genero, actor.name, actor.gender)


def update_actor_genero(id_pelicula, c_actor, c_genero, v_actor, v_genero):
    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        sql = "UPDATE dataset_final SET " + c_actor + " = %s, " + c_genero + " = %s WHERE id = %s;"

        data = (v_actor, v_genero, id_pelicula)

        cursor.execute(sql, data)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.commit()
            connection.close()


def get_actores_from_id(id):
    lista_actores = []

    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        sql = "SELECT id, name, gender FROM item_caracter WHERE type = %s AND iditem = %s LIMIT 28;"
        data = ('Movie', id)

        cursor.execute(sql, data)
        record = cursor.fetchall()

        for row in record:
            mi_actor = Actor(pType='Movie', pId=row[0], pName=row[1], pGender=row[2], pIdItem=id)
            lista_actores.append(mi_actor)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

    return lista_actores


def get_data():
    lista_elementos = []

    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        sql = "SELECT id FROM dataset_final;"

        cursor.execute(sql)
        record = cursor.fetchall()

        for row in record:
            lista_elementos.append(row[0])
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

    return lista_elementos


if __name__ == '__main__':
    lista_elementos = []

    lista_elementos = get_data()

    print('Actualizando actores')
    update_actores_generos(lista_elementos)

    print('Actualizando género películas')
    update_genero_pelicula(lista_elementos)

    print('Actualizando productoras')
    update_productora_pelicula(lista_elementos)
