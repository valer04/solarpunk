import random


def menu():
    """
    Este es el menu del juego. Aqui se accede a todas las opciones.
    """
    print('\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    print('+ Bienvenido al menu del juego!             +')
    print('+ 1. Jugar                                  +')
    print('+ 2. Informacion sobre solar punk           +')
    print('+ 3. Informacion sobre pueblos originarios  +')
    print('+ 4. Informacion sobre el conflicto         +')
    print('+    en Cabagra, Costa Rica                 +')
    print('+ 5. Referencias                            +')
    print('+ 6. Salir                                  +')
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')
    selection = obtener_seleccion()  # llama a la opcion seleccionada en el menu
    if selection == 1:
        inicio_juego()
    elif selection == 2:
        informacion_solar()
    elif selection == 3:
        informacion_originarios()
    elif selection == 4:
        informacion_conflicto()
    elif selection == 5:
        referencias()
    elif selection == 6:
        salir_del_juego()
    else:
        print('\nSelecciona una opcion valida')
        menu()


def informacion_solar():
    print('Signalis')


def informacion_originarios():
    print('Signalis')


def informacion_conflicto():
    print('Signalis')


def referencias():
    print('Signalis')


def salir_del_juego():
    print('\nGracias por jugar!')
    exit(0)


def informacion_juego():
    print('Lore dump')


def obtener_seleccion():
    """
    Funcion para selecciones con numeros
    """
    selection = input('Introduce tu seleccion: ')
    if selection.isdigit():
        return int(selection)
    else:
        print('\nIntroduce un numero valido')
        obtener_seleccion()


tablero = [1]


def inicio_juego():
    """
    inicia juego
    """
    global tablero
    # se definen columnas
    print('Escribe la cantidad de columnas de tu tablero')

    num = obtener_seleccion()

    while not (3 <= num <= 9):
        print('Debe ser un numero entre 3 y 9')
        num = obtener_seleccion()

    else:
        columnas = num * tablero

        # se aniaden las filas a la cuadrircular
        print('Escribe la cantidad de filas de tu tablero')
        num = obtener_seleccion()
        filas = num * [columnas]
        return dia(filas)


def dia(ciudad):
    for casilla in ciudad:
        print(casilla, end=' ')
        print()

    print('Donde deseas realizar un proyecto?')
    x = obtener_seleccion()
    y = obtener_seleccion()
    if not -1 < x < len(ciudad[0])-1:
        print('Debe ser un valor dentro de los parametos de la matriz.')
    elif not -1 < y < len(ciudad)-1:
        print('Debe ser un valor dentro de los parametos de la matriz.')
    else:
        ciudad[x][y] = 2
        for casilla in ciudad:
            print(casilla, end=' ')
            print()

def main():
    """
    La funcion principal llama al menu para iniciar
    """
    while True:
        menu()


if __name__ == "__main__":
    main()
