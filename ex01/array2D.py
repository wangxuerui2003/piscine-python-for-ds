import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slice the family 2d list by start and end parameters
    """

    if not isinstance(family, list):
        print("family must be a list!")
        return []

    try:
        np_arr = np.array(family)
        if np_arr.ndim != 2:
            print("family must be 2D list!")
            return []

        print("My shape is", np_arr.shape)
        np_arr = np_arr[start:end]
        print("My new shape is", np_arr.shape)
        return np_arr.tolist()

    except ValueError:
        print("Lists not same size!")
        return []
    except Exception as e:
        print("Error:", e)
        return []
