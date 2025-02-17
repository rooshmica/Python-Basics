# Input the file name
filename = input("Enter the filename: ")

# keep going until the user provides a valid file or chooses to quit
while True:
    # try to open it with read access
    try:
        with open(filename) as input_file:
            # return the contents of the file as a list of lines
            contents = input_file.readlines()
            print("Read", len(contents), "lines from the file")
            break # exit from while loop
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IsADirectoryError as dir_error:
        print(dir_error)
    except PermissionError as permission_error:
        print(permission_error)

    # ask the user if they want to try with a different file
    choice = input("Try again with a different file (y/n)? ").lower()

    if choice in ["y", "yes"]:
        filename = input("Enter a different filename: ")
    else:
        break









