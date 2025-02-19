
def convert_to_metres(feet, inches):
    """
    Convert a distance from feet and inches to metres

    Parameters
    ----------
    feet : int
        The feet part of the distance.
    inches : float
        The inches part of the distance.

    Returns
    -------
    float
        The distance in metres.
    """
    # converting using the formula
    return (feet*12 + inches) * 0.0254


def convert_to_imperial(metres):
    """
    Convert a distance from metres to feet and inches

    Parameters
    ----------
    metres : float
        The distance in metres.

    Returns
    -------
    whole_feet : int
        The feet part of the distance.
    inches : float
        The inches part of the distance.
    """
    # Calculate metres to feet
    feet = metres * 3.28084

    # Calculate whole_feet as integer part of feet
    whole_feet = int(feet)

    # Calculate the remaining inches
    inches = (feet - whole_feet) * 12

    # return the results as a tuple
    return whole_feet, inches

