def cups_gram (cups, grams):
    return cups * grams 
def tbsp_tsp (tablespoons):
    return tablespoons * 3 
def grams_cup (grams, cups):
    return grams / cups

while True: 
    print ("1. Convert cups to grams")
    print ("2. Convert tablespoons to teaspoons")
    print ("3. Convert grams to cups")
    print ("4. Exit.")
    choice = int(input("Enter your choice:"))
    if choice == 1 :
        cups = int(input("Enter the number of cups:") )
        grams = float(input("Enter the number of grams in each cup:"))
        print ("Result:", cups_gram(cups,grams)) 
    elif choice == 2 : 
        tablespoons = int(input("Enter the number of tablespoons:"))
        print ("Result:", tbsp_tsp(tablespoons))
    elif choice == 3 : 
        grams = float(input("Enter the number of grams:"))
        cups = int(input("Enter the number of cups:"))
        print ("Results:", grams_cup(grams,cups))
    elif choice == 4 :
        break  
    else :
      print ("Error")