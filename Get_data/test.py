import psycopg2
import sys
import os
from dotenv import load_dotenv

sys.path.insert(1, "./DDBB/")
import config

def conectar():
    connection = None

    try:
        connection = config.get_connection_by_config()        
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM genre;')
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

def variableEntornoAPI():    
    load_dotenv()
    
    if not os.getenv('API_KEY_TMDB'):
        raise Exception('No encontrada API KEY TMDB')

if __name__ == '__main__':
    conectar()
    variableEntornoAPI()