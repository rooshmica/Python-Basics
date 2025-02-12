# Program to calculate total, maximum and minimum web hits per day

# Input number of values
num_values = int(input("Enter number of values: "))

# initialise count and total variables
count = total = 0

# keep going until the count reaches num_values
while count < num_values:
    num_hits = int(input("Enter number of hits: "))
    
    # add it on to the total
    total += num_hits
    
    # if this is the first value
    if count == 0:
        # then set it as the maximum and minimum so far
        maximum = minimum = num_hits    
    # otherwise, if the current value is smaller than the minimum so far
    elif num_hits < minimum:
        # it becomes the new minimum
        minimum = num_hits
    # otherwise, if the current value is bigger than the maximum so far
    elif num_hits > maximum:
        # it becomes the new maximum
        maximum = num_hits
    
    # increase the count by 1
    count += 1
    
# Display the total, average, maximum and minimum
print()
print(f"Total hits {total}")
print(f"Average: {total/num_values:.1f}")
print(f"Maximum hits per day: {maximum}")
print(f"Minimum hits per day: {minimum}")

