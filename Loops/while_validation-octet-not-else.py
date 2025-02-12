# Check for an invalid IP address octet

octet = int(input("Enter the octet: "))

while not 0 <= octet <= 255:
	print("Invalid, try again")
	octet = int(input("Enter the octet: "))
else:
	print("Valid")
