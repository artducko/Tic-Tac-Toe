active_game = True
nums = [0,0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
winCond = []
#game = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
game = ["-" for i in range(9)]
# displays game board
def game_board():
    print( game[0] + "|" + game[1] + '|' + game[2])
    print( game[3] + "|" + game[4] + '|' + game[5])
    print( game[6] + "|" + game[7] + '|' + game[8])


def user():
    position = input("Make a move: ")
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Make a move: ")

        #converts user to int from str
        position = int(position) - 1

        #checks if space is available
        if position + 1 not in nums:
            print("Try Again")
        else:
            nums.remove(position + 1)
        # prints nums to see if available comps if working
        #print(nums)
        if game[position] == '-':
            game[position] = 'X'
            valid = True


def comp_choice():
    import random
    # checks for tie
    if game.count('-') == 0:
        active_game = False
        pass
    else:
        # make random move based on nums list
        compy = random.choice(nums[2:-1])
        # choice from nums list
        nums.remove(compy)

        # prints nums to see if available comp move is working
        #print("removed: ", compy)
        #print(nums)

        # places comp choice on board
        game[compy - 1] = "O"

    # shows number of available spots on the board
    #print("spaces left: ", game.count('-'))


def end_game():
    # setting up rows, col and diags to check for winner
    global active_game
    rowA = [game[0], game[1], game[2]]
    rowB = [game[3], game[4], game[5]]
    rowC = [game[6], game[7], game[8]]
    colA = [game[0], game[3], game[6]]
    colB = [game[1], game[4], game[7]]
    colC = [game[2], game[5], game[8]]
    diagUp = [game[0], game[4], game[8]]
    diagDown = [game[2], game[4], game[6]]

    # setting up wins via count of "X" per row, col and diag
    xWin = [rowA.count("X"), rowB.count("X"), rowC.count("X"), colA.count("X"), colB.count("X"), colC.count("X"),
            diagUp.count("X"), diagDown.count("X")]
    ## setting up wins via count of "O" per row, col and diag
    oWin = [rowA.count("O"), rowB.count("O"), rowC.count("O"), colA.count("O"), colB.count("O"), colC.count("O"),
            diagUp.count("O"), diagDown.count("O")]

    validO = False
    validX = False

    # checks if "O" is a winner
    for item in oWin:
        if item == 3:
            validO = True
        else:
            # checks if "X" is a winner
            for item in xWin:
                if item == 3:
                    validX = True
    # prints "X" is winner and ends game
    if validX is True:
        game_board()
        print("X WINS")
        active_game = False
    # prints "O" is winner and ends game
    if validO is True:
        game_board()
        print("O WINS")
        active_game = False

    # prints "TIE" and ends game
    if validX == False and  validO == False:
        if game.count('-') == 0:
            game_board()
            print("TIE")
            active_game = False

def game_play():
    global active_game
    while active_game:
        game_board()

        user()

        comp_choice()

        end_game()

game_play()