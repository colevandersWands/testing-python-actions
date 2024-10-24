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
    if isinstance(km, float) or isinstance(km, int) or isinstance(km, str):
        miles = km / 1.60934
        return round(miles, 2)
    else:
        raise TypeError(f"Input must be a float or int. Input was {type(km)}")
