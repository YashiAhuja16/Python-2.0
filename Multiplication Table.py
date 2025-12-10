while True:
  print ("Welcome to Multiplication Table Generator")
  x = int(input("Enter the number you choose from:"))
  print ("1.Till 10")
  print ("2.Till 20")
  print ("3.Till 30")
  choice = int(input("Enter your choice:"))
  if choice == 1:
    for i in range(1,11,1):
      print ("{} x {} = {}".format(x,i,x*i))
  elif choice == 2:
    for i in range(1,21,1):
      print ("{} x {} = {}".format(x,i,x*i))
  elif choice == 3:
    for i in range(1,31,1):
      print ("{} x {} = {}".format(x,i,x*i))
  else: 
    print ("Invalid Choice")