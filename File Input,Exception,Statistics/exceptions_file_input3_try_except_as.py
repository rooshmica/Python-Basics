# Input the file name
filename = input("Enter the filename: ")

# try to open it with read access
try:
    with open(filename) as input_file:
        # return the contents of the file as a list of lines
        contents = input_file.readlines()
        print("Read", len(contents), "lines from the file")
# the syntax except ExceptionName as something_error
# allows you to access the exception object, for example to print it
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IsADirectoryError as dir_error:
    print(dir_error)
except PermissionError as permission_error:
    print(permission_error)
    

