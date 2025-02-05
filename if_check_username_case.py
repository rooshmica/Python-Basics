# Purpose: To check if a username contains no uppercase characters
# Example of: Decision Making with Strings

# Input username
username = input("Enter the username: ")

# Check if the length is valid
if username.islower():
    print("Username is acceptable")
else:
    print("Username contains uppercase character(s)")
    
