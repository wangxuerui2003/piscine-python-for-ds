import sys
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_red
from pimp_image import ft_invert
from pimp_image import ft_grey
from pimp_image import show_img
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


IMAGE_PATH = '../landscape.jpg'
EXTENSION = 'jpg'

try:
    # save the original image
    img = Image.open(IMAGE_PATH)
    plt.imshow(img)
    plt.savefig(f'original.{EXTENSION}')
    img.close()
except FileNotFoundError:
    print("Image not found!")
    sys.exit()

img_arr = ft_load(IMAGE_PATH)

print()
print('""" Red filter """')
red_arr = ft_red(img_arr)
show_img(red_arr, 'red', EXTENSION)

print()
print('""" Green filter """')
green_arr = ft_green(img_arr)
show_img(green_arr, 'green', EXTENSION)

print()
print('""" Blue filter """')
blue_arr = ft_blue(img_arr)
show_img(blue_arr, 'blue', EXTENSION)

print()
print('""" Invert filter """')
invert_arr = ft_invert(img_arr)
show_img(invert_arr, 'invert', EXTENSION)

print()
print('""" Grey filter """')
grey_arr = ft_grey(img_arr)
show_img(grey_arr, 'grey', EXTENSION)

print()
print('""" Docstrings """')
print("ft_blue:", ft_blue.__doc__)
print("ft_green:", ft_green.__doc__)
print("ft_red:", ft_red.__doc__)
print("ft_grey:", ft_grey.__doc__)
print("ft_invert:", ft_invert.__doc__)
