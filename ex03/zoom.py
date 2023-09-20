import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load


def ft_zoom(img_arr: np.ndarray, scale: float) -> np.ndarray:
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

    img_arr = img_arr[vert_start:vert_end, hori_start:hori_end, 0]
    return img_arr


def main():
    """
        Main function
    """

    img = ft_load('../animal.jpeg')
    if img.size == 0:
        sys.exit()

    try:
        img = ft_zoom(img, 0.5)
    except ValueError as e:
        print(e)

    img = Image.fromarray(img.squeeze())
    plt.imshow(img, cmap='gray')
    plt.savefig('output.jpeg')


if __name__ == '__main__':
    main()
