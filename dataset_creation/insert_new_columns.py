import psycopg2
from DDBB import config
from Get_data.actor import Actor


def update_actores_generos(lista):
    contador = 0

    for pelicula in lista:
        lista_actores = get_actores_from_id(pelicula)

        for actor in lista_actores:
            contador += 1

            campo_actor = 'actor' + str(contador)
            campo_genero = 'genero_actor' + str(contador)

            update_actor_genero(pelicula, campo_actor, campo_genero, actor.name, actor.gender)


def update_actor_genero(id_pelicula, c_actor, c_genero, v_actor, v_genero):
    connection = None
    print(id_pelicula)

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

    update_actores_generos(lista_elementos)
