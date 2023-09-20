import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load
import sys


def ft_zoom(img_arr: np.ndarray, scale: float):
    """
        Zoom into the image by scale.
        Raise exception for error
    """

    if scale < 1:
        raise ValueError("Scale should be greater than 1!")

    scale = 1 / scale

    # slicing
    height, width = img_arr.shape[0:2]
    size = min(height * scale, width * scale)
    vert_start = int((height - size) / 2)
    vert_end = int(height - vert_start)
    hori_start = int((width - size) / 2)
    hori_end = int(width - hori_start)

    print(vert_start, vert_end, hori_start, hori_end)

    img_arr = img_arr[vert_start:vert_end, hori_start:hori_end, 0]


def main():
    img = ft_load('../animal.jpeg')
    if img.size == 0:
        sys.exit()

    ft_zoom(img, 2.0)

    img = Image.fromarray(img.squeeze())
    plt.imshow(img, cmap='gray')
    plt.savefig('output.jpeg')


if __name__ == '__main__':
    main()
