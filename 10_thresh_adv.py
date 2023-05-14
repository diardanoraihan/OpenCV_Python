'''
Image Kernels: https://setosa.io/ev/image-kernels/ 

One of the downside of the simple thresholding technique is that
we have to set manually the value of the threshold.
In some cases, this might work, in some advance cases, this might not work especially
when it comes to different illumination.

In adaptive thresholding, we let the computer specifies the optimal thresh value
by itself.
'''
import cv2 as cv

img = cv.imread('assets/hand_grabbed_paddy.jpeg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Adaptive Thresholding
'''
In the mean adaptive thresholding, it computes a mean over those neighborhood pixels,
and finds the optimal threshold value for that specific part. Then, it slides over
to the right and down over every part of the image.
'''
adaptive_thresh_mean = cv.adaptiveThreshold(
  src = gray,
  maxValue = 255,
  adaptiveMethod = cv.ADAPTIVE_THRESH_MEAN_C,
  thresholdType = cv.THRESH_BINARY,
  blockSize = 11,
  C = 3)
cv.imshow("Adaptive Threshold - Mean", adaptive_thresh_mean)

'''
In the gaussian adaptive thresholding, it adds a weight to each pixel value, 
and compute the mean across those pixels. Then, it slides over
to the right and down over every part of the image.
'''
adaptive_thresh_gaussian = cv.adaptiveThreshold(
  src = gray,
  maxValue = 255,
  adaptiveMethod = cv.ADAPTIVE_THRESH_GAUSSIAN_C,
  thresholdType = cv.THRESH_BINARY,
  blockSize = 11,
  C = 3)
cv.imshow("Adaptive Threshold - Gaussian", adaptive_thresh_gaussian)

cv.waitKey(0)
cv.destroyAllWindows()