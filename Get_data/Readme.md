# Descarga de datos TMDb
En esta parte descargaremos los datos necesarios usando la API de [TMDb](https://www.themoviedb.org/documentation/api?language=es) y los insertaremos en la base de datos Postgre SQL que creamos en el [apartado anterior](https://github.com/Dynam1co/kc_practica_final/blob/master/DDBB/DDBB.md).

## Sobre la api key de TMDB ⌨️
Ya que la api key para la api de TMDb es personal, he usado la librería **dotenv** para tratarla como una variable de entorno, por lo que dicha clave no está en el repositorio, para hacer las pruebas de esta parte deberás registrarte en TMDb y obtener tu propia clave, después crear en el proyecto un fichero **.env** y guardarla allí con el nombre "API_KEY_TMDB" de la siguiente forma:
```
API_KEY_TMDB=abcerkd73847
```

## Anotación importante sobre la ingesta 📌
Viendo que se encuentran más datos de películas que de series y que no sería correcto mezclar en el mismo modelo las dos partes, decido centrarme solo en las películas, por lo que el dataset general con la unión de datos de todas las tablas se hará solo de las películas al igual que la obtención del id de IMDb y del presupuesto.

## Scrapeo de la variable presupuesto 🕵️
En la API de TMDb está la variable presupuesto, pero 4000 de las 10000 películas no tenían ese valor relleno, por lo que se decide obtener una nueva variable de la API, el **Id de IMDb** con ese dato y haciendo uso de las librerías **Scrapy** y **Requests** obtenemos el valor de la variable presupuesto de las películas que podamos scrapeando directamente la web de IMDb.

## Descarga de imágenes 🖼️
Desde el fichero [**downloadData.py**](downloadData.py) también se descargan las imágenes de las películas a una carpeta del proyecto llamada **img** por cuestiones de tamaño y copyright las imágenes no están subidas al repositorio.

He decidido descargar las imágenes del poster de la película en lugar de las capturas de algún frame porque había menos nulos en esa columna.

Hemos usado el mismo script que hace la descarga de datos para redimensionar las imágenes ya que son muy grandes y además no todas tienen el mismo tamaño. Todas las imágenes se han quedado a 224x336 píxeles.

## Descarga de items e inserción en la base de datos ⚙️
Dentro de esta carpeta (Get_data) se encuentran los siguientes ficheros:
- [**downloadData.py**](downloadData.py): Este fichero es el principal, el que inicia la descarga de todos los datos necesarios. Al tener una función "main" solo habría que ejecutar este fichero de la siguiente forma: ```python downloadData.py``` En la consola veremos en cada momento qué se está descargando.
- [**genero.py**](genero.py): Es una clase con los atributos de géneros de películas y un método para insertar dichos métodos en la base de datos.
- [**itemCatalogo.py**](itemCatalogo.py): Es la clase de la película/serie. Contiene los atributos y un método para insertar en la base de datos.
- [**todo.py**](todo.py): Este archivo contiene funciones que devuelven la url de cada método de la API.
- [**prodCompany.py**](prodCompany.py): Es la clase de las productoras de cada serie o película. Al no tener un método en la API para descargar las productoras únicas, he hecho una query en SQL para obtener las productoras únicas:
```
insert into production_companies (id, name)
    select distinct id, name from item_production_companies group by id, name;
```
- [**actor.py**](actor.py): Es la clase para los actores de las series y películas. Al igual que pasaba con las productoras, no hay ningún método en la API que liste todos los actores, por lo que mediante una query en SQL creamos nuestra tabla de actores.
```
insert into caracter (id, name, gender)
    select distinct id, name, gender from item_caracter group by id, name, gender;
```
- [**scraperImdb.py**](scraperImdb.py): Se usa la librería Scrapy para obtener los presupuestos faltantes de la web IMDb. Esta es la única ingesta que no se ejecuta desde el fichero **downloadData.py** para ejecutar esta parte basta con ir a la terminal y ejecutar: ```python scraperImdb.py```.