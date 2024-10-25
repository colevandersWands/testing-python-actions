"""KM to Miles"""


def km_to_miles(km: float) -> float:
    """
    Converts kilometers to miles

    Args:
        km (float): Kilometers to convert to miles

    Returns:
        float: Miles

    Raises:
        TypeError: If input is not a float or int
    """
    if isinstance(km, (float, int, str)):
        miles = km / 1.60934
        return round(miles, 2)
        print(2)

    raise TypeError(f"Input must be a float or int. Input was {type(km)}")
