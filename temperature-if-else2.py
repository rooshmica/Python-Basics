# Program to display high temperature status

# Input temperature
temperature = float(input("Enter Celsius Temperature: "))

# If temperature > 27
if temperature > 27:    
    status = "Yellow"
else:
    status = "Green"

# Print status
print("Temperature Status:", status)


