import random
grid = [] #actual list

def create_grid () :
  for y in range (4) :
    row = [] # temporary list
    # creating columns
    for x in range (4):
      row.append ("-")
    grid.append (row)
  return grid

### MAIN PART
grid = create_grid ()  # calling function
print ("Welcome to the Treasure Hunt Game!")
# place treasure
actual_row = random.randint (0,3)
actual_col = random.randint (0,3)
attempts = 0
while True : 
  for row in grid :
    print (" ".join(row))
  # get the user input 
  try :
    guess_row = int (input ("Guess row number (0-3) :"))
    guess_col = int (input ("Guess column number (0-3) :"))
  except ValueError :
    print ("Invalid input, Enter a number")
    continue
  # check
  if guess_row == actual_row and guess_col == actual_col :
    print ("Congratulations! You found the treasure! You found the treasure in {} attempts.".format(attempts))
    break
  else :
      # hints
      if guess_row > actual_row : 
        print ("Hint:Move up")
      elif guess_row < actual_row : 
        print ("Hint:Move down")
      elif guess_col > actual_col :
        print ("Hint:Move left")
      elif guess_col < actual_col : 
        print ("Hint:Move right")
  # increase attempts 
  attempts += 1 