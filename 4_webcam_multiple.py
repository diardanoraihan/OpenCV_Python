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
  
  # Get the properties of the frame
  width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  
  # Create a blank canvas in black
  image = np.zeros(frame.shape, np.uint8)
  
  # Create a smaller frame
  smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
  
  # Copy and Paste the smaller frame to the blank canvas
  image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # top left corner rotated by 180 deg
  image[height//2:, :width//2] = smaller_frame # bottom left corner
  image[height//2:, width//2:] = smaller_frame # bottom right corner
  image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # top right corner rotated by 180 deg
  
  # Display the frame with the speed of 1ms/frame
  cv2.imshow('frame', image)
  
  # Quit the loop if any time within the 1ms the user presses the 'q' key
  if cv2.waitKey(1) == ord('q'):
    break

# Release the device (camera resource) so other programs can use it now
cap.release()
cv2.destroyAllWindows()