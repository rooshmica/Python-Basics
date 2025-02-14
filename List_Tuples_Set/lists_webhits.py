webhits = [859, 1257, 724, 1003, 982, 672, 598]

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

