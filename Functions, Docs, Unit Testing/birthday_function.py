# File: section05_example03_birthday_function.py
# Purpose: to print the Happy Birthday song
# EXAMPLE OF: Function with parameter
# From Zelle, Chapter 6
def happy_birthday(name):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear", name)
    print("Happy birthday to you!")

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    person = input("Enter the person's name: ")
    happy_birthday(person)

