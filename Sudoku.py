""""
Programa que ingresa desde el teclado las casillas del Sudoku, fila a fila, y determina si el
tablero es correcto y cumple con las condiciones


    Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
    Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
    Cada uno de los 9 subcuadros de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.

"""

def comprobar_filas(tablero):
    digitos = []
    #creando el arreglo que contiene numeros 0,1,2,3,4,5,6,7,8,9
    for ch in range(1,10):
        digitos.append(str(ch))
        print (digitos)

    #comprobando las filas
    #for fila in tablero:
    #    for char in digitos:
    #        if char not in fila:
    #            return False
    #comprabando las columnas
    for col in range(9):
        #for fila in range(9):
            #if tablero[fila][col] not in digitos:
             #   return False 
        col_aux = [fila[col] for fila in tablero]
        for char in digitos:
            if char not in col_aux:
                return False
    return True

  #  pos_columnas = pos_filas = 0
   # tablero_temporal = []
    #while pos_columnas <= 8 and pos_filas <= 8:
     #   for filas in range(3):
      #      for col in range(3):
       #         tablero_temporal.append(tablero[pos_filas:filas][pos_columnas:col])

    #next_col =  pos_columnas + 2 if pos_columnas == 0 else pos_columnas +3
    #next_fila = pos_filas + 2 if pos_filas == 0 else pos_filas + 3
    #next_fila = pos_filas +3 

    #next_col = pos_columnas +3
    
            
tablero = []

tablero = [
    ["0","1","2","3","4","5","6","7","8","9"],
    ["9","1","2","3","4","5","6","7","8","0"],
    ["1","0","2","3","4","5","6","7","8","9"],
    ["2","1","0","3","4","5","6","7","8","9"],
    ["3","1","2","0","4","5","6","7","8","9"],
    ["4","1","2","3","0","5","6","7","8","9"],
    ["5","1","2","3","4","0","6","7","8","9"],
    ["6","1","2","3","4","5","0","7","8","9"],
    ["8","1","2","3","4","5","6","7","0","9"]
]

tablero_2 =[    
    ["9","2","5","7","4","3","8","6","1"],
    ["4","3","1","8","6","5","9","2","7"],
    ["8","7","6","1","9","2","5","4","3"],
    ["3","8","7","4","5","9","2","1","6"],
    ["6","1","2","3","8","7","4","9","5"],
    ["5","4","9","2","1","6","7","3","8"],
    ["7","6","3","5","2","4","1","8","9"],
    ["9","2","8","6","7","1","3","5","4"],
    ["1","5","4","9","3","8","6","7","2"] 
]

tablero_3 = [
    ["2","9","5","7","4","3","8","6","1"],
    ["4","3","1","8","6","5","9","2","7"],
    ["8","7","6","1","9","2","5","4","3"],
    ["3","8","7","4","5","9","2","1","6"],
    ["6","1","2","3","8","7","4","9","5"],
    ["5","4","9","2","1","6","7","3","8"],
    ["7","6","3","5","2","4","1","8","9"],
    ["9","2","8","6","7","1","3","5","4"],
    ["1","5","4","9","3","8","6","7","2"] 
]



print("Ingrese el valor de las filas 1 a 1: ")
#for n in range(9):
#    fila = input(f"Ingrese el valor de la fila {n}: ")
#   tablero.append(list(fila))

continuar = input("break")
if comprobar_filas(tablero_3):
    print("si")
else: print("no")