positions = [1,2,3,4,5,6,7,8,9]
n = len(positions)

def printGrid(positions):
    for i in range(0,n):
        if (i+1) % 3 == 0:
            print(positions[i], end='\n')
        else:
            print(positions[i] , end=' | ')

def switchPositions(positions, value, symbol):
    newGrid = positions
    for j in range(0,n):
        if newGrid[j] == value:
            newGrid[j] = symbol
            return newGrid

def promptUser(symbol):
    user_input = int(input('Where do you want to place ' + symbol + '? : '))
    return user_input

def checkRows(positions):
    for i in range(0, n):
        # if we are at position 3 6 or 9
        if (i+1) % 3 == 0:
            if positions[i] == positions[i-1] and positions[i-1] == positions[i-2]:
                printGrid(positions)
                print(positions[i], 'won.')
                return 0
    return 1
        
def checkColumns(positions):
    for i in range(0, n):
        # if we are at positions 1 2 or 3
        if i == 0 or i == 1 or i == 2:
            if positions[i] == positions[i+3] and positions[i+3] == positions[i+6]:
                printGrid(positions)
                print(positions[i], 'won.')
                return 0
    return 1

def checkDiagonales(positions):
    # Check diagonales
    if positions[0] == positions[4] and positions[4] == positions[8]:
        printGrid(positions)
        print(positions[0], 'won.')
        return 0
    elif positions[2] == positions[4] and positions[4] == positions[6]:
        printGrid(positions)
        print(positions[2], 'won.')
        return 0
    else:
        return 1

def checkTie(positions):
    nb_symbol = 0
    for i in range(0, n):
        if type(positions[i]) != int:
            nb_symbol += 1
    if nb_symbol == n:
        printGrid(positions)
        print('Tie!')
        return 0
    else: 
        printGrid(positions)
        return 1
        

# Initial Grid
printGrid(positions)
nb_turn = 0


# Repeat this until all the positions are taken (recursive)
def play(positions, nb_turn):
    if nb_turn >= n:
        return
    else:
        # Prompt user_1 to get position of X
        user_1 = promptUser('X')
        # if position is already taken
        if user_1 not in positions:
            # reprompt user_1
            user_1 = promptUser('X')
        # else if position isn't taken yet
        else:
            # Switch position of symbol
            new_positions = switchPositions(positions, user_1, 'X')
            nb_turn += 1
            # Check Result
            if checkRows(new_positions) == 1 and checkColumns(new_positions) == 1 and checkDiagonales(new_positions) == 1 and checkTie(new_positions) == 1:
                # Prompt user_2 to get position of O
                user_2 = promptUser('O')
                # if position is already taken
                if user_2 not in new_positions:
                    # reprompt user_2
                    user_2 = promptUser('O')
                # else if position isn't taken yet
                else:
                    # Switch position of symbol
                    new_positions_2 = switchPositions(new_positions, user_2, 'O')
                    nb_turn += 1
                    # Check Result
                    if checkRows(new_positions_2) == 1 and checkColumns(new_positions_2) == 1 and checkDiagonales(new_positions_2) == 1 and checkTie(new_positions_2) == 1:
                        # Repeat all recursive (until all positions are filled)
                        play(new_positions_2, nb_turn)
                        

play(positions, nb_turn)