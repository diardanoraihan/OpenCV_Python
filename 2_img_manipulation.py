'''
We will cover image manipulation, such as:
- how the image being represented in the computer
- how the image actually works
- etc.
'''

import cv2
import numpy as np
import random as rd

img = cv2.imread('assets/person_fixing_street_light.jpeg', -1)
print(img)
print(img.shape)
'''
(600, 426, 3)
The image is represented in 3 dimensional array. 
It means it has 600 rows (height), 426 columns (width), and 3 channels 
(the color space, with the order of BGR: Blue, Green, Red in openCV)

For example, here is the values of the img in the corresponding index:

>> print(img)
[[[86 74 70]
  [88 76 72]
  [89 75 69]
  ...
  [74 80 79]
  [73 78 77]
  [87 92 90]]

 [[86 74 70]
  [87 75 71]
  [89 75 69]
  ...
  [70 75 76]
  [62 67 66]
  [77 82 80]]

 [[87 75 71]
  [87 75 71]
  [88 74 68]
  ...
  [65 70 71]
  [53 58 57]
  [70 72 72]]

 ...
...
  ...
  [14 53 45]
  [64 98 91]
  [39 73 66]]]
  
>> print(img[:, :, 0])
[[86 88 89 ... 74 73 87]
 [86 87 89 ... 70 62 77]
 [87 87 88 ... 65 53 70]
 ...
 [68 68 68 ... 50 38 19]
 [68 68 68 ... 54 65 33]
 [68 68 68 ... 14 64 39]]
'''

# Access specific row
print(img[0, :, :])

# Access specific channel
print(img[:, :, 0])

# Changing pixel colors
# img.shape -> (852, 1200, 3)
for i in range(100):
  for j in range(img.shape[1]):
    img[i][j] = [rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)]
    # img[i][j] = [0, 0, 0] # this will result in all black for the top of the image

cv2.imwrite('assets/person_fixing_street_light_rand_color.jpeg', img)
cv2.imshow('Image with new color', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Copy and paste parts of image
triangleSign = img[320:520, 900:1100] # slice part of the image you want to copy
img[163:363, 200:400] = triangleSign # place it to the desired part of the old image
cv2.imwrite('assets/person_fixing_street_light_rand_color_copy_&_paste.jpeg', img)
cv2.imshow('Image with new color and pasted object', img)
cv2.waitKey(0)
cv2.destroyAllWindows()