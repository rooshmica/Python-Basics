

num_values = int(input("Enter number of values: "))

count = 0


while count < num_values:
    num_hits = int(input("Enter number of hits: "))
    
    # if this is the first value
    if count == 0:
        # then set it as the minimum so far
        minimum = num_hits
    
    # ptherwise, if the current value is smaller than the minimum so far
    elif num_hits < minimum:
        # it becomes the new minimum
        minimum = num_hits
    
    # increase the count by 1
    count += 1
    
# Display the minimum
print()
print(f"Minimum hits per day: {minimum}")

