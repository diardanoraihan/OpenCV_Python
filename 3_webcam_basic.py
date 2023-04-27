import numpy as np
import cv2

'''
Load a webcam image / video capture device
- Inside the .VideoCapture(), put the number of the webcam you want to use.
- If you have multiple devices, 0 would access one of them, 1 would access the next one, and so forth.

Note: 
- If you don't have any webcam, you can use video with any format/type. 
- Store the video in your folder project, then load the video by giving its path to the .VideoCapture() func.
- i.e. cv2.VideoCapture('assets/my_video.mp4')
'''

# Define your video capture device
cap = cv2.VideoCapture(0)

# Use the device in the while loop. 
# The loop will keep displaying the video until we press any key on keyboard to quit
while(True):
  '''
  cap.read() will return two things:
  - ret: return boolean value saying if the webcam can be used or not (False if the webcam cannot be accessed due to faulty or being used by other software/resource)
  - frame: the image itself in the form of numpy array 
  '''
  # Get the frame from our device
  ret, frame = cap.read()
  
  # Display the frame with the speed of 1ms/frame
  cv2.imshow('frame', frame)
  
  # Quit the loop if any time within the 1ms the user presses the 'q' key
  if cv2.waitKey(1) == ord('q'):
    break

# Release the device (camera resource) so other programs can use it now
cap.release()
cv2.destroyAllWindows()