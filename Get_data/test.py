import psycopg2
import sys

sys.path.insert(1, "./DDBB/")
import config

def conectar():
    connection = None

    try:
        connection = config.get_connection_by_config()

        cursor = connection.cursor()

        cursor.execute('SELECT * FROM pelicula;')
        record = cursor.fetchone()
        print(record)
    except (Exception, psycopg2.Error) as error:
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == '__main__':
    conectar()