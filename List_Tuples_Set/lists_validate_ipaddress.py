print("Program to validate an IPv4 address")

# input the ip address
ip = input("Enter the IP address: ")

# Split into octects
octets_list = ip.split(".")

# check the number of octets
if len(octets_list) != 4:
    print("Invalid IP address")

# it has 4 octets, so it's ok (so far)
else:
    # check each octet number
    for number in octets_list:
        # is it in the correct range
        if not 0 <= int(number) <= 255:
            # if not, it"s invalid
            print("Invalid IP address")
            break
    else:
        # the 4 octet numbers are valid
        print (ip,"is a valid IP address")


