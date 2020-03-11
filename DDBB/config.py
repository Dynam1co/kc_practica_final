from configparser import ConfigParser
import psycopg2


def get_connection_by_config(archivo='../DDBB/base_de_datos.ini', seccion='postgresql'):
    # Crear el parser y leer el archivo
    parser = ConfigParser()
    parser.read(archivo)
 
    # Obtener la sección de conexión a la base de datos
    db = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            key = param[0]
            value = param[1]
            db[key] = value

        conn = psycopg2.connect(**db)
        return conn
    else:
        raise Exception('Secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))