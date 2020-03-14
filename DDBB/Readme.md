# Creación base de datos Postgre SQL
En esta misma carpeta se encuentra el [Dockerfile](Dockerfile). Una vez nos hayamos clonado el proyecto, desde la consola navegaremos a la ruta donde se encuentre el Dockerfile y ejecutaremos el siguiente comando:
```
$ docker build -t eg_postgresql .
```
Este comando nos habrá generado una imagen llamada **eg_postgresql**

Con este comando creamos un nuevo contenedor a partir de la nueva imagen (si ya lo tenemos creado, solo habrá que arrancarlo, saltar al siguiente paso) indicamos que redirija el puerto por defecto de Posgres (5432) de nuestra máquina local, al puerto de Postgres del contenedor:
```
$ docker run -i -p 5432:5432 --name pruebaPython eg_postgresql
```
Arrancar contenedor **pruebaPython** (no ejecutar si no teníamos creado el contenedor previamente):
```
$ docker start pruebaPython
```
Este comando dejará en ejecución el entorno de Postgre, abrimos una nueva terminal y nos conectamos al bash del contenedor **eg_postgresql** con el siguiente comando:
```
$ docker run --rm -t -i --link pruebaPython:pg eg_postgresql bash
```
Una vez ya conectados al bash del contenedor, abrimos el cliente de Postgres y nos conectamos directamente a la base de datos que creamos en el Dockerfile **db_practica_kc** con el siguiente comando:
```
postgres@7ef98b1b7243:/$ psql -h $PG_PORT_5432_TCP_ADDR -p $PG_PORT_5432_TCP_PORT -d db_practica_kc -U fjasensi --password
```
Nos pedirá la contraseña que especificamos en el Dockerfile cuando creamos el usuario de BBDD y ya estaríamos dentro del cliente de Postgres.

## Diagrama base de datos y scripts creación 🗄️
Una vez montado el contenedor con el entorno Postgre SQL solo tendríamos que crear las tablas necesarias en la misma base de datos que se creó en el Dockerfile.
### Diagrama
![Diagrama SQL](Diagram_DDBB.png)
### Script creación BBDD
Aquí esta el script de creación de las tablas [Script](script.sql)

## Notas adicionales 💡
Para salir del cliente de Postgres tecleamos:
```
\q
```
Esto nos devolverá al bash del contenedor, para salir de él y volver a nuestra terminal escribimos:
```
exit
```