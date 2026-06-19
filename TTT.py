def get_user_coordinates():
    is_valid_number = False
    while is_valid_number == False:
        answer = input("Where would you like to go?")
        if int(answer) > 9:
            print("Sorry, but you cannot ask for a number over 9")
        elif int(answer) < 1:
            print("Sorry, but you cannot ask for a number under 1")
        else:
            is_valid_number = True
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
    return map[int(answer)]
def display_board():
    for row in board:
        print(row)
def player_placement():
    user_coordinates = get_user_coordinates()
    row = user_coordinates[0]
    column = user_coordinates[1]
    board[row][column] = "o"
board = [
    ["","",""],
    ["","",""],
    ["x","",""],
    ]
display_board()
player_placement()

is_player_1_turn = True
for i in range (9):
    player_number = None
    if is_player_1_turn is True:
        player_number = 1
    else:
        player_number = 2
    print("player: "+ str(player_number))
    is_player_1_turn = not is_player_1_turn
display_board()
