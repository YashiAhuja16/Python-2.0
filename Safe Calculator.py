def safe_calculator(): 
  print("Welcome to the Safe Calculator")
  while True: 
    try: 
      x = float(input("Enter the first number:"))
      y = float(input("Enter the second number:"))
    except ValueError:
      print ("Invalid, please try again.")
      continue 
    choice = input("Choose what operation you would like to do, +, -, *, /:")
    try :
      if choice == "+" :
        print ("The result is", x+y)
      elif choice == "-" :
        print("The result is", x-y)
      elif choice == "*" : 
        print("The result is", x*y)
      elif choice == "/" :
        print("The result is", x/y)
      else:
          print ("Invalid choice, try again")
    except ZeroDivisionError: 
        print ("Invalid. We cannot divide a number by zero. Try again.")
        continue
    z = input("Do you want to perform another calculation? yes/no:")
    if z == "yes":
      continue
    elif z == "no":
      print ("Bye!")
      break 
    else: 
      print("Not an option")
    
safe_calculator()