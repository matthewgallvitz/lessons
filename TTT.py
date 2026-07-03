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
    print("top left corner",board[0][0]) 
    print("middle left",board[1][0])
    print("bottem left corner",board[2][0])
# to do:
# check cell that each is equal
# start creating an if statment
# make it so the system checks each number to find if the pieces match in a column
    pass
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
    ["","",""],
    ["","",""],
    ["","",""],
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
    check_winning_column(board)