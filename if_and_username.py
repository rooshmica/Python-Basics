# Purpose: To validate a username
# Example of: decision making with string methods


# Input username
username = input("Enter username: ")

# Check if the username is valid
if len(username) <= 15 and username.islower():
    print("Username is acceptable")
else:
    print("Username does not meet requirements")
  

