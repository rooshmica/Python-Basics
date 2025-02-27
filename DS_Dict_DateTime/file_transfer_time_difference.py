
import datetime

# open the file
with open("xferlog", "r", encoding="utf-8") as logfile:
    #  read in the contents of the file as a list of lines
    lines = logfile.readlines()

    # extract the date and time information from the first 24 characters of the first line
    first_date_string = lines[0][:24] # lines[0] is the first line, and then [0][:24] is a slice of the first 24 characters
    print("First file transfer recorded on", first_date_string)
    
    # create a datetime object
    first_date = datetime.datetime.strptime(first_date_string, "%a %b %d %H:%M:%S %Y")    
    
    # repeat the process for the last line of the file
    last_date_string = lines[-1][:24] # lines[-] is the last item in the list, i.e. the last line
    print("Last file transfer recorded on", last_date_string)
    last_date = datetime.datetime.strptime(last_date_string, "%a %b %d %H:%M:%S %Y")
    
    # calculate the time difference between the two files
    delta = last_date - first_date
    print("Time difference between transfers:", delta)

    

