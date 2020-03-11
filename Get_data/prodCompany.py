import psycopg2
from DDBB import config


class ProductionCompany:
    def __init__(self, pType, pIdItem, pId, pName):
        self.type = pType
        self.idItem = pIdItem
        self.id = pId
        self.name = pName

    def insertar(self):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = """
                DO
                    $do$
                        BEGIN
                            IF NOT EXISTS (SELECT * FROM item_production_companies WHERE id = %s AND idItem = %s AND type = %s) THEN
                                INSERT INTO item_production_companies (id, idItem, type, name) VALUES (%s, %s, %s, %s);
                            end if;
                        END
                    $do$
            """

            data = (self.id, self.idItem, self.type, self.id, self.idItem, self.type, self.name)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()
