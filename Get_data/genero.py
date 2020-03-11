import psycopg2
from DDBB import config


class Genero:
    def __init__(self, pId, pNombre):
        self.id = pId
        self.name = pNombre

    def insertar(self):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = """
                DO
                    $do$
                        BEGIN
                            IF NOT EXISTS (SELECT * FROM genre WHERE id = %s) THEN
                                INSERT INTO genre (id, name) VALUES (%s, %s);
                            end if;
                        END
                    $do$
            """

            data = (self.id, self.id, self.name)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()
