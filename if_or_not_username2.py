# Purpose: To validate a username
# Example of: decision making with string methods

print("This program validates a username")

# Input username
username = input("Enter username: ")

# Check if the username is valid
if len(username) > 15 or not username.islower():
    print("Username does not meet requirements")          
else:
    print("Username is acceptable")



