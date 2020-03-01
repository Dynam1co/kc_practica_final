import psycopg2

#connection = psycopg2.connect("dbname='db_practica_kc' user='fjasensi' host='localhost' password='passPractica'")
connection = psycopg2.connect(
    user = 'fjasensi',
    password='passPractica',
    host='localhost',
    port='5432',
    database='db_practica_kc'
)


cursor = connection.cursor()

cursor.execute('SELECT * FROM pelicula;')
record = cursor.fetchone()
print(record)

if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")