# Start with an empty list
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

# Sort the values in increasing order
webhits.sort()
print("The values in order are", webhits)

# Calculate the index of the middle value
mid_index = int(len(webhits)/2)

# Caclulate and display the median value
if len(webhits) % 2 == 1: # odd number of values
    median = webhits[mid_index]
else:  # even number of values
    median = sum(webhits[mid_index-1:mid_index+1])/2

print(f"Median value is: {median}")    
    
