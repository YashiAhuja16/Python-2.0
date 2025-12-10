import random 

# list of words 
list_words = ["teddy","cupcake","perfume","money","squishy"]

# jumble words
def jumble_words(word):
  # word that is picked needs to coverted to list
  letters = list(word)
  random.shuffle(letters)
  # list to string
  return "".join(letters)
  
round = 5
score = 0   # <-- added score variable

for round_num in range (1, round+1, 1) :
  print("Round - {}".format (round_num))
  # pick a word fron the list
  word = random.choice(list_words)
  scrambled_word = jumble_words(word)
  print ("Here is your scrambled word : {}" . format (scrambled_word))
  
  x = input("Would you like a hint? Yes/No:").lower()
  if x == "yes" :
    print("The first letter of the word is {}".format (word[0]))
  
  y = input("Ok, what is the word?:")
  if y == word: 
    print("Correct!")
    score += 1     # <-- increase score when correct
  else: 
    print("Wrong!The word was {}".format(word))

  print("Score:", score)   # <-- show updated score

print("Final Score:", score)