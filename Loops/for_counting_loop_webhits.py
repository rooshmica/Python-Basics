# Program to calculate total and average web hits per day
# Counting for Loop

# Input number of values
num_values = int(input("Enter number of values: "))

# initialise total variable
total = 0

# keep going until i reaches num_values
for i in range(num_values):
    num_hits = int(input("Enter number of hits: "))
    
    # add on to the total
    total += num_hits
    
# Display the total
print("Total hits:", total)
print(f"Average: {total/num_values:.1f}")

