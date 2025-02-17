import os
import os.path

# Input the file name
filename = input("Enter the filename: ")

# check if the file exists
if os.path.exists(filename):
    # check if the file is a file (not a directory)
    if os.path.isfile(filename):
        # check if we have permission to read the file
        if os.access(filename, os.R_OK):
            # we can read from the file: open it with read access
            with open(filename) as input_file:
                # return the contents of the file as a list of lines
                contents = input_file.readlines()
                print("Read", len(contents), "lines from the file")
        else:
            print("Error: No permissions to read file", filename)
    else:
        print("Error:", filename, "is a directory")
else:
    print("Error:", filename, "does not exist")

