import psycopg2
import sys
from dotenv import load_dotenv

sys.path.insert(1, "./DDBB/")
import config


class Actor:
    def __init__(self, pType, pId, pName, pGender, pIdItem):
        self.type = pType
        self.id = pId
        self.name = pName
        self.gender = pGender
        self.idItem = pIdItem

    def insertar(self):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = """
                DO
                    $do$
                        BEGIN
                            IF NOT EXISTS (SELECT * FROM item_caracter WHERE id = %s AND idItem = %s AND type = %s) THEN
                                INSERT INTO item_caracter (id, idItem, type, name, gender) VALUES (%s, %s, %s, %s, %s);
                            end if;
                        END
                    $do$
            """

            data = (self.id, self.idItem, self.type, self.id, self.idItem, self.type, self.name, self.gender)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()
