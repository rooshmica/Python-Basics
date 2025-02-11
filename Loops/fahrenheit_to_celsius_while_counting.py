
print("This program converts Fahrenheit temperatures to Celsius")

# start the count at zero
count = 0

# keep going until the count reaches 6
while count < 6:
    #Input fahrenheit temperature
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    
    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)
    
    # Print Celsius temperature 
    print(f"The temperature in Celsius is: {celsius:.1f}")

    # inbcrease the count
    count = count + 1
  
print()
print("All temperatures processed")


