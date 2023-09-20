from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_red
from pimp_image import ft_invert
from pimp_image import ft_grey
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def show_img(img_arr: np.ndarray, filename: str, extension='jpg'):
    """
        Helper function.
        Use matplotlib to plot the image and save to filename.extension
    """

    img = Image.fromarray(img_arr)
    plt.imshow(img)
    plt.savefig(f"{filename}.{extension}")


IMAGE_PATH = '../landscape.jpg'
EXTENSION = 'jpg'

""" Original image"""
img = Image.open(IMAGE_PATH)
plt.imshow(img)
plt.savefig(f'original.{EXTENSION}')
img.close()

img_arr = ft_load(IMAGE_PATH)

""" Red filter """
red_arr = ft_red(img_arr)
show_img(red_arr, 'red', EXTENSION)

""" Green filter """
green_arr = ft_green(img_arr)
show_img(green_arr, 'green', EXTENSION)

""" Blue filter """
blue_arr = ft_blue(img_arr)
show_img(blue_arr, 'blue', EXTENSION)

""" Invert filter """
invert_arr = ft_invert(img_arr)
show_img(invert_arr, 'invert', EXTENSION)

""" Grey filter """
grey_arr = ft_grey(img_arr)
show_img(grey_arr, 'grey', EXTENSION)
