# Program to display high temperature status

# Input temperature
temperature = float(input("Enter Celsius Temperature: "))

# Set the status
status = "Yellow" if temperature > 27 else "Green"

# Print status
print("Temperature Status:", status)


