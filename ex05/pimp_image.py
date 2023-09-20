import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
        Inverts the color of the image received.
    """

    copy = array.copy()
    copy[:, :, :] = 255 - copy[:, :, :]
    return copy


def ft_red(array: np.ndarray) -> np.ndarray:
    """
        Retain only the red color channel
    """

    copy = array.copy()
    copy[:, :, 1] = 0  # ignore green channel
    copy[:, :, 2] = 0  # ignore blue channel
    return copy


def ft_green(array: np.ndarray) -> np.ndarray:
    """
        Retain only the green color channel
    """

    copy = array.copy()
    copy[:, :, 0] = 0  # ignore red channel
    copy[:, :, 2] = 0  # ignore blue channel
    return copy


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
        Retain only the blue color channel
    """

    copy = array.copy()
    copy[:, :, 0] = 0  # ignore red channel
    copy[:, :, 1] = 0  # ignore green channel
    return copy


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
        Turn an image into greyscale
    """

    average: np.ndarray = np.mean(array, axis=2).astype(int)
    copy = array.copy()
    copy[:, :, :3] = average[:, :, np.newaxis]
    return copy
