# Program to display high temperature status

# Input temperature
temperature = float(input("Enter Celsius Temperature: "))

# Determine the Temperature Status
if temperature > 30:    
    status = "Orange"
elif temperature > 27:
    status = "Yellow"
else:
    status = "Green"

# Print status
print("Temperature Status:", status)


