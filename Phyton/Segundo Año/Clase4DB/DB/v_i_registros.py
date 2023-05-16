import psycopg2 #ESTO ES PARA CONECTARNOS A POSTGREE

conexion = psycopg2.connect(
    user= 'postgres',
    password= 'BELGRANO.,97',
    host= '127.0.0.1',
    port= '5432',
    database= 'test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@mail.com') #Tupla de Tuplas
                ('Marcos', "Canto", 'mcanto@mail.com')
                ('Marcelo', 'Cuenca', 'cuencam@mail.com')
            ) #Esto es una tupla
            cursor.executemany(sentencia, valores) #De esta manera ejecutamos la sentencia
            registros_insertados = cursor.rowcount
            print(f'Los registros son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()