
from time import gmtime, localtime

# gmtime returns the current UTC time as a time structure
print("Current UTC time:", gmtime())
print("\nEpoch:", gmtime(0)) # 0 seconds since the start of the Epoch

# gmtime returns the current local time as a time structure
print("\nCurrent local time:", localtime())


