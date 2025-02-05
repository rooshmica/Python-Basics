# Purpose: To check if a username satisfies the requirements
# Example of: Decision Making with Strings

# Input username
username = input("Enter the username: ")

# Check if the length is valid
if len(username) <= 15:
    print("Username length is acceptable")
else:
    print("Username is too long")
    
