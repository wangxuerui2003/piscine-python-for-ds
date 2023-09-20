import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load


def ft_invert(array: np.ndarray) -> np.ndarray:
    pass


def ft_red(array: np.ndarray) -> np.ndarray:
    copy = array.copy()
    copy[:, :, 1] = 0
    copy[:, :, 2] = 0
    return copy


def ft_green(array: np.ndarray) -> np.ndarray:
    pass


def ft_blue(array: np.ndarray) -> np.ndarray:
    pass


def ft_grey(array: np.ndarray) -> np.ndarray:
    pass
