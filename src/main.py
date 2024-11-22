import os


BOARD_SIZE = {
    "filas": 3,
    "columnas": 3
}


def limpiar_terminal():
    """
    
    """
    os.system("cls")


def pausa():
    """
    
    """
    input("\nPresione ENTER para continuar...")


def crear_tablero(filas: int, columnas: int) -> list:
    """
    
    """
    tablero = []

    for i in range(filas):
        tablero.append([])
        for _ in range(columnas):
            tablero[i].append(" ")

    return tablero


def mostrar_tablero(tablero: list) -> str:
    """
    
    """
    tablero_completo = ""
    separador_lineas = "-" * (len(tablero[0]) * 4) + "-"

    i = 1

    for fila in tablero:
        tablero_completo += f"\n| {' | '.join(map(str, fila))} | {i}" + f"\n{separador_lineas}"
        i += 1

    tablero_completo = "  1   2   3\n" + separador_lineas + tablero_completo
    return tablero_completo


def actualizar_tablero(tablero: list[list[str]], x: int, y: int, jugador):
    """
    
    """
    if jugador == 1:
        ficha = "x"
    else:
        ficha = "o"
    try:
        tablero[x][y] = ficha
    except IndexError:
        print("*ERROR* La ficha no puede ir ahí.")

    return tablero
    

def mostrar_menu():
    return"""
    ¡Bienvenidos al Tres en Raya!

    El objetivo del juego es alinear tres símbolos iguales, ya sea en fila, columna o diagonal.
    La partida termina cuando uno de los jugadores consigue alinear tres símbolos o cuando el tablero está lleno.  

    ¡Buena suerte!
    """


def mostrar_opciones():
    """
    
    """
    pass


def preguntar_casilla(jugador) -> tuple:
    """
    
    """
    validar_posicion = False
    while not validar_posicion:
        posicion = input(f"JUGADOR {jugador} ¿Dónde quieres colocar tu ficha? (EJ: '1 1') >> ")
        if len(posicion) != 3:
            print("*ERROR* Debes seleccionar tu posición con el formato 'N N.")
        elif posicion[1] != " ":
            print("*ERROR* Debe tener un espacio entre los dos números.")
        else:
            x, y = posicion.split(" ")
            try:
                x = int(posicion[0])
                y = int(posicion[2])
                if x == 0 or y == 0:
                    raise Exception("*ERROR* Los números no pueden ser 0.")
                validar_posicion = True
            except ValueError:
                print("*ERROR* Debes introducir dos números.")
            except Exception as e :
                print(e)

    return y-1, x-1, jugador


def turno_jugador(jugador):
    """
    
    """
    pass


def mostrar_info_ronda():
    """
    
    """
    pass


def condicion_ganador():
    """
    
    """
    pass


def comenzar_partida():
    """
    
    """
    tablero = crear_tablero(BOARD_SIZE["filas"],BOARD_SIZE["columnas"])

    print(mostrar_menu())

    pausa()

    limpiar_terminal()

    salir = False
    while not salir:
        print(mostrar_tablero(tablero))
        x, y, jugador = preguntar_casilla(1)
        actualizar_tablero(tablero, x, y, jugador)
        pausa()
        limpiar_terminal()
        print(mostrar_tablero(tablero))
        x, y, jugador = preguntar_casilla(2)
        actualizar_tablero(tablero, x, y, jugador)
        pausa()
        limpiar_terminal()


def main():
    limpiar_terminal()

    comenzar_partida()


if __name__ == "__main__":
    main()