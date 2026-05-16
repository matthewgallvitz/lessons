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

answer = input("Where would you like to go?")
print(answer)