num_values = int(input("Enter number of values: "))
count = 0
maximum = 0

while count < num_values:
    num_hits = int(input("Enter number of hits: "))
    
    if num_hits > maximum:

        maximum = num_hits
    
    count += 1
    

print()
print(f"Maximum hits per day: {maximum}")


