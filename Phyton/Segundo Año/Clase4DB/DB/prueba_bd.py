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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #placeholder
            id_persona = input("Digite un número para el id")
            cursor.execute(sentencia, (id_persona,)) #De esta manera ejecutamos la sentencia
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()