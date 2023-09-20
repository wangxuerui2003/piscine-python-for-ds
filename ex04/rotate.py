import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load


def ft_rotate(img: np.ndarray):
    """
        Rotate the img 90 deg anti-clockwise if the array is squeezable to 2D
        How it works:
            iterate the columns and put all of them into a list,
            then map the list into a np.ndarray.
    """

    img = img.squeeze()  # eliminate the 3rd dimension if possible
    if not img.ndim == 2:
        raise ValueError("Image array must be squeezable to 2D to rotate")

    return np.array([img[:, i] for i in range(img.shape[1])])


def ft_zoom(img_arr: np.ndarray, scale: float) -> np.ndarray:
    """
        Zoom into the image by scale.
        Raise exception for error
    """

    if scale < 1:
        raise ValueError("Scale should be greater or equal to 1!")

    scale = 1 / scale

    # slicing
    height, width = img_arr.shape[0:2]
    size = min(height * scale, width * scale)
    vert_start = int((height - size) / 2)
    vert_end = height - vert_start
    hori_start = int((width - size) / 2)
    hori_end = width - hori_start

    img_arr = img_arr[vert_start:vert_end, hori_start:hori_end, 0:1]
    return img_arr


def main():
    """
        Main function
    """

    img_arr = ft_load('../animal.jpeg')
    if img_arr.size == 0:
        sys.exit()

    try:
        img_arr = ft_zoom(img_arr, 2.0)
        shape = img_arr.shape
        print(f"The shape of image is: {shape} or {shape[0:2]}")
        print(img_arr)

        # img_arr = img_arr.squeeze().transpose()
        img_arr = ft_rotate(img_arr)
        print("New shape after Transpose:", img_arr.shape)
        print(img_arr)

        img = Image.fromarray(img_arr)
        plt.imshow(img, cmap='gray')
        plt.savefig('output.jpeg')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
