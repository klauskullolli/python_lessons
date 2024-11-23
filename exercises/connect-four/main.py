File_name = "moves.txt"
ROW_NUM = 6
COLL_NUM = 7


# Prepare empty grid
def prepare_empty():
    slit = [["-" for _ in range(COLL_NUM)] for _ in range(ROW_NUM)]
    return slit


def print_slit(slit):
    # for row in slit:    
    #     print("".join(row))  
    # or 
    # for i in range(ROW_NUM):    
    #     for j in range(COLL_NUM):    
    #         print(slit[i][j], end="")    
    #     print("")
    # or    
    for row in slit:
        print(*row, sep="")


# Detect the next available row in the given column
def detect_spot(COLL, slit):
    x = int(COLL)  # Convert column input to integer
    # Check from the bottom row upwards
    for i in range(ROW_NUM - 1, -1, -1):
        if slit[i][x] == "-":  # Find the first empty slot
            return i
    return None  # If the column is full


def check_winner(slit):
    # Check horizontally
    for i in range(ROW_NUM):
        for j in range(COLL_NUM - 3):
            if (
                slit[i][j] == "O"
                and slit[i][j + 1] == "O"
                and slit[i][j + 2] == "O"
                and slit[i][j + 3] == "O"
            ):
                return "G1"
            elif (
                slit[i][j] == "X"
                and slit[i][j + 1] == "X"
                and slit[i][j + 2] == "X"
                and slit[i][j + 3] == "X"
            ):
                return "G2"
    for j in range(COLL_NUM):
        for i in range(ROW_NUM - 3):
            if (
                slit[i][j] == "O"
                and slit[i + 1][j] == "O"
                and slit[i + 2][j] == "O"
                and slit[i + 3][j] == "O"
            ):
                return "G1"
            elif (
                slit[i][j] == "X"
                and slit[i + 1][j] == "X"
                and slit[i + 2][j] == "X"
                and slit[i + 3][j] == "X"
            ):
                return "G2"
    for i in range(ROW_NUM - 3):
        for j in range(COLL_NUM - 3):
            if (
                slit[i][j] == "O"
                and slit[i + 1][j + 1] == "O"
                and slit[i + 2][j + 2] == "O"
                and slit[i + 3][j + 3] == "O"
            ):
                return "G1"
            elif (
                slit[i][j] == "X"
                and slit[i + 1][j + 1] == "X"
                and slit[i + 2][j + 2] == "X"
                and slit[i + 3][j + 3] == "X"
            ):
                return "G2"
    for i in range(ROW_NUM-1, 2, -1): 
        for j in range(COLL_NUM - 3):    
            if (
                slit[i][j] == "O"
                and slit[i - 1][j + 1] == "O"
                and slit[i - 2][j + 2] == "O"
                and slit[i - 3][j + 3] == "O"
            ):
                return "G1"
            elif (
                slit[i][j] == "X"
                and slit[i - 1][j + 1] == "X"
                and slit[i - 2][j + 2] == "X"
                and slit[i - 3][j + 3] == "X"
            ):
                return "G2"

    return None


# Process moves from file
def move(File_name, slit):
    try:
        with open(File_name, "r") as f:
            for line in f:
                line_strip = line.strip()
                PLAYER, COLL = line_strip.split(" ")
                COLL = int(COLL)  # Convert column input to integer
                # Find the row to place the piece
                row = detect_spot(COLL, slit)
                if row is not None:
                    # Place the piece based on the player
                    if PLAYER == "G1":
                        slit[row][COLL] = "O"
                    elif PLAYER == "G2":
                        slit[row][COLL] = "X"

                winner = check_winner(slit)
                if winner == "G1" or winner == "G2":
                    print(f"Winner is {winner} ")
                    print_slit(slit)
                    break
                print_slit(slit)
                print("")
    except OSError as e:
        print("error")


def main():
    slit = prepare_empty()
    move(File_name, slit)


if __name__ == "__main__":
    main()
