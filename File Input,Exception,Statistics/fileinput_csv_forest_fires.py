print("This program process forest fire data")

fires_list = [] # starts with an empty list

print()
print("Fires per month in Brazil, 1998-2017")
# open the file
with open("amazon.csv", encoding="ISO-8859-1") as data_file:
    # for each line in the file
    for line in data_file:
        # split each line into components
        year, state, month, fires, date = line.split(",")

        fires = int(fires) # convert the value into an integer
        fires_list.append(fires) # add it on to the list

print()
print(f"Number of values: {len(fires_list)}")
print(f"Total number of fires: {sum(fires_list)}")
print(f"Average number of fires per month: {sum(fires_list)/len(fires_list):.0f}")
print(f"Maximum number of fires: {max(fires_list)}")
print(f"Minimum number of fires: {min(fires_list)}")



