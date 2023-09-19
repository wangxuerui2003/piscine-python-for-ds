import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Return a list of bmi by inputting a list of height and weight
    """

    height_arr = np.array(height)
    if not (height_arr.dtype == int or height_arr.dtype == float):
        raise ValueError("Height List must contain only int or float!")

    weight_arr = np.array(weight)
    if not (weight_arr.dtype == int or weight_arr.dtype == float):
        raise ValueError("Weight List must contain only int or float!")

    if not len(height_arr.shape) == len(weight_arr.shape) == 1:
        raise ValueError("Height and Weight list must be 1D lists!")

    if not height_arr.shape == weight_arr.shape:
        raise ValueError("Height and Weight List must have same size!")

    height_arr *= height_arr
    bmi_arr = weight_arr / height_arr
    return bmi_arr.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Return a list of bool represents if the bmi is over the limit
    """

    return [bmi_value > limit for bmi_value in bmi]
