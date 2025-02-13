print("User management program")

users = [] # start with an empty list

while True:
    # menu of choices 
    choice = input("[A]dd [R]emove [D]isplay [C]lear [Q]uit? ")
    
    # process the user's choice - check the first character of their choice
    if choice[0].lower() == "q": # quit
        break
    elif choice[0].lower() == "a":# add
        name = input("Enter name of new user: ")
        users.append(name)
        print("Added user", name)
    elif choice[0].lower() == "r": # remove
        name = input("Enter name of user to remove: ")
        if name in users:
            users.remove(name)
            print("Removed user", name)
        else:
            print("No such user", name)
    elif choice[0].lower() == "d": # display
        print("Number of users:", len(users))
        users.sort() # sort the names in order
        for user in users:
            print(user)
    elif choice[0].lower() == "c": # clear the list
        response = input("Remove all users from the list? (y/n) ")
        if response.lower() == "y":
            users.clear()
    else:
        print("Invalid choice")


