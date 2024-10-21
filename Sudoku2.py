""""
Programa que ingresa desde el teclado las casillas del Sudoku, fila a fila, y determina si el
tablero es correcto y cumple con las condiciones


    Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
    Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
    Cada uno de los 9 subcuadros de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.

"""

def comprobar_filas(tablero):
    """"
    Función que comprueba que se cumpla la condición de que todas las filas
    del tablero contengan todos los números del 1 al 9

    Argumentos: tablero[][]:str

    Devuelve: True or False
    """
    #comprobando las filas
    for fila in tablero:
        for char in digitos:
            if char not in fila:
                return False
    return True

    

    
    #pos_filas = pos_columnas = 0
    #for filas in range(3):
    #    for columnas in range(3):
    #        tablero_aux = [[tablero[fila][columna] for columna in range(pos_columnas,pos_columnas+3)] for fila in range(pos_filas,pos_filas+3)]
    #        pos_columnas+=3
    #        tablero_aux = []
    #    pos_filas+=3
    #    pos_columnas = 0
    #print(tablero_aux)

    

def comprobar_columnas(tablero):
    """"
    Función que comprueba que se cumpla la condición de que todas las columnas
    del tablero contengan todos los números del 1 al 9

    Argumentos: tablero[][]:str

    Devuelve: True or False
    """
    #comprabando las columnas
    for col in range(9):
        col_aux = [fila[col] for fila in tablero]
        for char in digitos:
            if char not in col_aux:
                return False
    return True




def comprobar_submatriz(tablero):
    """"
    Función que comprueba que se cumpla la condición de que todas las sub-matrices
    de 3x3 del tablero contengan todos los números del 1 al 9

    Argumentos: tablero[][]:str

    Devuelve: True or False
    """
    
    #Comprobando los elementos de las submatrices de 3x3 elementos
    pos_filas = pos_columnas = 0
    for filas in range(3):
        for columnas in range(3):
            #Extrayendo una sub-matriz de 3x3 y almacenandola en una lista plana
            tablero_aux = [tablero[fila][columna] for fila in range(pos_filas,pos_filas+3) for columna in range(pos_columnas,pos_columnas+3) ]
            #comprobando que los caracteres de la lista esten dentro de la lista de digitos
            for char in digitos:
                if char not in tablero_aux:
                    return False
            pos_columnas+=3
            tablero_aux = []
        pos_filas+=3
        pos_columnas = 0
    
    return True 



digitos = []
#creando el arreglo que contiene numeros 0,1,2,3,4,5,6,7,8,9
for ch in range(1,10):
    digitos.append(str(ch))
    print (digitos)

#   Tableros de prueba
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

tablero_4 = [
    ["2","9","5","7","4","3","8","6","1"],
    ["4","3","1","8","6","5","9","2","7"],
    ["8","7","6","1","9","2","5","4","3"],
    ["3","8","7","4","5","9","2","1","6"],
    ["6","1","2","3","7","7","4","9","5"],
    ["5","4","9","2","1","6","7","3","8"],
    ["7","6","3","5","2","4","1","8","9"],
    ["9","1","8","6","7","1","3","6","4"],
    ["1","5","4","9","3","8","6","7","2"] 
]



print("Ingrese el valor de las filas 1 a 1: ")
for n in range(9):
    fila = input(f"Ingrese el valor de la fila {n}: ")
    tablero.append(list(fila))


if comprobar_filas(tablero_3) and comprobar_columnas(tablero_3) and comprobar_submatriz(tablero_3):
    print("El tablero es válido")
else: print("El tablero no es válido")

continuar = input("break")