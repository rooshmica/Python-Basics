def metres_to_imperial(metres):
    # Calculate feet as metres x 3.28084
    feet = metres * 3.28084

    # Calculate whole_feet as integer part of feet
    whole_feet = int(feet)

    # Calculate inches as (feet - whole_feet) * 12
    inches = (feet - whole_feet) * 12

    # return the results as a tuple
    return whole_feet, inches

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    # Input metres
    metres = float(input("Enter the distance in metres: "))

    # convert to feet and inches
    feet, inches = metres_to_imperial(metres)

    # Print whole_feet, inches
    print(f"Equivalent distance is {feet} feet, {inches:.1f} inches")

