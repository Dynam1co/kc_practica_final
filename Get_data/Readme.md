# Descarga de datos TMDb
En esta parte descargaremos los datos necesarios usando la API de [TMDb](https://www.themoviedb.org/documentation/api?language=es) y los insertaremos en la base de datos Postgre SQL que creamos en el [apartado anterior](https://github.com/Dynam1co/kc_practica_final/blob/master/DDBB/DDBB.md).

## Librerías Python usadas 🛠️
- **psycopg2**: Python-PostgreSQL Database Adapter [Fuente](https://pypi.org/project/psycopg2/)
- **dotenv**: Reads the key-value pair from .env file and adds them to environment variable. It is great for managing app settings during development and in production using 12-factor principles. [Fuente](https://pypi.org/project/python-dotenv/)
- **request**: Request library is the de facto standard for making HTTP requests in Python. [Fuente](https://realpython.com/python-requests/)
- **time**: Para no hacer muchas llamadas seguidas a la API.

## Sobre la api key de TMDB ⌨️
Ya que la api key para la api de TMDb es personal, he usado la librería **dotenv** para tratarla como una variable de entorno, por lo que dicha clave no está en el repositorio, para hacer las pruebas de esta parte deberás registrarte en TMDb y obtener tu propia clave, después crear en el proyecto un fichero **.env** y guardarla allí con el nombre "API_KEY_TMDB" de la siguiente forma:
```
API_KEY_TMDB=abcerkd73847
```

## Descarga de items e inserción en la base de datos ⚙️
Dentro de esta carpeta (Get_data) se encuentran los siguientes ficheros:
- [**downloadData.py**](downloadData.py): Este fichero es el principal, el que inicia la descarga de todos los datos necesarios. Al tener una función "main" solo habría que ejecutar este fichero de la siguiente forma: ```python downloadData.py``` En la consola veremos en cada momento qué se está descargando.
- [**genero.py**](genero.py): Es una clase con los atributos de géneros de películas y un método para insertar dichos métodos en la base de datos.
- [**itemCatalogo.py**](itemCatalogo.py): Es la clase de la película/serie. Contiene los atributos y un método para insertar en la base de datos.
- [**todo.py**](todo.py): Este archivo contiene funciones que devuelven la url de cada método de la API.