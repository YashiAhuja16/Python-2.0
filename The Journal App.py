import datetime

while True:
    print("---- Journal App ----")
    print("1. Add an Entry.")
    print("2. View Entries.")
    print("3. Leave the journal.")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':  
        name = input("Write your entry: ")
        with open("journal.txt", "a") as x:  
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            x.write (" Date: {}\nEntry: {}\n\n".format (date, name))
        print("Your entry has been added.")
    
    elif choice == '2':  
        with open("journal.txt", "r") as x:  
            content = x.read()
            if content:
                print("---- Your Journal Entries ----")
                print(content)
            else:
                print("No entries found.")
    
    elif choice == '3':  
        print("Exiting the journal. Goodbye!")
        break
    
    else:
        print("Invalid choice, please try again.")