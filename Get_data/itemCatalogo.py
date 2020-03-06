import psycopg2
import sys
from dotenv import load_dotenv

sys.path.insert(1, "./DDBB/")
import config


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

    def insertGenreId(self, pId):
        self.genre_ids.append(pId)

    def getAll(pTipo):
        listaElementos = []

        connection = None

        try:
            connection = config.get_connection_by_config()

            cursor = connection.cursor()
            
            sql = """
                    select id from item itm where 
                        not exists(select * from item_production_companies pc where pc.type = itm.type AND pc.iditem = itm.id) 
                        AND type = '%s';
                """
            
            data = (pTipo)

            cursor.execute(sql, data)
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