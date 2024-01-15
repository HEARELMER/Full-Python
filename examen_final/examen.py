# Ejercicio 1 

# Crea un programa que sea capaz de generar e imprimir todas las 
# permutaciones disponibles formadas por las letras de una palabra.
#  - Las palabras generadas no tienen por qué existir.
#  - Deben usarse todas las letras en cada permutación.
#  - Ejemplo: sol, slo, ols, osl, los, lso 
#             sol slo   osl ols lso los

def generate_permutations(word):
    if len(word) <= 1:
        return [word]

    permutations = []
    for i, char in enumerate(word):
        resto_palabra = word[:i] + word[i + 1:]
        subpermutation = generate_permutations(resto_palabra)
        permutations.extend([char + p for p in subpermutation])

    return permutations

def print_permutations(word_user):
    try:
        for permutation in generate_permutations(word_user):
            print(permutation)
    except Exception as e:
        print(f"Error: {e}")

try:
    palabra_input = input('Ingresa una palabra: ')
    print_permutations(palabra_input)

except Exception as e:
    print(f"Error: {e}")



# Ejericio 2

# Crea un programa capaz de gestionar una pieza de Tetris.
#   - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
#   - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
#    
#     🔳🔳🔳🔳
#   - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
#     🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#     🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
#     recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
#   - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
#   - Debes tener en cuenta los límites de la pantalla de juego.


class TetrisBoard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [['🔲' for _ in range(columns)] for _ in range(rows)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()


class TetrisPiece:
    def __init__(self):
        self.shape = [['🔳', '🔳', '🔳', '🔳']]
        self.position = [0, 0]

    def show_on_board(self, board):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                board[self.position[0] + i][self.position[1] + j] = cell

    def move_right(self):
        self.position[1] = min(self.position[1] + 1, 10 - len(self.shape[0]))

    def move_left(self):
        self.position[1] = max(self.position[1] - 1, 0)

    def move_down(self):
        self.position[0] = min(self.position[0] + 1, 10 - len(self.shape))

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))


def play_tetris():
    try:
        board = TetrisBoard(10, 10)
        piece = TetrisPiece()

        piece.show_on_board(board.board)

        while True:
            board.print_board()
            action = input("Movimiento (derecha:'d', izquierda:'i', abajo:'a', rotar:'r', salir: 's'): ").lower()

            if action == 's':
                break

            if action == 'd':
                piece.move_right()
            elif action == 'i':
                piece.move_left()
            elif action == 'a':
                piece.move_down()
            elif action == 'r':
                piece.rotate()
            else:
                print('Opción no válida. Vuelve a intentar. 😒')

            # limpiar el tablero antes de mostrar la pieza en su nueva posición
            board = TetrisBoard(10, 10)
            piece.show_on_board(board.board)

    
    except Exception as e:
        print(f"Error: {e}")


play_tetris()
