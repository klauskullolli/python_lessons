
ROWS = 6
COLUMNS = 7
WIN_CONDITION = 4
MOVES_FILE = "game_moves.txt"

BOARD = [["-" for _ in range(COLUMNS)] for _ in range(ROWS)]



def return_bottom_row(column):
    row  = ROWS - 1
    while row >= 0:
        if BOARD[row][column] == "-":
            return row
        row -= 1
    return -1



def read_moves(file_path):

    pass

def check_win(board):
    pass

def print_board():
    for row in BOARD:
        print(*row)

def add_move():
    pass


if __name__ == "__main__":
    print_board()
    pass