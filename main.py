from PIL import Image
from PIL import ImageOps
import numpy as np
import sys


def grayscale_to_monochrome(image: Image) -> Image:
    array_grayscale = np.asfarray(image)
    array_monochrome = np.zeros((image.size[1], image.size[0]))
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            array_monochrome[y, x] = 255 if array_grayscale[y, x] > 127 else 0
    return Image.fromarray(array_monochrome)


image = Image.open(sys.argv[1]).convert("L")
image.show()
bw = grayscale_to_monochrome(image)
bw.show()
print("Didn't Crash")
