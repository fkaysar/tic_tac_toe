# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# def: Player 1 chooses a symbol
def choose_symb_1():
    while True:
        symb = input('Player 1, please choose a symbol: ')
        try:
            int(symb)
            print('Please enter a letter...')
        except:
            print(f'Player 1 chose the symbol: {symb}')
            break
    return symb

# def: Player 2 chooses a symbol
def choose_symb_2():
    while True:
        symb = input('Player 2, please choose a symbol: ')
        if symb == symb_1:
            print('Player 2 has chosen this symbol. Please choose another one')
        try:
            int(symb)
            print('Please enter a letter...')
        except:
            print(f'Player 2 chose the symbol: {symb}')
            break
    return symb

# write symbols on the board
def take_turn(pb_l):
    while True:
        try:
            choice = int(input("Type your choice: "))
            if 0 < choice < 10 and choice in pb_l:
                break
        except:
            print("Choose a number between 1 and 9 that is still available")

    for n in range(len(pb_l)):
        if pb_l[n] == choice:
            pb_l[n] = symb
    return pb_l

# Check for win
def check_for_win(pb_l, turn_count, game_ended):
    for i in pb_l:
        if all([pb_l[0] == symbols[0], pb_l[1] == symbols[0], pb_l[2] == symbols[0]]): # top row horizontal Player 1
            print('Player 1 has won! Check top row')
            game_ended = True
            break
        elif all([pb_l[0] == symbols[1], pb_l[1] == symbols[1], pb_l[2] == symbols[1]]): # top row horizontal Player 2
            print('Player 2 has won! Check top row')
            game_ended = True
            break
        elif all([pb_l[3] == symbols[0], pb_l[4] == symbols[0], pb_l[5] == symbols[0]]): # middle row horizontal Player 1
            print('Player 1 has won! Check middle row')
            game_ended = True
            break
        elif all([pb_l[3] == symbols[1], pb_l[4] == symbols[1], pb_l[5] == symbols[1]]): # middle row horizontal Player 2
            print('Player 2 has won! Check middle row')
            game_ended = True
            break
        elif all([pb_l[6] == symbols[0], pb_l[7] == symbols[0], pb_l[8] == symbols[0]]): # bottom row horizontal Player 1
            print('Player 1 has won! Check bottom row')
            game_ended = True
            break
        elif all([pb_l[6] == symbols[1], pb_l[7] == symbols[1], pb_l[8] == symbols[1]]): # bottom row horizontal Player 2
            print('Player 2 has won! Check bottom row')
            game_ended = True
            break
        elif all([pb_l[0] == symbols[0], pb_l[3] == symbols[0], pb_l[6] == symbols[0]]): # left column Player 1
            print('Player 1 has won! Check left column')
            game_ended = True
            break
        elif all([pb_l[0] == symbols[1], pb_l[3] == symbols[1], pb_l[6] == symbols[1]]): # left column Player 2
            print('Player 2 has won! Check left column')
            game_ended = True
            break
        elif all([pb_l[1] == symbols[0], pb_l[4] == symbols[0], pb_l[7] == symbols[0]]): # middle column Player 1
            print('Player 1 has won! Check middle column')
            game_ended = True
            break
        elif all([pb_l[1] == symbols[1], pb_l[4] == symbols[1], pb_l[7] == symbols[1]]): # middle column Player 2
            print('Player 2 has won! Check middle column')
            game_ended = True
            break
        elif all([pb_l[2] == symbols[0], pb_l[5] == symbols[0], pb_l[8] == symbols[0]]): # right column Player 1
            print('Player 1 has won! Check right column')
            game_ended = True
            break
        elif all([pb_l[2] == symbols[1], pb_l[5] == symbols[1], pb_l[8] == symbols[1]]): # right column Player 2
            print('Player 2 has won! Check right column')
            game_ended = True
            break
        elif all([pb_l[0] == symbols[0], pb_l[4] == symbols[0], pb_l[8] == symbols[0]]): # vertical top left to bottom right Player 1
            print('Player 1 has won! Check vertical, top left to bottom right')
            game_ended = True
            break
        elif all([pb_l[0] == symbols[1], pb_l[4] == symbols[1], pb_l[8] == symbols[1]]): # vertical top left to bottom right Player 2
            print('Player 2 has won! Check vertical, top left to bottom right')
            game_ended = True
            break
        elif all([pb_l[2] == symbols[0], pb_l[4] == symbols[0], pb_l[6] == symbols[0]]): # vertical top right to bottom left Player 1
            print('Player 1 has won! Check vertical, vertical top right to bottom left')
            game_ended = True
            break
        elif all([pb_l[2] == symbols[1], pb_l[4] == symbols[1], pb_l[6] == symbols[1]]): # vertical top right to bottom left Player 2
            print('Player 2 has won! Check vertical, vertical top right to bottom left')
            game_ended = True
            break
        elif turn_count == 9:
            print("It's a draw!!")
            game_ended = True
    return game_ended

def update_board(pb_l):
    print(f'{pb_l[0]} {pb_l[1]} {pb_l[2]} \n{pb_l[3]} {pb_l[4]} {pb_l[5]} \n{pb_l[6]} {pb_l[7]} {pb_l[8]} ')
# Welcome message
print('Welcome to a new game of tic tac toe!')
# A playing board is displayed (3x3)
pb = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
pb_l = list(pb.values())
update_board(pb_l)

symb_1 = choose_symb_1()
symb_2 = choose_symb_2()
symb = ''
symbols = [symb_1, symb_2]
turn_count = 1
game_ended = False


# Tic-tac-toe game
if __name__ == "__main__":
    while not game_ended:

        if turn_count % 2 != 0:
            print("it's player 1's turn")
            symb = symb_1
        else:
            print("it's player 2's turn")
            symb = symb_2

        take_turn(pb_l)

        update_board(pb_l)

        game_ended = check_for_win(pb_l, turn_count, game_ended)

        # if game_ended == True:
        #     break

        turn_count += 1