"""
In order to extract/detect a color from an image, we need to convert
our BGR color into HSV (Hue, Saturation, Lightness/Brightness)
"""

import cv2
import numpy as np

# Define your video capture device
cap = cv2.VideoCapture(0)

# Use the device in the while loop
while True:
    # Get the frame and its properties from our device
    ret, frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Convert BGR color into HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Pick the lower and upper of the color you want to extract in the HSV format
    lower_blue = np.array([90, 50, 50])  # Lighter blue
    upper_blue = np.array([130, 255, 255])  # Darker blue

    # Define a mask (a portion of the frame)
    # This will return a new image or mask that has only the blue pixels existing, if yes then 1 (255 == white), otherwise will be blacked out (0 == black)
    mask = cv2.inRange(src=hsv, lowerb=lower_blue, upperb=upper_blue)

    # Apply the mask to the original frame
    # This will only keep the pixels in our original frame that match with this mask by comparing pixel by pixel
    result = cv2.bitwise_and(src1=frame, src2=frame, mask=mask)
    """
    .bitwise_and will take two source images and blend them using a mask.
    In our case, we only have one source image, so we pass the second source with the same one.
    .bitwise_and works like this:
    >> 1 1 = 1
    >> 1 0 = 0
    >> 0 1 = 0
    >> 0 0 = 0
    As you can see, we compare the bits from our mask to the bits in our image.
    And, if this return 1, it means there is a blue color. Otherwise, we don't keep it.
    """
    # Display the frame with the speed of 1ms/frame
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

"""
Pro Tips
--------
In order to get the upper and lower bound of a specific color, you can go 
to HSV color picker and pick a light and darker color of your interest.
>> BGR_color = np.array([[[255, 0, 0]]], dtype=np.uint8)
>> HSV_color = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
>> HSV_color[0][0] --> array([120, 255, 255]) --> the upper_blue
"""
