import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale mode
image = cv.imread('assets/BSE_Google_noisy.jpeg', 0)

cv.imshow("Original image", image)

plt.hist(x=image.flat, bins=100, range=(0, 255))
plt.show()

'''
From the histogram, we can see that it has two pixel centers around 50 and 150,
with the valley between both is 100. 
'''

# cv.waitKey(0)
# cv.destroyAllWindows()

