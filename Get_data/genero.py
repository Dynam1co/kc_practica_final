import psycopg2
import sys
import os
from dotenv import load_dotenv

sys.path.insert(1, "./DDBB/")
import config


class Genero:
    def __init__(self, pTipo, pId, pNombre):
        self.type = pTipo
        self.id = pId
        self.name = pNombre

    def insertar(self):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = "INSERT INTO genre (id, name, type) VALUES (%s, %s, %s);"
            data = (self.id, self.name, self.type)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()                
