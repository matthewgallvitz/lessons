def get_user_coordinates():
    map = {
        1: [0,0],
        2: [0,1],
        3: [0,2],
        4: [1,0],
        5: [1,1],
        6: [1,2],
        7: [2,0],
        8: [2,1],
        9: [2,2],
    }
    is_valid_number = False
    while is_valid_number == False:
        answer = input("Where would you like to go?")
        print(map[int(answer)])
        if int(answer) > 9:
            print("Sorry, but you cannot ask for a number over 9")
        elif int(answer) < 1:
            print("Sorry, but you cannot ask for a number under 1")
        user_coordinates = map[int(answer)]
        row = user_coordinates[0]
        column = user_coordinates[1]
        if board[row][column] == "" :
            is_valid_number = True
        else:
            print("There is already a piece here")
            print("Please choose again")
    return map[int(answer)]

def check_winning_column(board):
    for column in range(3):
        Top_Piece = board[0][column]
        Middle_Piece = board[1][column]
        Bottom_Piece = board[2][column]
        if Top_Piece == Middle_Piece and Middle_Piece == Bottom_Piece:
            return True
        return False

def check_row_win(board):
    for row in board:
        left_piece = row[0]
        middle_piece = row[1]
        right_piece = row[2]
        if left_piece == middle_piece and left_piece == right_piece:
            return True 
    return False

def check_diagonal_win(board):
    top_left_corner = board[0][0]
    top_right_corner = board [0][3]
    middle_piece = board[1][1]
    bottom_left_corner = board[3][0]
    bottom_right_corner = board[3][3]
    if ((top_left_corner == middle_piece and bottom_right_corner == top_left_corner) or
    (top_right_corner == middle_piece and top_right_corner == bottom_left_corner)):
        return True
    return False

def display_board():
    for row in board:
        print(row)
def player_placement():
    user_coordinates = get_user_coordinates()
    row = user_coordinates[0]
    column = user_coordinates[1]
    if is_player_1_turn is True:
        board[row][column] = "x"
    else:
        board[row][column] = "o"
board = [
    ["","x","x"],
    ["","x",""],
    ["","x","x"],
]
display_board()

is_player_1_turn = True
for i in range (9):
    player_number = None
    if is_player_1_turn is True:
        player_number = 1
    else:
        player_number = 2
    print("player: "+ str(player_number))
    player_placement()
    display_board()
    is_player_1_turn = not is_player_1_turn
    print()
    game_over = check_winning_column(board) or check_row_win(board) or check_diagonal_win(board)
    if game_over:
        print("game over")
        exit()