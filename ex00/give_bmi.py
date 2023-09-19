import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Return a list of bmi by inputting a list of height and weight
    """

    if not (isinstance(height, list) and isinstance(weight, list)):
        print("Both height and weight parameter has to be lists!")
        return []

    height_arr = np.array(height)
    if not (height_arr.dtype == int or height_arr.dtype == float):
        print("Height List must contain only int or float!")
        return []

    if not np.all(height_arr > 0):
        print("Height List must contain only positive numbers!")
        return []

    weight_arr = np.array(weight)
    if not (weight_arr.dtype == int or weight_arr.dtype == float):
        print("Weight List must contain only int or float!")
        return []

    if not np.all(weight_arr > 0):
        print("Weight List must contain only positive numbers!")
        return []

    if not height_arr.ndim == weight_arr.ndim == 1:
        print("Height and Weight list must be 1D lists!")
        return []

    if not height_arr.shape == weight_arr.shape:
        print("Height and Weight List must have same size!")
        return []

    height_arr *= height_arr
    bmi_arr = weight_arr / height_arr
    return bmi_arr.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Return a list of bool represents if the bmi is over the limit
    """

    if not isinstance(bmi, list):
        print("bmi parameter must be a list!")
        return []

    bmi_arr = np.array(bmi)
    if not (bmi_arr.dtype == int or bmi_arr.dtype == float):
        print("bmi list must contain only int or float!")
        return []

    if not bmi_arr.ndim == 1:
        print("bmi list must be 1D lists!")
        return []

    bool_arr = bmi_arr > limit
    return bool_arr.tolist()
