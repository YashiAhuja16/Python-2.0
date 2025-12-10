def dollars_rupees (dollars):
    return dollars * 86 
def dollars_euros (dollars):
    return dollars * 0.85 
def dollars_yuan (dollars):
    return dollars * 7 
def dollars_yen (dollars):
    return dollars * 146
def dollars_pesos (dollars):
    return dollars * 18 

while True:
    print ("Choose an option")
    print ("1. Convert dollars to rupees")
    print ("2. Convert dollars to euros")
    print ("3. Convert dollars to yuan")
    print ("4. Convert dollars to yen")
    print ("5. Convert dollars to pesos")
    print ("6. Exit")
    choice = int(input("Enter your choice:")) 
    if choice == 1: 
        dollars = float(input("Enter how much money you have in dollars:"))
        print("Results:", dollars_rupees(dollars))
    elif choice == 2:
      dollars = float(input("Enter how much money you have in dollars:"))
      print("Results:", dollars_euros(dollars))
    elif choice == 3:
      dollars = float(input("Enter how much money you have in dollars:"))
      print("Results:", dollars_yuan(dollars))
    elif choice == 4:
      dollars = float(input("Enter how much money you have in dollars:"))
      print("Results:", dollars_yen(dollars))
    elif choice == 5:
      dollars = float(input("Enter how much money you have in dollars:"))
      print("Results:", dollars_pesos(dollars))
    elif choice == 6: 
      break 
    else: 
      print("Error")
      