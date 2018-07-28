from random import randint
#STEP 1: Set up game board
board = []

for x in range(5): #how big your board is - 5x5
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row) #turns 'O' into O

print_board(board)

#STEP 2: Create random ship location
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board) #puts ship on random row
ship_col = random_col(board) #puts ship on random col
#check answers
print "Row Answer: " + str(ship_row)
print "Col Answer: " + str(ship_col)

# STEP 3: Create Guesses! Everything from here on should go in your for loop! Be sure to indent four spaces!
for turn in range(4): #creates max 4 turns 
  guess_row = int(raw_input("Guess Row (0 to 4): "))
  guess_col = int(raw_input("Guess Col (0 to 4): "))
  
#STEP 4: Create outcomes for guesses
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    #break #game ends.. rematch?
  else: #if player picks loser
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): #if player guesses off board
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already." #if player guesses the same one twice
    else: #if player misses
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"#turns OintoX
    if turn == 3: #if player runs out of guesses
      print "Game Over"

  #re-match?
  if (guess_row == ship_row and guess_col == ship_col) or turn == 3: #if win or lose satisfied, ask for rematch
    reMatch = raw_input("re-match? Type Y/N: ")
    if (reMatch == "Y" or reMatch == "y"): #if reMatch = Y, restart game
      turn = 0
      ship_row = random_row(board) #resets ship
      ship_col = random_col(board) #resets ship#check
      print "Row Answer: " + str(ship_row)
      print "Col Answer: " + str(ship_col)
    elif (reMatch == "N" or reMatch == "n"): #if reMatch = N, end game
      print "Game Over"
      break
    
  print "Turn", turn + 1 # Print (turn + 1) here!
  print_board(board)
  
