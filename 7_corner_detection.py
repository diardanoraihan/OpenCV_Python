"""
In this tutorial, we will learn on how to detect corners in an image or video capture device.

A lot of the times when we detect features like edges, corners, you will CONVERT THE IMAGE
INTO GREY SCALE before you pass it to the algorithms since it will be easier to detect it.
"""
import numpy as np
import cv2

# Load the image
img = cv2.imread("assets/Chess_Board.png", flags=1) # assume the image is in BGR color format

# Resize the image to be a bit small
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# Convert BGR to gray scale color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners. 
# The function will return a list of x y corner coordinates
corners = cv2.goodFeaturesToTrack(image=gray, maxCorners=100, qualityLevel=0.01, minDistance=10)

# Convert the floating point into integer
corners = np.intp(corners)

# Extract all the corner coordinates
for corner in corners:
  '''
  Flat the array regardless its dimension (remove the interior rents)
  >> [[[1, 2]]] --> [1, 2]
  >> [[[1, 2]], [[4, 5]]] --> [1, 2, 4, 5]
  '''
  x, y = corner.ravel() 
  # Draw the corner on the colored image
  img = cv2.circle(img=img, center=(x , y), radius=5, color=(0, 0, 255), thickness=-1)

for i in range(len(corners)):
  for j in range(i + 1, len(corners)):
    corner1 = tuple(corners[i][0])
    corner2 = tuple(corners[j][0])
    color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
    cv2.line(img, corner1, corner2, color, 1)

# Display the image
cv2.imshow("Chess Board", img)

# Save the image
cv2.imwrite('assets/Chess_Board_corner_detection_line.png', img)

# Close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
