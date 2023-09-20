import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def show_img(img_arr: np.ndarray, filename: str, extension='jpg'):
    """
        Helper function.
        Use matplotlib to plot the image and save to filename.extension
    """

    img = Image.fromarray(img_arr)
    plt.imshow(img)
    plt.savefig(f"{filename}.{extension}")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""

    print("The shape of image is:", array.shape)
    copy = array.copy()
    copy = 255 - copy
    print(copy)
    print("The shape of image after filter is:", copy.shape)
    return copy


def ft_red(array: np.ndarray) -> np.ndarray:
    """Retain only the red color channel"""

    print("The shape of image is:", array.shape)
    copy = array.copy()
    copy[:, :, [1, 2]] = 0  # ignore green and blue channel
    print(copy)
    print("The shape of image after filter is:", copy.shape)
    return copy


def ft_green(array: np.ndarray) -> np.ndarray:
    """Retain only the green color channel"""

    print("The shape of image is:", array.shape)
    copy = array.copy()
    copy[:, :, [0, 2]] = 0  # ignore red and blue channel
    print(copy)
    print("The shape of image after filter is:", copy.shape)
    return copy


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Retain only the blue color channel"""

    print("The shape of image is:", array.shape)
    copy = array.copy()
    copy[:, :, [0, 1]] = 0  # ignore red and green channel
    print(copy)
    print("The shape of image after filter is:", copy.shape)
    return copy


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Turn an image into greyscale"""

    print("The shape of image is:", array.shape)

    # for each pixel, take the mean value of its rgb value
    # and put all into a 2D np array
    average: np.ndarray = np.mean(array, axis=2).astype(int)
    copy = array.copy()

    # add an empty 3rd axis to perform the assignment
    copy[:, :, :] = average[:, :, np.newaxis]

    print(copy)
    print("The shape of image after filter is:", copy.shape)
    return copy
