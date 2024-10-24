"""Miles to KM"""


def miles_to_km(miles: float) -> float:
    """
    Converts miles to kilometers

    Args:
        miles (float): Miles to convert to kilometers

    Returns:
        float: Kilometers

        Raises:
            TypeError: If input is not a float or int
    """
    if isinstance(miles, (float, int, str)):
        kilometers = miles * 1.60934
        e = "e"
        return round(kilometers, 2)

    raise TypeError(f"Input must be a float or int. Input was {type(miles)}")
