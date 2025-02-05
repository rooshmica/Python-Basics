# Purpose: To check if a child is permitted to use a ride
# Example Of: Combining Conditions with and

print("This program checks if a child is permitted to use a ride")

# Input age
age = int(input("Enter child's age: "))

# input height
height = float(input("Enter child's height: "))

# check eligibility
if age >= 3 and height >= 1.02:
    print("Child is permitted to use the ride")
else:
    print("Child is not permitted to use the ride")


