import psycopg2
from DDBB import config


class ItemCatalogo:
    def __init__(self, pTipo, pPopularity, pVoteCount, pPosterPath, pId, pAdult, pBackdropPath, pOriginalLanguage, pOriginalTitle, 
            pTitle, pVoteAverage, pOverview, pReleaseDate):

        self.tipo = pTipo
        self.popularity = pPopularity
        self.vote_count = pVoteCount
        self.poster_path = pPosterPath
        self.id = pId
        self.adult = pAdult
        self.backdrop_path = pBackdropPath
        self.original_language = pOriginalLanguage
        self.original_title = pOriginalTitle
        self.genre_ids = []
        self.title = pTitle
        self.vote_average = pVoteAverage
        self.overview = pOverview
        self.release_date = pReleaseDate
        self.budget = None
        self.extId = None

    def insertGenreId(self, pId):
        self.genre_ids.append(pId)

    def urlsImdb():
        listaElementos = []

        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = """
                    SELECT 'https://www.imdb.com/title/' || imdb_id as url_imdb 
                    FROM item where type = 'Movie' and budget = 0 and imdb_id is not null;
                """

            cursor.execute(sql)
            record = cursor.fetchall()

            for row in record:
                listaElementos.append(row[0])
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()                
                connection.close()

        return listaElementos

    def getAll(pTipo, pProdCompany, pCast):
        listaElementos = []

        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()
            
            if pProdCompany:
                sql = """
                        select id from item itm where 
                            not exists(select * from item_production_companies pc where pc.type = itm.type AND pc.iditem = itm.id) 
                            AND type = '%s';
                    """ % pTipo
            elif pCast:
                sql = """                    
                        select id from item itm where 
                            not exists(select * from item_caracter pc where pc.type = itm.type AND pc.idItem = itm.id) 
                            AND type = '%s';
                    """ % pTipo
            else:
                sql = """
                        select id from item where type = '%s';
                    """ % pTipo
            
            cursor.execute(sql)
            record = cursor.fetchall()

            for row in record:
                listaElementos.append(row[0])
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()                
                connection.close()

        return listaElementos

    def actualizaIdExterno(pTipo, pId, pIdExterno):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = "UPDATE item SET imdb_id = %s WHERE type = %s AND id = %s;"                

            data = (pIdExterno, pTipo, pId)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()

    def actualizaPresupuesto(pTipo, pId, pPresupuesto):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = "UPDATE item SET budget = %s WHERE type = %s AND id = %s;"                

            data = (pPresupuesto, pTipo, pId)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()

    def actualizaPresupuestoImdb(pTipo, pIdImdb, pPresupuesto):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = "UPDATE item SET budget = %s WHERE type = %s AND imdb_id = %s;"

            data = (pPresupuesto, pTipo, pIdImdb)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()

    def insertar(self):
        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()

            sql = """
                DO
                    $do$
                        BEGIN
                            IF NOT EXISTS (SELECT * FROM item WHERE id = %s AND type =  %s) THEN
                                INSERT INTO item (id, type, popularity, vote_count, poster_path, adult, backdrop_path, original_language, original_title, title, 
                                    vote_average, overview, release_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            END IF;
                        END;
                    $do$
            """

            data = (self.id, self.tipo, self.id, self.tipo, self.popularity, self.vote_count, self.poster_path, self.adult, 
                self.backdrop_path, self.original_language, self.original_title, self.title, self.vote_average, self.overview, self.release_date)

            cursor.execute(sql, data)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.commit()
                connection.close()

        # Categorías del elemento
        for cat in self.genre_ids:
            try:
                connection = config.get_connection_by_config()

                cursor = connection.cursor()

                sql = """
                    DO
                        $do$
                            BEGIN
                                IF NOT EXISTS (SELECT * FROM item_genres WHERE idItem = %s AND type =  %s AND idGenre = %s) THEN
                                    INSERT INTO item_genres (idItem, type, idGenre) VALUES (%s, %s, %s);
                                END IF;
                            END;
                        $do$
                """

                data = (self.id, self.tipo, cat, self.id, self.tipo, cat)

                cursor.execute(sql, data)
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)
            finally:
                # closing database connection.
                if(connection):
                    cursor.close()
                    connection.commit()
                    connection.close()