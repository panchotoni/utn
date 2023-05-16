from dominio.Peliculas import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Listar las peliculas')
        print('3. Eliminar catálogo de peliculas')
        print('4. Salir')
        opcion = int(input('Digite una de las opciones: '))

        if opcion == 1:
            nombre_pelicula = input('Digite el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_peliculas(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrio un error de tipo: {e}')
        opcion = None

    else:
        print('Salimos del Programa')

