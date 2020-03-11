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
La idea final del proyecto es poder predecir el éxito que pueda tener una posible película o serie en el mercado americano. Partiremos de un dataset etiquetado que escrapearemos también en este proyecto.

Los pasos a seguir serán:
- Creación del servidor de base de datos dockerizado con motor Postgre SQL. 📝 [Instrucciones](DDBB)
- Creación de las tablas en Postgre SQL.
- Obtención de datos atacando a la API Rest pública de [TMDb](https://www.themoviedb.org/documentation/api?language=es) usando Python. 📝 [Instrucciones](Get_data)

## Herramientas usadas 🔧
Estas son las herramientas usadas durante el desarrollo del proyecto:
- [Docker](https://www.docker.com/): Para el servidor Postgre SQL.
- [PyCharm Professional](https://www.jetbrains.com/es-es/pycharm/download): Como editor de código Python y Jupyter Notebook.
- [Postgre SQL](https://www.postgresql.org/): Como motor de bases de datos.
- [Data Grip](https://www.jetbrains.com/datagrip/?gclid=Cj0KCQiAwP3yBRCkARIsAABGiPp9LUgvaKBbgjd69efrNyAz1KU7Lyoab6hKzCIaSgV2ujDK3i7m5AEaAh6UEALw_wcB): Como IDE de Sql.

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓
* Sígueme en [Twitter](https://twitter.com/AsensiFj) 🐦