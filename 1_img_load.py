import cv2

'''
Insert a path of the image you want to load
Various flag modes you can set:
>> -1, cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be neglected. It is the default flag.
>> 0, cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode.
>> 1, cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel.
'''

# Load the image
img = cv2.imread('assets/person_fixing_street_light.jpeg', -1)

# Resize the image by pixels
# img = cv2.resize(img, (400, 400))

# Resize the image by scale
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Rotate the image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save the image
cv2.imwrite('assets/person_fixing_street_light_new.jpeg', img)

# Display the image
cv2.imshow('myImage', img)

# Close the window
cv2.waitKey(0) # 0 means wait infinite amount of time for you to press any key on the keyboard.
# cv2.waitKey(5000) # Hence, 5000 means wait for 5 seconds. If you don't press any key within 5 seconds, it automatically will get skipped.
cv2.destroyAllWindows()
