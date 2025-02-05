# Program to check cholesterol levels
# EXAMPLE OF: two-way decision, if-else

# Input hdl
hdl = float(input("Enter hdl cholesterol: "))

# Input ldl
ldl = float(input("Enter ldl cholesterol: "))

# calculate total
total = hdl + ldl

# display total
print("Total cholesterol is:", total)

# determine and display message
if total <= 5:
    print("Healthy cholesterol level")
elif total <= 6.4:
    print("Mildly high cholesterol level")
elif total <= 7.8:
    print("Moderately high cholesterol level")
else:
    print("Very high cholesterol level")
    
