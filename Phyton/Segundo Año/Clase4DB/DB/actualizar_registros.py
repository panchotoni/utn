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
            sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1) #Esto es una tupla
            cursor.executemany(sentencia, valores) #De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount
            print(f'Los registros son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()