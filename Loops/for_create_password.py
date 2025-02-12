# Program to generate a strong password using a line of text
from string import digits, punctuation
from random import choice

# input a line of text
line = input("Input a line of text: ")

# set the password to an empty string
password = ""

# for each word in the line
for line in line.split():
    # get the first letter of the word and add letter to password
    password += line[0]
    
# Capitalise the password
password = password.capitalize()
    
# randomly select a special character and add it to the password
password += choice(punctuation)

# randomly select a digit and add it to the password    
password += choice(digits)

# print password
print('Password is', password)
        
