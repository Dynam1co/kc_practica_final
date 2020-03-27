# Práctica final - BootCamp Big Data & Machine Learning
Toda la práctica ha sido realizada bajo el sistema operativo Windows 10 Pro.

No he hecho despliegue en cloud por los costes y por no poder usar una cuenta gratiuita ya que es necesaria la persistencia de los datos.

## Especificaciones del PC 🖥️
- Procesador: Comet Lake i7-10710U
- Memoria RAM: DDR IV 32 GB
- GPU: Nvidia GeForce GTX 1650 MAX Q

Todos los Docker 🐳 usados han sido de tipo Linux.

## Base de datos 💾
La base de datos seleccionada será [Postgre SQL](https://www.postgresql.org/) en ella se guardarán los datos scrapeados en tablas relacionales y una vez obtenidos se generará un único dataset.

## Comenzando 🚀
La idea final del proyecto es poder predecir el éxito que pueda tener una posible película o serie en el mercado americano. Partiremos de un dataset etiquetado que generaremos nosotros mismos leyendo datos de una API y escrapeando de una conocida web de películas.

Los pasos a seguir serán:
1. Creación del servidor de base de datos dockerizado con motor Postgre SQL. 📝 [Instrucciones](DDBB)
2. Creación de las tablas en Postgre SQL. 📝 [Instrucciones](DDBB)
3. Obtención de datos atacando a la API Rest pública de [TMDb](https://www.themoviedb.org/documentation/api?language=es) y scrapeando la web de [IMDb](https://www.imdb.com/?ref_=nv_home) usando Python. 📝 [Instrucciones](Get_data)
4. Generar dataset final a partir de los datos obtenidos 📝 [Instrucciones](dataset_creation)
5. Limpieza y generación de características ![Jupyter](jupyter_logo.png) [Notebook](limpieza_datos.ipynb)
6. Predicción:
    1. Predicción usando algoritmos de machine learning clásico ![Jupyter](jupyter_logo.png) [Notebook](machine_learning_clasico.ipynb)
    2. Predicción usando algoritmos de deep learning solo datos numéricos ![Jupyter](jupyter_logo.png) [Notebook](deep_learning_datos_numericos.ipynb)
    3. Predicción usando algoritmos de deep learning cominando datos numéricos (MLP) con imágenes (CNN) ![Jupyter](jupyter_logo.png) [Notebook](deep_learning_combinado.ipynb)

## Resultados 📊
Se han entrenado varios modelos de Machine Learning y de Deep Learning, estos son los porcentajes de error de cada uno de los modelos:
- Regresión lineal: 11,59%
- Lasso: 11,53%
- Random forest: 11,60%
- Red neuronal MLP: 12,08%
- Red neuronal mixta (MLP + CNN): 11,48%

## Herramientas usadas 🔧
Estas son las herramientas usadas durante el desarrollo del proyecto:
- [Docker](https://www.docker.com/): Para el servidor Postgre SQL.
- [PyCharm Professional](https://www.jetbrains.com/es-es/pycharm/download): Como editor de código Python y Jupyter Notebook.
- [Postgre SQL](https://www.postgresql.org/): Como motor de bases de datos.
- [Data Grip](https://www.jetbrains.com/datagrip/?gclid=Cj0KCQiAwP3yBRCkARIsAABGiPp9LUgvaKBbgjd69efrNyAz1KU7Lyoab6hKzCIaSgV2ujDK3i7m5AEaAh6UEALw_wcB): Como IDE de Sql.

## Librerías Python usadas 🛠️
- **psycopg2**: Python-PostgreSQL Database Adapter [Fuente](https://pypi.org/project/psycopg2/)
- **dotenv**: Reads the key-value pair from .env file and adds them to environment variable. It is great for managing app settings during development and in production using 12-factor principles. [Fuente](https://pypi.org/project/python-dotenv/)
- **request**: Request library is the de facto standard for making HTTP requests in Python. [Fuente](https://realpython.com/python-requests/)
- **time**: Para no hacer muchas llamadas seguidas a la API.
- **Scrapy**: Para scrapear la variable presupuesto de la web IMDb.
- **urllib**: Para descarga de imágenes de películas
- **pandas**: Para análisis y manipulación de datos. [Fuente](https://pandas.pydata.org/)
- **cv2**: Para el redimensionado de imágenes. [Fuente](https://pypi.org/project/opencv-python/)
- **Numpy**: Para operar a alto nivel con vectores o matrices. [Fuente](https://numpy.org/)
- **Matplotlib**: Para la generación de gráficos a partir de datos de NumPy. [Fuente](https://matplotlib.org/)
- **Tensorflow**: Para poder construir y entrenar redes neuronales. [Fuente](https://www.tensorflow.org/)
- **Keras**: Para facilitar el uso de Tensorflow. [Fuente](https://keras.io/)
- **Scikit-Learn**: Para funciones de aprendizaje automático. [Fuente](https://scikit-learn.org/stable/)

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓
* Sígueme en [Twitter](https://twitter.com/AsensiFj) 🐦