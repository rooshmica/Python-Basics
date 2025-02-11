
print("This program converts Fahrenheit temperatures to Celsius")

# assume the user wants to convert at least 1 temperapture
choice = "y" # for "yes"

# keep going while the user's choice is "y"
while choice == "y":
    #Input fahrenheit temperature
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    
    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)
    
    # Print Celsius temperature 
    print(f"The temperature in Celsius is: {celsius:.1f}")

    # ask the user if s/he wants to convert another temperature
    choice = input("Convert another temperature (y/n)? ")
  
print()
print("All temperatures processed")


