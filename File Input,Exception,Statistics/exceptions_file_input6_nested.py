# Input the file name
filename = input("Enter the filename: ")

# keep going until the user provides a valid file or chooses to quit
while True:
    # try to open it with read access
    try:
        with open(filename) as input_file:
            # read the lines one at a time
            for line in input_file:
                try:
                    # split the line into firstname and lastname
                    firstname, lastname = line.strip().split()
                    print(f"{lastname}, {firstname}")
                except ValueError:
                    print("name not in correct format:", line.strip())

            break # exit from while loop

    # the syntax except ExceptionName as something_error
    # allows you to access the exception object, for example to print it
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









