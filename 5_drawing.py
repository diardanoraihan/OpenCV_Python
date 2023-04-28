import numpy as np
import cv2

# Define your video capture device
cap = cv2.VideoCapture(0)

# Use the device in the while loop
while True:
    # Get the frame and its properties from our device
    ret, frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Draw a line.
    """
    In computer vision, the top left corner of the image is the origin (0,0)
    - As we increase the X, we go further to the right
    - As we increase the Y, we go further to the bottom
    """
    img = cv2.line(
        img=frame, pt1=(0, 0), pt2=(width, height), color=(255, 0, 0), thickness=10
    )
    img = cv2.line(
        img=img, pt1=(width, 0), pt2=(0, height), color=(0, 0, 255), thickness=5
    )

    # Draw a rectangle.
    img = cv2.rectangle(
        img=img,
        pt1=(100, 100),
        pt2=(200, 200),
        color=(100, 255, 100),
        thickness=-1,  # -1 to fill the rectangular with the color
    )

    # Draw a rectangle.
    img = cv2.circle(
        img=img, center=(300, 300), radius=60, color=(0, 0, 255), thickness=5
    )

    # Draw a font.
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(
        img=img,
        text="Diar is great!!",
        org=(200, height - 30),  # the origin starts from the bottom left of the image
        fontFace=font,
        fontScale=2,
        color=(255, 255, 255),
        thickness=3,
        lineType=cv2.LINE_AA,
    )

    # Display the frame with the speed of 1ms/frame
    cv2.imshow("frame", img)

    # Quit the loop if any time within the 1ms the user presses the 'q' key
    if cv2.waitKey(1) == ord("q"):
        break

# Release the device (camera resource) so other programs can use it now
cap.release()
cv2.destroyAllWindows()
