import pickle
import sys
from math import floor

import numpy as np
from PIL import Image


def grayscale_to_monochrome(image: Image) -> Image:
    array_grayscale = np.asarray(image)
    array_monochrome = np.zeros((image.size[1], image.size[0]))
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            array_monochrome[y, x] = 255 if array_grayscale[y, x] > 127 else 0
    return Image.fromarray(array_monochrome)


def crop_unneeded(image: Image) -> Image:
    array = np.asarray(image)
    maxX = maxY = 0
    minX = image.size[0]
    minY = image.size[1]
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if array[y, x] == 0:
                minX = x if x < minX else minX
                maxX = x if x > maxX else maxX
                minY = y if y < minY else minY
                maxY = y if y > maxY else maxY
    array_cropped = np.zeros((maxY-minY, maxX-minX))
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            array_cropped[y-minY, x-minX] = array[y, x]
    return Image.fromarray(array_cropped)


def scale_keeping_aspect(array: np.array, height: int) -> np.array:
    scale = float(len(array)) / height
    width = int(round(len(array[0]) * height / len(array)))
    scaled_array = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            scaled_array[y, x] = array[int(floor(scale * y)), int(floor(scale*x))]
    return scaled_array
image = Image.open(sys.argv[1]).convert("L")
bw = grayscale_to_monochrome(image)
cropped = crop_unneeded(bw)
result = ocr(cropped)
print(f"{result[0]}: {result[1]}% confidence.")
print("Didn't Crash")
