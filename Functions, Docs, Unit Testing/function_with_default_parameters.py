def check_password_length(password, minlen=8, maxlen=32):
    if minlen <= len(password) <= maxlen:
        print("Password is correct length")
    else:
        print("Password is not the correct length")

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    password = input('Enter your password ')

    # use the function to check the password
    check_password_length(password) # use defaults for minlen and maxlen
    check_password_length(password, 10) # use default for maxlen
    check_password_length(password, 10, 20) # no defaults


