def square(number: float) -> float:
    """
    Calculate the square of a number.

    Parameters
    ----------
    number : float
        The number to be squared.

    Returns
    -------
    float
        The number squared.
    """
    return number * number

def greeting(name: str) -> str:
    """
    Return a greeting using the name provided

    Parameters
    ----------
    name : str
        A person's name.

    Returns
    -------
    str
        The greeting, which includes the person's name.
    """
    return "Hello " + name

def is_valid_password_length(password: str, minlen: int = 8, maxlen: int = 32) -> bool:
    """
    Check if the length of a password is between specified minimum and maximum

    Parameters
    ----------
    password : str
        The password to be checked..
    minlen : int, optional
        The minimum acceptable password length. The default is 8.
    maxlen : int, optional
        The maximum acceptable password length. The default is 32.

    Returns
    -------
    bool
        Whether or not the password length is valid.
    """
    return minlen <= len(password) <= maxlen


if __name__ == "__main__":
    print(greeting("Joe Bloggs"))

