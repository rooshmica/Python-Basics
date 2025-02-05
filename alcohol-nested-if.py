# Purpose: To determine if the weekly alcohl intake has been exceeded
# Example of: Nested If

print("This program checks if you have exceeded the recommended weekly alcohol limit")

# Input gender
gender = input("Enter your gender (Male/Female): ")

# Input number of units consumed
units = float(input("Number of units of alcohol consumed this week: "))

# check if the user has exceeded her/his weekly limit
if gender.lower() == "female":
    if units > 11:
        print("You have exceeded the recommended alcohol limit for a woman")
    else:
        print("You have not exceeded the recommended alcohol limit for a woman")
        
elif gender.lower() == "male":
    if units > 17:
        print("You have exceeded the recommended alcohol limit for a man")
    else:
        print("You have not exceeded the recommended alcohol limit for a man")
        
else:
    print("Unable to process gender input")
