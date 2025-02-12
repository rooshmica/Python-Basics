# Simple simulation of a user login
# Using a counting loop

count = 0 # number of login attempts

while count < 3: # maximum 3 attempts
    # input username and password
    username = input("Username: ")
    password = input("Password: ")

    # check if they match the correct username and password
    if username == "jbloggs" and password == "Secret123":
        print("Login succesful")
        break # exits the loop
    else:
        print("Login failed")
        count += 1 

# check: too many attempts
if count ==3:
    print("Too many failed attempts")
    exit() # terminate the program (will also terminate the iPython console!)
    
print("\nWelcome")



