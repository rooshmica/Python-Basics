# Regular expressions in Python
# Example of capturing output from a command
import re
from subprocess import getoutput

# run the ip a command and store the output
output = getoutput("ip a")

# search for the firstIP address
match = re.search("(?:\d{1,3}\.){3}\d{1,3}", output)

if match:
    # print the IPv4 addresses found
    print("First IP address found:", match.group())
else:
    print("No IPv4 address found")




