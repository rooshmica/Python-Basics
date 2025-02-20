
def is_valid_password(password):
    return 8 <= len(password) <= 15

def is_valid_password2(password):
    if 8 <= len(password) <= 15:
        return True
    else:
        return False

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    password = input('Enter your password ')

    # use the function to check the password
    if is_valid_password(password):
        print("Password length is ok")
    else:
        print("Password is too short")

