# Program to check a strong password
password = input("Enter password: ")

# initialise flag variables
lowercase = False
uppercase = False
digit = False
special = False

# check each character in the password
for character in password:
    if character.islower():
        lowercase = True
    elif character.isupper():
        uppercase = True
    elif character.isdigit():
        digit = True
    elif not character.isalnum():
        special = True

# check if all flags are True
if lowercase and uppercase and digit and special:
    print("Valid password.")
else:
    print("Invalid password.")
    print("Include upper and lowercase letters, digits and special characters.")


    
