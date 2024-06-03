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
    Función para selecciones con números
    """
    selection = input('Introduce tu selección: ')
    if selection.isdigit():
        return int(selection)
    else:
        print('\nIntroduce un número válido')
        return obtener_seleccion()


tablero = [' ']


def win(persona):
    """
    Verifica si el jugador ha ganado.
    """
    # Verifica filas
    for fila in persona:
        if all(celda == 'P' for celda in fila):
            print("¡Has ganado!")
            return menu()

    # Verifica columnas
    for col in range(len(persona[0])):
        if all(fila[col] == 'P' for fila in persona):
            print("¡Has ganado!")
            return menu()

    # Si no se ha encontrado una fila o columna completa de 'P', el juego continúa.
    print("El juego continúa.")


def lose(signalis):
    """
    Verifica si el jugador ha perdido.
    """
    # Verifica filas
    for fila in signalis:
        if all(celda == 'X' for celda in fila):
            print("¡Has perdido! Los usurpadores separaron la ciudad.")
            return menu()

    # Verifica columnas
    for col in range(len(signalis[0])):
        if all(fila[col] == 'X' for fila in signalis):
            print("¡Has perdido! Los usurpadores separaron la ciudad.")
            return menu()


flag = False


def pipipi(pi):
    global flag
    while flag:
        for i in range(len(pi)):
            for j in range(len(pi[i])):
                if pi[i][j] == 'I':
                    pi[i][j] = 'P'
        flag = False
        dia(pi)


def inicio_juego():
    """
    Inicia el juego
    """
    # Se definen columnas
    print('Escribe la cantidad de columnas de tu tablero')
    num = obtener_seleccion()

    while not (3 <= num <= 9):
        print('Debe ser un número entre 3 y 9')
        num = obtener_seleccion()

    columnas = [' '] * num  # Inicializa una fila con el número correcto de columnas

    # Se añaden las filas a la cuadrícula
    print('Escribe la cantidad de filas de tu tablero')
    num = obtener_seleccion()

    while not (3 <= num <= 9):
        print('Debe ser un número entre 3 y 9')
        num = obtener_seleccion()
    filas = [columnas[:] for _ in range(num)]  # Crea una matriz de filas y columnas

    return dia(filas)


def dia(ciudad):
    global tablero
    tablero = ciudad
    pipipi(tablero)
    for fila in tablero:
        print(("[{0}]".format(', '.join(map(str, fila)))))
    win(tablero)
    print('Que deseas hacer?\n'
          '1. Proyecto\n'
          '2. Iniciativa\n'
          '3. Cultura\n')
    seleccion = obtener_seleccion()
    if seleccion == 1:
        iniciativa(tablero)
    elif seleccion == 2:
        proyecto()
    elif seleccion == 3:
        cultura()
    else:
        print('Seleccion invalida')
        dia(tablero)


def iniciativa(ciudad):
    global tablero, flag
    tablero = ciudad
    print('¿Dónde deseas realizar un proyecto? (Escribe 00 para devolverte)')
    x = obtener_seleccion()
    y = obtener_seleccion()

    # Validación de índices
    if not 0 <= x < len(ciudad[0]):
        print('Debe ser un valor dentro de los parámetros de la matriz.')
        iniciativa(tablero)
    elif not 0 <= y <= len(ciudad):
        print('Debe ser un valor dentro de los parámetros de la matriz.')
        iniciativa(tablero)
    elif ciudad[y][x] == 0:
        print('Esta casilla ha sido usurpada')
        iniciativa(tablero)
    elif x == 9 and y == 9:
        dia(tablero)
    else:
        # Modifica solo el valor específico
        tablero[y][x] = 'I'  # Usamos y para las filas y x para las columnas
        for fila in tablero:
            print(("[{0}]".format(', '.join(map(str, fila)))))
            flag = True
    return noche(tablero)


def proyecto():
    print('WIP')
    dia(tablero)


def cultura():
    print('WIP')
    dia(tablero)


def noche(ciudad):
    global tablero
    print('Empieza la noche')
    for i in range(len(ciudad)):
        for j in range(len(ciudad[i])):
            if random.random() < 0.1:  # 10% de probabilidad de ser usurpado
                if ciudad[i][j] == 'I':
                    ciudad[i][j] = 'I'
                else:
                    ciudad[i][j] = 'X'

    tablero = ciudad
    for fila in tablero:
        print(("[{0}]".format(', '.join(map(str, fila)))))
    print('La noche ha pasado')
    lose(tablero)

    return dia(tablero)


def main():
    """
    La funcion principal llama al menu para iniciar
    """
    while True:
        menu()


if __name__ == "__main__":
    main()
