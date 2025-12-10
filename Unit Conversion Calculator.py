def meters_feet (meters):
    return meters * 3 
def inches_centimeters (inches):
    return inches * 2.54 
def kilo_lbs (kilo):
    return kilo * 2.2
def C_F (celsius):
    return celsius * 1.8 + 32 
    
while True: 
    print ("Choose an option")
    print ("1. Convert meters to feet")
    print ("2. Convert inches to centimeters")
    print ("3. Convert kilograms to pounds")
    print ("4. Convert Celsisus to Fahrenheit")
    print ("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1 :
      meters = float(input("Enter how many meters you want to convert:"))
      print("Results:", meters_feet(meters))
    elif choice == 2 :
      inches =  float(input("Enter how many inches you want to convert:"))
      print("Results:", inches_centimeters(inches))
    elif choice == 3 : 
      kilograms = float (input("Enter how many kilograms you want to convert:"))
      print("Results:", kilo_lbs(kilograms))
    elif choice == 4 : 
      celsius = float(input("Enter the amount of degrees in Celsius:"))
      print("Results:", C_F(celsius))
    elif choice == 5 : 
      print ("You are out of the program.")
      break 
    else: 
      print("Error")
