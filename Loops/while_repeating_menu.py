from subprocess import getoutput

while True: 
	print() 
	print("1.Disk Free Information")
	print("2.Memory")
	print("3.Uptime")
	choice = int(input("Enter your choice of 0 to quit: ")	)
	
	
	if choice == 0:
		break
		
	elif choice == 1: # Disk Free 
		print(getoutput("df -h /"))
		
	elif choice == 2: # Memory
		print(getoutput("free -g"))
		
	elif choice == 3: # Uptime
		print(getoutput("uptime"))
		
	else:
		print("Invalid input, try again")

print()
print("Program finished")

