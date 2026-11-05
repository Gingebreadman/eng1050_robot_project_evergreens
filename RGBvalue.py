#Lewis Kidd
#november 3rd
#melissa collins
#MU Gold RGB value


from matplotlib import image
import pandas as pd
import numpy as np

from glob import glob
import matplotlib.pyplot as plt
import cv2 as cv
import sys

plt.style.use('ggplot')

#finding image. His way of finding the image did not work for me but I found a tutorial and code from cv2 directly
#The code I found in the tutorial is what is below. cited at the bottome of my work.
img_cv = cv.imread(cv.samples.findFile("c:\\Users\\lewis\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-11-03 152234.png"))
#That links to the mizzou logo
if img_cv is None:
    sys.exit("Could not read the image.")
cv.imshow("cool panda", img_cv)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("panda.png", img_cv)

blue, green, red = img_cv.mean(axis=(0,1))
print(f"Red: {red:.1f}")
print(f"Green: {green:.1f}")
print(f"Blue: {blue:.1f}")

# it printed red: 241, Green: 184, Blue: 45


