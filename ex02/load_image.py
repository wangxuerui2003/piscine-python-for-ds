import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
        Load the image with the path and return the array representation.
        Handles only /jpg/jpeg/png images
    """

    if not isinstance(path, str):
        print("Path must be a string!")
        return np.empty(shape=[0])

    suffix = path.split('.')[-1]
    if suffix.lower() not in ['jpg', 'jpeg', 'png']:
        print("Invalid image format!")
        return np.empty(shape=[0])

    try:
        img = Image.open(path)
        img_arr = np.array(img)

        print("The shape of the image is:", img_arr.shape)
        return img_arr
    except FileNotFoundError:
        print("Invalid path!")

    return np.empty(shape=[0])
