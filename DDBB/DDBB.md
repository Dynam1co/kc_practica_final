# Creación base de datos Postgre SQL
En esta misma carpeta se encuentra el [Dockerfile](Dockerfile). Una vez nos hayamos clonado el proyecto, desde la consola navegaremos a la ruta donde se encuentre el Dockerfile y ejecutaremos el siguiente comando:
```
$ docker build -t eg_postgresql .
```
Este comando nos habrá generado una imagen llamada **eg_postgresql**

Con este comando creamos un nuevo contenedor a partir de la nueva imagen (o lo arrancará si ya lo tenemos creado):
```
$ docker run -P --name pg_test eg_postgresql
```
Este comando dejará en ejecución el entorno de Postgre, abrimos una nueva terminal y nos conectamos al bash del contenedor **eg_postgresql** con el siguiente comando:
```
$ docker run --rm -t -i --link pg_test:pg eg_postgresql bash
```
Una vez ya conectados al bash del contenedor, abrimos el cliente de Postgres y nos conectamos directamente a la base de datos que creamos en el Dockerfile **db_practica_kc** con el siguiente comando:
```
postgres@7ef98b1b7243:/$ psql -h $PG_PORT_5432_TCP_ADDR -p $PG_PORT_5432_TCP_PORT -d db_practica_kc -U fjasensi --password
```
Nos pedirá la contraseña que especificamos en el Dockerfile cuando creamos el usuario de BBDD y ya estaríamos dentro del cliente de Postgres.

## Notas adicionales 💡
Para salir del cliente de Postgres tecleamos:
```
\q
```
Esto nos devolverá al bash del contenedor, para salir de él y volver a nuestra terminal escribimos:
```
exit
```