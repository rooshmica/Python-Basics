from random import choice, randint
from string import punctuation

print("Program to generate random password from the 'words' file")


with open("words") as wordsfile:
    # read in the entire contents of the file as a list of lines
    wordlist = wordsfile.readlines()

    # keep going until the user is finished
    while True:
    
        # randomly pick two words
        word1 = choice(wordlist).strip().capitalize()
        word2 = choice(wordlist).strip().capitalize()
    
        # randomly pick a digit
        digit = randint(0, 9)
    
        # randomly pick a special character
        special = choice(punctuation)
    
        # join them together
        password = word1 + str(digit) + word2 + special

        # print the password
        print("Password:", password)

        # ask the user if they want to go again
        response = input("Generate another password? ").lower()

        if response not in ["y", "yes"]:
            break

