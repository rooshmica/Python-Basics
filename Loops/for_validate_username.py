# Program to validate a username
# Example of a for loop to process the characters in a string
username = input("Enter the username: ")

# Check if the username contains Admin
if "Admin" in username:
	print("Invalid: username must not contain Admin")
# Check if username is too long
elif len(username) > 15:
	print("Invalid: exceeds 15 characters")
# Check if it contains an invalid character
else:
	# process each character, one at a time
	for character in username:
		# if the character is invalid
		if not character.isalpha() and not character.isdigit() and character != '_':
			print("Invalid character: ", character)
			break # exit loop
	# reached end of username
	else:
		print(username, "is valid")

