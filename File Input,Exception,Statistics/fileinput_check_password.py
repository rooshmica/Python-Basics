print("Program to check if a password is a dictionary word")

# Input password
password = input("Enter the password: ")

# Open the wordlist (dictionary) file
with open("words") as wordsfile:
    # go through the words file, one line at a time
    for word in wordsfile:
        # compare the password with the current word
        if password == word.strip(): # remove the newline character
            print("Password is in the dictionary")
            break
    # reached end of file and didn"t find the password
    else:
        print("Password is not in the dictionary")


