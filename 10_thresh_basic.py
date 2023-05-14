'''
Thresholding is binarization of an image.
In general, we want to take an image and convert it to a binary image 
where pixels are either 0 (black) or 255 (white).

A very simple thresholding would be to take an image
and some particular value that we're going to call it the thresholding value.
Then, compare for each pixel of the image to this threshold value.

If that pixel is less than the threshold value, we set the pixel intensity to zero. Otherwise, 
we set it to 255 (white).
'''
import cv2 as cv

img = cv.imread('assets/person_fixing_street_light.jpeg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding
threshold_value, thresh = cv.threshold(src=gray, thresh=100, maxval=255, type=cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

threshold_value, thresh_inv = cv.threshold(src=gray, thresh=100, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh_inv)


cv.waitKey(0)
cv.destroyAllWindows()