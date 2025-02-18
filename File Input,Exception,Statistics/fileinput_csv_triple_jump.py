import shelve

print("This program inputs data from a csv file and stores them in a shelve file")

# open the shelve "database" file, or create a new one if it doesn't already exist
results = shelve.open("triple_jump2")

print()
print("2019 Women's Triple Jump Final Results")
print()
# open the file
with open("triple_jump2.csv") as data_file:
    # for each line in the file
    for line in data_file:
        # split each line into a list of components, but keep the jumps together
        values = line.strip().split(",", maxsplit=3)

        # for clarity, assigning the items in the values list to variables
        name = values[0]
        bib = values[1]
        country = values[2]

        # create a list of the jump distances
        jumps = [ float(x) for x in values[3].split(",")]

        # insert into the dictionary: key is (name, bib, country)
        results[bib] = (name, country, jumps)

        print(f"Storing data for competitor {bib:>4} {name:18} ({country:3})")

    # processed all the data in the csv file, so the for loop has finished
    else: # close the shelve
        results.close()






