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
    if isinstance(miles, float) or isinstance(miles, int) or isinstance(miles, str):
        km = miles * 1.60934
        x = 3
        return round(km, 2)
    else:
        raise TypeError(f"Input must be a float or int. Input was {type(miles)}")
