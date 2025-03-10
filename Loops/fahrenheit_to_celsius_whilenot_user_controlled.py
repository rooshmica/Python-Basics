print("This program converts Fahrenheit temperatures to Celsius")

# assume the user wants to convert at least 1 temperapture
finished = False # for not finished

# keep going until the user is finished
while not finished:
    #Input fahrenheit temperature
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    
    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)
    
    # Print Celsius temperature 
    print(f"The temperature in Celsius is: {celsius:.1f}")

    # ask the user if s/he is finished
    response = input("Are you finished (y/n)? ")
    if response.lower() == "y":
        finished = True    
  
print()
print("All temperatures processed")


