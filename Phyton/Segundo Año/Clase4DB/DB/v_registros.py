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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #placeholder
            entrada = input("Digite los id a buscar")
            llaves_primarias = (tuple(entrada.split(", ")),)
            cursor.execute(sentencia, llaves_primarias) #De esta manera ejecutamos la sentencia
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()