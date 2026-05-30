board = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","I"],
    ]

turn_1 = True

for i in range (9):
    player_number = None
    if turn_1 is True:
        player_number = 1
    else:
        player_number = 2
    print("player: "+ str(player_number))
    turn_1 = not turn_1
#print(board[2][0])

def get_user_coordinates():
    answer = input("Where would you like to go?")   
    print(answer)
    if int(answer) > 9:
        print("Sorry, but you cannot ask for a number over 9")
    elif int(answer) < 1:
        print("Sorry, but you cannot ask for a number under 1")
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
get_user_coordinates() 