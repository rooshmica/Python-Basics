# Input the file name
filename = input("Enter the filename: ")

# try to open it with read access
try:
    with open(filename) as input_file:
        # return the contents of the file as a list of lines
        contents = input_file.readlines()
        print("Read", len(contents), "lines from the file")

except: # if an exception was encountered in the try block
    print("Error reading from file", filename)

