"""+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   5   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+"""


#OJOOOOOOOO
#implementar el movimiento de la cpu con el diccionario casillas

from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
        print(f"""+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+""")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    
    incorrect = True
    while incorrect:
        while True:
            try:
                move = int(input("Ingresa tu movimiento: "))
                if move > 0 and move < 10:
                    break
            except:
                print("Entrada errónea.")
    
        libres = make_list_of_free_fields(board)
        if casillas[move] in libres:
            board[casillas[move][0]][casillas[move][1]] = "O"
            incorrect = False
        else:
            print("Casilla ocupada")
         
        

   
def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    
    signs = ["X","O"]
    libres = []
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] not in signs:
                libres.append((fila,columna))
    
    return libres
    print(f"Casillas libres: {libres}")

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

    #0-> Draw
    #1-> CPU Wins
    #2 -> User Wins
    
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[0][0] == sign[0]:
            return 1
        else: return 2

    for fila in board:
        if fila[0] == fila[1] == fila[2]:
            if fila[0] == sign[0]:
                return 1
            else: return 2
        
    for columna in range(3):
        if board[0][columna] == board[1][columna] == board[2][columna]:
                if board[0][columna] == sign[0]:
                    return 1
                else: return 2
    return 0
    
#def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    #libres = make_list_of_free_fields(board)
#    libres = make_list_of_free_fields(board)
#    move = randrange(0,len(libres))
#    board[libres[move][0]][libres[move][1]]= "X"
    
def draw_move(board):
    global cont_cpu
    if cont_cpu == 0:
        board[1][1] = "X"
    else:
        libres = make_list_of_free_fields(board)
        jugada_incorrecta = True
        while jugada_incorrecta:
            move = randrange(1,10)
            if casillas[move] in libres:
                board[casillas[move][0]][casillas[move][1]] = "X"
                jugada_incorrecta = False
    cont_cpu+=1   


again = "y"

while again == "y":
    board = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    casillas = {
            1: (0,0),
            2: (0,1),
            3: (0,2),
            4: (1,0),
            5: (1,1),
            6: (1,2),
            7: (2,0),
            8: (2,1),
            9: (2,2),
    }  
    cont_cpu = 0

    sign = ["X","O"]
  
    print(board)
    display_board(board)

    print(victory_for(board,sign))
    while True:
        #CPU´S TURN
        if len(make_list_of_free_fields(board)) > 0:
            draw_move(board)
            display_board(board)
            if victory_for(board,sign):
                print("CPU WINS!!!!")
                break
            
        #USER´S TURN
        if len(make_list_of_free_fields(board)) > 0:
            enter_move(board)
            display_board(board)
            
            if victory_for(board,sign):
                print("USER WINS!!!!")
                break
        if len(make_list_of_free_fields(board)) == 0 and victory_for(board,sign) == 0:
            print("Draw :(")
            break
        
    print (victory_for(board, sign))

    print("===============================================")
    again = input("Desea jugar otra vez? Sí-y No-n: ")
    
    
    
#make_list_of_free_fields(board)
#cpu move
#for i in range(11):
#    draw_move(board)
#    display_board(board)

#enter_move(board)
#draw_move(board)
#display_board(board)



