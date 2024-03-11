# Program : Tic Tac Toe game, the first who complete three numbers up to 15 in one line wins
#           and I solved game 2
# Author  : Mohamed Ahmed Kotb
# ID      : 20230315
# Version : 4.0
# Date    : 2/3/2024


# Define a function to print the Tic Tac Toe board
def print_board(places):
    # show the board layout using string formatting
    board = (f"|{places[1]}|{places[2]}|{places[3]}|\n"
             f"|{places[4]}|{places[5]}|{places[6]}|\n"
             f"|{places[7]}|{places[8]}|{places[9]}|")
    print(board)


# Define a function to determine the player's turn based on the turn count
def player_turn(turn):
    # If the turn count is even, return 'odd', otherwise return 'even'
    if turn % 2 == 0:
        return 'odd'
    else:
        return 'even'


# Define a function to check if a player has won the game
def check_win(places):
    # Checking if a line contains 3 numbers up to 15

    # Horizontally
    if places[1] + places[2] + places[3] == 15:
        if places[1] != places[2] != places[3] != 0:
            return True

    elif places[4] + places[5] + places[6] == 15:
        if places[4] != places[5] != places[6] != 0:
            return True

    elif places[7] + places[8] + places[9] == 15:
        if places[7] != places[8] != places[9] != 0:
            return True

    # Vertically
    elif places[1] + places[4] + places[7] == 15:
        if places[1] != places[4] != places[7] != 0:
            return True

    elif places[2] + places[5] + places[8] == 15:
        if places[2] != places[5] != [8] != 0:
            return True

    elif places[3] + places[6] + places[9] == 15:
        if places[3] != places[6] != places[9] != 0:
            return True

    # Diagonally
    elif places[1] + places[5] + places[9] == 15:
        if places[1] != places[5] != places[9] != 0:
            return True

    elif places[3] + places[5] + places[7] == 15:
        if places[3] != places[5] != places[7] != 0:
            return True

    else:
        return False


# Print a welcome message and take the names of the players
print("Welcome to Tic Tac Toe...")
print("The first who complete three numbers up to 15 in one line wins")
ply1 = input("Enter the name of player 1 who choose odd: ")
ply2 = input("Enter the name of player 2 who choose even: ")

# Initialize the Tic Tac Toe board and other variables
Places = [0, 0, 0,
          0, 0, 0,
          0, 0, 0, 0]
Turn = 0  # to move to the next player
draw_cond = 0  # to check if the game will end in draw
flag = 'true'
turns_played = []  # to prevent from repeating the same input
places_played = []

# Main loop
while True:
    # Print the current state of the board
    print_board(Places)

    if player_turn(Turn) == 'odd':
        # Determine the player 1 turn and wait for their choice
        print(ply1, "turn:")
        choice = input("Choose an odd number [1,3,5,7,9]: ")
        # Checking if the input is valid
        if not choice.isdigit() or int(choice) not in [1, 3, 5, 7, 9]:
            print("Please enter odd numbers from 1 to 9 to play !!!\n")
            continue

    if player_turn(Turn) == 'even':
        # Determine the player 2 turn and wait for their choice
        print(ply2, "turn:")
        choice = input("Choose an even number [2,4,6,8]: ")
        # Checking if the input is valid

        if not choice.isdigit() or int(choice) not in [2, 4, 6, 8]:
            print("Please enter even numbers from 1 to 9 to play !!!\n")
            continue

    # Check if the chosen place has already been played
    if int(choice) in turns_played:
        print("Repeated input....\n"
              "Please try again")
        continue
    while flag:
        i = input("Enter the place you want to play: ")
        # Checking if the input is valid

        if not i.isdigit() or int(i) not in range(0, 10):
            print("Please enter a valid place !!!\n")
            continue

        i = int(i)
        # Check if the chosen place has already been played
        if i in places_played:
            print("Repeated input....\n"
                  "Please try again")
            continue

        flag = 'false'
        break
    # Add the chosen place and turn to the list of played turns
    places_played.append(i)
    turns_played.append(int(choice))

    # Update the board with the current player's symbol
    Places[i] = int(choice)

    # Check if the current player has won the game
    if check_win(Places):
        # Print the final state of the board
        print_board(Places)
        # Determine the winner
        if player_turn(Turn) == 'odd':
            print(ply1, "is the winner")
        else:
            print(ply2, "is the winner")
        break

    # Increment the turn count and the draw condition
    Turn += 1
    draw_cond += 1
    # Check if the game has ended in a draw
    if draw_cond > 8:
        print_board(Places)
        print("Game is ended in draw.....")
        break
