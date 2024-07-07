"""
#Rules
 * Crea el juego conecta cuatro.
 * Game mode:
 * - Tablero de 7x6 (7 en el eje "x" y 6 en el "y").
 * - Fichas Rojas y Amarillas. La primera partida la comienza siempre la Roja
 *   (la segunda la Amarilla, la tercera la Roja...).
 * - No se puede jugar contra la maquina, deben haber 2 jugadores
 * - Al seleccionar la columna se coloca la ficha en la parte inferior.
 * - Guardar el número partidas ganadas de cada equipo mientras la App no se finaliza.
 * - Contador de victorias y derrotas.
⚪🔴🟡
"""
import os

victorias1 = 0
victorias2 = 0
Partida = 1

opciones = [1,2,3,4,5,6,7]

def info(victorias1,victorias2):
    print("".center(30,"-"))
    print(f"JUGADOR 1 \nVictorias: {victorias1}\n")
    print(f"\nJUGADOR 2 \nVictorias: {victorias2}\n")

def Column(icon):
    while True:

        try:
            column = int(input(f"Turno Jugador {icon}. Ingrese una columna [ {",".join(map(str,opciones))} ]=> "))
        except Exception as e:
            print("Ingresar algo valido!" )
            column = Column(icon)
            
        if 1<= column <=7:
            return column
        print("Columna fuera del tablero!")
        os.system("pause")

def turno(encuentro : int, tablero : iter):
    if encuentro % 2 != 0:
        icon = "🔴"
    if encuentro %2 == 0:
        icon = "🟡"
    columna = Column(icon)
    tablero = jugada(icon,tablero,columna-1)
    return tablero





def explorar(row : int, column : int, tablero : iter, icon : str, dir_row : int, dir_column : int):
    if 0<=column+dir_column<=6 and 0<=row+dir_row<=5 and tablero[row+dir_row][column+dir_column] == icon:
        return 1 + explorar(row+dir_row,column+dir_column,tablero,icon,dir_row,dir_column)
    return 0

def diag_positiva(row : int, column : int, tablero : iter, icon : str):
    return abajo_izquierda(row,column,tablero,icon)+arriba_derecha(row,column,tablero,icon)
def diag_negativa(row : int, column : int, tablero : iter, icon : str):
    return arriba_izquierda(row,column,tablero,icon)+abajo_derecha(row,column,tablero,icon)

def arriba_izquierda(row : int, column : int, tablero : iter, icon : str):
    return explorar(row,column,tablero,icon,-1,-1)
def abajo_derecha(row : int, column : int, tablero : iter, icon : str):
    return explorar(row,column,tablero,icon,+1,+1)

def abajo_izquierda(row : int, column : int, tablero : iter, icon : str):
    return explorar(row,column,tablero,icon,+1,-1)

def arriba_derecha(row : int, column : int, tablero : iter, icon : str):
    return explorar(row,column,tablero,icon,-1,+1)



def izquierda(row : int, column : int, tablero : iter, icon : str):
    return explorar(row,column,tablero,icon,0,+1)

def derecha(row : int, column : int, tablero : iter, icon : str):
    return explorar(row,column,tablero,icon,0,-1)



def abajo(row : int, column : int, tablero : iter, icon : str):
    if 0<=row < 5:
        if tablero[row+1][column] == icon:
            return 1 + abajo(row+1,column,tablero,icon,)
    return 0
    
def jugada(icon : str, tablero : iter, columna : int, row = 5):
    global victorias1,victorias2
    if tablero[row][columna] == "⚪":
        tablero[row][columna] = icon
        if row == 0:
            opciones.remove(columna+1)
        Diag_positiva =  diag_positiva(row,columna,tablero,icon)
        Diag_negativa =  diag_negativa(row,columna,tablero,icon)
        Izquierda = izquierda(row,columna,tablero,icon)
        Derecha = derecha(row,columna,tablero,icon)
        Abajo = abajo(row,columna,tablero,icon)
 
    
        horizontal = Izquierda+Derecha

        if horizontal >= 3 or Abajo >=3 or Diag_positiva>=3 or Diag_negativa>=3:
            print(f"Jugador {icon} Gana!")
            if icon == "🔴":
                victorias1 +=1
            if icon == "🟡":
                victorias2 +=1
            for row in tablero:
                print("".join(map(str,row)))
            return False
    elif row != 0:
        if not jugada(icon,tablero,columna,row-1):
            return False
    else:
        print("Columna llena")
        columna = Column(icon)
        if not jugada(icon,tablero,columna,row-1):
            return False
    return tablero

def partida():
    
    global victorias1,victorias2,Partida
    tablero = [list(["⚪"] * 7) for x in range(6)]
    
    print(f"Inicio de partida {Partida}!")
    
    info(victorias1,victorias2)
    
    for encuentro in range(1,100):
        print(f"Encuentro: {encuentro}")
        for row in tablero:
            print("".join(map(str,row)))
        tablero  = turno(encuentro,tablero)
        if not tablero:
            Partida +=1
            os.system("pause")
            os.system("cls")
            break
    partida()
        
        

partida()
