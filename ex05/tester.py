from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_red
from pimp_image import ft_invert
from pimp_image import ft_grey
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img = Image.open('../landscape.jpg')
plt.imshow(img)
plt.savefig('original.jpg')

img_arr = np.array(img)
red_arr = ft_red(img_arr)
red_img = Image.fromarray(red_arr)
plt.imshow(red_img)
plt.savefig('red.jpg')
