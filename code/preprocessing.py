# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-gOle3BuFxt55jsoh31O4wZbUagrvqml
"""

from PIL import Image, ImageOps
from skimage import io, color
from skimage.filters import threshold_otsu
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

image_list = [
    "imgs/3.jpg","imgs/4.jpg","imgs/5.jpg", "imgs/6.jpg", "imgs/7.jpg", "imgs/8.jpg", "imgs/9.jpg",
    "imgs/10.jpg", "imgs/11.jpg", "imgs/12.jpg", "imgs/13.jpg", "imgs/14.jpg",
    "imgs/15.jpg", "imgs/16.jpg", "imgs/17.jpg", "imgs/18.jpg", "imgs/19.jpg",
    "imgs/20.jpg", "imgs/21.jpg", "imgs/22.jpg", "imgs/23.jpg", "imgs/24.jpg",
    "imgs/25.jpg", "imgs/26.jpg", "imgs/27.jpg", "imgs/28.jpg", "imgs/29.jpg",
    "imgs/30.jpg", "imgs/31.jpg", "imgs/32.jpg", "imgs/33.jpg", "imgs/34.jpg",
    "imgs/35.jpg", "imgs/36.jpg", "imgs/37.jpg", "imgs/38.jpg", "imgs/39.jpg",
    "imgs/40.jpg", "imgs/41.jpg", "imgs/42.jpg", "imgs/43.jpg", "imgs/44.jpg",
    "imgs/45.jpg", "imgs/46.jpg"
]



for img in image_list:
    color_image = io.imread(f"drive/MyDrive/{img}")

    # Convert the color image to grayscale
    gray_image = color.rgb2gray(color_image[:,:,:3])

    # Use Otsu's method to compute the optimal threshold
    threshold_value = threshold_otsu(gray_image)

    # Binarize the image with the computed threshold
    binary_image = gray_image > threshold_value

    # Convert the binary image to Pillow Image
    bw_image = Image.fromarray((binary_image * 255).astype(np.uint8))

    # Save the binarized image
    bw_image.save(f"drive/MyDrive/bw_imgs/{img.split('/')[-1]}")