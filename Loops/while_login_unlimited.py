# Simple progam to input and check a username and password
# Purpose: to demonstrate a while loop
#
# This is not a realistic login program:
# 1. Password should not appear when input
# 2. Username and password are hard-coded
# 3. No encryption used

# Input username and password
username = input("Username: ")
password = input("Password: ") 

# keep going until the user 
while username != "jbloggs" or password != "Secret123": 
	print("Invalid username or password, try again")
    
    # Input username and password again
	username = input("Username: ")
	password = input("Password: ") 

print("Login successful")

