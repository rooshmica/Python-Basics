print("This program process forest fire data")

fires_list = [] # starts with an empty list

print()
print("Fires per month in Acre, 2016")
# open the file
with open("forest_fires.txt") as data_file:
    # for each line in the file
    for fires in data_file:
        fires = int(fires)
        print(fires) # print the current line
        fires_list.append(fires)

print()
print(f"Number of values: {len(fires_list)}")
print(f"Total number of fires: {sum(fires_list)}")
print(f"Average number of fires per month: {sum(fires_list)/len(fires_list)}")
print(f"Maximum number of fires: {max(fires_list)}")
print(f"Minimum number of fires: {min(fires_list)}")



