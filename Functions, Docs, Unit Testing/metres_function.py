# Program Name: section05_example05_metres_function.py
# Purpose: to convert a distance in feet and inches to metres
# Example of multiple parameters

def convert_to_metres(feet, inches):
    metres = (feet*12 + inches) * 0.0254
    print(f"Equivalent distance in metres is: {metres:.2f}m")

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    convert_to_metres(6, 2.5)

