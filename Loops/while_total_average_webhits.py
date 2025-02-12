# Input number of values
num_values = int(input("Enter number of values: "))

# initialise count and total variables
count = 0
total = 0

# keep going until the count reaches num_values
while count < num_values:
    num_hits = int(input("Enter number of hits: "))
    
    # add on to the total
    total += num_hits
        
    # increase the count by 1
    count += 1
    
# Display the total
print("Total hits:", total)
print(f"Average: {total/num_values:.1f}")

