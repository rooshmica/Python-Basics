webhits = []

# Input number of values
num_values = int(input("How many values? "))

# Start the count at 0
count = 0

# while count is less than number of values
while count < num_values:
    # input value
    value = int(input("Enter the value: "))
    
    # add it to the list
    webhits.append(value)
    
    # increase the count by 1
    count += 1

# Display the number of values in the list
print("Number of values is", len(webhits))

# Display the values SORTED in order
print("The values in order are", sorted(webhits))

# Display the total (SUM) of the values
print("The total number of hits is", sum(webhits))

# Calculate and display the average SUM/LEN
print(f"The average number of hits is {sum(webhits)/len(webhits):.1f}")

# Display the MINimum
print("The minimum number of hits is", min(webhits))

# Display the MAXimum
print("The maximum number of hits is", max(webhits))

# Display the dispersion (MAX - MIN)
print("The dispersion is", max(webhits) - min(webhits))

