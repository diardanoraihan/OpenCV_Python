"""
We will use HAAR CASCADE to do this face detection and classification.

Haar Cascade is pre-trained classifier that will look at an image,
and will try to pick out specific features in that image.
"""

import numpy as np
import cv2

try:
  cap = cv2.VideoCapture(0)

  # .CascadeClassifier will take an argument of a path to this classifier.
  # path --> "a path stored in our system" + "specific classifier that we want"
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
  eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

  while(True):
    ret, frame = cap.read()

    # Convert the frame into gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection: Get the locations of all of the faces in terms of positions
    # Reference for the function:
    # https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # (x, y, w, h) is the rectangle coordinate
    for (x, y, w, h) in faces:
      cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)

      # Use the face inside the rectangle to detect the eye using eye_classifier
      # roi = region of interest
      roi_color = frame[y:y+h, x:x+w]
      roi_gray = gray[y:y+h, x:x+w]

      # Eye Detection
      eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
      for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('Face and Eye Detector', frame)

    if cv2.waitKey(1) == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
except:
  print('Error: The camera cannot be identified')