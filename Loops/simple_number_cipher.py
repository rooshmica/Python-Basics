
from string import ascii_lowercase #abcdef...xyz

# Input a message 
plaintext = input("Enter the message to be enciphered: ")

ciphertext = ""


for character in plaintext.lower():
    # if the character is not a letter, skip it
    if not character.isalpha():
        continue 
        
    else:
        index = ascii_lowercase.index(character)
        
        ciphertext += str(index) + " "
        

print("The ciphertext is:", ciphertext)
        
        
    