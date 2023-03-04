# --------------------------------
# Tic Tac Toe game
# 
# Functions: whos_turn(), check_turn_ended(), game_ended()
#
# define dict board = {1 : '1', 2 : '2',...} assign new values to keys --> {1 : 'x',....}
# 2 players, 1 playing board
# A playing board is displayed (3x3) 
# --- NO FUNCTION NEEDED, AS THIS IS ONLY CALLED ONCE ---
pb = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
pb_l = list(pb.values())
print(f'{pb_l[0]} {pb_l[1]} {pb_l[2]} \n{pb_l[3]} {pb_l[4]} {pb_l[5]} \n{pb_l[6]} {pb_l[7]} {pb_l[8]} ')

# Player 1 chooses a symbol (i.e. x & o)
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

# Player 2 chooses a symbol
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

symb_1 = choose_symb_1()
symb_2 = choose_symb_2()
symb = ''
symbols = [symb_1, symb_2]
turn_count = 1
# WHILE game_ended == false:

    # if turn_count % 2 != 0:
    #     print("it's player 1's turn")
    #     symb = symb_1
    #  else:
    #     print("it's player 2's turn")
    #     symb = symb_2

    # WHILE player_turn_ended == false:
        # Player starts putting their symbol on the board (input('Player input': Replace int with player symbol))
        # if input is not an integer or if integer is not available or if integer out of range
            # print("it's still <players> turn")
        # else:
            # player_turn_ended == true

    # After each turn, check if 3 of the same symbol are in a straight line (8 different ways) or if 9 turns are reached
        # if game_ended = true:
            # print(game is ended)
            # Show new playing board. Call playing board function (updated)
            # break

    # Show new playing board. Call playing board function (updated)

    # turn_count += 1