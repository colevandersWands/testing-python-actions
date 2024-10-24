"""KM to Miles"""


def km_to_miles(kilometers: float) -> float:
    """
    Converts kilometers to miles

    Args:
        km (float): Kilometers to convert to miles

    Returns:
        float: Miles

    Raises:
        TypeError: If input is not a float or int
    """
    if isinstance(kilometers, (float, int, str)):
        miles = kilometers / 1.60934
        return round(miles, 2)
    else:
        raise TypeError(f"Input must be a float or int. Input was {type(kilometers)}")
