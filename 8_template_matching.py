"""
Template matching means detecting an object or a template image in another image.
For example, we can detect a ball, shoe, and post inside an football practice image.  

As for template matching, it's important that the template images (the image we try to locate in the base image)
have the same size or close to the same size as the actual image in our base image. 

Note:
A lot of the times when we detect features like edges, corners, you will CONVERT THE IMAGE
INTO GREY SCALE before you pass it to the algorithms since it will be easier to detect it.
"""

import numpy as np
import cv2

# Load the base image in a gray scale
img = cv2.imread('assets/football_practice.jpeg', 0)

# Load the template image in a gray scale
# template = cv2.imread('assets/ball.jpeg', 0)
template = cv2.imread('assets/shoe.jpeg', 0)

# Get the properties of the template image
template_height, template_width = template.shape

# Template matching methods
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
"""
There are 6 main methods of doing template matching.
Recommendation:
When we are starting the template matching, you try with all the different methods, 
then the method that's giving you the best result is the one you continue to use afterwards.
"""

for method in methods:
  """
  We need to copy the base image since we will draw 
  a rectangle to show where we're finding the template 
  image on the base image.
  If we don't copy it, then we will have multiple rectangles on the 
  base image for each method at once.
  """
  img2 = img.copy()
  
  # Perform convolution and store the result based on method
  result = cv2.matchTemplate(image=img2, templ=template, method=method)
  
  """
  result.shape = (W - w + 1, H - h + 1)
  
  Why? 
  Because if you have 4 x 4 image, and 2 x 2 template, 
  it will result in 3 x 3 image. So the size of the result
  is the number of times the template image can slide through 
  the base image.
  
  In the output array in the result, we look at the maximum or 
  minimum value depending on the method you're using, 
  you take that value, and you try to kind of reverse engineering
  where this position is gonna be in the original base image.
  
  Then, we can draw a rectangle there.
  
  Ex: 
  >> Base image
  [[255, 255,   0,   0]
   [255, 255,   0,   0]
   [255, 255, 255, 255]
   [255, 255, 255,255]]
  >> Template image
  [[0, 0]
   [0, 0]]
  >> Result
  [[0, 1, 1]
   [0, 1, 1]
   [0, 0, 0]]
  """
  # Take the max and min value
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  # print(max_loc, min_loc)
  
  # Sometimes the max is the best, sometimes otherwise. That's up to the method to decide!
  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    location = min_loc
  else:
    location = max_loc
  
  # Draw the rectangle based on the size of the template image
  bottom_right = (location[0] + template_width, location[1] + template_height)
  img2 = cv2.rectangle(img=img2, pt1=location, pt2=bottom_right, color=255, thickness=5)

  # Display the image
  cv2.imshow("Match", img2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()